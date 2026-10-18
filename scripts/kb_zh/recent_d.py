"""Simplified Chinese translations of kb_recent.RECENT_UPDATES, part D (entries [35:])."""

RECENT_UPDATES_ZH_D = {
    # ------------------------------------------------------------ 10 frontier
    "10_frontier_2024_2026/00_state_of_the_field": """
**研究现状快照，2026 年 10 月 18 日**

- “推理器 + 执行器”的分层式 VLA 已成为标准架构。
- 在若干工业技术栈中，人形机器人的全身控制已实现端到端学习。
- 对 VLA 进行强化学习（RL）微调（RECAP、πRL、SimpleVLA-RL）已成为常规做法。
- 视频生成式世界模型如今被用作数据引擎、评估器，并在世界-动作模型（world action model）中充当策略骨干网络。
- 开放模型（openpi、GR00T N1.7、X-VLA、SmolVLA、RDT2、LingBot）与 LeRobot 使其中许多思路得以复现。

**产业现状快照，2026 年 10 月 18 日**

- **资本处于历史最高水平。** 据 Crunchbase 统计，仅 2026 年上半年机器人领域风险投资就约达 $18.8B，超过 2025 年全年总额。
- **估值高企：**
  - Figure：$39B（2025 年 9 月）。
  - Skild AI：超过 $14B（2026 年 1 月）。
  - Physical Intelligence：据报道约 $11B（2026 年）。
- **首批人形机器人厂商已进入公开市场：**
  - Unitree 于 2026 年 8 月 19 日在上海科创板上市，首日收盘市值约 342B CNY。
  - Agility 已达成一项 SPAC 交易。
  - AgiBot 与 Galbot 正在筹备香港上市。
- **部署数量仍以千台计，能力证据仍主要为公司自报。**
  - 2025 年全球人形机器人出货量约 13,000 台。
  - 中国国家发展改革委（NDRC）于 2025 年 11 月就 150 余家人形机器人企业的泡沫风险发出警示。

**差距所在。** 决定性的差距在于：一侧是资本与演示，另一侧是经独立测量、计入人工干预的可靠性。
""",
    "10_frontier_2024_2026/04_spatial_intelligence": """
**具身推理模型如今会给出显式的空间输出。**

- **Gemini Robotics-ER 1.5、1.6 与 2** 输出点、边界框、轨迹以及成功与否的判断。
- **NVIDIA 的 Cosmos Reason 2**（2026 年 1 月）新增了 2D 与 3D 点定位能力。
- **MolmoAct** 生成具备深度感知的词元以及图像空间中的路径点规划。

**来自前馈模型的几何。** 在视觉方面，前馈式 3D 与 4D 重建已快到足以充当空间前端。CVPR 2025 最佳论文 VGGT 与 CVPR 2026 最佳论文 D4RT（从视频进行前馈式动态重建）是其中的里程碑；详见 3D 相关笔记。

**意义所在。** 这些进展共同使上文所述“在机器人坐标系中给出空间答案”这一要求得以大规模检验。然而，基准仍很少通过实际执行的动作来验证空间答案。
""",
    "10_frontier_2024_2026/05_world_model_vs_vla": """
**对于“世界模型还是 VLA”这一问题，2026 年的答案日益趋向“二者合于同一网络”。**

世界-动作模型（world action model）联合预测未来观测与动作。示例包括：

- NVIDIA 的 DreamZero，即 GR00T N2 预览版的基础；
- Cosmos 3；
- 1X 的“视频 + 逆动力学”世界模型；
- Unitree 的 UnifoLM-WMA-0。

在这些系统中，动作学习在一定程度上转化为基于想象未来的逆动力学问题。

**潜在预测式方案保留了二者的分离。** V-JEPA 2-AC、RoboJEPA 与 AMI Labs 在表征空间而非像素空间中进行规划，并保留独立的规划器。

**可问责性。** 上文所论证的区分——架构上的可问责性——依然适用。联合模型应报告：

- 其能力中有多少来自视频先验、多少来自动作数据；
- 控制频率（DreamZero 报告的闭环频率为 7 Hz）；
- 在执行前是否将想象的推演与现实进行核对。
""",
    "10_frontier_2024_2026/07_future_roadmaps": """
**以 2026 年 10 月的证据检验 2026 年 6 月的路线图**

- **分层架构、连续动作头与端侧推理：** 按预期取得进展。
- **世界模型作为数据引擎：** 实现速度快于预期。此外，世界模型还成为评估器与策略骨干网络。
- **恢复与无人值守运行：** 仍是证据最为薄弱的能力。

**近期值得关注的事项（截至 2026 年 10 月 18 日）**

- **GR00T N2：** NVIDIA 承诺于 2026 年底前发布。
- **Tesla Optimus V3** 的发布亮相及实际产量。
- **1X NEO** 首批面向消费者的交付。
- **Agility 的公开上市**（继其 SPAC 交易之后）。
- **AgiBot 的香港 IPO。**
- **CoRL 2026**，于奥斯汀举行，11 月 9–12 日。
- **第二届 BEHAVIOR 类挑战赛的结果**（如举办）。
- **ISO 25785-1：** 这一面向动态稳定型工业移动机器人的安全标准的进展；该标准此前仍处于委员会草案阶段。
""",
    # ---------------------------------------------------------- 11 resources
    "11_datasets_papers_labs/01_must_read_papers": """
2025 年中至 2026 年 10 月新增的必读文献，按主题分组。

**策略与 VLA**

- **π\\*0.6 / RECAP**（arXiv 2511.14759）：面向 VLA 的、基于经验与纠正的强化学习。
- **TRI, "A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation"**（arXiv 2507.05331）。
- **SmolVLA**（arXiv 2506.01844）。
- **X-VLA**（arXiv 2510.10274，ICLR 2026）。
- **RDT2**（arXiv 2602.03310，ICML 2026）。
- **MEM：多尺度具身记忆（multi-scale embodied memory）**（arXiv 2603.03596）。

**世界模型**

- **V-JEPA 2**（arXiv 2506.09985）：支持动作条件规划的自监督视频世界模型。
- **Dreamer 4**（arXiv 2509.24527）。
- **Ctrl-World**（arXiv 2510.10125，ICLR 2026）。
- **在 Veo 世界模拟器中评估 Gemini Robotics 策略（Evaluating Gemini Robotics policies in a Veo world simulator）**（arXiv 2512.10675）。
- **DreamZero: World Action Models are Zero-shot Policies**（arXiv 2602.15922）。
- **RoboJEPA**（arXiv 2610.10515）。

**面向 VLA 的强化学习**

- **SimpleVLA-RL**（arXiv 2509.09674）。
- **πRL**（arXiv 2510.25889）。

**评估**

- **RoboArena**（arXiv 2506.18123，CoRL 2025）。

**获奖论文**

- **OmniRetarget**（据报道获 ICRA 2026 最佳会议论文奖）。
- **"Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning"**（ICRA 2026 机器人学习最佳论文奖）。
- **D4RT**（CVPR 2026 最佳论文）：前馈式 4D 重建。

**感知与几何**

- **VGGT**（CVPR 2025 最佳论文）。
- **MASt3R-SLAM**（CVPR 2025）。
- **CUT3R**（CVPR 2025）。
- **π³**（ICLR 2026）。
- **MapAnything**（3DV 2026）。
- **Depth Anything 3**（arXiv 2511.10647）。
- **FoundationStereo**（CVPR 2025）。
- **DINOv3**（Meta，2025 年 8 月）。
- **SAM 3: Segment Anything with Concepts**（ICLR 2026）。
- **EgoDex**（ICLR 2026）。
""",
    "11_datasets_papers_labs/02_major_labs_and_companies": """
截至 2026 年 10 月的产业状况。融资数字为公告时所报数据；除非另有说明，估值均为投后估值。

| 机构 | 方向 | 最新已核实里程碑 |
|------|------|------------------|
| Physical Intelligence | VLA 基础模型 | π\\*0.6（2025 年 11 月）、π0.7（2026 年 4 月）、API 公测（2026 年 10 月）；以约 $5.6B 估值融资 $600M（2025 年 11 月）；据报道 2026 年完成约 $11B 估值的一轮融资 |
| Google DeepMind | Gemini Robotics VLA + ER | 1.5（2025 年 9 月）、ER 1.6（2026 年 4 月）、Gemini Robotics 2 / ER 2 / On-Device 2（2026 年 7 月）；合作伙伴包括 Apptronik、Boston Dynamics、Agile Robots |
| NVIDIA | 算力、仿真、GR00T、Cosmos | Jetson Thor 正式发售（2025 年 8 月）；GR00T N1.6/N1.7、N2 预览版；Cosmos 3（2026 年 6 月）；Newton 物理引擎（Linux Foundation，2025 年 9 月）、Isaac Lab 3.0 测试版（2026 年 3 月）、Isaac Sim 6.0（2026 年 6 月） |
| Figure AI | 人形机器人 + Helix | $39B 估值 C 轮（2025 年 9 月）；Figure 03（2025 年 10 月）；Helix 02（2026 年 2 月）；BMW Spartanburg 工厂部署（2026 年 6 月） |
| Tesla | Optimus | Fremont 产线改造；首批机器人用于内部数据采集；V3 尚未发布（2026 年 10 月） |
| Boston Dynamics / Hyundai | 电动版 Atlas | 量产版 Atlas（2026 年 1 月）；与 TRI 合作的 LBM 全身控制演示（2025 年 8 月）；Hyundai 目标为 2028 年前形成年产 3 万台机器人的产能 |
| Skild AI | 全具身（omni-bodied）机器人大脑 | Skild Brain（2025 年 7 月）；以超过 $14B 估值融资约 $1.4B（2026 年 1 月） |
| Generalist AI | 大规模真实世界数据模型 | GEN-0（2025 年 11 月）、GEN-1（2026 年 4 月）；以约 $2B 估值融资 $400M（2026 年 6 月） |
| 1X | NEO 家用人形机器人、世界模型 | 开放预订（2025 年 10 月）；世界模型（2026 年 1 月）；Hayward 工厂（2026 年 4 月） |
| Agility Robotics | Digit 物流人形机器人 | 以 $2.5B 投前估值达成 SPAC 协议（2026 年 6 月） |
| Apptronik | Apollo 人形机器人 | $520M A 轮扩展融资（2026 年 2 月）；Gemini Robotics 2 平台 |
| Unitree | 低成本人形/四足机器人 | R1（2025 年 7 月）、H2（2025 年 10 月）；科创板 IPO（2026 年 8 月 19 日） |
| AgiBot | 人形机器人、GO 系列模型 | 据 Omdia，2025 年出货量第一；GO-2（2026 年 4 月）；香港 IPO 进程（2026 年 7 月） |
| UBTech | Walker S 工业人形机器人 | 2025 年售出 1,079 台全尺寸人形机器人（年度业绩） |
| Toyota Research Institute | 大型行为模型 | LBM 研究（2025 年 7 月）；Atlas 合作 |
| Meta FAIR / AMI Labs | 潜在世界模型 | V-JEPA 2（2025 年 6 月）；AMI Labs $1.03B 种子轮（2026 年 3 月） |
| Hugging Face | 开放工具链 | SmolVLA（2025 年 6 月）；LeRobot v0.6.0（2026 年 7 月） |

其他值得关注的动向：

- SoftBank 同意以 $5.375B 收购 ABB Robotics（2025 年 10 月；尚未查到交割完成的公告）。
- Mobileye 同意以约 $900M 收购 Mentee Robotics（2026 年 1 月）。
- Microsoft 凭借 Rho-alpha 进入机器人领域（2026 年 1 月）。
- Amazon 部署的机器人突破一百万台，并发布了 DeepFleet 协调模型（2025 年 7 月）。
""",
    "11_datasets_papers_labs/03_open_source_ecosystem": """
**2025 年中以来新增的开源项目**

- **模型：**
  - `openpi`：π0、π0-FAST 与 π0.5，提供 JAX 与 PyTorch 实现。
  - SmolVLA。
  - GR00T N1.5、N1.6 与 N1.7。N1.7 可商用授权；请逐一核查每个检查点的许可证。
  - X-VLA。
  - RDT2。
  - Galaxea G0。
  - LingBot-VLA。
  - MolmoAct。
  - Unitree 的 UnifoLM-WMA-0。
  - V-JEPA 2。
  - Cosmos Predict 2.5 与 Cosmos 3。
- **工具链：**
  - LeRobot v0.6.0，包含世界模型策略、奖励模型、`lerobot-eval` 以及 DAgger 推演。
  - RLinf，用于大规模具身强化学习。
  - Newton 物理引擎。
  - MuJoCo Playground 与 MuJoCo Warp。
  - ManiSkill3。
- **评估：** 社区评测平台 RoboArena 与 RoboChallenge。

**许可证。** 许可证如今已成为一个实际的研究变量。若干模型家族将 Apache-2.0 代码与非商用权重混合发布，且部分数据集的许可证在发布后发生过变更。
""",
    "11_datasets_papers_labs/04_conference_map": """
**奖项与亮点，2025 年中至 2026 年 10 月**

- **CoRL 2025（首尔）**
  - 最佳论文：UniFP（面向足式移动操作的统一位置与力控制）与 Fabrica（双臂多零件装配）。
  - 最佳学生论文：VideoMimic（面向情境化人形机器人控制的视觉模仿）。
- **NeurIPS 2025：** 举办了首届 BEHAVIOR Challenge。
- **ICRA 2026（维也纳）**
  - 最佳会议论文：OmniRetarget（据 IEEE RAS 的报道）。
  - 机器人学习最佳论文："Do You Know Where Your Camera Is?"
- **CVPR 2026（丹佛）**
  - 最佳论文：D4RT。
  - 最佳学生论文："Native and Compact Structured Latents for 3D Generation"（TRELLIS.2）。
  - SAM 3D 获得荣誉提名。
  - Embodied AI 研讨会以世界模型为主题。
- **RSS 2025（洛杉矶）：** 杰出论文奖授予 FEAST。
- **ICCV 2025：** Marr 奖授予 BrickGPT。
- **CVPR 2025：** 最佳论文授予前馈式多视图几何模型 VGGT。MegaSaM 与 Navigation World Models 获得荣誉提名。
- **RSS 2026（悉尼）**
  - 杰出论文：FlashSAC（面向高维控制的快速、稳定离策略强化学习）。
  - 杰出系统论文：NeuralActuator（据报道）。
- **CoRL 2026：** 将于 2026 年 11 月 9–12 日在奥斯汀举行，晚于本快照时间。
""",
    # ------------------------------------------------------------- 01 history
    "01_history/06_embodied_ai_2024_2026": """
**该时期后半段的压缩时间线**

- **2025 年**
  - **6 月：** V-JEPA 2、SmolVLA、Gemini Robotics On-Device、Real-Time Chunking。
  - **7 月：** ByteDance GR-3、TRI 的 LBM 研究、Skild Brain。
  - **8 月：** Genie 3、MolmoAct、Atlas LBM 演示、Jetson Thor 正式发售。
  - **9 月：** Gemini Robotics 1.5 与 ER 1.5；π0.5 开放权重；Figure 的 $39B 估值融资。
  - **10 月：** Figure 03；Cosmos Predict 2.5；1X NEO 开放预订。
  - **11 月：** π\\*0.6 与 RECAP；GEN-0。
  - **12 月：** GR00T N1.6；BEHAVIOR Challenge。
- **2026 年**
  - **1 月：** 量产版 Atlas 亮相 CES；1X 世界模型；Microsoft Rho-alpha；Skild 的 $1.4B 融资。
  - **2 月：** Helix 02；DreamZero。
  - **3 月：** MEM；GR00T N1.7 与 N2 预览版；基于 Newton 的 Isaac Lab 3.0 测试版。
  - **4 月：** π0.7；GEN-1；Gemini Robotics-ER 1.6；北京人形机器人半程马拉松。
  - **6 月：** Cosmos 3；ICRA 与 CVPR 奖项；BMW–Figure 部署。
  - **7 月：** Gemini Robotics 2；LeRobot v0.6。
  - **8 月：** Unitree 科创板 IPO。
  - **10 月：** RoboJEPA；Pi API 公测。

2024–2026 年的历史意义在于从单次演示转向工业化流水线。该流水线将大规模专有数据采集、强化学习后训练、世界模型数据引擎以及首批进入公开市场的人形机器人公司结合在一起。而独立的可靠性证据则全面滞后于这一切。
""",
    # ---------------------------------------------------------------- 12 meta
    "12_meta/02_how_to_update_this_database": """
**2026 年 10 月更新**

- 2026 年 10 月的更新为受影响的笔记添加了带日期的“近期进展”章节，并重写了 2025 年与 2026 年的前沿笔记。
- 本次更新新增了 `10_frontier_2024_2026/08_industry_status_2026.md`。
- 更新内容位于 `scripts/kb_recent.py` 以及 `scripts/build_kb.py` 的 `SPECIAL` 条目中。

**本次更新的信息来源**

- 大多数条目收集自指向一手来源的网络搜索结果：公司博客、arXiv、官方新闻稿与监管备案文件。
- 标注为“据报道”的条目依赖二手报道，引用前应重新核实。

**简体中文参考版**

- 简体中文参考版由 `scripts/build_kb_zh.py` 根据 `scripts/kb_zh/` 中的译文生成，输出至 `Chinese translation/`。
- 每篇中文笔记均链接至其英文原文。

**同步更新两个版本**

1. 编辑英文源文件。
2. 运行 `python3 scripts/build_kb.py`。
3. 将对应译文添加到 `scripts/kb_zh/`。
4. 运行 `python3 scripts/build_kb_zh.py`。中文构建器遇到任何未翻译的新条目都会报错失败，因此两个版本不会在不知不觉中出现偏差。
""",
}
