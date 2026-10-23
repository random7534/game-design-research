# 来源与适用限制

首版检索与核读于 2026-10-23 至 2026-10-24，以下来源访问日逐项记录。资料原意与操作建议分开；操作建议为本库综合，尚不代表玩家验证或任何人的个人认可。日期空缺保持空缺，不用检索抓取时间补写。

来源 ID 用于在方法中定位依据，机器可读版本见 [sources.json](sources.json)。社区来源只作为问题线索，完整阅读范围见 [小红书记录](community-notes.md)。

## D01 · MDA: A Formal Approach to Game Design and Game Research

- 来源：[AAAI / Northwestern author-hosted PDF](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)；作者：Robin Hunicke、Marc LeBlanc、Robert Zubek。
- 日期：2004-06-20；AAAI paper metadata。访问：2026-10-23。
- 读取：full_text_opened；证据位置：PDF p.2: definitions, designer/player perspectives；PDF pp.3-4: dynamic models and tuning；PDF p.5: conclusions。
- 原意或可见内容：机制、运行行为与玩家期望情绪体验彼此关联，设计和调优需要在这些层次之间往返。
- 本库建议：先写体验与可观察行为的因果假设，评审功能对行为的影响并用游玩观察修正。
- 限制：分析框架不提供乐趣配方；Aesthetics 不等于画风；不强制艺术探索从数值设计开始。

## D02 · Level 7: Decision-Making and Flow Theory

