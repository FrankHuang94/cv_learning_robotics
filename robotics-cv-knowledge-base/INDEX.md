# Research Navigation Index

> **Last Updated:** 2026-06-11

This index maps a robotics-first computer-vision survey centered on one question: **how does vision become actionable, spatial, embodied intelligence for robots operating in the real world?** Every checked file is populated with technical discussion, systems, datasets, evaluation criteria, failure modes, open problems, and reading links.

## Start Here

1. Read [Scope Overview](00_scope_and_map/00_overview.md) and [What Counts as Robotics CV](00_scope_and_map/01_what_counts_as_robotics_cv.md).
2. Establish geometry and uncertainty through [Robot Perception Overview](02_robot_perception_foundations/00_robot_perception_overview.md).
3. Study the task interface in [Core Task Map](03_core_robotics_cv_problems/00_task_map.md).
4. Move to [3D and Spatial Understanding](04_3d_and_spatial_understanding/00_overview.md).
5. Read the [Embodied Foundation Model Roadmap](06_vla_and_embodied_foundation_models/00_overview_roadmap.md).
6. Finish with [State of the Field](10_frontier_2024_2026/00_state_of_the_field.md) and [Future Roadmaps](10_frontier_2024_2026/07_future_roadmaps.md).

## Most Important Files

- [VLA and Embodied Foundation Model Roadmap](06_vla_and_embodied_foundation_models/00_overview_roadmap.md)
- [VLA Model Architectures](06_vla_and_embodied_foundation_models/01_vla_model_architectures.md)
- [World Models for Robotics](06_vla_and_embodied_foundation_models/05_world_models_for_robotics.md)
- [Generalist vs Specialist](06_vla_and_embodied_foundation_models/07_generalist_vs_specialist.md)
- [Affordance Detection](03_core_robotics_cv_problems/03_affordance_detection.md)
- [Deformable Object Perception](03_core_robotics_cv_problems/08_deformable_object_perception.md)
- [Spatial Reasoning Bottlenecks](04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks.md)
- [Robot Data Bottleneck](07_data_simulation_and_training/01_robot_data_bottleneck.md)

## Latest Frontier Topics

The 2024–2026 notes track open VLAs, flow and diffusion action heads, heterogeneous co-training, humanoid whole-body policies, 3D Gaussian scene memory, action-conditioned world models, spatial intelligence, and visuotactile control. These files explicitly mark rapidly changing claims and should be refreshed from primary sources.

## Core Debates

- End-to-end VLA policy versus explicit world model and planner
- Generalist scaling versus specialist reliability
- Web-scale semantic priors versus robot-native interaction data
- Explicit metric 3D state versus implicit latent representations
- Passive video prediction versus action-conditioned causal learning
- Open-vocabulary semantics versus task-grounded affordances
- Simulation scale versus real-world contact fidelity

## Full Directory Map and Completion

### `00_scope_and_map/`
This topic establishes what belongs in a robotics-first vision agenda and prevents passive-image benchmark logic from substituting for embodied evidence.

- [x] [Overview](00_scope_and_map/00_overview.md)
- [x] [What Counts As Robotics Cv](00_scope_and_map/01_what_counts_as_robotics_cv.md)
- [x] [Field Map](00_scope_and_map/02_field_map.md)
- [x] [Major Debates](00_scope_and_map/03_major_debates.md)
### `01_history/`
The history matters because today's foundation policies inherit unresolved assumptions from calibration, stereo, SLAM, recognition, and behavior cloning.

