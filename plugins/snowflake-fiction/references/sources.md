# 方法来源与改编边界

本包的十步对应 Randy Ingermanson 的 [How To Write A Novel Using The Snowflake Method](https://www.advancedfictionwriting.com/articles/snowflake-method/)（核对日期：2026-10-08）。本文档和模板为原创概括，没有转载原文段落或示例；本包不代表原作者背书。

对应关系：一句话核心、一段梗概、人物摘要、短梗概、人物视角故事、长梗概、人物档案、场景清单、可选场景扩写、初稿。详细技能以各阶段具体产物区分，不混淆第 3、5、7 步。

原文允许返回修订，明确第 9 步可选，并讨论对已有稿件使用方法。小时/周数、页数、英文词数及三次灾难是建议，不作为中文写作硬限制。大纲覆盖结局，不能误作避免剧透的宣传文案。

本包增加了项目状态、版本依据、事实确认、影响追踪、分批导入和按场景正文；这些是 Codex 协作设计，不声称为原方法额外规定。

包装依据：[官方插件规范](https://developers.openai.com/plugins/build/plugins)、[技能规范](https://learn.chatgpt.com/docs/build-skills)、[提交错误与限制](https://developers.openai.com/plugins/deploy/submission-errors)。使用仍受支持的 `.codex-plugin/plugin.json`，与本仓库已有 documentation 插件结构一致；无需 MCP、联网写作服务或第三方凭据。

## 实际采用的 Matt Pocock 指导

核验 [mattpocock/skills](https://github.com/mattpocock/skills/tree/b0618bc436ad893b3c5e84e55fba86586d34a404) 的固定提交 `b0618bc436ad893b3c5e84e55fba86586d34a404`，直接读取原文件，未执行安装脚本、未迁入原文。

- [writing-for-agents](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/writing-for-agents/SKILL.md)：将各步入口写为明确输入、任务与可观察完成条件；公共状态/修订规则集中到 `workflow.md`，每步只写自己的检查重点，模板按需读取。
- [SKILL-MECHANICS.md](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)：区分发现和执行。十步均保留精确描述供 Codex 发现；导航通过读取同包指令执行，未承诺跨技能调用 API。其 `disable-model-invocation` 属于不同宿主约定，本包采用 Codex 元数据与默认可发现行为。
- [ask-matt](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/ask-matt/SKILL.md)：导航在推荐或建议跳过前，先读目标技能本身；路由表仅是入口索引，已有材料是中途入口。
- [grilling](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md)：采用“查证事实由 agent 负责，作品决定交作者”及问题按依赖推进的原则；按本任务的渐进创作要求缩小每次提问范围，不逐轮穷尽整个小说设计。
- [code-review](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/code-review/SKILL.md)：交付前分别核对规范质量与需求忠实度。具体证据见验证记录；Matt 库不是 Codex 端到端测试框架。
