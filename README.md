# 游戏设计与开发公开研究库

更新于 2026-10-24。本库保存公开来源的短摘要、可执行方法和一个 Codex Skill。资料用于帮助作出可验证的设计与开发决定，不声称提供成功配方，也不代表任何读者已经认可全部观点。

## 从这里开始

| 用途 | 入口 |
|---|---|
| 在游戏任务中调用方法 | [game-design-development Skill](skills/game-design-development/SKILL.md) |
| 按问题学习设计与开发逻辑 | [知识地图](docs/knowledge-map.md) |
| 检查原始出处与适用条件 | [来源卡](skills/game-design-development/references/sources.md) · [结构化来源表](skills/game-design-development/references/sources.json) |
| 看一个具体设计推演 | [《雨夜送信》虚构例子](skills/game-design-development/references/worked-example.md) |
| 审阅待验证方法 | [候选方法清单](docs/candidates.md) |
| 社区经验与读取范围 | [小红书补充研究](skills/game-design-development/references/community-notes.md) |
| 区分外部材料与个人认可 | [知识采纳规则](skills/game-design-development/references/knowledge-adoption.md) |
| 查看本 Skill 如何验证 | [验证记录](docs/validation.md) |

## 覆盖与边界

包括体验目标、玩家行动与选择、规则状态、系统数值、教学与关卡、叙事和证据、表现反馈、原型与生产、玩家测试、可访问性、性能及发布证据。AI 运行时是可选分支，重点是行动与状态一致、记忆边界和失败恢复。

首版核读 18 项一手资料，另补充 ink、游戏程序更新模式与生成式 Agent 论文，合计 21 项一手来源。小红书阅读 5 篇实质内容（其中1篇证据不足已排除）、1篇部分图文、1篇视频元数据；覆盖与未核验项逐篇记录。来源互相补充，不以条数作为结论可靠性的评分。

没有覆盖所有类型的实战细节。多人网络同步、反作弊、实时战斗、3D美术管线、主机认证、发行预算和长期经济需要按具体项目继续研究。旧文章只借用仍有解释力的方法；接口和平台规则在实际使用时重新核对。

## 使用 Skill

将 `skills/game-design-development` 整个目录复制到 Codex 的用户技能目录，例如 `~/.codex/skills/`。可用 `$game-design-development` 显式调用，也保留正常自动发现。示例请求：“使用这个 Skill 评审当前玩法，先找最危险的假设，并完成一个能验证它的原型。”

`assets/templates` 的模板按需使用。私有学习库的位置可放在用户目录的 `game-design-development.local.json`，不要把个人路径、认可记录或项目私密数据提交到本库。外部来源、项目实验和用户认可分别保存；本库不包含个人认可台账。

## 更新与引用

来源保留作者、日期精度、访问日、读取范围、主张与限制。新增综合建议要回指来源并写明验证办法，原作仍按原站许可；本库只保存简短原创摘要与链接，不分发原论文、课件、截图或平台全文。

检查资料结构可运行 `python tools/validate_library.py`；Skill 格式另用当前环境的 `skill-creator` 校验器检查。结构检查通过不等于方法已被玩家或市场验证。未指定统一的下游再授权条款；需要复用时区分本库原创整理与所链接原作，并确认各自权限。