- [x] [Timeline Overview](01_history/00_timeline_overview.md)
- [x] [Classical Robot Vision](01_history/01_classical_robot_vision.md)
- [x] [Learning Based Robot Vision](01_history/02_learning_based_robot_vision.md)
- [x] [RGB-D And 3D Perception](01_history/03_rgbd_and_3d_perception.md)
- [x] [Deep Robot Perception](01_history/04_deep_robot_perception.md)
- [x] [Multimodal And Foundation Models](01_history/05_multimodal_and_foundation_models.md)
- [x] [Embodied Ai 2024 2026](01_history/06_embodied_ai_2024_2026.md)
### `02_robot_perception_foundations/`
Reliable robot behavior depends on calibrated geometry, temporal estimation, uncertainty, fusion, and timing; semantic accuracy alone cannot guarantee a physically valid action.

- [x] [Robot Perception Overview](02_robot_perception_foundations/00_robot_perception_overview.md)
- [x] [Geometry And Coordinate Frames](02_robot_perception_foundations/01_geometry_and_coordinate_frames.md)
- [x] [Camera Models Calibration](02_robot_perception_foundations/02_camera_models_calibration.md)
- [x] [Depth Stereo RGB-D](02_robot_perception_foundations/03_depth_stereo_rgbd.md)
- [x] [Motion And Temporal Perception](02_robot_perception_foundations/04_motion_and_temporal_perception.md)
- [x] [State Estimation And Uncertainty](02_robot_perception_foundations/05_state_estimation_and_uncertainty.md)
- [x] [Sensor Fusion](02_robot_perception_foundations/06_sensor_fusion.md)
- [x] [Real Time Constraints](02_robot_perception_foundations/07_real_time_constraints.md)
### `03_core_robotics_cv_problems/`
This problem converts visual evidence into state variables that manipulation, navigation, and interaction policies can use under clutter, occlusion, contact, and time pressure.

- [x] [Task Map](03_core_robotics_cv_problems/00_task_map.md)
- [x] [Object Detection For Robotics](03_core_robotics_cv_problems/01_object_detection_for_robotics.md)
- [x] [Pose Estimation And 6D Pose](03_core_robotics_cv_problems/02_pose_estimation_and_6d_pose.md)
- [x] [Affordance Detection](03_core_robotics_cv_problems/03_affordance_detection.md)
- [x] [Grasp Perception](03_core_robotics_cv_problems/04_grasp_perception.md)
- [x] [Scene Understanding For Manipulation](03_core_robotics_cv_problems/05_scene_understanding_for_manipulation.md)
- [x] [Semantic Mapping For Navigation](03_core_robotics_cv_problems/06_semantic_mapping_for_navigation.md)
- [x] [Egocentric Perception](03_core_robotics_cv_problems/07_egocentric_perception.md)
- [x] [Deformable Object Perception](03_core_robotics_cv_problems/08_deformable_object_perception.md)
- [x] [Human Robot Scene Understanding](03_core_robotics_cv_problems/09_human_robot_scene_understanding.md)
- [x] [Failure Modes In Robot Perception](03_core_robotics_cv_problems/10_failure_modes_in_robot_perception.md)
### `04_3d_and_spatial_understanding/`
Robots act in metric 3D worlds that persist and change over time; 2D recognition must therefore be lifted into spatial, temporal, and uncertainty-aware representations.

- [x] [Overview](04_3d_and_spatial_understanding/00_overview.md)
- [x] [Point Clouds Voxels Meshes](04_3d_and_spatial_understanding/01_point_clouds_voxels_meshes.md)
- [x] [Sfm Slam And Visual Odometry](04_3d_and_spatial_understanding/02_sfm_slam_and_visual_odometry.md)
- [x] [Neural Scene Representations](04_3d_and_spatial_understanding/03_neural_scene_representations.md)
- [x] [3D Gaussian Splatting For Robotics](04_3d_and_spatial_understanding/04_3d_gaussian_splatting_for_robotics.md)
- [x] [Dynamic 4D Scene Understanding](04_3d_and_spatial_understanding/05_dynamic_4d_scene_understanding.md)
- [x] [Occupancy And World Representation](04_3d_and_spatial_understanding/06_occupancy_and_world_representation.md)
- [x] [Spatial Reasoning Bottlenecks](04_3d_and_spatial_understanding/07_spatial_reasoning_bottlenecks.md)
### `05_multimodal_perception/`
Vision is informative before contact, but touch, force, proprioception, depth, and language resolve ambiguities that RGB alone cannot observe.

