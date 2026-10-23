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
