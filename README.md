# 游戏玩法策划公开研究库

更新于 2026-10-25。本库以游戏玩法策划为主，研究玩家怎样行动、选择，机制如何产生变化，以及为什么愿意继续玩。保存公开来源的短摘要、可执行方法和一个 Codex Skill；开发、测试和发布资料按任务需要使用。外部研究不自动代表个人认可。

## 从这里开始

| 用途 | 入口 |
|---|---|
| 在游戏任务中调用方法 | [game-design-development Skill](skills/game-design-development/SKILL.md) |
| 先研究怎样策划玩法 | [玩法策划工作法](skills/game-design-development/references/gameplay-planning.md) |
| 按问题学习玩法逻辑 | [知识地图](docs/knowledge-map.md) |
| 编排战斗、合作与成长 | [战斗遭遇](skills/game-design-development/references/combat-encounters.md) · [多人协作](skills/game-design-development/references/cooperative-play.md) · [长期成长](skills/game-design-development/references/long-term-progression.md) |
| 查看本轮深化、修订及仍缺的证据 | [研究深度与边界](docs/research-depth.md) |
| 看方法在当前项目怎样用、哪些判断被修正 | [四项目实用回收](docs/project-trials.md) |
| 按作品学习关卡与误导设计 | [《疑案追声》策划学习包](docs/case-studies/unheard/README.md) |
| 研究公开信息、随机应变与构筑取舍 | [《杀戮尖塔》一代设计研究](docs/case-studies/slay-the-spire/README.md) |
| 检查原始出处与适用条件 | [来源卡](skills/game-design-development/references/sources.md) · [结构化来源表](skills/game-design-development/references/sources.json) |
| 看一个具体设计推演 | [《雨夜送信》虚构例子](skills/game-design-development/references/worked-example.md) |
| 审阅待验证方法 | [候选方法清单](docs/candidates.md) |
| 将作品分析转成可检验的策划经验 | [跨案例方法](skills/game-design-development/references/case-derived-planning.md) · [案例证据范围](skills/game-design-development/references/case-observations.json) |
| 社区经验与读取范围 | [小红书补充研究](skills/game-design-development/references/community-notes.md) |
| 区分外部材料与个人认可 | [知识采纳规则](skills/game-design-development/references/knowledge-adoption.md) |
| 查看本 Skill 如何验证 | [验证记录](docs/validation.md) |

## 覆盖与边界

主要内容是关键动作、玩法循环、信息与决策、风险收益、机制相互作用、复杂度与深度、成长奖励、教学关卡、挑战节奏、重复可玩性和玩法原型。策略、操作、表达、创作和放松可以采用不同的设计目标，不要求每款作品都有资源短缺、胜负或长期成长。

规则状态、系统数值、叙事与证据支持玩法落实；工程生产、设备和发布是按需参考。运行时 AI 也是可选分支，需要说明它改变了什么可玩的行动和结果。

来源表现有 50 项一手来源记录。本轮新增 11 项，核读全文或对应设计、方法、结果与局限章节；此前 M04 仍只取得摘要。小红书仍保留此前 7 条覆盖记录（5 篇实质内容中 1 篇已排除，另有部分图文及视频元数据）。开发者经验、概念框架、实证研究与摘要的证明能力不同，来源互相引用也不算独立验证。

案例现有 9 条：此前 5 条项目分析，另有本轮 4 条实际使用回收，覆盖原作内局部操作、派遣原型运行、冻结输入的生产模型和音频解码。候选方法仍为 36 条，其中 6 条据实践修订条件与验证方式；游戏内文案另明确简洁和玩家信息范围。具体结果见 [四项目实用回收](docs/project-trials.md)。案例不并入文献计数，也没有新增个人认可或跨项目玩家效果结论。

本库仍不足以代替完整实战经验。新增三方向已有工作法和可复算例子，仍缺目标作品的实玩、多组合作观察与真实长期积累证据；触屏及更多不同能力玩家的需求仍需深入；网络同步、主机认证和发行预算也没有全面覆盖。旧文章采用有解释力的方法，版本相关规则使用前另查。

## 使用 Skill

将 `skills/game-design-development` 整个目录复制到 Codex 的用户技能目录，例如 `~/.codex/skills/`。可用 `$game-design-development` 显式调用，也保留正常自动发现。示例请求：“使用这个 Skill 评审当前玩法，先找最危险的假设，并完成一个能验证它的原型。”

`assets/templates` 的模板按需使用。私有学习库的位置可放在用户目录的 `game-design-development.local.json`，不要把个人路径、认可记录或项目私密数据提交到本库。外部来源、项目实验和用户认可分别保存；本库不包含个人认可台账。

## 更新与引用

来源保留作者、日期精度、访问日、读取范围、主张与限制。新增综合建议要回指来源并写明验证办法，原作仍按原站许可；本库只保存简短原创摘要与链接，不分发原论文、课件、截图或平台全文。

检查资料结构可运行 `python tools/validate_library.py`；Skill 格式另用当前环境的 `skill-creator` 校验器检查。结构检查通过不等于方法已被玩家或市场验证。未指定统一的下游再授权条款；需要复用时区分本库原创整理与所链接原作，并确认各自权限。
