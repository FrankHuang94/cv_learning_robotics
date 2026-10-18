"""Simplified Chinese README and INDEX page templates.

``<<UPDATED>>`` is replaced with the build date and ``<<SECTIONS>>`` (INDEX only)
with the generated directory sections by ``scripts/build_kb_zh.py``.
"""

README_ZH = """# 机器人计算机视觉知识库

> **最后更新：** <<UPDATED>>
>
> **英文原文：** [README.md](../robotics-cv-knowledge-base/README.md)

本目录是英文知识库的简体中文参考译本，供参考阅读之用；如需精确措辞与引用，请以各篇笔记所链接的英文原文为准。

本仓库是一个持续更新、以机器人为先（机器人优先）的研究数据库，关注从被动视觉识别向可执行的空间智能的转变。内容聚焦于机器人操作、导航、三维/四维场景理解、多模态感知、视觉-语言-动作模型（VLA）、世界模型、机器人数据以及闭环评估。

这些笔记以研究简报而非术语条目的形式撰写。每篇笔记现均包含形式化的问题陈述、明确的假设、假说与基线设计、抗数据泄漏的评估划分、统计报告规范、诊断性消融、可复现性检查清单，以及达到学位论文层面的研究问题。第 06 部分针对 VLA、动作生成器、世界模型、语言接地和跨具身扩展，补充了面向具体架构的数学与实验分析。

2026 年 10 月的更新为 45 篇笔记新增了标注日期的“近期进展”小节，重写了 2025 年与 2026 年的前沿笔记，并在 [2026 年产业现状](10_frontier_2024_2026/08_industry_status_2026.md) 中新增了产业现状快照。结构相同的英文原版位于 [`robotics-cv-knowledge-base/`](../robotics-cv-knowledge-base/README.md)。

## “机器人优先的计算机视觉”意味着什么

机器人计算机视觉（机器人 CV）的评判标准在于：视觉状态能否支撑安全而有效的动作。检测与分割之所以重要，是因为它们能够改进位姿、可达性、可供性（affordance）、记忆、规划、控制或恢复。因此，本数据库弱化通用基准的发展史，而着重强调几何、时间、不确定性、接触、具身形态（本体）、延迟和分布偏移。

## 组织结构

各编号目录依次覆盖：范围与发展历史、感知基础、核心问题、空间与多模态理解、具身基础模型、数据、控制、硬件、2024–2026 前沿、资源以及研究工作流程。建议从 [知识库索引](INDEX.md) 开始，然后按照 [博士生阅读路线](12_meta/01_reading_path_for_phd_student.md) 继续阅读。

## 更新数据库

收录一篇新论文时，应记录其发表日期、稳定 URL、任务、具身形态、传感器、动作表示、训练数据、评估划分、试验次数以及主要局限。须区分作者自行报告的演示与独立复现的结果。更新“最后更新”（`Last Updated`）字段，在相邻笔记中补充链接，并在提交前运行仓库审计。

前沿文件最需要严谨：应依据论文或官方技术报告核实各项主张，标注非常新近的结果，避免从视频中外推结论，并存档基准评测协议的变更。年度快照应保留当时的认识，而不是悄无声息地改写历史。
"""

INDEX_ZH = """# 研究导航索引

> **最后更新：** <<UPDATED>>
>
> **英文原文：** [INDEX.md](../robotics-cv-knowledge-base/INDEX.md)

本索引梳理了一份以机器人为先的计算机视觉综述，其核心问题只有一个：**视觉如何成为在真实世界中运行的机器人所具备的可执行、空间化、具身化的智能？** 每个已勾选的文件都包含技术讨论、代表性系统、数据集、评估标准、失效模式、开放问题以及阅读链接。

## 从这里开始

1. 阅读 [范围与领域地图：概述](00_scope_and_map/00_overview.md) 与 [什么算作机器人计算机视觉](00_scope_and_map/01_what_counts_as_robotics_cv.md)。
2. 通过 [机器人感知概述](02_robot_perception_foundations/00_robot_perception_overview.md) 建立几何与不确定性的基础。
3. 在 [任务地图](03_core_robotics_cv_problems/00_task_map.md) 中学习任务接口。
4. 进入 [三维与空间理解：概述](04_3d_and_spatial_understanding/00_overview.md)。
5. 阅读 [VLA 与具身基础模型：概述与路线图](06_vla_and_embodied_foundation_models/00_overview_roadmap.md)。
6. 最后阅读 [领域现状](10_frontier_2024_2026/00_state_of_the_field.md)、[2026 年当前前沿](10_frontier_2024_2026/03_2026_current_frontier.md)、[2026 年产业现状](10_frontier_2024_2026/08_industry_status_2026.md) 与 [未来路线图](10_frontier_2024_2026/07_future_roadmaps.md)。

## 最重要的文件

- [VLA 与具身基础模型：概述与路线图](06_vla_and_embodied_foundation_models/00_overview_roadmap.md)
- [VLA 模型架构](06_vla_and_embodied_foundation_models/01_vla_model_architectures.md)
- [面向机器人的世界模型](06_vla_and_embodied_foundation_models/05_world_models_for_robotics.md)
- [通才模型与专才模型](06_vla_and_embodied_foundation_models/07_generalist_vs_specialist.md)
- [可供性检测](03_core_robotics_cv_problems/03_affordance_detection.md)
- [可变形物体感知](03_core_robotics_cv_problems/08_deformable_object_perception.md)
- [空间推理瓶颈](04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks.md)
- [机器人数据瓶颈](07_data_simulation_and_training/01_robot_data_bottleneck.md)

## 最新前沿主题

2024–2026 年的笔记追踪开放 VLA、流匹配与扩散动作头、异构数据联合训练、人形机器人全身策略、基于 3D 高斯的场景记忆、动作条件世界模型、空间智能以及视触觉控制。2026 年 10 月的更新新增了以下内容：VLA 的强化学习微调（RECAP、piRL）、“推理器 + 执行器”分层架构（Gemini Robotics 1.5 与 2、GR00T N1.6）、世界动作模型（DreamZero、Cosmos 3）、隐空间世界模型（V-JEPA 2、RoboJEPA）、前馈式 3D/4D 重建（VGGT、D4RT）、概念分割（SAM 3）、竞技场式评估（RoboArena），以及 2026 年的产业格局。这些文件明确标注了快速变化的主张，应依据一手来源定期更新。

每篇笔记的英文原文均可在 [英文版索引](../robotics-cv-knowledge-base/INDEX.md) 中查阅；本译本中每个条目后也附有对应的英文原文链接。

## 核心争论

- 端到端 VLA 策略与显式世界模型加规划器之争
- 通才模型的规模扩展与专才模型的可靠性之争
- 网络规模的语义先验与机器人原生交互数据之争
- 显式度量三维状态与隐式潜在表示之争
- 被动视频预测与动作条件因果学习之争
- 开放词汇语义与任务接地的可供性之争
- 仿真规模与真实世界接触保真度之争

## 完整目录地图与完成情况

<<SECTIONS>>
"""
