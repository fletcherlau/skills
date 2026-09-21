# skills

个人维护的技能与插件。

## Documentation

[documentation 插件](plugins/documentation/) 用于逐步构建文档工作流，目前包含：

- [documentation-review](plugins/documentation/skills/documentation-review/SKILL.md)：总审查流程与配套报告模板（上游原版，待适配；依赖的 `documentation-build` 尚未引入）。
- [documentation-diataxis](plugins/documentation/skills/documentation-diataxis/SKILL.md)：审查文档分类、读者需求与质量，提供改进建议。
- [documentation-structure](plugins/documentation/skills/documentation-structure/SKILL.md)：依据仓库约定审查通用 Markdown 的标题、命名、元数据、导航和链接结构。
- [documentation-verify](plugins/documentation/skills/documentation-verify/SKILL.md)：按声明类型核对相关仓库、契约、设计与运行证据，报告不一致及证据缺口。
- [documentation-style](plugins/documentation/skills/documentation-style/SKILL.md)：依据项目规范和通用 Markdown 指南审查表达、术语与排版，按语言选择规则并引用依据。

`documentation-diataxis` 和 `documentation-review` 原样引入 Canonical；`documentation-structure` 和 `documentation-style` 已适配通用 Markdown；`documentation-verify` 已移除单仓库和代码作为唯一依据的假设。来源、修改说明与许可证见 [UPSTREAM.md](plugins/documentation/UPSTREAM.md)。
