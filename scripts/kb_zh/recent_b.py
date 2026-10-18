"""Simplified Chinese translations of kb_recent.RECENT_UPDATES, entries [8:19].

Covers 06_vla_and_embodied_foundation_models/08_levels_of_generalization through
09_robot_platforms_and_hardware/02_humanoid_platforms.
"""

RECENT_UPDATES_ZH_B = {
    "06_vla_and_embodied_foundation_models/08_levels_of_generalization": """
近期的一些声称让“沿哪条轴泛化”这一问题变得具体：

- **π0.7：** 在没有目标平台数据的情况下，将任务组合式迁移到该机器人上（公司报告）。
- **GR00T N2 / DreamZero：** 仅凭 10–20 分钟纯视频的跨具身数据，就在未见任务上取得提升（论文）。
- **Physical Intelligence 的人到机器人迁移工作：** 迁移到仅在人类视频中出现过的任务（2025 年 12 月）。

这些结果分别对应上文分类体系中的不同行：具身形态、任务组合与数据模态。不应将它们合并为单一的“泛化”分数。

基准的发展未能跟上：

- **趋于饱和的基准：** LIBERO 已接近饱和，报告的平均成功率达到 98% 及以上。
- **分布式真实世界评测：** RoboArena（CoRL 2025）在评测者自行选择的 DROID 平台上，通过盲测成对比较对策略进行排名。这能检验开放式泛化，但除非对任务进行记录和分层，否则会混淆各条泛化轴。
""",
    "06_vla_and_embodied_foundation_models/09_language_conditioned_control": """
语言越来越多地被用作中间控制通道，而不仅仅是任务规格说明。

- **Gemini Robotics-ER 1.5、1.6 和 2**
  - 它们能分解指令、调用工具、跟踪进度并协调多台机器人。
  - 它们将自然语言步骤交给 VLA 执行。
  - ER 1.6（2026 年 4 月）新增了与 Boston Dynamics 合作开发的仪表与仪器读数能力。
- **π0.7（2026 年 4 月）** 接受混合提示：子任务文本、关于期望速度与质量的元数据，以及子目标图像。“如何去做”由此可以在测试时调控。
- **Physical Intelligence 的 MEM** 将过去事件写成文本摘要，作为长时程记忆。

这些设计使语言成为推理与控制之间可记录、可审计的接口。然而，它们也继承了语言模型的失效模式，例如自信但错误的进度报告，以及看似合理却无法执行的计划。因此，验证应包括基于实际观测的成功检测，而不能只依赖模型自身的叙述。
""",
    "06_vla_and_embodied_foundation_models/10_embodiment_scaling_questions": """
**新的规模化证据，其中大部分为公司自报**

- **Generalist AI**
  - GEN-0（2025 年 11 月）报告了真实世界预训练数据（超过 270,000 小时）与下游性能之间的幂律关系。
  - 它还报告了一个明显的容量阈值：较小的模型会“僵化”（ossify）。
  - GEN-1（2026 年 4 月）声称数据量超过 500,000 小时。
- **RoboJEPA**（2026 年 10 月）报告了在 12 种具身形态上，隐空间世界模型误差随算力变化的幂律。
- **Skild Brain**（2025 年 7 月）致力于打造一个“全具身”（omni-bodied）模型，在覆盖四足机器人、人形机器人和机械臂的仿真数据与人类视频上进行预训练。
- **X-VLA** 通过学习得到的软提示（soft prompt）对具身形态进行编码。

**人类视频作为规模化资源**

多个团队如今将第一人称人类视频视为主要数据来源：

- Physical Intelligence 的人到机器人迁移（2025 年 12 月）；
- Figure 的 Project Go-Big；
- 来自 Tesla Optimus 团队的报道。

这在一定程度上使数据增长与机器人工时脱钩。

**仍未解答的问题**

- 机器人规模化定律的独立复现。
- 对数据量、多样性与具身形态进行受控分离。
- 测得的指数在更换评测协议后是否依然成立。
""",
    "07_data_simulation_and_training/01_robot_data_bottleneck": """
**规模。** 公司自报的真实机器人数据规模在 2024 年至 2026 年间增长了一个数量级：

- Physical Intelligence：π0.5 检查点背后有超过 10,000 小时的数据。
- Ant Group 的 LingBot-VLA：约 20,000 小时。
- Generalist AI：GEN-0 超过 270,000 小时，GEN-1 超过 500,000 小时，均通过分布式的人工操作设备采集。

**实验室遥操作之外的数据采集**

- **UMI 式手持夹爪。** RDT2 使用了超过 10,000 小时的增强版 UMI 数据。
- **第一人称人类视频**，被 Physical Intelligence、Figure 的 Project Go-Big、1X 和 Tesla 采用。
- **面向消费者部署，并对未知任务进行远程“专家”遥操作。** 这是 1X NEO 公布的模式，自 2025 年 10 月起接受预订。
- **兼作数据引擎的工厂试点。** Tesla 表示，其首批 Optimus 量产机型将交付内部的“Optimus Academy”用于数据采集，而非交付客户（2026 年第二季度更新）。

瓶颈已从原始时长转向带标签的结果、失败与恢复的覆盖度，以及不同采集方之间可比的元数据。
""",
    "07_data_simulation_and_training/03_cross_embodiment_datasets": """
**2025–2026 年发布或扩充的大型异构数据集**

- **Galaxea Open-World Dataset：** 超过 500 小时的移动双臂数据，覆盖约 50 个场景。
- **AgiBot 的数据集与 Genie Sim 工具链。**
- Hugging Face Hub 上的 **LeRobot 社区数据集**。
- **BEHAVIOR-1K 挑战赛数据：** 10,000 条遥操作示范，超过 1,200 小时。
- **开源 VLA 背后的多具身预训练语料：**
  - LingBot-VLA：约 20,000 小时，来自九种双臂机器人。
  - RDT2：UMI 人类示范，旨在零样本迁移到未见过的机械臂。

**持续存在的可比性问题**

不同来源在动作约定、相机布局、成功标签和许可协议上各不相同。例如，Galaxea 曾多次更改其许可协议。

具身感知的模型组件是在吸收异构性，而非消除它。例子包括 X-VLA 的软提示、GR00T 的具身模块，以及 π 式的动作专家。
""",
    "07_data_simulation_and_training/04_simulation_platforms": """
仿真正在围绕 GPU 并行物理、开放标准和学习式世界模拟器进行整合。

**物理引擎与模拟器**

- **Newton：** 由 Disney Research、Google DeepMind 和 NVIDIA 基于 NVIDIA Warp 与 OpenUSD 构建的开源 GPU 物理引擎。它于 2025 年 9 月被贡献给 Linux Foundation，目前作为底层支撑 MuJoCo Warp 和 NVIDIA 的各模拟器。
- **NVIDIA Isaac Sim 与 Isaac Lab：**
  - Isaac Sim 5.0 与 Isaac Lab 2.2 在 SIGGRAPH（2025 年 8 月）上正式发布（GA），Isaac Sim 扩展同时开源。
  - Isaac Lab 3.0 于 2026 年 3 月进入 beta 阶段，带有 Newton 后端。
  - Isaac Sim 6.0 于 2026 年 6 月正式发布，集成了 Newton。
- **MuJoCo Playground**（RSS 2025）将 MJX 与批量渲染相结合，并报告了基于状态和基于像素两种输入的零样本仿真到现实迁移。
- **ManiSkill3** 报告其 GPU 并行操作仿真速度超过 30,000 FPS。
- **Genesis：** 其背后的公司 Genesis AI 于 2025 年 7 月成立，获得 1.05 亿美元（$105M）种子轮融资。

**任务套件**

- **RoboCasa365**（ICLR 2026）将家庭操作扩展到 365 个任务和 2,500 个厨房，包含超过 600 小时的人类示范和 1,600 小时的合成示范，并提供排行榜。
- **AgiBot 的 Genie Sim 3.0** 被用于纯仿真训练，该公司报告其可迁移到真实机器人。
- **LeRobot v0.6** 在 `lerobot-eval` 下统一了六个仿真基准。

**学习式模拟器**

学习式模拟器如今已成为一个互补类别：基于 Veo 的策略评估、Ctrl-World、Cosmos 和 Genie。由高斯泼溅构建的真实到仿真（real-to-sim）孪生同样属于此类；arXiv 2511.04665 报告，在软体任务上仿真成功率与真实成功率之间的相关系数至少为 0.897。它们提供外观真实感和低成本评测，但接触保真度仍是悬而未决的问题。
""",
    "07_data_simulation_and_training/06_synthetic_data_and_video_data": """
**合成数据与视频数据已成为工业界训练方案的核心。**

- NVIDIA 在训练 GR00T N1.5 时部分使用了由 Cosmos 生成的“GR00T-Dreams”轨迹。
- Cosmos Predict 与 Transfer 2.5（2025 年 10 月）以及 Cosmos 3（2026 年 6 月）作为开放的机器人训练视频生成器提供。
- Unitree 的 UnifoLM-WMA-0 将世界模型同时用作合成数据引擎和策略增强器。

**人类视频作为机器人行为的来源**

- Physical Intelligence 报告，在机器人预训练充分时，从第一人称人类视频的迁移能力会涌现出来。
- Figure 报告了仅从人类视频学到的语言条件家庭导航。
- 1X 在机器人微调之前，先将经网络数据预训练的视频模型适配到第一人称人类视频上。

**上文的告诫依然适用。** 不含动作的视频无法识别力、控制器状态或反事实结果。每一种此类方案最终仍以带动作标签的机器人数据收尾。解读报告的提升时，应同时考虑这部分最终机器人数据的数量。
""",
    "07_data_simulation_and_training/08_evaluation_and_benchmarks": """
评测基础设施在 2025–2026 年间的变化，超过了自 LIBERO 和 CALVIN 发布以来的任何时期。

**分布式真实机器人评测**

- **RoboArena**（arXiv 2506.18123，CoRL 2025）
  - 评测者自行选择任务和场景，在 DROID 平台上进行盲测成对 A/B 比较。
  - 偏好被汇总为全局排名。
- **RoboChallenge / Table30**（arXiv 2510.17950）：在远程实体机器人上运行提交的策略。

**大型标准化套件**

- **BEHAVIOR Challenge 2025**（NeurIPS 2025）
  - 50 个完整长度的家庭任务，采用部分得分的 Q-score。
  - 据报道，获胜方案（一个基于 π0.5 的参赛方案）得分约 26%，表明长时程家庭自主能力仍相距甚远。
- **GM-100**（上海交通大学）：100 个真实世界任务，已被多篇 2026 年的 VLA 论文用作基准。

**学习式评估器**

- 基于 Veo 的 Gemini Robotics 策略评估。
- Ctrl-World。
- RoboJEPA 的想象误差代理指标。
- 这些方法有望实现低成本的策略排名，但需要定期通过实体试验加以验证。

**饱和与新的声称**

- LIBERO 实际上已饱和，报告的平均成功率达到 98% 及以上。
- 公司在 RoboArena 或其他竞技场上的排行榜声称（例如 DreamZero 的声称），应对照该竞技场自身公布的排名及日期进行核实。
""",
    "08_manipulation_navigation_and_control/03_bimanual_and_dexterous_tasks": """
**灵巧与双臂能力如今在更长、更真实的运行中得到报告。** 以下所有结果均为公司自报。

- **Physical Intelligence π\\*0.6：** 持续数小时的意式浓缩咖啡制作、衣物折叠和纸箱组装。
- **Dyna Robotics：** 连续超过 24 小时折叠餐巾，成功率高于 99%。
- **ByteDance GR-3**（2025 年 7 月）：长时程双臂移动任务。
- **Gemini Robotics 2**（2026 年 7 月）报告了各任务的灵巧操作成功率：
  - 拧下灯泡为 92%；
  - 打开 Ziploc 密封袋约为 40%；
  - 处理垃圾袋为 44%。

这些数字既说明了进展，也表明可靠性在多大程度上仍依赖于具体任务。

**硬件与感知**

- Figure 03 增加了手掌相机和触觉指尖。
- Microsoft 的 Rho-alpha（2026 年 1 月）通过一个独立的动作专家输入触觉信号。
- OmniRetarget 从人体运动生成保持交互关系的人形机器人移动操作数据。IEEE RAS 的报道称其获得了 ICRA 2026 最佳会议论文奖。
""",
    "08_manipulation_navigation_and_control/04_long_horizon_task_execution": """
**长时程记忆与恢复得到了直接的架构层面关注。**

- **Physical Intelligence 的 MEM**（2026 年 3 月）将短时程视频记忆与自行撰写的文本摘要相结合，支持超过十分钟的任务。
- **Helix 02** 演示了一段长达四分钟、包含 61 个动作的洗碗机操作序列，全程无需重置。
- **Gemini Robotics-ER 2**（2026 年 7 月）新增了实时视频理解、进度跟踪和多机器人协调能力。

**评测证据则不那么乐观。** BEHAVIOR Challenge 2025 的获胜方案在 50 个家庭任务上仅取得约 26% 的部分得分 Q-score。

关于“8 小时自主轮班”（Figure，2026 年 5 月）的报道主要通过二手报道传播。在干预与重置统计公布之前，应将其视为未经证实。
""",
    "09_robot_platforms_and_hardware/02_humanoid_platforms": """
截至 2026 年 10 月的人形机器人平台格局。除非另有标注，所列数字均为公司声明或媒体报道。

**美国与欧洲**

- **Figure 03**（2025 年 10 月）面向量产制造和 Helix 而设计。BMW 于 2026 年 6 月宣布在 Spartanburg 部署。
- **Boston Dynamics 量产版电动 Atlas**（CES，2026 年 1 月）
  - 约 56 个自由度（DoF）。
  - 2026 年的全部产量已承诺供应给 Hyundai 的 Robot Metaplant Application Center 和 Google DeepMind。
  - Hyundai 计划到 2028 年形成每年 30,000 台机器人的产能，Atlas 将于 2028 年进入其 Georgia 工厂。
- **Apptronik Apollo 2** 是 Gemini Robotics 2 的参考平台。Apptronik 于 2026 年 2 月将其 A 轮融资追加 5.2 亿美元（$520M）。
- **Agility Digit** 正在多个站点从事物流工作。Agility 于 2026 年 6 月同意通过 SPAC 上市，声称已获得超过 3 亿美元（$300M）的多年期 Digit 订单。
- **1X NEO** 于 2025 年 10 月开放消费者预订（售价 $20,000 或每月 $499）。其 Hayward 工厂于 2026 年 4 月启用。截至 2026 年 10 月初，尚无经独立证实的消费者交付报道。
- **Tesla Optimus**
  - Tesla 正在将 Fremont 的 Model S/X 产线改造为 Optimus 生产线。
  - 首批产品用于内部数据采集。
  - 截至 2026 年 10 月中旬，Optimus V3 尚未公开亮相。
- **NVIDIA 的 Isaac GR00T Reference Humanoid**（2026 年 6 月）将 Unitree H2、Sharpa 灵巧手和 Jetson Thor 打包，供研究使用。

**中国**

- **Unitree** 推出了售价 39,900 元人民币（CNY）的 R1（2025 年 7 月）和全尺寸的 H2（2025 年 10 月）。
- 分析机构 Omdia 统计，2025 年全球人形机器人出货量约 13,000 台，其中约 90% 来自中国企业。领先者：
  - AgiBot：约 5,200 台。
  - Unitree：按 Omdia 统计为 4,200 台，而据其自身招股说明书为交付超过 5,500 台。
  - UBTech：约 1,000 台。
- 中国的大多数出货流向科研、教育、零售和娱乐领域，而非工厂劳动。
- **XPeng** 计划于 2027 年上半年交付 IRON。

**评估**

与已公布的产能相比，实际出货量仍然很小。这些平台上的视觉感知已趋同于：多相机 RGB 头部、腕部或手掌相机、用于导航的深度传感，以及越来越多的触觉指尖。
""",
}