- [x] [Overview](05_multimodal_perception/00_overview.md)
- [x] [Rgb Depth Tactile Proprioception](05_multimodal_perception/01_rgb_depth_tactile_proprioception.md)
- [x] [Visuotactile Learning](05_multimodal_perception/02_visuotactile_learning.md)
- [x] [Language Grounded Perception](05_multimodal_perception/03_language_grounded_perception.md)
- [x] [Open Vocabulary Robot Perception](05_multimodal_perception/04_open_vocabulary_robot_perception.md)
- [x] [Documentation Of Scene Memory](05_multimodal_perception/05_documentation_of_scene_memory.md)
- [x] [Event Cameras And High Speed Vision](05_multimodal_perception/06_event_cameras_and_high_speed_vision.md)
### `06_vla_and_embodied_foundation_models/`
Embodied foundation models place visual representation learning inside a perception-memory-reasoning-action loop, where errors alter the next observation and can cause physical failure.

- [x] [Overview Roadmap](06_vla_and_embodied_foundation_models/00_overview_roadmap.md)
- [x] [VLA Model Architectures](06_vla_and_embodied_foundation_models/01_vla_model_architectures.md)
- [x] [RT-1 RT-2 RT-X](06_vla_and_embodied_foundation_models/02_rt1_rt2_rtx.md)
- [x] [Openvla Octo And Open Models](06_vla_and_embodied_foundation_models/03_openvla_octo_and_open_models.md)
- [x] [pi0 GR00T Helix](06_vla_and_embodied_foundation_models/04_pi0_gr00t_helix.md)
- [x] [World Models For Robotics](06_vla_and_embodied_foundation_models/05_world_models_for_robotics.md)
- [x] [Diffusion Policy And Action Generation](06_vla_and_embodied_foundation_models/06_diffusion_policy_and_action_generation.md)
- [x] [Generalist Vs Specialist](06_vla_and_embodied_foundation_models/07_generalist_vs_specialist.md)
- [x] [Levels Of Generalization](06_vla_and_embodied_foundation_models/08_levels_of_generalization.md)
- [x] [Language Conditioned Control](06_vla_and_embodied_foundation_models/09_language_conditioned_control.md)
- [x] [Embodiment Scaling Questions](06_vla_and_embodied_foundation_models/10_embodiment_scaling_questions.md)
### `07_data_simulation_and_training/`
Robot learning is constrained less by raw model capacity than by expensive action-labeled trajectories, inconsistent embodiments, sparse failures, and weak evaluation.

- [x] [Overview](07_data_simulation_and_training/00_overview.md)
- [x] [Robot Data Bottleneck](07_data_simulation_and_training/01_robot_data_bottleneck.md)
- [x] [Teleoperation And Demonstrations](07_data_simulation_and_training/02_teleoperation_and_demonstrations.md)
- [x] [Cross Embodiment Datasets](07_data_simulation_and_training/03_cross_embodiment_datasets.md)
- [x] [Simulation Platforms](07_data_simulation_and_training/04_simulation_platforms.md)
- [x] [Sim2Real And Domain Randomization](07_data_simulation_and_training/05_sim2real_and_domain_randomization.md)
- [x] [Synthetic Data And Video Data](07_data_simulation_and_training/06_synthetic_data_and_video_data.md)
- [x] [Self Supervised Robot Perception](07_data_simulation_and_training/07_self_supervised_robot_perception.md)
- [x] [Evaluation And Benchmarks](07_data_simulation_and_training/08_evaluation_and_benchmarks.md)
### `08_manipulation_navigation_and_control/`
Perception becomes useful only when it closes the loop: selecting goals, constraining plans, detecting contact and progress, and triggering recovery.

