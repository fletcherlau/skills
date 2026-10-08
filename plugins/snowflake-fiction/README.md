# 雪花小说创作插件

给 Codex 使用的中文小说创作技能包：十步各一个独立 Skill，加一个总体导航。支持从灵感、大纲或稿件接入、跳步、回退修订和按场景写初稿。题材、文风与作品决定属于作者。

## 安装

本 PR 尚未合并时使用功能分支：

```sh
git clone --branch codex-snowflake-fiction-plugin https://github.com/fletcherlau/skills.git
cd skills
codex plugin marketplace add .
```

从仓库根运行（市场根路径必须是这个 checkout，不能是 `.agents/plugins`）。随后在支持本地插件的 Codex 桌面端重启/刷新，打开插件目录，选择 **Fletcher 的技能插件**，安装 **雪花小说创作**。安装可用性取决于客户端版本；添加 marketplace 本身不证明插件已经安装。

已有 checkout 可切换到该功能分支，或在合并后从 `master` 使用相同步骤。只操作自己的干净 checkout，保留其他未完成工作。请勿把小说正文存进插件目录。

仓库市场 [catalog](https://github.com/fletcherlau/skills/blob/codex-snowflake-fiction-plugin/.agents/plugins/marketplace.json) 以 `./plugins/snowflake-fiction` 指向本包；官方仍支持的兼容清单位于 [.codex-plugin/plugin.json](.codex-plugin/plugin.json)。本包无需外部服务认证；`ON_INSTALL` 是市场策略值，不表示必须提供账号。仓库市场仅登记本插件，不引用尚未合并的 documentation PR。

若客户端没有插件安装界面，可将**整个本包**复制到小说项目的 `tools/snowflake-fiction/`，然后对 Codex 说：“读取 `tools/snowflake-fiction/skills/snowflake-navigator/SKILL.md` 并执行。”这是直接读取工作流的备用方式，不等于完成插件安装。保留整包以保证共享协议和模板可解析，不要单独复制 SKILL.md。

## 使用

技能选择器中选择对应技能；CLI/IDE 可输入 `$snowflake-navigator`，若显示插件命名空间则选择 `snowflake-fiction:snowflake-navigator`。每个名字都使用小写字母、数字和连字符。导航判断实际材料与任务，不按最大步骤号强制推进。

- “用 $snowflake-navigator 看 `novel/海边/outline.md`，只推荐下一项工作；不要改题材。”
- “用 $snowflake-01-premise 把这段灵感提炼成一句话，提供候选让我选。”
- “用 $snowflake-05-character-synopsis 从反派视角重述已有故事，保留结局。”
- “已有三章稿件在 `novel/海边/draft/`。用 $snowflake-navigator 接入并找续写入口，未读章节先标明。”
- “跳过第 9 步。用 $snowflake-10-draft-scene 写场景 S014，沿用原稿风格，本次约 1200 字。”
- “主角改为不知晓信件内容。用 $snowflake-navigator 查受影响的档案、场景和正文，先给修订选项。”
- “从 `novel/海边/snowflake-state.md` 恢复；只继续下一场景，保留上次待决结局。”

[阶段表](references/stage-map.md) 连接全部十步；各技能包含输入、具体任务、模板、完成条件和一致性检查。导航内有 [状态模板](skills/snowflake-navigator/assets/project-state.md)，共同 [协议](references/workflow.md) 定义恢复、事实与候选、局部完成和 stale 传播。无文件工具时可在对话使用，明确状态尚未保存。

原方法及改编边界见 [来源说明](references/sources.md)。页数、时长和转折形状可调整，第 9 步可跳过；正文默认一场景，不一次生成整本书。

## 验证

在仓库根运行：

```sh
python3 plugins/snowflake-fiction/scripts/validate_package.py
python3 plugins/snowflake-fiction/scripts/test_validate_package.py
```

仅使用 Python 标准库，检查全部 11 个技能的元数据、名称、组合标识限制、清单/市场路径、模板和本地链接可分发性。不会写入小说或修改安装设置。行为验证方案与实际边界见 [验证记录](VERIFICATION.md)，结构检查不代表真实创作质量或客户端已安装。
