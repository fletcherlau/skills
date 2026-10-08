#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check this package's simple metadata and references, not runtime behavior.

Uses stdlib; metadata parsing supports this package's scalar subset, not full YAML.
"""
import json
import re
import sys
from pathlib import Path

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def metadata(text, path):
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.DOTALL)
    require(match is not None, f"{path}: missing complete frontmatter boundaries")
    block, body = match.groups()
    require(body.strip(), f"{path}: empty instructions")
    fields = {}
    for line in block.rstrip().splitlines():
        key, value = line.split(":", 1)
        require(key in {"name", "description"}, f"{path}: unsupported field {key}")
        require(key not in fields, f"{path}: duplicate {key}")
        value = value.strip()
        fields[key] = json.loads(value) if value.startswith('"') else value
    require(set(fields) == {"name", "description"}, f"{path}: missing metadata")
    return fields


def validate(repo):
    repo = repo.resolve()
    package = repo / "plugins/snowflake-fiction"
    manifest = json.loads((package / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    plugin = manifest["name"]
    require(NAME.fullmatch(plugin), "invalid plugin name")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "invalid version")
    skill_root = (package / manifest["skills"]).resolve()
    require(skill_root == package / "skills", "skills root must stay inside package")
    catalog = json.loads((repo / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    entries = [entry for entry in catalog["plugins"] if entry["name"] == plugin]
    require(len(entries) == 1, "marketplace must register this plugin once")
    source = entries[0]["source"]
    require(source["source"] == "local" and source["path"].startswith("./"), "invalid market source")
    require((repo / source["path"]).resolve() == package, "market path must resolve from repo root")
    skills = sorted(skill_root.glob("*/SKILL.md"))
    require(len(skills) == 11, "expected navigator plus ten step skills")
    stages, names = set(), set()
    max_id = 0
    for skill in skills:
        data = metadata(skill.read_text(encoding="utf-8"), skill)
        name, desc = data["name"], data["description"]
        require(NAME.fullmatch(name) and name == skill.parent.name, f"{skill}: incompatible name")
        require(name not in names, f"{skill}: duplicate name")
        names.add(name)
        require(0 < len(desc) <= 1024, f"{skill}: description length")
        combined = f"{plugin}:{name}"
        require(len(combined) <= 64, f"{skill}: combined identifier too long")
        max_id = max(max_id, len(combined))
        if name != "snowflake-navigator":
            stages.add(int(name.split("-")[1]))
        ui = (skill.parent / "agents/openai.yaml").read_text(encoding="utf-8")
        require(ui.splitlines()[0] == "interface:", f"{skill}: invalid UI mapping")
        interface = {}
        for line in ui.splitlines()[1:]:
            key, value = line.strip().split(":", 1)
            require(key not in interface, f"{skill}: duplicate UI key")
            interface[key] = json.loads(value.strip())
        require(set(interface) == {"display_name", "short_description", "default_prompt"}, f"{skill}: UI fields")
        require(25 <= len(interface["short_description"]) <= 64, f"{skill}: UI description length")
        require(f"${name}" in interface["default_prompt"], f"{skill}: prompt must mention skill")
        require(any((skill.parent / "assets").glob("*.md")), f"{skill}: no reusable template")
    require(stages == set(range(1, 11)) and "snowflake-navigator" in names, "step coverage")
    links = 0
    for doc in package.rglob("*.md"):
        text = doc.read_text(encoding="utf-8")
        require("[TODO:" not in text, f"{doc}: unfinished scaffold")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"https?://|#", target):
                continue
            target = target.split("#", 1)[0]
            resolved = (doc.parent / target).resolve()
            require(package == resolved or package in resolved.parents, f"{doc}: reference escapes package: {target}")
            require(resolved.is_file(), f"{doc}: missing target {target}")
            links += 1
    print(f"PASS: {len(skills)} skills; 10 steps + navigator; {links} local links; longest ID {max_id}/64; marketplace resolves")


if __name__ == "__main__":
    try:
        validate(Path(__file__).resolve().parents[3])
    except (ValueError, KeyError, OSError, IndexError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
