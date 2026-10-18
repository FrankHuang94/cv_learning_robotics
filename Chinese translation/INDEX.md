# 研究导航索引

> **最后更新：** 2026-10-18
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

### `00_scope_and_map/` — 范围与领域地图
本主题界定机器人优先的视觉研究议程应涵盖哪些内容，并防止以被动图像基准的评价逻辑替代具身证据。

- [x] [概述](00_scope_and_map/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/00_scope_and_map/00_overview.md)）
- [x] [什么算作机器人计算机视觉](00_scope_and_map/01_what_counts_as_robotics_cv.md)（[英文原文](../robotics-cv-knowledge-base/00_scope_and_map/01_what_counts_as_robotics_cv.md)）
- [x] [领域地图](00_scope_and_map/02_field_map.md)（[英文原文](../robotics-cv-knowledge-base/00_scope_and_map/02_field_map.md)）
- [x] [主要争论](00_scope_and_map/03_major_debates.md)（[英文原文](../robotics-cv-knowledge-base/00_scope_and_map/03_major_debates.md)）
### `01_history/` — 发展历史
历史之所以重要，是因为当今的基础策略继承了标定、立体视觉、SLAM、识别与行为克隆中尚未解决的假设。

- [x] [时间线概览](01_history/00_timeline_overview.md)（[英文原文](../robotics-cv-knowledge-base/01_history/00_timeline_overview.md)）
- [x] [经典机器人视觉](01_history/01_classical_robot_vision.md)（[英文原文](../robotics-cv-knowledge-base/01_history/01_classical_robot_vision.md)）
- [x] [基于学习的机器人视觉](01_history/02_learning_based_robot_vision.md)（[英文原文](../robotics-cv-knowledge-base/01_history/02_learning_based_robot_vision.md)）
- [x] [RGB-D 与三维感知](01_history/03_rgbd_and_3d_perception.md)（[英文原文](../robotics-cv-knowledge-base/01_history/03_rgbd_and_3d_perception.md)）
- [x] [深度学习机器人感知](01_history/04_deep_robot_perception.md)（[英文原文](../robotics-cv-knowledge-base/01_history/04_deep_robot_perception.md)）
- [x] [多模态与基础模型](01_history/05_multimodal_and_foundation_models.md)（[英文原文](../robotics-cv-knowledge-base/01_history/05_multimodal_and_foundation_models.md)）
- [x] [具身智能（2024–2026）](01_history/06_embodied_ai_2024_2026.md)（[英文原文](../robotics-cv-knowledge-base/01_history/06_embodied_ai_2024_2026.md)）
### `02_robot_perception_foundations/` — 机器人感知基础
可靠的机器人行为依赖于经过标定的几何、时序估计、不确定性、多源融合与时序同步；仅凭语义准确性无法保证动作在物理上有效。

- [x] [机器人感知概述](02_robot_perception_foundations/00_robot_perception_overview.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/00_robot_perception_overview.md)）
- [x] [几何与坐标系](02_robot_perception_foundations/01_geometry_and_coordinate_frames.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/01_geometry_and_coordinate_frames.md)）
- [x] [相机模型与标定](02_robot_perception_foundations/02_camera_models_calibration.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/02_camera_models_calibration.md)）
- [x] [深度、立体视觉与 RGB-D](02_robot_perception_foundations/03_depth_stereo_rgbd.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/03_depth_stereo_rgbd.md)）
- [x] [运动与时序感知](02_robot_perception_foundations/04_motion_and_temporal_perception.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/04_motion_and_temporal_perception.md)）
- [x] [状态估计与不确定性](02_robot_perception_foundations/05_state_estimation_and_uncertainty.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/05_state_estimation_and_uncertainty.md)）
- [x] [传感器融合](02_robot_perception_foundations/06_sensor_fusion.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/06_sensor_fusion.md)）
- [x] [实时性约束](02_robot_perception_foundations/07_real_time_constraints.md)（[英文原文](../robotics-cv-knowledge-base/02_robot_perception_foundations/07_real_time_constraints.md)）
### `03_core_robotics_cv_problems/` — 机器人视觉核心问题
该问题将视觉证据转化为状态变量，供操作、导航与交互策略在杂乱、遮挡、接触和时间压力下使用。