- [x] [Overview](08_manipulation_navigation_and_control/00_overview.md)
- [x] [Perception For Manipulation](08_manipulation_navigation_and_control/01_perception_for_manipulation.md)
- [x] [Perception For Mobile Navigation](08_manipulation_navigation_and_control/02_perception_for_mobile_navigation.md)
- [x] [Bimanual And Dexterous Tasks](08_manipulation_navigation_and_control/03_bimanual_and_dexterous_tasks.md)
- [x] [Long Horizon Task Execution](08_manipulation_navigation_and_control/04_long_horizon_task_execution.md)
- [x] [Task And Motion Interface](08_manipulation_navigation_and_control/05_task_and_motion_interface.md)
- [x] [Planning With Visual Representations](08_manipulation_navigation_and_control/06_planning_with_visual_representations.md)
- [x] [Closed Loop Robot Vision](08_manipulation_navigation_and_control/07_closed_loop_robot_vision.md)
### `09_robot_platforms_and_hardware/`
Embodiment determines observability, action space, control rate, data compatibility, and which visual errors become dangerous.

- [x] [Overview](09_robot_platforms_and_hardware/00_overview.md)
- [x] [Robot Arms And Manipulators](09_robot_platforms_and_hardware/01_robot_arms_and_manipulators.md)
- [x] [Humanoid Platforms](09_robot_platforms_and_hardware/02_humanoid_platforms.md)
- [x] [Mobile Robots And Navigation Stacks](09_robot_platforms_and_hardware/03_mobile_robots_and_navigation_stacks.md)
- [x] [Sensor Suites](09_robot_platforms_and_hardware/04_sensor_suites.md)
- [x] [Compute Latency And Deployment](09_robot_platforms_and_hardware/05_compute_latency_and_deployment.md)
### `10_frontier_2024_2026/`
This is a very recent, rapidly changing area; claims here are dated and should be distinguished from independently reproduced evidence.

- [x] [State Of The Field](10_frontier_2024_2026/00_state_of_the_field.md)
- [x] [2024 Breakthroughs](10_frontier_2024_2026/01_2024_breakthroughs.md)
- [x] [2025 Breakthroughs](10_frontier_2024_2026/02_2025_breakthroughs.md)
- [x] [2026 Current Frontier](10_frontier_2024_2026/03_2026_current_frontier.md)
- [x] [Spatial Intelligence](10_frontier_2024_2026/04_spatial_intelligence.md)
- [x] [World Model Vs VLA](10_frontier_2024_2026/05_world_model_vs_vla.md)
- [x] [Robotics Cv Open Problems](10_frontier_2024_2026/06_robotics_cv_open_problems.md)
- [x] [Future Roadmaps](10_frontier_2024_2026/07_future_roadmaps.md)
### `11_datasets_papers_labs/`
A research database is useful only if it distinguishes landmark evidence, reproducible resources, institutional incentives, and benchmark blind spots.

- [x] [Must Know Datasets](11_datasets_papers_labs/00_must_know_datasets.md)
- [x] [Must Read Papers](11_datasets_papers_labs/01_must_read_papers.md)
- [x] [Major Labs And Companies](11_datasets_papers_labs/02_major_labs_and_companies.md)
- [x] [Open Source Ecosystem](11_datasets_papers_labs/03_open_source_ecosystem.md)
- [x] [Conference Map](11_datasets_papers_labs/04_conference_map.md)
### `12_meta/`
Research notes need explicit definitions, reading order, update rules, and falsifiable questions to remain useful as the field changes.

- [x] [Research Glossary](12_meta/00_research_glossary.md)
- [x] [Reading Path For Phd Student](12_meta/01_reading_path_for_phd_student.md)
- [x] [How To Update This Database](12_meta/02_how_to_update_this_database.md)
- [x] [Research Questions Backlog](12_meta/03_research_questions_backlog.md)
