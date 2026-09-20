# 上游来源

## documentation-diataxis

- 引入文件：`skills/documentation-diataxis/SKILL.md`
- 项目：[canonical/workshop](https://github.com/canonical/workshop)
- 原文：[documentation-diataxis/SKILL.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-diataxis/SKILL.md)
- 获取日期：2026-09-18
- 获取分支：`main`；未取得上游提交 SHA，以文件 SHA-256 标识本次引入内容。
- SHA-256：`331716ee5d241a478339aae8e6ec8ef448f5128b70c8e0c825b36cb66b24ed64`
- 本地修改：无，SKILL.md 与下载的上游原文逐字节一致。
- 上游仓库根目录许可证：[LICENSE](https://github.com/canonical/workshop/blob/main/LICENSE)（GNU GPL v3），副本保存在 [LICENSE.canonical-workshop](LICENSE.canonical-workshop)。

## documentation-structure

- 改编文件：`skills/documentation-structure/SKILL.md`
- 项目：[canonical/workshop](https://github.com/canonical/workshop)
- 原文：[documentation-structure/SKILL.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-structure/SKILL.md)
- 获取与修改日期：2026-09-18
- 获取分支：`main`；未取得上游提交 SHA，以原文件 SHA-256 标识改编基线。
- 原文件 SHA-256：`1c56898fca5a7c7cfd780208258296d94c8bada91a601979875aaeaf75d92b5f`
- 本地修改：改写为中文通用 Markdown 审查；将 Sphinx/reST/MyST 专用导航与引用要求替换为仓库实际约定；补充标题层级、引用式链接、图片、入站引用和未验证项处理；命名、元数据及分类目录要求均以仓库约定为依据。保留只读审查边界。
- 上游仓库根目录许可证：[LICENSE](https://github.com/canonical/workshop/blob/main/LICENSE)（GNU GPL v3），副本保存在 [LICENSE.canonical-workshop](LICENSE.canonical-workshop)。

## documentation-verify

- 引入目录：`skills/documentation-verify/`
- 项目：[canonical/workshop](https://github.com/canonical/workshop)
- 原文：[documentation-verify/SKILL.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-verify/SKILL.md)
- 配套参考：[verification_procedures.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-verify/references/verification_procedures.md)、[report_format.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-verify/references/report_format.md)
- 获取日期：2026-09-18
- 获取分支：`main`；未取得上游提交 SHA，以下 SHA-256 标识原始引入内容，作为改编基线。
- 修改日期：2026-09-20。
- 本地修改：入口、验证流程和报告模板同步改写为中文；按声明确定证据范围，不预设单仓库或特定工作区布局；按实现、运行、要求、历史和计划选择证据并核对适用条件；区分文档不准确、实现与约定不一致、证据冲突及证据不足，不再默认以代码为唯一依据或只建议修改文档。
- 上游仓库根目录许可证：[LICENSE](https://github.com/canonical/workshop/blob/main/LICENSE)（GNU GPL v3），副本保存在 [LICENSE.canonical-workshop](LICENSE.canonical-workshop)。

| 文件（相对于技能目录） | SHA-256 |
| --- | --- |
| `SKILL.md` | `b66cd3ec85fea07326f364d3e21db4a7c87577f882f28a051a1b301702f7e829` |
| `references/verification_procedures.md` | `681f31f991881ca170d33cf4ef439a4764f03c8c43bf9fd43a3d6cb20ce152fb` |
| `references/report_format.md` | `0ea0a7549a177b398c46d050d101cffb304f0c6b9c7708fda97fd94199490a89` |

## documentation-style

- 引入目录：`skills/documentation-style/`
- 项目：[canonical/workshop](https://github.com/canonical/workshop)
- 原文：[documentation-style/SKILL.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-style/SKILL.md)
- 配套参考：[doc-style-guide.md](https://github.com/canonical/workshop/blob/main/.github/skills/documentation-style/references/doc-style-guide.md)
- 获取日期：2026-09-20
- 获取分支：`main`；未取得上游提交 SHA，以下 SHA-256 标识原始引入内容，作为改编基线。
- 修改日期：2026-09-20。
- 本地修改：入口与配套指南同步改写为中文通用 Markdown 风格审查；移除 MyST/reST、Sphinx 和 Workshop 专用语法、术语、目录及发布模板要求；采用用户要求、项目规范、通用指南的规则优先级，按语言和实际扩展选择适用规则；补充基础语言错误检查、按读者影响排序与变更上下文规则；每条发现引用依据，区分语言错误、规范违规、改进建议及未审查／待确认事项。与结构及准确性审查明确分工，保留只读边界。
- 原版运行时获取 MyST/reST 语法指南的要求已移除；仅在项目明确采用且审查需要时读取相应外部规范。
- 上游仓库根目录许可证：[LICENSE](https://github.com/canonical/workshop/blob/main/LICENSE)（GNU GPL v3），副本保存在 [LICENSE.canonical-workshop](LICENSE.canonical-workshop)。

| 文件（相对于技能目录） | SHA-256 |
| --- | --- |
| `SKILL.md` | `53910266335efda76fd78852a9ce381d9e1c0675cb1f9920a003cf816c7c680c` |
| `references/doc-style-guide.md` | `31a955706f6932ed520bf5059e5cdad3516b64799029ecbcbd4c49dfd6465613` |

此来源记录及许可证对应上述引入和改编文件，不为仓库内其他独立内容指定许可证。