- [x] [任务地图](03_core_robotics_cv_problems/00_task_map.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/00_task_map.md)）
- [x] [面向机器人的目标检测](03_core_robotics_cv_problems/01_object_detection_for_robotics.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/01_object_detection_for_robotics.md)）
- [x] [位姿估计与 6D 位姿](03_core_robotics_cv_problems/02_pose_estimation_and_6d_pose.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/02_pose_estimation_and_6d_pose.md)）
- [x] [可供性检测](03_core_robotics_cv_problems/03_affordance_detection.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/03_affordance_detection.md)）
- [x] [抓取感知](03_core_robotics_cv_problems/04_grasp_perception.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/04_grasp_perception.md)）
- [x] [面向操作的场景理解](03_core_robotics_cv_problems/05_scene_understanding_for_manipulation.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/05_scene_understanding_for_manipulation.md)）
- [x] [面向导航的语义建图](03_core_robotics_cv_problems/06_semantic_mapping_for_navigation.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/06_semantic_mapping_for_navigation.md)）
- [x] [第一人称（自我中心）感知](03_core_robotics_cv_problems/07_egocentric_perception.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/07_egocentric_perception.md)）
- [x] [可变形物体感知](03_core_robotics_cv_problems/08_deformable_object_perception.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/08_deformable_object_perception.md)）
- [x] [人机场景理解](03_core_robotics_cv_problems/09_human_robot_scene_understanding.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/09_human_robot_scene_understanding.md)）
- [x] [机器人感知中的失效模式](03_core_robotics_cv_problems/10_failure_modes_in_robot_perception.md)（[英文原文](../robotics-cv-knowledge-base/03_core_robotics_cv_problems/10_failure_modes_in_robot_perception.md)）
### `04_3d_and_spatial_understanding/` — 三维与空间理解
机器人在持续存在且随时间变化的度量三维世界中行动；因此，二维识别必须被提升为具备空间、时间与不确定性感知的表示。

- [x] [概述](04_3d_and_spatial_understanding/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/00_overview.md)）
- [x] [点云、体素与网格](04_3d_and_spatial_understanding/01_point_clouds_voxels_meshes.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/01_point_clouds_voxels_meshes.md)）
- [x] [SfM、SLAM 与视觉里程计](04_3d_and_spatial_understanding/02_sfm_slam_and_visual_odometry.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/02_sfm_slam_and_visual_odometry.md)）
- [x] [神经场景表示](04_3d_and_spatial_understanding/03_neural_scene_representations.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/03_neural_scene_representations.md)）
- [x] [面向机器人的 3D 高斯泼溅](04_3d_and_spatial_understanding/04_3d_gaussian_splatting_for_robotics.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/04_3d_gaussian_splatting_for_robotics.md)）
- [x] [动态 4D 场景理解](04_3d_and_spatial_understanding/05_dynamic_4d_scene_understanding.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/05_dynamic_4d_scene_understanding.md)）
- [x] [占据与世界表示](04_3d_and_spatial_understanding/06_occupancy_and_world_representation.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/06_occupancy_and_world_representation.md)）
- [x] [空间推理瓶颈](04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks.md)（[英文原文](../robotics-cv-knowledge-base/04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks.md)）
### `05_multimodal_perception/` — 多模态感知
视觉在接触发生之前提供信息，而触觉、力、本体感觉、深度与语言能够消解仅凭 RGB 无法观测的歧义。

- [x] [概述](05_multimodal_perception/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/00_overview.md)）
- [x] [RGB、深度、触觉与本体感觉](05_multimodal_perception/01_rgb_depth_tactile_proprioception.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/01_rgb_depth_tactile_proprioception.md)）
- [x] [视触觉学习](05_multimodal_perception/02_visuotactile_learning.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/02_visuotactile_learning.md)）
- [x] [语言接地感知](05_multimodal_perception/03_language_grounded_perception.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/03_language_grounded_perception.md)）
- [x] [开放词汇机器人感知](05_multimodal_perception/04_open_vocabulary_robot_perception.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/04_open_vocabulary_robot_perception.md)）
- [x] [场景记忆的记录与组织](05_multimodal_perception/05_documentation_of_scene_memory.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/05_documentation_of_scene_memory.md)）
- [x] [事件相机与高速视觉](05_multimodal_perception/06_event_cameras_and_high_speed_vision.md)（[英文原文](../robotics-cv-knowledge-base/05_multimodal_perception/06_event_cameras_and_high_speed_vision.md)）
### `06_vla_and_embodied_foundation_models/` — VLA 与具身基础模型
具身基础模型将视觉表示学习置于“感知—记忆—推理—动作”闭环之中，其中的误差会改变下一时刻的观测，并可能导致物理层面的失效。