- 来源：[Game Design Concepts, author course](https://gamedesignconcepts.wordpress.com/2009/07/20/level-7-decision-making-and-flow-theory/)；作者：Ian Schreiber。
- 日期：2009-07-20；article footer。访问：2026-10-23。
- 读取：full_text_opened；证据位置：Things Not To Do；What Makes Good Decisions?；What About Action Games?；Emotional Decisions。
- 原意或可见内容：取舍、风险、时机与情感会影响选择价值；作者指出无影响、明显答案和缺乏信息的选择问题，也保留情感选择例外。
- 本库建议：为高频选择记录信息、代价、后果与情感价值，再检查盲猜或占优解。
- 限制：作者分类非统一标准；不能删掉全部表达性选择，刻意未知与低策略体验可有独立用途。

## D03 · Level 2: Numeric Relationships

- 来源：[Game Balance Concepts, author course](https://gamebalanceconcepts.wordpress.com/2010/07/14/level-2-numeric-relationships/)；作者：Ian Schreiber。
- 日期：2010-07-14；article footer。访问：2026-10-23。
- 读取：full_text_opened；证据位置：This Week’s Topic；Interactions Between Relationships；How Relationships Interact；If You’re Working On a Game Now…。
- 原意或可见内容：资源数值通过关系才有意义，转换链条和循环可叠加或抵消，应画图识别。
- 本库建议：列资源与转换、获取消耗、上限和重置，跑返回同一资源的循环，并按阶段检查边界。
- 限制：数值等价不能覆盖位置、操作、信息和协同；平衡不等于全部选项相等。

## D04 · Level 10: Final Boss

- 来源：[Game Balance Concepts, author course](https://gamebalanceconcepts.wordpress.com/2010/09/08/level-10-final-boss/)；作者：Ian Schreiber。
- 日期：2010-09-08；article footer。访问：2026-10-23。
- 读取：full_text_opened；证据位置：Economic Systems；Scarcity；Inflation；Trading。
- 原意或可见内容：资源生成、销毁、交换、稀缺和玩家交易行为影响游戏体验与持久世界经济。
- 本库建议：按单局、有限流程与持久世界分别检查产出消耗、囤积、交易、持有分布和进入条件。
- 限制：供需推演依赖简化假设，不能直接推断所有游戏市场；单人有限流程不必照搬 MMO 经济治理。

## D05 · The Chemistry Of Game Design

- 来源：[Gamasutra, currently Game Developer](https://www.gamedeveloper.com/design/the-chemistry-of-game-design)；作者：Daniel Cook。
- 日期：2007-07-19；article header。访问：2026-10-23。
- 读取：full_text_opened；证据位置：Chapter 3: Skill Atoms；Chaining Of Game Mechanics；Lack Of The Correct Initial Skills；Pre-mastery Of Skills Taught In The Game。
- 原意或可见内容：动作、模拟更新、反馈和玩家理解组成技能原子，技能依赖及玩家初始能力可帮助定位学习断点。
- 本库建议：教学验证玩家是否理解结果并能在变化情境独立运用，分别记录操作、观察与理解失败。
- 限制：采用其诊断模型，不把文中关于所有乐趣和神经化学的强推论当作实证定律。

## D06 · Game Design as Narrative Architecture

- 来源：[MIT author page](https://web.mit.edu/~21fms/People/henry3/games%26narrative.html)；作者：Henry Jenkins。
- 日期：未标示或未确认；webpage undated; no inferred publication date used。访问：2026-10-23。
- 读取：full_text_opened；证据位置：opening five qualifications；SPATIAL STORIES AND ENVIRONMENTAL STORYTELLING；EMBEDDED NARRATIVES；EMERGENT NARRATIVES。
- 原意或可见内容：游戏不必讲故事；空间可唤起联想、承载事件、嵌入叙事信息或支持涌现故事。
- 本库建议：把重要信息映射到可观察、可操作对象，检查发现顺序、遗漏补救及状态影响。
- 限制：空间分析不排除对白、文字和线性演出；玩家理解需要实际验证。

## D07 · Integrating Narrative and Design: A Portal Post-Mortem

- 来源：[Valve / GDC](https://cdn.fastly.steamstatic.com/apps/valve/2008/GDC2008_PortalPostMortem.pdf)；作者：Kim Swift、Erik Wolpaw。
- 日期：2008-02；Valve publications index, month precision。访问：2026-10-23。
- 读取：full_text_opened_and_selected_slides_requested；证据位置：PDF p.7: Delta Theory；PDF pp.12-14: design goals and playtesting；PDF pp.24-31: Companion Cube and incineration training。
- 原意或可见内容：团队借助游玩测试反复调整叙事和玩法，两者能够互相影响。
- 本库建议：比较角色动机、实际奖励和玩家行为，确定矛盾是否有意，并通过可玩片段验证改动。
- 限制：Portal 的少叙事策略有项目背景；不可普遍推导为删除对白或消除一切矛盾。

## D08 · The AI Systems of Left 4 Dead

- 来源：[Valve / AIIDE, Stanford University](https://cdn.fastly.steamstatic.com/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf)；作者：Michael Booth。
- 日期：2009；Valve publications index, year precision。访问：2026-10-23。
- 读取：full_text_opened_and_selected_slide_requested；证据位置：PDF pp.78-82: dramatic pacing and state cycle；PDF p.92: pacing frequency vs difficulty amplitude。
- 原意或可见内容：L4D 用强度估计调节威胁出现的节奏；该方案明确将节奏与难度分开。
- 本库建议：分别记录遭遇强度、持续时间、间隔和恢复，诊断疲劳或空白后改一个段落。
- 限制：合作生存射击案例；不要迁移具体秒数，不默认所有游戏需要自适应导演。

## PROD-01 · How to make your dream game, publish it and not die in the process

- 来源：[Godot Engine](https://godotengine.org/article/how-actually-make-your-dream-game/)；作者：Juan Linietsky。
- 日期：2017-08-11；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Making a prototype；Making a vertical slice；Developing until Alpha；Fill it with assets, go towards Beta!；Gold。
- 原意或可见内容：原型验证玩法，纵向切片验证目标质量的生产能力，完整流程需要单独完成。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：经验文章，官网提示过时；不沿用其市场断言、投资比例或无条件快速脏代码建议。阶段可按项目合并。

## PROD-02 · Saving games

- 来源：[Godot Engine documentation](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Identify persistent objects；Serializing；Some notes；JSON vs binary serialization。
- 原意或可见内容：先选持久字段；示例省略加载前游戏状态设置，嵌套对象和 JSON 类型有额外限制。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：教程示例不提供完整存档架构；版本迁移、写入中断和坏文件策略是项目所需设计。

## PROD-03 · Resource

- 来源：[Godot Engine documentation](https://docs.godotengine.org/en/stable/classes/class_resource.html)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Description；resource_local_to_scene；duplicate；duplicate_deep。
- 原意或可见内容：路径加载资源可共享缓存引用；浅复制共享嵌套对象，深复制和场景本地资源有具体条件。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：须核对项目的 Godot 版本，不能将当前 stable API 用法直接套入旧版。

## PROD-04 · General optimization tips

- 来源：[Godot Engine documentation](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：The nature of slowness；Measuring performance；Detective work；Principles；The optimization process。
- 原意或可见内容：设计时考虑性能；测量目标设备瓶颈，优化后重测，区分低帧、卡顿与加载慢。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：平均 FPS 与单台开发机不能覆盖所有性能问题；CPU profiler 也不覆盖全部 GPU 和系统开销。

## PROD-05 · Exporting projects

- 来源：[Godot Engine documentation](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Export menu；Resource options；Configuration files；Exporting from the command line。
- 原意或可见内容：仅 PCK/ZIP 数据导出不能代表可玩构建；导出需预设模板，非资源文件要检查过滤规则，凭据通常不应共享。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：构建成功仍需从实际产物启动与验证；不能仅凭 ZIP 扩展名判断可玩性。

## PROD-06 · Xbox Accessibility Guidelines V3.2

- 来源：[Microsoft Learn](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines)；作者：机构文档。
- 发布：2023-06-08；更新：2026-08-14；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Introduction；Overview of XAG components；In this section。
- 原意或可见内容：指南用于设计、实现与测试，先判断适用交互；官方明确不等于法律或合规认证。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：单个示例仅演示相关条目；清单通过不能据此宣称面向所有残障玩家完全可访问。

## PROD-07 · Making games accessible

- 来源：[Microsoft Learn](https://learn.microsoft.com/en-us/windows/uwp/gaming/accessibility-for-games)；作者：机构文档。
- 发布：未标示或未确认；更新：2026-03-03；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Is the game you are making today accessible?；Review；Playtest and iterate；Game accessibility features。
- 原意或可见内容：尽早设计并持续审查可访问性；邀请有相关需求的玩家实际游玩和反馈。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：不沿用旧人口数据或医学阈值；模拟器不能替代相关玩家的完整流程测试。

## PROD-08 · Steam Playtest

- 来源：[Valve / Steamworks](https://partner.steamgames.com/doc/features/playtest)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：How does it work?；How do I set it up?；Gathering Feedback From Players；Frequently Asked Questions。
- 原意或可见内容：可用独立关联 App ID 控制试玩分发；开发者仍需自行组织反馈与说明测试问题。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：平台渠道仅按项目目标选择；公开 Playtest 不天然保密，样本不自动代表目标市场。

## PROD-09 · Review Process

- 来源：[Valve / Steamworks](https://partner.steamgames.com/doc/store/review_process)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Overview；Reviewing Store Presence；Reviewing Product Build。
- 原意或可见内容：商店声明与所提交构建应一致，所列系统能够启动；Ready for release 为审核通过待发布状态。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：审核不替代完整质量验证；提交日需要重查政策与周期，审核通过不能称已经发布。

## PROD-10 · Steam Deck and Steam Machine Compatibility Review

- 来源：[Valve / Steamworks](https://partner.steamgames.com/doc/steamhardware/compat)；作者：机构文档。
- 日期：未标示或未确认；页面标示日期；null表示页面未标示，stable文档仍可能更新。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Compatibility Ratings；Compatibility Checklist；Requirements for Steam Deck and Steam Machine；Steam Deck Specific Requirements。
- 原意或可见内容：兼容性分级区分经过验证、需调整、无法运行与未知；输入、性能和显示须按目标设备验证。
- 本库建议：按项目阶段和风险采用，见 production.md 与系统、验证参考。
- 限制：该设备门槛不应通用于全部游戏；自测不构成 Valve Verified，兼容性审查与一般发布审查独立。

## R01 · Writing with ink

- 来源：[inkle official repository](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md)；作者：inkle。
- 日期：未标示或未确认；持续维护文档，未使用页面抓取时间代替发布日期。访问：2026-10-23。
- 读取：relevant_sections_read；证据位置：Choices；Branching and joining；Variables and Logic；Advanced: Game-side logic。
- 原意或可见内容：文档展示选择、分支汇合、变量、条件与游戏端逻辑接口。
- 本库建议：记录分支条件与持久变化，再检查汇合是否保留承诺的后果。
- 限制：工具机制不保证叙事有效；不要求全部项目改用 ink。

## R02 · Update Method

- 来源：[Game Programming Patterns, author site](https://gameprogrammingpatterns.com/update-method.html)；作者：Robert Nystrom。
- 日期：未标示或未确认；网页未标日期。访问：2026-10-23。
- 读取：chapter_text_read；证据位置：When to Use It；Objects all simulate each frame but are not truly concurrent；Be careful modifying the object list while updating。
- 原意或可见内容：分帧更新适合需随时间运行的对象，更新顺序会影响观察到的状态；棋类策略不一定适用。
- 本库建议：区分程序循环与玩法循环，定义结算顺序，按实际并行或实时需求选组织方式。
- 限制：代码范例说明模式，不是默认架构；不同游戏与引擎有不同实现。

## R03 · Generative Agents: Interactive Simulacra of Human Behavior

- 来源：[UIST 2023 / author arXiv paper](https://arxiv.org/html/2304.03442v2)；作者：Joon Sung Park、Joseph C. O’Brien、Carrie J. Cai、Meredith Ringel Morris、Percy Liang、Michael S. Bernstein。
- 发布：2023-04-07；更新：2023-08-06；arXiv v1提交与v2修订记录。访问：2026-10-23。
- 读取：abstract_architecture_and_limitations_read；证据位置：Abstract；4 Generative Agent Architecture；7.2 Boundaries and Errors；8.2 Future Work and Limitations。
- 原意或可见内容：论文用记忆、反思和计划支持可信社会行为，也报告记忆检索、地点规范和过度合作等错误。
- 本库建议：按游戏目标测行动一致、知情边界、长局记忆与失败恢复，另测成本和延迟。
- 限制：可信行为指标不能代替乐趣、留存或商业可运行性；本文未验证当前游戏。

## XHS-01 · 一人开发独游，艰难上线后的感慨

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6a96bd45000000002b01e47f)；作者：黑暗肉渣。
- 日期：未标示或未确认；页面可见 09-01，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：6/6 张图文，以及页面可见作者回复。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：作者以《陋室与猫》上线后的经历讨论个人开发对能力与工期的高估，资金不足后接外包对进度的挤占，以及缺少外部反馈对判断的影响。
- 本库建议：独立开发排期是否留出返工与生活费用？首次外部试玩安排在什么时间？正式版与演示版是否分别通过稳定性检查？
- 限制：未独立核验项目质量、销售与工期。作者末页同时称试玩版频繁崩溃且暂不修复，此做法不宜转成发布建议。

## XHS-02 · MA GameDesign 学习随记 Week3 D1

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6ac43db1000000001403ad3e)；作者：蜜桃拿铁。
- 日期：未标示或未确认；页面可见 10-06，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：完整文字正文；未读取附带的 2 张图片。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：作者记录课堂任务：选取现有电子游戏的关键机制，做成非数字游戏。跨媒介改编需要理解原作的游玩感受，并重新组织规则与反馈。小组先列举、筛选机制，再制作小原型。
- 本库建议：想保留的是哪一种玩家决策或感受？纸牌、骰子、轮次能否低成本测试它？哪些机制依赖实时操作，不能用纸面结果代替数字原型验证？
- 限制：属于个人课堂记录。正文转引的论文及具体桌游分析尚未核验，不能作为原始学术证据。

## XHS-03 · 把游戏创意变成可玩的样子：5分钟原型流程

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6915ded30000000004015346)；作者：全栈爱好者。
- 日期：未标示或未确认；页面可见 2025-11-13。。访问：2026-10-23/2026-10-24。
- 读取：文字正文及 5/5 张图文。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：笔记把玩法拆成玩家动作、系统反馈与目标，先做输入、对象变化、计分和重玩；使用占位资源，并以计时或固定路线替代复杂行为，以便快速试验。
- 本库建议：本轮只验证哪一个假设？简化掉的系统会不会恰好决定玩法成立？玩家是否能理解选择、反馈并主动重试？
- 限制：未展示可运行产物、计时记录或试玩结果。“5 分钟”只能视为作者的练习时间盒，不能作为完整开发估时；单人短试玩也不能证明乐趣或市场需求。

## XHS-04 · 独立游戏参加游戏展会的经验复盘和建议指

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6a72c5a70000000035016f2e)；作者：四无。
- 日期：未标示或未确认；页面可见 08-05，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：前 7/30 张图片，含封面；未读后 23 页，不推断全文结论。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：作者对比《白蛇之子》与另一项目的活动数据，区分展示、商店访问和后续转化；也提醒统计周期、产品阶段、素材与受众不同会影响比较。
- 本库建议：活动要增加曝光、吸引目标玩家，还是促成试玩？是否有访问、试玩和愿望单等后续数据？比较时的周期与入口是否一致？
- 限制：未读取原始后台，两个项目也不构成可控实验。不能据此给出通用点击率标准，或断定某种题材、某场展会必然更好。

## XHS-05 · 独立游戏开发者们，别再参加gamejam了

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6ab777d40000000018029bc8)；作者：喷喷Dvion。
- 日期：未标示或未确认；页面可见 09-26，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：完整文字正文。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：作者称自己的 Jam 原型被复制，维权挤占开发时间；正文也承认 Jam 对练手、社交和完成小项目仍有价值。可提取的问题是公开原型的范围、时机与证据保存。
- 本库建议：公开的是视频、可执行文件还是源码？素材授权、版本记录与首次公开时间是否保存？交流收益是否值得当前项目承担相应成本？
- 限制：侵权经过、其他案例与法律判断未独立核验。不能从这篇自述推导出普遍退出 Game Jam 的建议，也不据此作法律结论。

## XHS-E01 · 做了两年独立游戏，还是失败了

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6aace481000000001103a0d3)；作者：吗喽爱炫砂糖橘。
- 日期：未标示或未确认；页面可见 09-18，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：完整文字正文及页面首屏公开评论。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：该复盘未给出可以独立核对的作品信息，本库不采用其销量、收入或失败归因。
- 本库建议：只记录核查范围，不采用未核实的事实与归因。
- 限制：实质阅读但证据不足，保留为核查范围记录，不作为事实案例。

## XHS-E02 · 开发独立游戏的第二次失败

- 来源：[小红书公开笔记](https://www.xiaohongshu.com/explore/6ac73a90000000001403860b)；作者：开发游戏的couple。
- 日期：未标示或未确认；页面可见 10-08，未显示年份。。访问：2026-10-23/2026-10-24。
- 读取：标题、标签、封面和页面可见评论；没有读取视频叙述或完整字幕。；证据位置：浏览器可见公开页面；详见 xhs-research.md。
- 原意或可见内容：未核验视频正文，不提取内容结论。
- 本库建议：只记录核查范围，不采用未核实的事实与归因。
- 限制：不提取该视频的收入、销售、开发过程与因果结论，不计入实质阅读的 5 篇。

## G01 · Ask the Developer Vol. 11, Super Mario Bros. Wonder — Chapter 1

- 来源：[Nintendo UK](https://www.nintendo.com/en-gb/News/2023/October/Ask-the-Developer-Vol-11-Super-Mario-Bros-Wonder-Chapter-1-2460393.html)；作者：Takashi Tezuka、Shiro Mouri、Koichi Hayashida、Masanobu Sato、Koji Kondo。
- 日期：2023-10-17；article header: 17/10/2023。访问：2026-10-24。
- 读取：玩法构想、机制原型、惊喜与愉悦、通常规则与变化反馈；证据位置：Chapter 1: developer direction and hidden surprises questions；Tezuka: at least one surprising or delightful element per course；Hayashida: idea-sharing session, bending pipe prototype, Wonder prototype meetings；Sato: trust in normal pipe behavior and the Wonder effect。
- 原意：团队以原型探索关卡变化带来的惊喜，并通过通常规则与奇异变化的区分维护玩家理解。
- 本库建议：把点子写成可操作变化，比较规则变体，保留产生趣味的部分并呈现新规则生效的迹象。
- 限制：惊喜无需转化为策略或成长；不能照搬无限定开发期限与大量创意的预算条件。

## G02 · New World Order

- 来源：[Wizards of the Coast / Making Magic](https://magic.wizards.com/en/news/making-magic/new-world-order-2011-12-05)；作者：Mark Rosewater。
- 日期：2011-12-05；article header: Dec 5, 2011。访问：2026-10-24。
- 读取：理解复杂度、盘面复杂度、策略复杂度、规则负担分配；证据位置：A Complex Problem: Comprehension Complexity, Board Complexity, Strategic Complexity；Common Knowledge: rarity and complexity allocation；A Whole New World: bookkeeping and incentives。
- 原意：理解文字、追踪交互和策略运用属于不同复杂度；文字简明不保证局面易懂，复杂度应有用途与分配。
- 本库建议：对同一玩法分别检查能否读懂、能否跟踪、能否灵活运用，优先减少无趣记账与例外。
- 限制：稀有度方案依赖 Magic 环境；策略不是所有游戏的主要价值；原文图形为示意，不是数据。

## G03 · Living in Synergy

- 来源：[Wizards of the Coast / Making Magic](https://magic.wizards.com/en/news/making-magic/living-synergy-2013-02-25)；作者：Mark Rosewater。
- 日期：2013-02-25；article header: Feb 25, 2013。访问：2026-10-24。
- 读取：构件组合、机制依赖、多种解法、交叉用途、解题与发现；证据位置：Synergy Hides Complexity；Synergy Increases Skill and Strategy；Synergy Whiz: Build Dependencies Into the Structure；Create Answers for Your Dependencies；Crisscross Your Solutions；Layer Your Solutions；Create Resources That Can Be Harnessed。
- 原意：从机制需求创造多种解法，并让解法跨机制复用，可以形成协同与发现；复杂度不与技巧简单成正比。
- 本库建议：为玩法需求设计不同办法，以构件和情境的小表检查新用途、重复与无用组合；谜题可逆推巧思条件。
- 限制：组合增加仍须检查理解负担和唯一最优解；不据其总体观点认定所有游戏都需要技能成长。

## G04 · Balancing Multiplayer Games, Part 2: Viable Options

- 来源：[Sirlin.Net](https://www.sirlin.net/articles/balancing-multiplayer-games-part-2-viable-options)；作者：David Sirlin。
- 日期：2014-08-15；article header: August 15, 2014。访问：2026-10-24。
- 读取：行动与回应、反制、支配行动、功能差异、局部与整体平衡；证据位置：Yomi Layer 3: Honda/Ken example and generalized options；Local vs. Global Balance；Checkmate Situations；Lame-duck Situations；Explore the Design Space；Wheat from the Chaff。
- 原意：行动、反制和变招可形成相互制约的可行选项；局部不必公平，但漫长的胜负已定阶段会削弱体验。
- 本库建议：对高频强行动检查有效条件、识别迹象、回应代价和变招弱点，并通过距离、位置、时机等功能差异扩大实际用途。
- 限制：面向竞争玩法；不机械要求三层反制，不要求局部与终局处处机会相等，不推广为全部游戏的目标。


## 2026-10-24 深化研究

本轮新增 14 条记录，其中 13 条读取了正文或相关方法、结果与局限章节，M04 仅为摘要级补充。开发者经验、概念文章、实证与理论使用研究分别标注，不按篇数计算独立验证。

### Q01 · Prototypes & Vertical Slice

- 来源：[Let's Talk About Production / author newsletter](https://ltpf.ramiismail.com/prototypes-and-vertical-slice/)；作者：Rami Ismail。
- 日期：2022-09-26；文章标题下标示日期。 访问：2026-10-24。
- 读取：正文全文；采用设计疑问、原型保真度和生产切片段落，不采用其素材侵权建议、融资时长或发行商普遍判断。
- 证据位置：Should you make the game? paragraphs 1–5；Can you make the game? paragraphs 1–7。
- 原意：作者将原型用于回答设计疑问，按问题选择资产与组合范围；纵向切片检验生产，并用下一代表单元校准制作成本。
- 本库建议：列出测试决定、必须保留的变量及会使观察失效的简化，分别报告玩法证据与生产证据。
- 限制：开发者经验文，非实验结论；可合并小项目阶段，不把单个单元耗时线性外推为完整工期。

### Q02 · In Search of Lost Time: On Game Goals and Failure Costs

- 来源：[Foundations of Digital Games 2010 / author-hosted paper](https://jesperjuul.net/text/losttime/)；作者：Jesper Juul。
- 日期：2010-06；作者页文献头注明 FDG conference, Monterey, CA, June 2010；保留月份精度。 访问：2026-10-24。
- 读取：摘要、正文七节、结论与参考文献全文；图示说明已读，图6明确为假设游戏的模拟，未当作玩家实测。
- 证据位置：sections 2–3: difficulty and lost time；section 4: Permanent and Transient Goals；sections 5–7: failure communication, repetition, limitations。
- 原意：作者用时间投入、重试体验与失败表达分析失败成本，并区分持续可完成的目标与一局即结算的目标。
- 本库建议：分别诊断挑战要求、重试负担和目标结构，再比较检查点、反馈及重试变化。
- 限制：概念分析及作品例子，不提供普遍最优惩罚值；未采用低失败成本是大众成功条件的推测；重试时间不自动等于浪费，随机变化也不必然改善体验。

### F01 · Celeste & Forgiveness

- 来源：[Maddy Makes Games](https://www.maddymakesgames.com/articles/celeste_and_forgiveness/index.html)；作者：Maddy Thorson。
- 日期：未确认；所读作者网页未显示发表日期；说明内容来自作者早前的 Twitter thread，不据搜索抓取日期推断发表日期。 访问：2026-10-24。
- 读取：十个小节与结语正文全文；嵌入动图未逐帧核读。
- 证据位置：1. Coyote Time / 2. Jump Buffering；4. Jump Corner Correction / 5. Dash Corner Correction；10. Stamina Refunds；结语：时间或位置窗口。
- 原意：作者描述边界输入的时间与空间宽容；落地前跳跃缓冲例子含按下并保持条件，相近动作可短时转换并返还消耗。
- 本库建议：分别规格化时间与空间容错，并用误差被吸收和意图被错误改写两类情境测试。
- 限制：特定平台游戏的作者案例；无对照实验，不提供通用容错参数；此处未独立运行游戏验证。

### F02 · Combat Canceled: God of War & Action Game Design

- 来源：[Game Developer / Gamasutra（经作者允许转载并改编自 Pushing Buttons）](https://www.gamedeveloper.com/game-platforms/combat-canceled-i-god-of-war-i-action-game-design)；作者：Eric Williams。
- 日期：2008-02-15；转载网页正文署名旁日期；不声称是原博客首次发表日期。 访问：2026-10-24。
- 读取：正文全文，包含定义、伪代码例子、作品比较与作者对 God of War 设计的说明；未核验文中其他作品具体行为。
- 证据位置：What Is It, Exactly?：Partial / Complete、Buffer / Instant；The Effects Of Implementation；God Of War And Its Intended Audience：L1+Button specials 限制理由。
- 原意：作者将取消时机与指令缓冲分开，并说明战神强招限制早期取消承担平衡和风险教学作用。
- 本库建议：为各动作阶段编写转换与退款表，检查命中、落空后取消如何改变压制和行动风险。
- 限制：作者自己的项目为参与者经验；其他作品论述包含作者推测；旧作具体数量、帧数及普遍比例不作为通用设计标准。

### F03 · Clarity in League

- 来源：[Riot Games / League of Legends](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/)；作者：bananaband1t。
- 日期：2021-03-12；正文显示 2021-03-12T16:00:00.000Z。 访问：2026-10-24。
- 读取：主体正文全文，包括层级、轮廓、技能、外观、地图和变身段落；轮播媒体未逐项打开，不声称覆盖所有图示案例。
- 证据位置：The Unbreakable Vows；Abilities / hierarchy rules；Filling Up Buckets；Abilities：clarity parity；Cosmetic Animations。
- 原意：团队将反馈优先级与玩法重要性相连，同时控制噪声、判定误读和外观变化造成的识别成本。
- 本库建议：按危险与可回应性排提示优先级，在重叠场面和外观变体中检查信号含义是否仍一致。
- 限制：竞技 MOBA 的官方目标与案例，非效果量研究；不强制叙事或恐怖作品公开所有信息。

### F04 · Opinion: Dealing With Designer Input Latency

- 来源：[Game Developer / Gamasutra（转载自 AltDevBlogADay）](https://www.gamedeveloper.com/design/opinion-dealing-with-designer-input-latency)；作者：Norm Nazaroff。
- 日期：2011-04-18；转载网页正文显示日期；不声称是原文首次发表日期。 访问：2026-10-24。
- 读取：正文全文：输入事件与状态、长按、双击、状态变更、缓冲、打断和结语；未实测举例游戏。
- 证据位置：How Do We Create Designed Latency?；Dealing With Holds；Dealing With State Changes；Buffering Is Helpful；They Go Together Like Lamb And Tuna Fish。
- 原意：输入识别和状态规则本身可制造等待；输入保留过久可能在意图改变后执行，复用按钮也可能误判意图。
- 本库建议：明确按下/松开/持续状态、保留期、替换和清理条件，区分收到输入与允许执行。
- 限制：作者意见文，以数字手柄按钮为范围；原文时间估计无此处可用的测量依据；长按并非只能等松开才响应；作者引用 F02，因此二者相关内容不计为独立验证。

### L01 · Puzzle Level Idea Strategies

- 来源：[Patrick Traynor personal website](https://cwpat.me/misc/puzzle-level-idea-strategies/)；作者：Patrick Traynor。
- 日期：2022-07-14；HTML article heading displays 2022-07-14 访问：2026-10-24。
- 读取：Read entire HTML article text, including Other notes; illustrations were not separately examined.
- 证据位置：Find an interaction and force it；Enumerate action sequences；Create a possible level, then make it impossible；Keep your eyes open for things almost happen moments；Turn alternate solutions into separate levels；Other notes: Investigate variations while iterating。
- 原意：Puzzle ideas can be sought through required interactions, changed sequences and constraints, boundary cases, tester misunderstandings, near-solutions and alternate solutions. Many drafts will not become good puzzles.
- 本库建议：Record an intended discovery, build a minimal scenario, investigate a small set of transformations, and preserve unexpected solutions as possible material for further puzzles.
- 限制：A personal toolkit with acknowledged contributors, not an exhaustive or experimentally ranked method. A required interaction suits focused discovery; unrestricted systems may benefit from multiple valid solutions. Do not copy another game's level layouts.

### L02 · Puzzle Dependency Charts

- 来源：[Grumpy Gamer](https://grumpygamer.com/puzzle_dependency_charts/)；作者：Ron Gilbert。
- 日期：2014-08-10；Article displays Aug 10, 2014 访问：2026-10-24。
- 读取：Read full HTML article text. Did not separately inspect all diagram image contents.
- 证据位置：Definition paragraph: graph nodes are puzzles or steps and edges indicate prerequisites；Basement example: unlocking and oiling can be pursued in parallel；Sub-diamond expansion and contraction；Acts ending in a bottleneck。
- 原意：Prerequisite graphs expose parallel puzzles and bottlenecks; the author designs backwards from the end of a puzzle chain and groups adventures into acts.
- 本库建议：Map actual prerequisites, inspect what remains available when the player is stuck, and distinguish these hard conditions from recommended play order or clue links.
- 限制：Adventure-game practice and strong personal preferences. A suggested two-or-three branch structure and rejection of linearity are not universal rules. Graph structure alone cannot establish puzzle quality.

### L03 · Outer Wilds: A Game of Curiosity-Driven Space Exploration

- 来源：[University of Southern California, School of Cinematic Arts; original thesis accessed through a PDF mirror](https://sbekumod.github.io/Assets/OWtesi.pdf)；作者：Alex Beachum。
- 日期：2013-05；PDF title page: May, 2013; DataCite Issued: 2013-04-30. Preserve both records without inventing a combined exact date. 访问：2026-10-24。
- 读取：Read extracted text of all 29 mirror PDF pages, revisiting truncated sections; figures not visually audited. USC catalog returned 403; DOI identity subsequently verified through DataCite API.
- 证据位置：pp.9–11 A Web of Curiosities: knowledge-based access；pp.13–15 Exploring the 4th Dimension / Knowledge Over Agency；pp.18–21 A Flawed Introduction；pp.21–24 Welcome to the Space Program / Building Models；pp.25–27 Future Extensions and Conclusions explicitly state most POIs/Curiosities are not implemented；Identity: https://api.datacite.org/dois/10.25549/usctheses-c3-248860。
- 原意：The thesis proposes a knowledge-led exploration network and reports failed and revised introductions. Early forced tasks did not convey the intended use of tools or prepare players for flight. Familiar local context and interactive models helped in the author's playtest observations.
- 本库建议：Distinguish learned knowledge from system unlock flags; compare tutorial actions with actual gameplay use; test whether a discovery creates an investigable question for players entering in different orders.
- 限制：2013 student version; most proposed knowledge network was not implemented. Teaching observations involved multiple simultaneous changes, not controlled causal evidence. Bibliographic identity checked against DataCite; mirror has not been compared with official PDF bytes.

### L05 · Why Adventure Games Suck And What We Can Do About It

- 来源：[Grumpy Gamer](https://grumpygamer.com/why_adventure_games_suck/)；作者：Ron Gilbert。
- 日期：2004-05-12；Web republication displays May 12, 2004; introductory paragraph and article copyright identify original writing as 1989 访问：2026-10-24。
- 读取：Read full HTML text including the 2004 preface and entire republished essay.
- 证据位置：2004 preface: author no longer agrees with everything；End objective needs to be clear；Live and learn；Backwards Puzzles；I forgot to pick it up；Real time is bad drama；Give the player options。
- 原意：For story adventures the author recommends intelligible objectives, motivated prerequisites, survivable learning and alternative puzzles when stuck. He explicitly acknowledges exceptions and later disagreement with some original claims.
- 本库建议：Audit whether a solution requires unavailable or unknowable information and whether blocked progress offers useful alternatives; evaluate these recommendations against the intended experience and the game's retry structure.
- 限制：1989 adventure-game context with a 2004 qualifying preface. Opposition to death-based learning or independent world time is not suitable as a universal rule, particularly for deliberately repeated observation and time-loop structures.

### M01 · The Motivational Pull of Video Games: A Self-Determination Theory Approach

- 来源：[Motivation and Emotion / Springer; author PDF hosted by Center for Self-Determination Theory](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf)；作者：Richard M. Ryan、C. Scott Rigby、Andrew Przybylski。
- 日期：2006；原 PDF 标注 2006，保留年份精度；未确认精确出版日。DOI: 10.1007/s11031-006-9051-8 访问：2026-10-24。
- 读取：已取得全文，核读概念、Studies 1–4 方法和主要结果、总讨论和局限；未重算统计。
- 证据位置：PDF pp. 3–4: theory and constructs；PDF pp. 5, 8, 10, 12: methods；PDF pp. 12–14: Study 4 measures and results；PDF pp. 15–16: general discussion and limitations。
- 原意：需求满足与体验和未来意向有关；第一项含当场继续/换游戏的行为选择，第四项未来游玩以自报计划月份测量。
- 本库建议：将行为、体验、意愿和真实回访分别记录；以需求概念生成具体设计问题，避免直接当机制配方。
- 限制：学生与自选 MMO 社区样本；需求主要为问卷测量，游戏安排随机化不等于操纵需求。原 PDF 部分样本总数与分项不齐，未核正误表，不统一各指标样本量。未证实任意机制的因果作用或长期留存。

### M02 · Iwata Asks: Animal Crossing: New Leaf — 2. Being the Mayor

- 来源：[Nintendo](https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Animal-Crossing-New-Leaf/Animal-Crossing-New-Leaf/2-Being-the-Mayor/2-Being-the-Mayor-738645.html)；作者：Satoru Iwata、Aya Kyogoku、Isao Moro、Koji Takahashi。
- 日期：2012-10-31；同一访谈第 1 章编者注注明日本原刊日期；日期不代表英语网页发布日期。 访问：2026-10-24。
- 读取：已读第 1、2 章正文；本记录以第 2 章设计过程为主。
- 证据位置：Chapter 2: shop hours and the player's circumstances；Chapter 2: mayor duties and easy-going life；Chapter 2: public works completion ceremony and refusal；Chapter 1 editor note: original publication date。
- 原意：开发者讲述作息适配、履职自由和完工仪式；拒绝仪式仍有角色失落回应。
- 本库建议：为自定目标提供可操作材料和成果回应，并检查拒绝或结束后的实际反馈是否符合目标体验。
- 限制：具体作品的开发者叙述，没有对照实验；情感压力分析为本轮推断，不能声称所有玩家都作相同理解。

### M03 · Self-Determination Theory and HCI Games Research: Unfulfilled Promises and Unquestioned Paradigms

- 来源：[arXiv author preprint, v1](https://arxiv.org/html/2405.12639v1)；作者：April Tyack、Elisa D. Mekler。
- 日期：2024-05-21；arXiv:2405.12639v1，2024-05-21；提交页标注 TOCHI 接收并关联 DOI 10.1145/3673230，本次仍仅引用已读 v1。 访问：2026-10-24。
- 读取：核读理论定义、文献筛选及编码、结果、设计讨论和局限；未逐一核读被引研究。
- 证据位置：Section 5.1 and Table 2；Section 8.2；Sections 9.1–9.2；Section 11。
- 原意：259 篇 HCI 游戏论文的分析指出浅层理论应用问题，倡导明确用途与情境；语料止于 2021 年。
- 本库建议：要求每个动机概念指出它改变了哪项设计、预期现象和失败条件；把退出与重新进入也纳入自主性的考虑。
- 限制：研究对象是理论使用，无法证明 SDT 无效或某种玩法优劣；选刊与 GDC 材料有限，引用方式也不能完全代表真实设计实践。

### M04 · Towards understanding the effects of individual gamification elements on intrinsic motivation and performance

- 来源：[Computers in Human Behavior / Elsevier; University of Basel institutional record](https://edoc.unibas.ch/entities/publication/ccec8ccc-aa54-417d-b205-334b518d6eed)；作者：Elisa D. Mekler、Florian Brühlmann、Alexandre N. Tuch、Klaus Opwis。
- 日期：2017-06；出版商记录为 Volume 71, June 2017, pp.525–534，保留月份精度；不采用机构库可能占位的 2017-01-01。 访问：2026-10-24。
- 读取：已核读机构库摘要和出版商记录；未获得可读全文。作者学位论文旧链接重定向后要求登录，停止获取。
- 证据位置：Institutional record: Abstract；Publisher record: Highlights and bibliographic information, https://www.sciencedirect.com/science/article/abs/pii/S0747563215301229。
- 原意：该图像标注研究中，游戏化元素增加产出数量，未检出胜任感或内在动机的显著变化。
- 本库建议：将产出数量和体验效果分开评估；只作摘要级补充，不据此制定奖励的普遍规律。
- 限制：样本量、排除规则、效应量和具体实现本轮未从正文核实；非游戏任务，不能直接外推娱乐游戏或解释无显著差异为完全无影响。