- [x] [概述与路线图](06_vla_and_embodied_foundation_models/00_overview_roadmap.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/00_overview_roadmap.md)）
- [x] [VLA 模型架构](06_vla_and_embodied_foundation_models/01_vla_model_architectures.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/01_vla_model_architectures.md)）
- [x] [RT-1、RT-2 与 RT-X](06_vla_and_embodied_foundation_models/02_rt1_rt2_rtx.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/02_rt1_rt2_rtx.md)）
- [x] [OpenVLA、Octo 与开放模型](06_vla_and_embodied_foundation_models/03_openvla_octo_and_open_models.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/03_openvla_octo_and_open_models.md)）
- [x] [pi0、GR00T 与 Helix](06_vla_and_embodied_foundation_models/04_pi0_gr00t_helix.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/04_pi0_gr00t_helix.md)）
- [x] [面向机器人的世界模型](06_vla_and_embodied_foundation_models/05_world_models_for_robotics.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/05_world_models_for_robotics.md)）
- [x] [扩散策略与动作生成](06_vla_and_embodied_foundation_models/06_diffusion_policy_and_action_generation.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/06_diffusion_policy_and_action_generation.md)）
- [x] [通才模型与专才模型](06_vla_and_embodied_foundation_models/07_generalist_vs_specialist.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/07_generalist_vs_specialist.md)）
- [x] [泛化的层级](06_vla_and_embodied_foundation_models/08_levels_of_generalization.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/08_levels_of_generalization.md)）
- [x] [语言条件控制](06_vla_and_embodied_foundation_models/09_language_conditioned_control.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/09_language_conditioned_control.md)）
- [x] [具身形态扩展问题](06_vla_and_embodied_foundation_models/10_embodiment_scaling_questions.md)（[英文原文](../robotics-cv-knowledge-base/06_vla_and_embodied_foundation_models/10_embodiment_scaling_questions.md)）
### `07_data_simulation_and_training/` — 数据、仿真与训练
制约机器人学习的与其说是原始模型容量，不如说是昂贵的带动作标注轨迹、不一致的具身形态、稀少的失败样本以及薄弱的评测。

- [x] [概述](07_data_simulation_and_training/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/00_overview.md)）
- [x] [机器人数据瓶颈](07_data_simulation_and_training/01_robot_data_bottleneck.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/01_robot_data_bottleneck.md)）
- [x] [遥操作与示范](07_data_simulation_and_training/02_teleoperation_and_demonstrations.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/02_teleoperation_and_demonstrations.md)）
- [x] [跨具身数据集](07_data_simulation_and_training/03_cross_embodiment_datasets.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/03_cross_embodiment_datasets.md)）
- [x] [仿真平台](07_data_simulation_and_training/04_simulation_platforms.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/04_simulation_platforms.md)）
- [x] [仿真到现实与域随机化](07_data_simulation_and_training/05_sim2real_and_domain_randomization.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/05_sim2real_and_domain_randomization.md)）
- [x] [合成数据与视频数据](07_data_simulation_and_training/06_synthetic_data_and_video_data.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/06_synthetic_data_and_video_data.md)）
- [x] [自监督机器人感知](07_data_simulation_and_training/07_self_supervised_robot_perception.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/07_self_supervised_robot_perception.md)）
- [x] [评估与基准](07_data_simulation_and_training/08_evaluation_and_benchmarks.md)（[英文原文](../robotics-cv-knowledge-base/07_data_simulation_and_training/08_evaluation_and_benchmarks.md)）
### `08_manipulation_navigation_and_control/` — 操作、导航与控制
感知只有在闭合回路时才真正有用：选择目标、约束规划、检测接触与进展，并触发恢复。

- [x] [概述](08_manipulation_navigation_and_control/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/00_overview.md)）
- [x] [面向操作的感知](08_manipulation_navigation_and_control/01_perception_for_manipulation.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/01_perception_for_manipulation.md)）
- [x] [面向移动导航的感知](08_manipulation_navigation_and_control/02_perception_for_mobile_navigation.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/02_perception_for_mobile_navigation.md)）
- [x] [双臂与灵巧任务](08_manipulation_navigation_and_control/03_bimanual_and_dexterous_tasks.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/03_bimanual_and_dexterous_tasks.md)）
- [x] [长时程任务执行](08_manipulation_navigation_and_control/04_long_horizon_task_execution.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/04_long_horizon_task_execution.md)）
- [x] [任务与运动接口](08_manipulation_navigation_and_control/05_task_and_motion_interface.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/05_task_and_motion_interface.md)）
- [x] [基于视觉表示的规划](08_manipulation_navigation_and_control/06_planning_with_visual_representations.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/06_planning_with_visual_representations.md)）
- [x] [闭环机器人视觉](08_manipulation_navigation_and_control/07_closed_loop_robot_vision.md)（[英文原文](../robotics-cv-knowledge-base/08_manipulation_navigation_and_control/07_closed_loop_robot_vision.md)）
### `09_robot_platforms_and_hardware/` — 机器人平台与硬件
具身形态决定了可观测性、动作空间、控制频率、数据兼容性，以及哪些视觉误差会变得危险。

- [x] [概述](09_robot_platforms_and_hardware/00_overview.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/00_overview.md)）
- [x] [机械臂与操作器](09_robot_platforms_and_hardware/01_robot_arms_and_manipulators.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/01_robot_arms_and_manipulators.md)）
- [x] [人形机器人平台](09_robot_platforms_and_hardware/02_humanoid_platforms.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/02_humanoid_platforms.md)）
- [x] [移动机器人与导航栈](09_robot_platforms_and_hardware/03_mobile_robots_and_navigation_stacks.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/03_mobile_robots_and_navigation_stacks.md)）
- [x] [传感器套件](09_robot_platforms_and_hardware/04_sensor_suites.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/04_sensor_suites.md)）
- [x] [算力、延迟与部署](09_robot_platforms_and_hardware/05_compute_latency_and_deployment.md)（[英文原文](../robotics-cv-knowledge-base/09_robot_platforms_and_hardware/05_compute_latency_and_deployment.md)）
### `10_frontier_2024_2026/` — 2024–2026 前沿
这是一个非常新且快速变化的领域；此处的论断具有时效性，应与经过独立复现的证据加以区分。

- [x] [领域现状](10_frontier_2024_2026/00_state_of_the_field.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/00_state_of_the_field.md)）
- [x] [2024 年突破](10_frontier_2024_2026/01_2024_breakthroughs.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/01_2024_breakthroughs.md)）
- [x] [2025 年突破](10_frontier_2024_2026/02_2025_breakthroughs.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/02_2025_breakthroughs.md)）
- [x] [2026 年当前前沿](10_frontier_2024_2026/03_2026_current_frontier.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/03_2026_current_frontier.md)）
- [x] [空间智能](10_frontier_2024_2026/04_spatial_intelligence.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/04_spatial_intelligence.md)）
- [x] [世界模型与 VLA 之争](10_frontier_2024_2026/05_world_model_vs_vla.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/05_world_model_vs_vla.md)）
- [x] [机器人视觉开放问题](10_frontier_2024_2026/06_robotics_cv_open_problems.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/06_robotics_cv_open_problems.md)）
- [x] [未来路线图](10_frontier_2024_2026/07_future_roadmaps.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/07_future_roadmaps.md)）
- [x] [2026 年产业现状](10_frontier_2024_2026/08_industry_status_2026.md)（[英文原文](../robotics-cv-knowledge-base/10_frontier_2024_2026/08_industry_status_2026.md)）
### `11_datasets_papers_labs/` — 数据集、论文与实验室
研究数据库只有在能够区分里程碑式证据、可复现资源、机构激励与基准盲点时才有用。

- [x] [必知数据集](11_datasets_papers_labs/00_must_know_datasets.md)（[英文原文](../robotics-cv-knowledge-base/11_datasets_papers_labs/00_must_know_datasets.md)）
- [x] [必读论文](11_datasets_papers_labs/01_must_read_papers.md)（[英文原文](../robotics-cv-knowledge-base/11_datasets_papers_labs/01_must_read_papers.md)）
- [x] [主要实验室与公司](11_datasets_papers_labs/02_major_labs_and_companies.md)（[英文原文](../robotics-cv-knowledge-base/11_datasets_papers_labs/02_major_labs_and_companies.md)）
- [x] [开源生态](11_datasets_papers_labs/03_open_source_ecosystem.md)（[英文原文](../robotics-cv-knowledge-base/11_datasets_papers_labs/03_open_source_ecosystem.md)）
- [x] [会议地图](11_datasets_papers_labs/04_conference_map.md)（[英文原文](../robotics-cv-knowledge-base/11_datasets_papers_labs/04_conference_map.md)）
### `12_meta/` — 元信息与研究方法
研究笔记需要明确的定义、阅读顺序、更新规则和可证伪的问题，才能在领域变化中保持有用。

- [x] [研究术语表](12_meta/00_research_glossary.md)（[英文原文](../robotics-cv-knowledge-base/12_meta/00_research_glossary.md)）
- [x] [博士生阅读路线](12_meta/01_reading_path_for_phd_student.md)（[英文原文](../robotics-cv-knowledge-base/12_meta/01_reading_path_for_phd_student.md)）
- [x] [如何更新本数据库](12_meta/02_how_to_update_this_database.md)（[英文原文](../robotics-cv-knowledge-base/12_meta/02_how_to_update_this_database.md)）
- [x] [研究问题清单](12_meta/03_research_questions_backlog.md)（[英文原文](../robotics-cv-knowledge-base/12_meta/03_research_questions_backlog.md)）
