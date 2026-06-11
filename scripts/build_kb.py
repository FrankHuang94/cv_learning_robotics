#!/usr/bin/env python3
"""Build the robotics-first computer-vision research knowledge base."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1] / "robotics-cv-knowledge-base"
UPDATED = date(2026, 6, 11).isoformat()

STRUCTURE = {
    "00_scope_and_map": "00_overview 01_what_counts_as_robotics_cv 02_field_map 03_major_debates",
    "01_history": "00_timeline_overview 01_classical_robot_vision 02_learning_based_robot_vision 03_rgbd_and_3d_perception 04_deep_robot_perception 05_multimodal_and_foundation_models 06_embodied_ai_2024_2026",
    "02_robot_perception_foundations": "00_robot_perception_overview 01_geometry_and_coordinate_frames 02_camera_models_calibration 03_depth_stereo_rgbd 04_motion_and_temporal_perception 05_state_estimation_and_uncertainty 06_sensor_fusion 07_real_time_constraints",
    "03_core_robotics_cv_problems": "00_task_map 01_object_detection_for_robotics 02_pose_estimation_and_6d_pose 03_affordance_detection 04_grasp_perception 05_scene_understanding_for_manipulation 06_semantic_mapping_for_navigation 07_egocentric_perception 08_deformable_object_perception 09_human_robot_scene_understanding 10_failure_modes_in_robot_perception",
    "04_3d_and_spatial_understanding": "00_overview 01_point_clouds_voxels_meshes 02_sfm_slam_and_visual_odometry 03_neural_scene_representations 04_3d_gaussian_splatting_for_robotics 05_dynamic_4d_scene_understanding 06_occupancy_and_world_representation 07_spatial_reasoning_bottlenecks",
    "05_multimodal_perception": "00_overview 01_rgb_depth_tactile_proprioception 02_visuotactile_learning 03_language_grounded_perception 04_open_vocabulary_robot_perception 05_documentation_of_scene_memory 06_event_cameras_and_high_speed_vision",
    "06_vla_and_embodied_foundation_models": "00_overview_roadmap 01_vla_model_architectures 02_rt1_rt2_rtx 03_openvla_octo_and_open_models 04_pi0_gr00t_helix 05_world_models_for_robotics 06_diffusion_policy_and_action_generation 07_generalist_vs_specialist 08_levels_of_generalization 09_language_conditioned_control 10_embodiment_scaling_questions",
    "07_data_simulation_and_training": "00_overview 01_robot_data_bottleneck 02_teleoperation_and_demonstrations 03_cross_embodiment_datasets 04_simulation_platforms 05_sim2real_and_domain_randomization 06_synthetic_data_and_video_data 07_self_supervised_robot_perception 08_evaluation_and_benchmarks",
    "08_manipulation_navigation_and_control": "00_overview 01_perception_for_manipulation 02_perception_for_mobile_navigation 03_bimanual_and_dexterous_tasks 04_long_horizon_task_execution 05_task_and_motion_interface 06_planning_with_visual_representations 07_closed_loop_robot_vision",
    "09_robot_platforms_and_hardware": "00_overview 01_robot_arms_and_manipulators 02_humanoid_platforms 03_mobile_robots_and_navigation_stacks 04_sensor_suites 05_compute_latency_and_deployment",
    "10_frontier_2024_2026": "00_state_of_the_field 01_2024_breakthroughs 02_2025_breakthroughs 03_2026_current_frontier 04_spatial_intelligence 05_world_model_vs_vla 06_robotics_cv_open_problems 07_future_roadmaps",
    "11_datasets_papers_labs": "00_must_know_datasets 01_must_read_papers 02_major_labs_and_companies 03_open_source_ecosystem 04_conference_map",
    "12_meta": "00_research_glossary 01_reading_path_for_phd_student 02_how_to_update_this_database 03_research_questions_backlog",
}

DOMAIN = {
    "00_scope_and_map": {
        "frame": "This topic establishes what belongs in a robotics-first vision agenda and prevents passive-image benchmark logic from substituting for embodied evidence.",
        "core": "Robotics CV is best understood as estimation for intervention. A representation is valuable when it preserves geometry, uncertainty, temporal persistence, and task-conditioned semantics well enough to select and monitor actions. The field therefore spans calibration, state estimation, mapping, grounding, affordances, active perception, contact sensing, and learned control. It overlaps mainstream CV, but differs in observability, distribution shift, latency, safety, and the causal effect of camera motion and robot action.",
        "systems": [("Marr's vision framework", 1982, "theory", "Separated computational goals, representations, and algorithms"), ("Active Vision", 1988, "paradigm", "Made sensing an action-selection problem"), ("SayCan", 2022, "robot system", "Combined language-model priors with grounded skill values"), ("RT-2", 2023, "VLA", "Connected web-scale visual-language knowledge to robot actions")],
        "datasets": [("RoboTHOR / AI2-THOR", "embodied navigation", "SPL, success", "Tests perception under action and viewpoint change"), ("BEHAVIOR-1K", "household activities", "task success", "Requires semantics, geometry, and state changes"), ("Open X-Embodiment", "cross-robot manipulation", "policy success", "Exposes embodiment and data-mixture effects")],
    },
    "01_history": {
        "frame": "The history matters because today's foundation policies inherit unresolved assumptions from calibration, stereo, SLAM, recognition, and behavior cloning.",
        "core": "Robot vision evolved through overlapping regimes rather than clean replacement: engineered geometry and control; probabilistic state estimation; RGB-D reconstruction; deep discriminative perception; self-supervised representation learning; and multimodal policies. Classical methods remain inside modern systems as coordinate transforms, optimization, tracking, collision checks, and safety monitors. The decisive shift is from estimating a static world for a downstream planner toward learning representations jointly with language and action.",
        "systems": [("Shakey", 1969, "mobile robot", "Linked perception, symbolic planning, and action"), ("SIFT", 1999, "feature method", "Enabled robust correspondence and localization"), ("KinectFusion", 2011, "RGB-D mapping", "Made dense online reconstruction practical"), ("AlexNet", 2012, "deep vision", "Accelerated learned perception"), ("RT-1", 2022, "robot transformer", "Demonstrated broad multi-task policy scaling")],
        "datasets": [("KITTI", "autonomous driving perception", "ATE, AP", "Standardized real mobile perception"), ("NYU Depth V2", "indoor RGB-D", "depth error, mIoU", "Supported indoor geometry and semantics"), ("ImageNet", "visual pretraining", "top-1", "Supplied transferable visual features, though not embodied supervision")],
    },
    "02_robot_perception_foundations": {
        "frame": "Reliable robot behavior depends on calibrated geometry, temporal estimation, uncertainty, fusion, and timing; semantic accuracy alone cannot guarantee a physically valid action.",
        "core": "A robot estimates latent state from partial, noisy, asynchronous observations. Coordinate frames connect camera measurements to bodies, end effectors, maps, and objects. Bayesian filtering, factor graphs, bundle adjustment, and learned estimators trade model bias against data-driven flexibility. Observability is action-dependent: a robot can move its camera, touch an object, or change illumination to resolve ambiguity. Production systems must also timestamp, synchronize, reject outliers, and expose confidence to planning.",
        "systems": [("Kalman filter", 1960, "estimator", "Canonical recursive uncertainty propagation"), ("ORB-SLAM3", 2021, "visual-inertial SLAM", "Strong geometry baseline across sensor configurations"), ("AprilTag 3", 2019, "fiducial system", "High-reliability calibration and pose reference"), ("Factor graphs / GTSAM", 2012, "optimization", "Unifies multi-sensor state estimation")],
        "datasets": [("EuRoC MAV", "visual-inertial odometry", "ATE, RPE", "Tests aggressive motion and synchronization"), ("TUM RGB-D", "RGB-D SLAM", "ATE, RPE", "Provides indoor trajectories and ground truth"), ("M2DGR", "multi-modal localization", "trajectory error", "Stresses fusion across cameras, LiDAR, GNSS, and IMU")],
    },
    "03_core_robotics_cv_problems": {
        "frame": "This problem converts visual evidence into state variables that manipulation, navigation, and interaction policies can use under clutter, occlusion, contact, and time pressure.",
        "core": "Robot perception tasks should be defined by downstream decision sufficiency, not annotation convenience. Detection without metric pose may be useless for grasping; a perfect mask may omit material, articulation, support, or reachability; a map may be geometrically accurate but stale after interaction. Strong systems combine object-level semantics, dense geometry, temporal tracking, uncertainty, and action-conditioned queries. Evaluation should include closed-loop task success and calibrated failure detection alongside offline accuracy.",
        "systems": [("Mask R-CNN", 2017, "instance segmentation", "Established strong object masks for manipulation pipelines"), ("DenseFusion", 2019, "6D pose", "Fused RGB and depth at pixel level"), ("Contact-GraspNet", 2021, "grasp perception", "Generated collision-aware 6-DoF grasps in clutter"), ("Grounded SAM", 2023, "open-vocabulary segmentation", "Composed language grounding with segmentation")],
        "datasets": [("YCB-Video", "6D object pose", "ADD-S, AUC", "Tests cluttered tabletop pose"), ("GraspNet-1Billion", "6-DoF grasping", "AP under friction thresholds", "Large-scale cluttered grasp evaluation"), ("BEHAVIOR-1K", "interactive household tasks", "task success", "Evaluates state changes and long-horizon perception")],
    },
    "04_3d_and_spatial_understanding": {
        "frame": "Robots act in metric 3D worlds that persist and change over time; 2D recognition must therefore be lifted into spatial, temporal, and uncertainty-aware representations.",
        "core": "Spatial representations encode different invariants. Point clouds preserve measurements but lack surfaces; voxels simplify collision and occupancy queries but scale cubically; meshes encode surfaces but are costly to update; implicit fields are continuous but expensive or opaque; Gaussian splats render quickly but need additional structure for physics. Robotics requires online updates, frame consistency, free-space reasoning, object permanence, and query interfaces for reachability, support, containment, and future occupancy.",
        "systems": [("TSDF fusion", 1996, "3D representation", "Integrates noisy depth into surfaces"), ("ORB-SLAM3", 2021, "SLAM", "Metric localization baseline"), ("NeRF", 2020, "neural rendering", "Popularized continuous scene fields"), ("3D Gaussian Splatting", 2023, "scene representation", "Enabled high-quality real-time rendering"), ("ConceptFusion", 2023, "open-set mapping", "Fused language-aligned features into 3D maps")],
        "datasets": [("ScanNet", "indoor 3D understanding", "mIoU, AP", "Real reconstructed indoor scenes"), ("Replica", "photorealistic indoor simulation", "rendering and navigation metrics", "Supports controlled embodied evaluation"), ("Dynamic Replica", "dynamic 3D scenes", "depth and motion error", "Targets time-varying geometry")],
    },
    "05_multimodal_perception": {
        "frame": "Vision is informative before contact, but touch, force, proprioception, depth, and language resolve ambiguities that RGB alone cannot observe.",
        "core": "Multimodal fusion requires alignment in space, time, and semantics. Early fusion exposes cross-modal interactions but is sensitive to calibration and missing sensors; late fusion is modular but can discard fine correspondences; token-level fusion is flexible but computationally expensive. Tactile signals are local and contact-triggered, proprioception is high-rate but indirect, and language supplies task priors rather than physical truth. Robust systems model modality reliability and train with sensor dropout.",
        "systems": [("CLIP", 2021, "vision-language model", "Provides open-vocabulary semantic priors"), ("GelSight", 2017, "tactile sensor", "Captures high-resolution contact geometry"), ("ViViDex", 2023, "visuotactile policy", "Uses human video and tactile sensing for dexterity"), ("Grounding DINO", 2023, "open-set detector", "Grounds free-form text in images")],
        "datasets": [("Touch and Go", "visuotactile learning", "retrieval and classification", "Pairs in-the-wild vision and touch"), ("Ego4D", "egocentric video", "task-specific metrics", "Provides first-person temporal priors"), ("ObjectFolder 2.0", "multisensory objects", "recognition and generation", "Models vision, audio, and touch")],
    },
    "06_vla_and_embodied_foundation_models": {
        "frame": "Embodied foundation models place visual representation learning inside a perception-memory-reasoning-action loop, where errors alter the next observation and can cause physical failure.",
        "core": "A VLA maps visual observations, language, and robot state to actions, often by adapting a pretrained VLM and adding an action decoder. Architectures differ in action tokenization, continuous regression, diffusion or flow heads, action chunking, memory, and control hierarchy. The central constraint is multi-timescale operation: semantic reasoning can run at a few hertz, while stable contact and whole-body control may require tens to hundreds of hertz. World models instead learn predictive state transitions and can support imagination or planning; hybrid systems increasingly combine both.",
        "systems": [("RT-1", 2022, "robot transformer", "Scaled multi-task real-robot behavior"), ("RT-2", 2023, "VLA", "Represented actions as language-like tokens"), ("OpenVLA", 2024, "open VLA", "Released a reproducible 7B VLA"), ("Octo", 2024, "open policy", "Generalist transformer trained across robot datasets"), ("pi0", 2024, "flow VLA", "Used a flow-matching action expert"), ("Helix", 2025, "humanoid VLA", "Separated 7-9 Hz semantics from 200 Hz control")],
        "datasets": [("Open X-Embodiment", "cross-embodiment policy learning", "per-task success", "Aggregates heterogeneous robot experience"), ("LIBERO", "lifelong manipulation", "task success", "Tests transfer and interference"), ("CALVIN", "language-conditioned long horizon", "sequence completion", "Measures chained skill execution")],
    },
    "07_data_simulation_and_training": {
        "frame": "Robot learning is constrained less by raw model capacity than by expensive action-labeled trajectories, inconsistent embodiments, sparse failures, and weak evaluation.",
        "core": "Robot data couples observations to actions, timing, embodiment, controller settings, and outcomes. Teleoperation yields grounded demonstrations but embeds operator strategy and hardware quirks. Simulation offers scale and privileged labels, yet visual, contact, dynamics, and behavior-policy gaps compound. Passive video supplies semantic and physical priors without executable actions. Effective training mixtures use web data for semantics, robot data for control, simulation for coverage, and autonomous rollouts for hard cases, while tracking provenance and leakage.",
        "systems": [("Domain Randomization", 2017, "sim-to-real method", "Trains invariance by broad synthetic variation"), ("RoboNet", 2020, "multi-robot dataset", "Early large-scale heterogeneous robot video"), ("DROID", 2024, "robot dataset", "Collects diverse manipulation in many scenes"), ("Open X-Embodiment", 2023, "data mixture", "Established cross-robot co-training"), ("Isaac Lab", 2024, "simulation stack", "GPU-parallel robot learning workflows")],
        "datasets": [("DROID", "in-the-wild manipulation", "downstream success", "Diverse scenes, tasks, and operators"), ("BridgeData V2", "language-conditioned manipulation", "policy success", "Broad tabletop skills"), ("RoboCasa", "simulated household manipulation", "task success", "Large procedural scenes and tasks")],
    },
    "08_manipulation_navigation_and_control": {
        "frame": "Perception becomes useful only when it closes the loop: selecting goals, constraining plans, detecting contact and progress, and triggering recovery.",
        "core": "Manipulation emphasizes pose, affordance, contact, and object-state change; navigation emphasizes localization, free space, semantics, and persistent memory. Long-horizon behavior needs both fast reactive feedback and slower task-level reasoning. Open-loop action chunks improve throughput but accumulate model error; fully reactive control can be myopic and computationally expensive. Practical systems mix learned visuomotor policies, geometric constraints, skill libraries, and explicit monitors.",
        "systems": [("MoveIt", 2012, "planning framework", "Connects perception to collision-aware manipulation"), ("SayCan", 2022, "language planning", "Grounds language plans with skill affordances"), ("Diffusion Policy", 2023, "visuomotor policy", "Models multimodal action sequences"), ("Mobile ALOHA", 2024, "mobile manipulation", "Demonstrates whole-body imitation learning")],
        "datasets": [("CALVIN", "long-horizon manipulation", "completed instruction chains", "Stresses memory and sequencing"), ("Habitat", "embodied navigation", "SPL, success", "Scalable navigation evaluation"), ("ManiSkill", "simulated manipulation", "task success", "Standardized contact-rich tasks")],
    },
    "09_robot_platforms_and_hardware": {
        "frame": "Embodiment determines observability, action space, control rate, data compatibility, and which visual errors become dangerous.",
        "core": "Hardware is part of the learning problem. Camera placement trades field of view against occlusion and calibration stability; wrist cameras provide local detail but move rapidly; head cameras support global context but suffer self-occlusion. Depth and LiDAR add geometry with material and range failure modes. Tactile and force sensing reveal contact after vision becomes least reliable. Compute budgets constrain image resolution, model size, thermal envelope, determinism, and control latency.",
        "systems": [("Franka Emika Panda", 2017, "manipulator", "Common research arm with torque sensing"), ("Stretch RE1", 2020, "mobile manipulator", "Accessible platform for household navigation and manipulation"), ("ALOHA", 2023, "bimanual platform", "Low-cost teleoperation and imitation learning"), ("Figure 02", 2024, "humanoid", "High-dimensional onboard visual control platform")],
        "datasets": [("ALOHA demonstrations", "bimanual manipulation", "task success", "Captures synchronized dual-arm behavior"), ("TartanAir", "visual navigation", "trajectory error", "Provides difficult synthetic motion and appearance"), ("KITTI-360", "mobile 3D perception", "mapping and detection metrics", "Long-range multi-sensor urban sequences")],
    },
    "10_frontier_2024_2026": {
        "frame": "This is a very recent, rapidly changing area; claims here are dated and should be distinguished from independently reproduced evidence.",
        "core": "The frontier is converging on heterogeneous co-training, continuous action generators, hierarchical reasoning, cross-embodiment transfer, open-world semantics, and predictive scene models. Demonstrations have improved faster than standardized evaluation. Key unknowns include whether scaling curves persist outside curated setups, how much autonomy is present in company videos, whether learned policies recover from rare contact failures, and how reliability changes over hours rather than short episodes. 2026 evidence should therefore be read as provisional unless accompanied by methods, data, and repeatable tests.",
        "systems": [("OpenVLA", 2024, "open VLA", "Made VLA training and adaptation inspectable"), ("pi0", 2024, "flow VLA", "Joined pretrained semantics with continuous action generation"), ("Gemini Robotics", 2025, "VLA", "Extended a multimodal model toward dexterous physical action"), ("Helix", 2025, "humanoid VLA", "Demonstrated asynchronous semantic and 200 Hz control"), ("pi0.5", 2025, "VLA", "Targeted unseen-home generalization with heterogeneous co-training")],
        "datasets": [("SimplerEnv", "VLA evaluation", "real-to-sim correlation and success", "Attempts scalable policy comparison"), ("LIBERO", "knowledge transfer", "task success", "Tests several generalization regimes"), ("BEHAVIOR-1K", "household activities", "task and predicate success", "Moves evaluation toward long-horizon physical state change")],
    },
    "11_datasets_papers_labs": {
        "frame": "A research database is useful only if it distinguishes landmark evidence, reproducible resources, institutional incentives, and benchmark blind spots.",
        "core": "Resources should be selected by the decision they enable. Dataset size alone hides environment diversity, operator diversity, failure coverage, action semantics, embodiment, sensor calibration, and licensing. Papers should be read with protocols and negative results, not only headline demonstrations. Lab and company maps should separate open publications from proprietary claims. Conferences provide different evidence cultures: CV venues emphasize perception metrics, robotics venues emphasize systems and hardware, and ML venues emphasize learning principles.",
        "systems": [("Papers with Code", 2018, "index", "Links methods, code, and benchmarks"), ("Hugging Face LeRobot", 2024, "open ecosystem", "Standardizes datasets, policies, and hardware interfaces"), ("Open X-Embodiment", 2023, "community dataset", "Coordinates cross-institution robot data"), ("ROS 2", 2017, "middleware", "Production-oriented communication and tooling")],
        "datasets": [("Open X-Embodiment", "generalist policies", "downstream success", "Largest influential cross-robot mixture"), ("Ego4D", "egocentric video", "episodic and interaction metrics", "Human first-person priors"), ("GraspNet-1Billion", "grasp perception", "grasp AP", "Dense cluttered-scene supervision")],
    },
    "12_meta": {
        "frame": "Research notes need explicit definitions, reading order, update rules, and falsifiable questions to remain useful as the field changes.",
        "core": "A living survey should separate stable foundations from frontier claims, record source dates, distinguish author-reported from independently reproduced results, and connect every benchmark to a robotics capability. Terminology must expose hidden assumptions: 'generalization' needs a specified axis; 'world model' needs a prediction target and action conditioning; 'real time' needs measured end-to-end latency; and 'open world' needs a failure and abstention protocol.",
        "systems": [("PRISMA", 2020, "review protocol", "Provides transparent literature selection practices"), ("Semantic Scholar", 2015, "literature graph", "Supports citation tracing"), ("Connected Papers", 2020, "discovery tool", "Maps neighboring literature"), ("Zotero", 2006, "reference manager", "Maintains source metadata and snapshots")],
        "datasets": [("Database completion audit", "coverage", "files and sections complete", "Prevents hollow scaffolding"), ("Citation freshness audit", "recency", "age and source class", "Flags unstable claims"), ("Replication audit", "evidence quality", "independent confirmations", "Separates demonstrations from established capability")],
    },
}

SPECIAL = {
    "00_overview_roadmap": """
The contemporary stack has four coupled layers. Perception converts sensor streams into object, geometry, motion, contact, and uncertainty estimates. Scene representation and memory maintain those estimates across occlusion and action. Reasoning or prediction selects subgoals, estimates consequences, and decides when more information is needed. Action generation and control produce embodiment-specific trajectories and close the loop at hardware-relevant rates. VLAs compress several layers into one trained system; modular planners keep interfaces explicit; world models predict transitions; diffusion or flow policies model local action distributions.

The important change from classical robot perception is not that detection disappeared. Detection, segmentation, pose, tracking, mapping, and calibration still occur either explicitly or inside learned features. What changed is the training objective and interface: perception is increasingly optimized jointly with language and action, and representations may be latent rather than human-labeled. This can preserve task-relevant cues that a hand-designed interface omits, but it also makes geometry, uncertainty, and failure causes harder to inspect.

A plausible near-term architecture is hierarchical and asynchronous. A large multimodal model performs open-vocabulary interpretation and task decomposition at low frequency; an object-centric 3D memory maintains persistent state; a predictive model evaluates candidate transitions; and a compact reactive policy executes action chunks under safety constraints. Figure's Helix makes the timescale split explicit, while pi0.5 combines high-level textual subtask prediction with a continuous flow-matching action expert. These are design points, not proof that hierarchy is solved: both persistent memory and recovery remain weakly evaluated.
""",
    "01_vla_model_architectures": """
A VLA consumes images, language instructions, and usually proprioceptive state, then predicts robot actions. It differs from a VLM with an action head because the training distribution is sequential and intervention-dependent: actions change camera pose, contact, object state, and future observations. The model must learn temporal alignment, embodiment conventions, controller semantics, and closed-loop correction, none of which follows automatically from image-text pretraining.

Common architectures pair a ViT or VLM visual encoder with a language backbone and one of four action decoders. Discrete token decoders quantize action dimensions and reuse autoregressive next-token training, as in RT-2-style formulations; continuous regression heads are efficient but average incompatible strategies; diffusion heads represent multimodal action sequences through iterative denoising; flow-matching heads learn a continuous transport field. Action chunking predicts several future controls at once, improving throughput at the cost of feedback frequency.

Short-horizon control asks the network to react locally, often at 10-50 Hz or faster. Long-horizon behavior additionally needs task decomposition, memory, termination prediction, and recovery. Humanoids sharpen the constraint: vision-language inference may run below 10 Hz while balance, fingers, and contact loops require 100-1000 Hz. Helix addresses this through an asynchronous 7-9 Hz semantic system and 200 Hz visuomotor system; other stacks place a VLA above conventional whole-body controllers.

Internally, VLAs must resolve referring expressions, parse object parts and support relations, infer occlusion and depth, identify grasp regions, track state changes, and distinguish reachable from merely visible objects. Internet pretraining supplies semantic breadth, but metric pose, force, friction, and embodiment-specific reachability still come primarily from robot data, geometry modules, or interaction.
""",
    "02_rt1_rt2_rtx": """
RT-1 introduced a Transformer policy trained on roughly 130,000 real-robot demonstrations spanning more than 700 tasks collected over 17 months on Everyday Robots hardware. Images and language were compressed with TokenLearner, and actions were discretized. Its contribution was empirical: scaling task and data diversity improved robustness and transfer within a relatively consistent embodiment and operating domain.

RT-2 reframed robot control as vision-language-action modeling. It co-fine-tuned PaLI-X or PaLM-E-style vision-language backbones on web-scale vision-language tasks and robot trajectories, expressing actions as text-like tokens. This allowed semantic concepts from web data to influence robot behavior. It did not remove embodiment constraints: low-level action tokens, camera geometry, gripper behavior, and evaluation remained tied to the robot setup, and inference latency limited control granularity.

Open X-Embodiment and RT-X shifted the scaling question from tasks on one fleet to heterogeneous experience across 22 embodiments and 60 datasets contributed by 21 institutions in the original release. RT-1-X and RT-2-X showed that co-training can improve many constituent datasets. Yet action normalization is not a universal interface: joint spaces, end-effector frames, control modes, horizons, grippers, and observation layouts differ. Cross-embodiment gains often transfer semantics and coarse manipulation priors more readily than precise dynamics.
""",
    "03_openvla_octo_and_open_models": """
OpenVLA and Octo made generalist robot-policy research inspectable. OpenVLA released a 7B-parameter VLA initialized from a vision-language backbone and trained on a large Open X-Embodiment mixture, together with adaptation recipes. Octo released smaller transformer policies with flexible observation and action readouts. Both enable controlled studies of data mixtures, parameter-efficient fine-tuning, action normalization, and deployment that are impossible with API-only systems.

Their openness does not erase the infrastructure gap. Closed labs may possess larger fleets, higher-quality teleoperation, consistent hardware, failure logs, safety engineering, and proprietary evaluation sites. Public mixtures contain inconsistent camera views, action conventions, labels, and success criteria. Reproducing pretraining also requires substantial accelerator resources and careful dataset weighting.

The open ecosystem is most valuable as a measurement platform. Researchers can freeze visual encoders, compare LoRA against full fine-tuning, test action tokenizers or diffusion heads, audit catastrophic forgetting, and evaluate on LIBERO, CALVIN, SimplerEnv, or local robots. LeRobot further standardizes dataset formats, policies, and lower-cost hardware.
""",
    "04_pi0_gr00t_helix": """
pi0, GR00T, and Helix represent different bets on physical foundation models. Physical Intelligence's pi0 couples a pretrained vision-language model to a flow-matching action expert, producing continuous action chunks for several embodiments. pi0.5, published April 22, 2025, extends the recipe with heterogeneous co-training over web multimodal tasks, cross-embodiment data, multiple environments, and verbal instruction traces; it alternates high-level textual subtask prediction with 50-step, one-second low-level action chunks.

NVIDIA's GR00T program is organized as a humanoid foundation-model and data-generation stack rather than only a single policy. It combines multimodal reasoning, embodiment-specific action modules, Isaac simulation, synthetic motion or video generation, and deployment tooling. Its strategic significance is integration across simulation, data processing, training, and hardware partners. Public versions and claims evolve rapidly, so exact comparisons require dated technical reports.

Figure's Helix, announced February 20, 2025, uses two jointly trained systems. A 7B open-weight VLM runs at 7-9 Hz and emits a semantic latent; an 80M visuomotor transformer runs at 200 Hz and outputs continuous upper-body targets for wrists, fingers, torso, and head. Figure reports about 500 hours of teleoperated data, asynchronous inference on two onboard GPUs, 35-DoF upper-body control, novel-object picking, and two-robot coordination. These are company-reported results rather than public benchmark reproduction.

The comparison is not a leaderboard. pi0 emphasizes a reusable continuous action expert and heterogeneous co-training; GR00T emphasizes a platform-scale synthetic-data and humanoid ecosystem; Helix emphasizes onboard, high-rate, high-dimensional control through timescale separation. Humanoids must coordinate gaze, torso, balance, hands, and whole-body reach while self-motion changes perception, making embodiment and deployment architecture central.
""",
    "05_world_models_for_robotics": """
A robot world model predicts how task-relevant state changes under action: p(z[t+1:t+H] | z[t], a[t:t+H-1]). The state may be pixels, object slots, occupancy, geometry, language-aligned features, or a learned latent. The model can support model-predictive control, counterfactual evaluation, policy training from imagined rollouts, data generation, or anomaly detection.

Pixel prediction preserves appearance and produces inspectable videos, but spends capacity on texture and can generate visually plausible yet physically inconsistent contact. Abstract latent prediction can focus on predictable structure and scale to longer horizons, but may discard small geometric or force cues needed for insertion and grasp stability. Object-centric models improve compositionality and permanence but require robust discovery and tracking. 3D or 4D models add viewpoint consistency at significant sensing and computation cost.

Passive video teaches object permanence, human-object interactions, rough dynamics, and semantic task structure. It does not identify the robot's action, applied force, controller state, or counterfactual outcomes. Action-conditioned trajectories provide causal grounding but are scarce and embodiment-specific. A practical recipe pretrains visual dynamics from video, aligns with robot actions, and continually corrects predictions from real interaction.

World models help perception by completing occluded objects, predicting where a moved object should reappear, maintaining state through self-motion, and distinguishing expected from anomalous outcomes. Their main failure is model exploitation: a planner finds trajectories that look good in the learned model but fail physically. Uncertainty, short replanning horizons, real-data correction, and hard constraints are necessary.
""",
    "07_generalist_vs_specialist": """
The generalist thesis argues that broad data and shared parameters produce transferable visual, semantic, and motor abstractions. The specialist thesis argues that physical reliability depends on task-specific sensing, models, controllers, and validation. Both are correct at different layers. A generalist model may identify a novel utensil and choose a strategy; a specialist grasp module may remain superior for collision-aware pickup; a certified controller may enforce force and speed limits.

End-to-end does not mean intermediate perception disappears. Object identity, pose, support, contact phase, and progress may be represented in latent activations rather than explicit APIs. This can avoid annotation bottlenecks, but it does not eliminate estimation. When a policy fails, latent state is harder to inspect, correct, cache, or share. Explicit CV modules remain valuable where geometry is measurable, safety constraints are formal, or data is scarce.

Robotic control resists a pure language-model scaling analogy because data is expensive and correlated; outputs are continuous and timing-sensitive; errors alter future observations and can damage hardware; and embodiments impose different kinematics and dynamics. More parameters cannot compensate for missing observability, calibration, or contact sensing.

The emerging architecture is hybrid: a generalist model handles language, semantics, task decomposition, and skill selection; persistent metric or object-centric memory supports spatial consistency; specialist policies execute contact-rich skills; and planning or control enforces constraints. The research question is which interfaces allow shared learning without sacrificing verifiability and rate.
""",
    "03_affordance_detection": """
Affordances are action opportunities relative to an agent, not immutable object labels. A mug can be graspable at its handle, containable in its cavity, and pourable under a suitable orientation; the same regions may be unreachable from the current configuration. Gibson's ecological framing and later robotics work therefore imply a conditional function A(x, a, e): feasibility depends on scene state x, candidate action a, and embodiment e.

Three formulations dominate. Object-level classification predicts verbs such as openable or sit-able, but loses contact geometry. Dense affordance segmentation predicts pixels or points associated with grasping, cutting, supporting, or traversing, but often treats labels as static. Action-conditioned scoring evaluates candidate interactions and is closest to control, yet requires expensive demonstrations or simulation. Modern VLMs improve semantic proposals and novel-object transfer, while methods such as Where2Act, VAT-Mart, and ActAfford expose 3D interaction points and trajectories. The unresolved issue is grounding linguistic plausibility in force closure, articulation, reachability, and post-contact state.
""",
    "08_deformable_object_perception": """
Deformables violate the rigid-body assumptions behind pose estimation, object permanence, and compact state. Cloth has effectively infinite configurations; cables combine continuous geometry with discrete knot and crossing structure; bags change topology between open, folded, and crumpled states; food and soft packaging exhibit irreversible deformation. A single SE(3) pose is therefore not a sufficient statistic.

Useful representations include keypoints and contours, dense particle or mesh states, learned latent states, graph models, and topological descriptors. Each fails differently: keypoints miss folds, meshes are difficult to reconstruct under self-occlusion, particles drift without correspondence, and latent states can be visually predictive while physically wrong. Contact is partially observed because the gripper occludes the manipulation region and RGB-D sensors fail on thin, reflective, or textureless material. Benchmarks such as SoftGym, DeformableRavens, and cloth-folding suites remain substantially simpler than laundry, cables in clutter, food handling, or opening flexible packaging.
""",
    "07_spatial_reasoning_bottlenecks": """
Multimodal models often answer spatial questions from dataset priors rather than maintaining a metric, viewpoint-consistent scene model. Left/right depends on reference frame; front/behind changes with viewpoint; containment requires boundary reasoning; support requires gravity and contact; reachability requires robot kinematics and collision geometry. Token-level language supervision rarely identifies these latent variables.

Failure categories include frame confusion, depth-order inversion, inconsistent counting, poor mental rotation, loss of object permanence, and inability to distinguish semantic proximity from executable reach. 2D benchmarks can reward plausible text without testing physical validity. Robotics evaluation should instead perturb viewpoints, move occluders, ask counterfactual action questions, and verify predictions through reachability or manipulation. Explicit 3D maps help geometry but do not automatically encode functional relations; implicit VLM representations carry semantics but are difficult to audit. Hybrid object-centric metric memory is a leading direction.
""",
    "01_robot_data_bottleneck": """
Robot trajectories are costly because every sample consumes wall-clock hardware time and couples to a specific camera layout, controller, gripper, calibration, and operator. Failures damage equipment and are under-recorded; successful demonstrations overrepresent smooth behavior and underrepresent recovery. Unlike text, robot data cannot be copied from the public web with its action semantics intact.

A robotics data flywheel deploys a partially capable policy, logs uncertainty and interventions, prioritizes informative failures, relabels outcomes, retrains, and redeploys. Its defensibility comes from fleet access, standardized hardware, teleoperation infrastructure, task distribution, and outcome labels rather than raw video volume. Google DeepMind's RT-X effort, Tesla's fleet logic, autonomous-driving programs, and humanoid startups illustrate different possible moats, but public evidence about proprietary dataset quality remains limited. Scaling must address selection bias, embodiment normalization, safety gating, and data governance.
""",
    "05_sim2real_and_domain_randomization": """
Domain randomization succeeds when simulation spans the real nuisance factors while preserving task-relevant causal structure. It is effective for texture, lighting, camera pose, object placement, and some rigid-body parameter variation. It fails when the simulator omits the relevant phenomenon: cable friction, cloth self-contact, suction leakage, transparent objects, actuator backlash, human behavior, or rare collisions.

Photorealism primarily reduces appearance gap; dynamics realism reduces transition and contact gap. Neither guarantees policy transfer if the simulated behavior distribution differs from deployment. Isaac Sim/Lab emphasizes GPU-parallel training and sensor simulation; MuJoCo provides mature contact dynamics and control research; ManiSkill standardizes manipulation; Habitat emphasizes navigation; Genesis targets high-throughput generative simulation. Neural rendering and 3D Gaussian splatting can replay captured appearance, but interactive dynamics still require models of geometry, material, articulation, and contact.
""",
    "04_spatial_intelligence": """
Spatial intelligence is the ability to build, transform, query, and act on representations of objects, agents, free space, geometry, and relations across viewpoints and time. It includes metric depth and pose, but also support, containment, articulation, reachability, visibility, object permanence, and expected state change. In robotics, a spatial answer is useful only if it is expressed in the robot's frame and can constrain an action.

Generic VLM capability is not sufficient. Internet image-text pairs rarely specify camera calibration, metric scale, hidden surfaces, robot kinematics, force, or counterfactual interventions. Language can state that a cup is “near” a plate without deciding whether a gripper can approach it. A model can identify a drawer yet fail to estimate its axis, handle, collision envelope, or current openness. Spatial intelligence therefore requires embodied geometry and interaction supervision in addition to semantics.

Evaluation should combine viewpoint-consistent question answering, 3D reconstruction, relation tracking after object motion, reachability prediction, manipulation planning, and active information gathering. A strong benchmark would vary reference frames, occlusion, scene rearrangement, embodiment, and camera pose while checking answers against executable actions. Current benchmarks usually isolate only one layer, allowing systems to score well without maintaining coherent world state.
""",
    "05_world_model_vs_vla": """
VLAs and world models make different primary commitments. A VLA directly models actions conditioned on observations and instructions; a world model predicts future states conditioned on actions and leaves action selection to planning or a learned policy. VLAs exploit demonstration supervision efficiently and can run reactively. World models expose counterfactual structure and can reuse predictions across goals, but accurate long-horizon physical prediction is harder than action imitation.

VLAs usually provide lower control latency because they emit an action or chunk in one policy pass, although large backbones and autoregressive decoding can still be slow. World-model planning requires evaluating candidate trajectories and can exceed real-time budgets; latent models and short model-predictive horizons reduce the cost. Interpretability is mixed: generated video is inspectable but may be physically false, while an explicit VLA subgoal can be understandable even if its motor latent is opaque.

Data efficiency depends on the target. Demonstrations strongly constrain useful actions but cover a narrow behavior distribution. A world model can learn from broader transitions and potentially reuse passive video, yet action-free data cannot identify intervention effects. VLAs transfer semantic priors and skill patterns; world models may transfer dynamics or object permanence if their state is compositional. Both fail under unseen contact, materials, or embodiment.

The likely convergence is hierarchical: a VLA proposes goals or action chunks, a predictive model evaluates consequences and detects surprise, and a fast specialist controller executes. The world model may predict occupancy, object state, contact events, or value-relevant latent features rather than pixels. Likewise, a VLA may internally learn predictive representations. The useful distinction is architectural accountability, not branding.
""",
    "06_robotics_cv_open_problems": """
The hardest open problems are coupled. Cluttered manipulation combines occlusion, long-tail objects, collision, and uncertain support. Deformables require topology and contact state beyond rigid pose. Persistent memory must survive viewpoint change and update after humans or robots move objects. Contact-rich uncertainty requires fusing vision, force, touch, and controller state at different rates. Spatial reasoning must resolve frames, containment, support, and reachability rather than produce plausible language.

Safety-aware perception needs calibrated detection of people, tools, fragile objects, forbidden regions, and model uncertainty under domain shift. Multi-agent scenes add intent prediction, communication, and mutual occlusion. Lifelong adaptation must incorporate new objects and sensor conditions without erasing validated behavior. Open-world perception must map semantic novelty to action relevance: an unknown object may be ignorable, graspable after inspection, or a reason to stop.

Research protocols should emphasize adversarial rearrangement, transparent and reflective objects, lighting and calibration drift, long unattended runs, recovery after induced errors, and worst-group performance. The key metric is a reliability profile: probability and severity of failure, detectability before harm, recovery probability, and human intervention burden.
""",
    "07_future_roadmaps": """
Over the next two years, VLA work is likely to emphasize better data mixtures, faster continuous action heads, memory, and on-device inference rather than parameter count alone. Cross-embodiment pretraining will increasingly separate shared semantic-spatial features from hardware-specific action experts. Evaluation pressure should move from curated tabletop episodes toward unseen buildings, hours-long operation, perturbations, and explicit recovery.

World models are likely to become data engines before universal planners. Near-term value includes generating candidate futures, relabeling video, prioritizing uncertain transitions, producing synthetic demonstrations, and detecting deviations from expected outcomes. Spatially structured prediction of occupancy, object state, and contact may outperform unconstrained pixel video for control. Video generators remain useful for priors and visualization but need causal action alignment.

Three- to five-year progress depends on robot-native spatial intelligence: persistent object-centric 3D/4D memory, affordance and reachability queries, dynamic human-aware maps, and representations that connect semantics to material and contact. Visuotactile fusion should expand from laboratory sensors to scalable fingertips and whole-hand sensing. Deformables, transparent objects, cables, packaging, and food will be decisive tests because they expose rigid visual abstractions.

Deployment will push compact encoders, asynchronous hierarchies, quantization, edge accelerators, and explicit latency budgets. Safety research must pair learned perception with runtime monitors, uncertainty-triggered help, constrained control, and auditable logs. The strongest roadmap is not “one model controls everything,” but a measurable architecture combining broad priors, persistent state, predictive checks, high-rate feedback, and graceful escalation.
""",
    "01_2024_breakthroughs": """
The 2024 inflection was openness and continuous action generation. OpenVLA and Octo made generalist policy weights and training recipes available for study. DROID expanded real-world manipulation diversity across scenes and operators. Mobile ALOHA showed that comparatively accessible hardware and imitation learning could produce coordinated mobile, bimanual behavior. Physical Intelligence's pi0 connected a pretrained multimodal backbone to a flow-matching action expert, making continuous action distributions central to the foundation-model discussion.

The year also exposed evaluation weakness. Models were trained on overlapping Open X-Embodiment mixtures but tested on different robots, tasks, resets, and success definitions. SimplerEnv attempted scalable VLA evaluation through real-to-sim correspondence, while LIBERO and CALVIN remained common but imperfect proxies. The durable breakthrough was not a universally superior policy; it was a research program around open generalist models, heterogeneous data, action chunks, and reproducible adaptation.
""",
    "02_2025_breakthroughs": """
In 2025 the frontier moved toward unseen environments, humanoid control, and hierarchical timescales. Physical Intelligence published pi0.5 on April 22, emphasizing heterogeneous co-training and generalization to homes absent from training. Figure announced Helix on February 20, pairing a 7-9 Hz VLM with a 200 Hz visuomotor controller for high-dimensional humanoid upper-body action. Google DeepMind announced Gemini Robotics and Gemini Robotics-ER on March 12, extending Gemini-derived multimodal reasoning toward physical action and embodied reasoning.

These systems should be compared cautiously. pi0.5 reports controlled ablations over web, multi-environment, and cross-embodiment data; Helix provides unusually concrete architecture, rate, parameter, and teleoperation details but remains a company system; Gemini Robotics emphasizes generality, interactivity, and dexterity across partner platforms but is not an open training recipe. NVIDIA's GR00T releases and Isaac tooling reinforced a parallel strategy centered on humanoid data generation and simulation. The shared trend is hierarchy plus heterogeneous data, not convergence on one action representation.
""",
    "03_2026_current_frontier": """
As of June 10, 2026, this section must be treated as provisional. The most credible trajectory is toward longer-horizon mobile manipulation, whole-body humanoid control, predictive data engines, and on-device multimodal policies. Public claims are arriving faster than peer-reviewed, independently reproduced evidence, and product names or versions may change within months.

The research bar for 2026 should therefore be longitudinal and operational: unseen-site deployment, hours between interventions, recovery after induced perturbations, calibrated stopping, whole-body collision safety, and transparent accounting of teleoperation or remote assistance. Short demonstration videos are useful qualitative evidence but cannot establish autonomy, reliability, or scaling laws. Updates to this note should cite a dated technical report, paper, benchmark protocol, or reproducible release and explicitly separate those from press or company claims.
""",
}

FRONTIER_SOURCES = [
    ("Open X-Embodiment / RT-X", "https://robotics-transformer-x.github.io/"),
    ("OpenVLA", "https://openvla.github.io/"),
    ("Octo", "https://octo-models.github.io/"),
    ("Physical Intelligence pi0", "https://www.pi.website/blog/pi0"),
    ("Physical Intelligence pi0.5", "https://www.pi.website/blog/pi05"),
    ("Figure Helix", "https://www.figure.ai/news/helix"),
    ("Gemini Robotics", "https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/"),
    ("NVIDIA GR00T", "https://developer.nvidia.com/isaac/gr00t"),
]

TOPIC_SYSTEMS = {
    "calibration": [("Zhang calibration", 2000, "calibration", "Standard planar-target camera calibration"), ("Kalibr", 2013, "toolkit", "Camera-IMU and multi-camera calibration")],
    "depth": [("Semi-Global Matching", 2008, "stereo", "Strong classical dense correspondence"), ("RAFT-Stereo", 2021, "learned stereo", "Iterative high-accuracy disparity estimation")],
    "motion": [("RAFT", 2020, "optical flow", "Iterative dense motion estimation"), ("TAPIR", 2023, "tracking", "Long-range point tracking through occlusion")],
    "uncertainty": [("Deep Ensembles", 2017, "uncertainty", "Practical epistemic uncertainty baseline"), ("Conformal prediction", 2021, "calibration", "Finite-sample coverage framework")],
    "detection": [("DETR", 2020, "detector", "Set prediction without hand-designed anchors"), ("OWL-ViT", 2022, "open-vocabulary detector", "Text-conditioned long-tail detection")],
    "pose": [("PoseCNN", 2018, "6D pose", "Direct pose estimation in clutter"), ("FoundationPose", 2024, "6D tracking", "Model-based pose and tracking for novel objects")],
    "affordance": [("Where2Act", 2021, "3D affordance", "Interaction proposals for articulated objects"), ("VAT-Mart", 2022, "trajectory affordance", "Predicts actionable interaction trajectories")],
    "grasp": [("Dex-Net 2.0", 2017, "grasp learning", "Synthetic analytic grasp supervision"), ("AnyGrasp", 2023, "grasp detection", "General 6-DoF grasp proposals in clutter")],
    "semantic_mapping": [("SemanticFusion", 2017, "semantic SLAM", "Fused CNN semantics into dense maps"), ("VLMaps", 2023, "language map", "Language-indexed spatial maps for navigation")],
    "egocentric": [("EgoVLP", 2022, "video-language pretraining", "Egocentric video-language alignment"), ("Ego-Exo4D", 2024, "multiview dataset", "Links first- and third-person skilled activity")],
    "deformable": [("SoftGym", 2020, "benchmark", "Standardized deformable manipulation simulation"), ("Diffusion Policy", 2023, "policy", "Strong visuomotor sequence modeling for bimanual tasks")],
    "slam": [("DROID-SLAM", 2021, "learned SLAM", "Dense recurrent bundle adjustment"), ("iMAP", 2021, "neural SLAM", "Online implicit scene mapping")],
    "neural_scene": [("iSDF", 2022, "neural field", "Real-time signed-distance learning for robotics"), ("NICE-SLAM", 2022, "neural SLAM", "Hierarchical implicit indoor mapping")],
    "gaussian": [("SplaTAM", 2024, "Gaussian SLAM", "Online tracking and mapping with Gaussian splats"), ("LERF", 2023, "language field", "Open-vocabulary queries in neural 3D scenes")],
    "dynamic_4d": [("D-NeRF", 2021, "dynamic field", "Canonical-space dynamic neural rendering"), ("Dynamic 3D Gaussians", 2024, "4D representation", "Tracks time-varying Gaussian scenes")],
    "occupancy": [("Voxblox", 2017, "mapping", "Incremental TSDF/ESDF maps for planning"), ("NeuralRecon", 2021, "3D reconstruction", "Real-time learned volumetric reconstruction")],
    "visuotactile": [("GelSight", 2017, "tactile vision", "High-resolution contact geometry"), ("See to Touch", 2023, "visuotactile policy", "Cross-modal pretraining for dexterous control")],
    "language_grounded": [("MDETR", 2021, "grounding", "End-to-end text-conditioned detection"), ("Grounding DINO", 2023, "grounding", "Open-set phrase-to-box detection")],
    "open_vocabulary": [("OWL-ViT", 2022, "open-vocabulary detector", "Text-query detection"), ("ConceptFusion", 2023, "3D mapping", "Open-set multimodal 3D maps")],
    "event_camera": [("E2VID", 2019, "event reconstruction", "Reconstructs intensity video from events"), ("UltimateSLAM", 2018, "event SLAM", "Event-frame-inertial odometry")],
    "diffusion": [("Diffusion Policy", 2023, "action generation", "Multimodal receding-horizon control"), ("3D Diffusion Policy", 2024, "3D policy", "Uses compact 3D visual representations")],
    "teleoperation": [("ALOHA", 2023, "teleoperation", "Low-cost bimanual data collection"), ("UMI", 2024, "demonstration interface", "Portable in-the-wild manipulation capture")],
    "simulation": [("MuJoCo", 2012, "simulator", "Contact-rich dynamics and control"), ("Isaac Lab", 2024, "simulator", "GPU-parallel robot learning workflows")],
    "long_horizon": [("SayCan", 2022, "hierarchical agent", "Grounded language plans with skill values"), ("VoxPoser", 2023, "planning", "Composes language and 3D value maps")],
    "humanoid": [("Digit", 2020, "humanoid platform", "Commercial bipedal logistics embodiment"), ("Apollo", 2023, "humanoid platform", "General-purpose industrial humanoid")],
}

TOPIC_DATASETS = {
    "calibration": [("TUM VI", "visual-inertial calibration and odometry", "ATE", "Difficult fisheye and inertial sequences")],
    "pose": [("BOP Challenge", "6D pose", "AR over pose errors", "Standardizes object-pose evaluation"), ("HOPE", "household pose", "ADD-S", "Photorealistic clutter and novel scenes")],
    "affordance": [("AffordanceNet", "object affordance segmentation", "mIoU", "Dense part-level affordance labels"), ("PartNet-Mobility", "articulated interaction", "pose and part metrics", "3D articulated object structure")],
    "grasp": [("Dex-Net", "parallel-jaw grasping", "robust grasp success", "Large synthetic analytic labels")],
    "semantic_mapping": [("HM3D", "indoor navigation", "SPL and success", "Large scanned-space navigation"), ("Matterport3D", "semantic indoor mapping", "mIoU and navigation metrics", "Real multistory environments")],
    "deformable": [("SoftGym", "deformable manipulation", "normalized performance", "Cloth, rope, and fluid tasks"), ("DeformableRavens", "deformable rearrangement", "task success", "Vision-based cloth and cable tasks")],
    "slam": [("TartanAir", "visual odometry", "ATE", "Diverse difficult synthetic trajectories")],
    "gaussian": [("Replica", "indoor novel-view mapping", "PSNR and tracking error", "High-quality controlled scenes")],
    "visuotactile": [("VisGel", "vision-touch representation learning", "retrieval and prediction", "Paired visual and tactile observations")],
    "open_vocabulary": [("OVMM", "open-vocabulary mobile manipulation", "task success", "Connects semantic search to physical pickup")],
    "event_camera": [("MVSEC", "event-based motion estimation", "flow and trajectory error", "Synchronized event, frame, IMU, and depth")],
    "teleoperation": [("DROID", "teleoperated manipulation", "downstream success", "Diverse operators and environments"), ("RH20T", "multimodal manipulation", "policy success", "Large multi-sensor real robot collection")],
    "long_horizon": [("ALFRED", "language-guided household tasks", "task and goal-condition success", "Long-horizon perception and planning")],
    "humanoid": [("HumanoidBench", "whole-body control", "task reward", "Standardized simulated humanoid tasks")],
}

DOMAIN_FORMALISM = {
    "00_scope_and_map": r"""
Let a robot receive observations \(o_{0:t}\), execute actions \(a_{0:t-1}\), and
operate under a task variable \(g\). A robotics-vision representation
\(z_t=f_\theta(o_{0:t},a_{0:t-1},g)\) is useful only insofar as it supports a
decision rule \(\pi(a_t\mid z_t,g)\) with low task risk. This definition is
deliberately stricter than requiring high mutual information with image labels.
It asks whether \(z_t\) preserves the geometry, temporal state, uncertainty, and
causal structure needed by the action. Two representations can be equivalent
for classification yet radically different for collision avoidance or contact.
""",
    "01_history": r"""
The history can be organized as successive factorizations of the same latent
state-estimation problem. Geometric systems specify an observation model
\(p(o_t\mid x_t)\) and transition model \(p(x_t\mid x_{t-1},a_{t-1})\);
discriminative systems estimate task variables directly; foundation models
learn broad priors before robot adaptation. These are not mutually exclusive.
Modern systems still solve coordinate transforms, correspondence, filtering,
and constrained optimization even when those operations are embedded in a
neural network.
""",
    "02_robot_perception_foundations": r"""
The canonical formulation is Bayesian filtering:
\[
p(x_t\mid o_{1:t},a_{1:t-1}) \propto
p(o_t\mid x_t)\int p(x_t\mid x_{t-1},a_{t-1})
p(x_{t-1}\mid o_{1:t-1},a_{1:t-2})\,dx_{t-1}.
\]
The state \(x_t\) may contain camera pose, object pose, velocity, calibration,
contact, or map variables. A learned estimator changes the parameterization,
but it does not remove observability, synchronization, or uncertainty. The
important question is which latent variables are identifiable under the
available sensor trajectory and which require active motion or contact.
""",
    "03_core_robotics_cv_problems": r"""
For a perception output \(y=f_\theta(o)\), the correct objective is not merely
\(\ell(y,y^\star)\) but expected downstream regret:
\[
\mathcal{R}(\theta)=\mathbb{E}\left[
J(\pi^\star,x)-J(\pi(f_\theta(o)),x)\right].
\]
This exposes why annotation metrics can be misleading. A small mask error on a
background pixel may be irrelevant, while a similar error at a grasp contact,
door edge, or traversability boundary changes the feasible action set. Research
should therefore report both task-native perception metrics and decision-aware
metrics that weight errors by their physical consequence.
""",
    "04_3d_and_spatial_understanding": r"""
A spatial model estimates a scene field or structured state \(S_t\) from posed
observations. It should answer at least four query classes: occupancy
\(p(\mathrm{occ}(q))\), semantics \(p(c\mid q)\), geometry such as signed
distance \(d(q)\), and dynamics \(p(S_{t+1}\mid S_t,a_t)\). Rendering quality is
not sufficient: planning needs conservative free space, consistent frames, and
bounded update latency. The representation must distinguish unobserved space
from observed free space, a distinction that image synthesis metrics often
erase.
""",
    "05_multimodal_perception": r"""
For modalities \(o_t^{1:M}\), fusion estimates
\(p(x_t\mid o_{1:t}^{1:M})\) while accounting for asynchronous timestamps,
calibration, and modality-dependent failure. Conditional independence is rarely
valid: tactile observations depend on actions and contact, depth failure
correlates with material, and proprioception shares controller latency. A
robust fusion model should expose reliability variables \(r_t^m\) and degrade
gracefully when one modality is delayed, saturated, absent, or inconsistent.
""",
    "06_vla_and_embodied_foundation_models": r"""
A VLA policy models an action sequence conditioned on multimodal history and a
goal:
\[
\pi_\theta(a_{t:t+H-1}\mid o_{t-K:t},q_{t-K:t},\ell,e),
\]
where \(q\) is proprioception, \(\ell\) is language, and \(e\) identifies the
embodiment or action convention. The horizon \(H\), observation window \(K\),
control rate, and execution strategy are part of the model definition. A
one-step policy, an open-loop action chunk, and a receding-horizon diffusion
policy induce different closed-loop systems even when trained on the same
trajectories.
""",
    "07_data_simulation_and_training": r"""
Robot data are samples from a behavior policy, not an independent and
identically distributed image corpus. A trajectory
\(\tau=(o_0,a_0,\ldots,o_T)\sim p_{\mu,e,\mathcal{E}}(\tau)\) depends on the
operator or collection policy \(\mu\), embodiment \(e\), and environment
\(\mathcal{E}\). Dataset scaling changes this mixture and therefore changes both
coverage and bias. Effective sample size can be far smaller than frame count
because adjacent observations, repeated resets, and scripted demonstrations are
strongly correlated.
""",
    "08_manipulation_navigation_and_control": r"""
Closed-loop performance follows the coupled dynamics
\(x_{t+1}=F(x_t,a_t,w_t)\), \(o_t=G(x_t,v_t)\), and
\(a_t=\pi_\theta(o_{0:t},g)\). Perception, planning, and control cannot be
evaluated as independent blocks when their errors change the next observation.
For action chunks, the executed command is often
\(a_{t:t+h-1}\) with \(h\leq H\); choosing \(h\) trades inference cost against
feedback and should be treated as an experimental variable.
""",
    "09_robot_platforms_and_hardware": r"""
Deployment feasibility is constrained by a latency budget
\[
T_{\mathrm{sense}}+T_{\mathrm{transfer}}+T_{\mathrm{infer}}+
T_{\mathrm{plan}}+T_{\mathrm{actuate}} \leq T_{\mathrm{deadline}}.
\]
Average throughput does not establish this inequality. Tail latency, thermal
throttling, sensor jitter, dropped frames, and asynchronous clocks determine
whether the robot observes and reacts to the same physical event. Hardware
comparisons should normalize image resolution, precision, batch size, power
mode, controller interface, and the portion of computation performed offboard.
""",
    "10_frontier_2024_2026": r"""
Frontier evidence should be represented as a set of dated claims
\(C=\{(c_i,s_i,t_i,r_i)\}\), where \(s_i\) is the source, \(t_i\) the date, and
\(r_i\) a reproducibility level. A peer-reviewed paper, an open checkpoint, a
company technical report, and a demonstration video provide different evidence.
They should not be collapsed into a single capability ranking. Claims about
generality require explicit train-test boundaries and claims about autonomy
require accounting for resets, interventions, remote operation, and selection.
""",
    "11_datasets_papers_labs": r"""
A resource map is useful when it records comparability, not only names.
For each dataset or paper, define the observation space, action convention,
embodiment, collection policy, train-test unit, evaluation protocol, license,
and known leakage. For each result, distinguish within-distribution performance,
adaptation performance, and zero-shot transfer. Missing metadata is itself a
research limitation because it prevents controlled aggregation and replication.
""",
    "12_meta": r"""
A research note should encode an argument, not a bibliography. Its minimal
structure is: problem definition, assumptions, formal objective, evidence,
counter-evidence, failure modes, and falsifiable next experiments. Confidence
should be tied to source quality and replication status. Updating a note means
changing the claim graph when evidence changes, preserving dates and unresolved
contradictions rather than silently replacing old conclusions.
""",
}

VLA_DEEP_DIVES = {
    "00_overview_roadmap": r"""
### A Taxonomy by Information Flow

The most informative taxonomy separates systems by where information is
compressed. In a monolithic policy, image, language, proprioception, and action
tokens share a backbone and the only externally visible state is the action.
In a hierarchical policy, a slow model predicts a subgoal, latent plan, or
semantic embedding consumed by a fast controller. In a modular stack, explicit
objects, maps, trajectories, or constraints cross component boundaries. In a
model-based agent, candidate actions are evaluated through predicted future
states. These choices determine not only accuracy but also debuggability,
latency, data reuse, and where safety constraints can be inserted.

The roadmap should therefore be read along four axes. **Representation** asks
whether state is token-based, object-centric, metric 3D, or an unstructured
latent. **Action generation** asks whether outputs are discrete tokens,
continuous regression, diffusion samples, flow trajectories, or references for
a lower-level controller. **Temporal organization** asks whether the system is
reactive, chunked, recurrent, memory-augmented, or explicitly hierarchical.
**Learning signal** asks how web data, video, demonstrations, simulation,
autonomous rollouts, and preferences contribute. A credible paper identifies
its position on all four axes and ablates the claimed source of progress.

### Research Milestones

A useful progression is harder than a sequence of larger demonstrations.
First, establish repeatable single-skill control under object and viewpoint
variation. Second, test compositional instructions while holding motor skills
fixed. Third, introduce persistent state changes and require recovery from
failed subgoals. Fourth, transfer across scenes and embodiments with a declared
adaptation budget. Fifth, evaluate unattended operation and calibrated
abstention. Each stage should preserve the earlier controls, otherwise apparent
long-horizon progress can come from easier resets, more permissive success
criteria, or hidden human assistance.
""",
    "01_vla_model_architectures": r"""
### Tokenization, Fusion, and Action Heads

Suppose image patches produce tokens \(v\), language produces \(w\),
proprioception produces \(q\), and previous actions produce \(u\). Early fusion
applies a shared transformer to \([v,w,q,u]\); late fusion encodes modalities
separately and combines them through cross-attention; a two-tower policy keeps a
large semantic backbone separate from a small action expert. Early fusion
maximizes interaction capacity but is expensive at control rate. Late fusion
can cache language or visual context but may bottleneck fine correspondence.
Two-system designs make rate separation explicit and permit embodiment-specific
experts, at the cost of deciding what information crosses the interface.

Discrete action modeling minimizes cross-entropy over bins or learned action
tokens. Its advantages are stable sequence training and compatibility with
language-model infrastructure; its liabilities are quantization, awkward
multivariate coupling, and sensitivity to action normalization. Gaussian
regression minimizes a continuous likelihood but tends to average distinct
strategies. Mixture-density, diffusion, and flow heads model multimodality at
increasing computational cost. Comparisons must equalize horizon, parameter
count, observation history, and inference budget. Otherwise an apparent
decoder advantage may actually come from more visual context or more control
updates.

### Architectural Ablations

A minimum ablation matrix removes language pretraining, freezes versus tunes the
vision backbone, varies proprioceptive input, replaces the action head, changes
chunk length, and tests with and without temporal history. Report both mean
success and failure composition. If removing language barely affects motor
tasks, the model may be a visual policy with an instruction selector rather
than a genuinely grounded VLA. If longer history helps only in the original
scene, the model may memorize reset dynamics instead of tracking state.
""",
    "02_rt1_rt2_rtx": r"""
### What the RT Line Actually Established

RT-1 demonstrated that a tokenized transformer policy could absorb a broad
multi-task real-robot dataset while retaining practical inference. Its
contribution is best understood as a scaling and representation result, not a
claim that discrete tokens are universally optimal. RT-2 reframed robot actions
as part of a vision-language token vocabulary and co-fine-tuned on web and
robotic data. The key hypothesis was that semantic concepts learned from the web
could alter physical action selection. RT-X and Open X-Embodiment shifted the
unit of scale from tasks on one platform to a heterogeneous mixture of
institutions, controllers, cameras, and embodiments.

Cross-embodiment learning introduces a latent alignment problem. A seven-degree
arm delta, a mobile base command, and an end-effector waypoint do not share a
literal action meaning. Normalizing each dimension to a common range aligns
numbers, not dynamics. Dataset mixtures can still help by sharing perception,
language grounding, object-state transitions, and high-level skill structure,
while leaving low-level decoding embodiment-specific. To demonstrate that
transfer, compare a shared backbone with separate experts against single-domain
training at equal target-domain data and optimization steps.

### Evaluation Caveats

The original systems use different robots, task sets, training corpora, and
success definitions, so their headline numbers are not a leaderboard.
Important controls include deduplicating visually or linguistically overlapping
tasks, separating novel instructions from novel physical skills, and reporting
per-dataset sampling weights. Negative transfer should be measured explicitly:
which source embodiments lower target performance, and does filtering by action
semantics, morphology, or visual domain recover it? These questions are more
scientifically useful than asking whether the largest pooled model wins on
average.
""",
    "03_openvla_octo_and_open_models": r"""
### Reproducibility as a Scientific Variable

Open models make questions accessible that closed demonstrations cannot answer:
which layers encode language grounding, how action tokenization affects
precision, whether parameter-efficient adaptation matches full fine-tuning, and
how performance changes under quantization or smaller visual backbones.
OpenVLA emphasizes adaptation of a large pretrained multimodal backbone with
tokenized actions. Octo emphasizes a generalist transformer policy and flexible
task or observation tokenization across heterogeneous robot data. Their design
differences should be studied under a common target task rather than inferred
from separate benchmark tables.

An adaptation study should specify checkpoint provenance, exact dataset
episodes, action normalization, image preprocessing, optimizer state, number of
gradient updates, random seeds, and deployment controller. LoRA rank, frozen
layers, and mixed-precision settings affect both compute and capacity. A fair
comparison reports wall-clock training, peak memory, inference latency, and
closed-loop trials. Offline action error is useful for detecting broken
pipelines but is not a policy metric because many actions are valid and small
errors can have state-dependent consequences.

### Open-Model Research Agenda

High-value experiments include swapping visual encoders while holding the
action decoder fixed; probing whether features encode depth, support, and
object permanence; testing calibration and camera shifts; and measuring the
data needed to adapt to a new embodiment. Release-quality work should include a
deployment script, normalization statistics, controller frequency, safety
limits, and raw per-trial outcomes. Without these, weights alone do not provide
reproducibility.
""",
    "04_pi0_gr00t_helix": r"""
### Three Distinct System Hypotheses

These systems should not be grouped merely because they target general-purpose
robots. The pi0 family tests whether a pretrained multimodal backbone plus a
continuous flow-based action expert can scale across tasks and embodiments.
GR00T is better interpreted as an integrated program spanning data generation,
simulation, multimodal pretraining, and humanoid adaptation. Helix tests an
asynchronous hierarchy in which a slower semantic model conditions a compact
high-rate visuomotor policy. The scientific hypotheses concern action
distribution, data infrastructure, and timescale separation respectively.

For flow matching, define a path between noise \(a^0\) and demonstrated action
chunks \(a^1\), for example \(a^\tau=(1-\tau)a^0+\tau a^1\). A network predicts
the velocity field \(v_\theta(a^\tau,\tau,c)\) under context \(c\), minimizing
\(\mathbb{E}\|v_\theta-(a^1-a^0)\|^2\). At inference, integrating the learned
field maps noise to a conditional action sample. The important robotics
variables are solver steps, chunk horizon, receding-horizon execution, and the
frequency at which visual context is refreshed.

For a two-system humanoid policy, the interface latent is a potential
bottleneck and a useful object of study. Does it encode object identity,
spatial target, desired contact, phase, or a complete motor plan? Probe it with
linear prediction, intervention, stale-latent tests, and bandwidth reduction.
Evaluate whether the fast policy can reject an obsolete semantic command after
the scene changes. A hierarchy is only robust if information can flow quickly
enough to stop or revise action, not merely initiate it.

### Evidence Standard

Company-reported demonstrations should be documented with exact dates and
treated as system evidence, not independent replication. A serious comparison
needs common tasks, matched hardware access, transparent training data, and
identical intervention accounting, which are generally unavailable. The
appropriate scholarly response is to compare disclosed mechanisms and derive
falsifiable experiments, while avoiding capability rankings unsupported by a
shared protocol.
""",
    "05_world_models_for_robotics": r"""
### Prediction Targets and Planning

A world model can predict pixels, discrete latent tokens, object states,
occupancy, contact events, rewards, or value-relevant features. Let an encoder
produce \(z_t=E(o_{\leq t})\), a dynamics model predict
\(\hat z_{t+1}=F(z_t,a_t)\), and a decoder or task head answer queries from
\(\hat z\). Pixel losses preserve appearance but overweight texture; latent
losses depend on what the encoder chooses to discard; object-centric losses
require stable discovery and correspondence; geometric losses provide
structure but may omit material and semantics. Multi-target training is often
necessary because no single prediction space captures all control-relevant
variables.

Planning chooses an action sequence by approximately optimizing
\(\arg\max_{a_{t:t+H}} \mathbb{E}_{F}[R(z_{t:t+H},a_{t:t+H})]\). Sampling-based
MPC, gradient-based planning, tree search, and policy-guided proposal methods
make different smoothness and compute assumptions. Every planner can exploit
model error. Robust protocols therefore test predicted and realized returns,
uncertainty growth with horizon, adversarial candidate actions, and replanning
frequency. Short-horizon predictive checks may be more reliable than claiming a
single model can imagine an entire household task.

### Causal and Epistemic Limits

Passive video identifies correlations among visual changes but not the result
of robot-specific interventions. It cannot determine which force, trajectory,
or controller caused an outcome when those variables are absent. Robot data,
simulation, and instrumented human demonstrations can align actions with
transitions, but each has bias. Ensembles, latent stochasticity, and
out-of-distribution scores should be evaluated by whether they prevent planning
through unsupported regions, not only by calibration on held-out frames.
""",
    "06_diffusion_policy_and_action_generation": r"""
### Score-Based Action Modeling

Diffusion policies corrupt demonstrated action sequences with noise and learn
to reverse that process conditioned on observations. In a standard
parameterization,
\(a^k=\sqrt{\bar\alpha_k}a^0+\sqrt{1-\bar\alpha_k}\epsilon\), and the network
minimizes \(\mathbb{E}\|\epsilon-\epsilon_\theta(a^k,k,c)\|^2\). The conditional
distribution can represent multiple valid grasps or trajectories without
averaging them. The cost is iterative inference and sensitivity to the noise
schedule, number of denoising steps, action normalization, and temporal horizon.

The deployed controller usually predicts \(H\) actions but executes only the
first \(h\). Small \(h\) improves feedback and raises inference load; large
\(h\) lowers compute but makes the policy open-loop. Temporal ensembling smooths
overlapping chunks but can blur abrupt contact transitions. Experiments should
sweep \(H\), \(h\), denoising steps, and observation latency jointly, because
the best offline denoising loss may not produce the best closed-loop policy.

### Comparison with Flow and Autoregression

Diffusion, rectified flow, flow matching, autoregressive tokens, and mixture
models differ in training objective and sampling path, but architecture and
compute often confound comparisons. Equalize visual backbone, dataset,
conditioning history, action horizon, and measured inference deadline. Report
mode coverage with task-relevant clusters, not just mean squared action error.
For contact-rich tasks, analyze approach, first contact, force buildup,
manipulation, and release separately; a decoder can be strong in free space and
unstable at contact.
""",
    "07_generalist_vs_specialist": r"""
### Capacity Allocation and Routing

The generalist-specialist debate can be formalized as a resource-allocation
problem. Shared parameters reduce estimation error by pooling data but increase
interference when tasks require incompatible features or control laws.
Specialists reduce interference but duplicate representation learning and need
routing. Mixture-of-experts, adapters, embodiment-specific action heads, and
skill libraries occupy intermediate points. The relevant quantity is not total
parameter count but target performance under fixed data, compute, latency, and
validation budgets.

Measure transfer with a matrix \(T_{ij}\): improvement on target \(j\) from
adding source \(i\) at a fixed target-data budget. Positive average transfer can
hide severe negative entries. Cluster sources by visual domain, task semantics,
kinematics, action convention, or contact regime and test which grouping best
predicts \(T\). This turns an architectural slogan into a falsifiable study of
what is actually shared.

### Hybrid Accountability

A hybrid system should define contracts between broad and narrow components.
Examples include a generalist proposing an object and subgoal while a geometric
module verifies reachability, or a language planner selecting a skill whose
specialist controller has a validated operating envelope. Interfaces need
confidence, frame conventions, termination conditions, and failure codes.
Otherwise modularity merely relocates ambiguity. Evaluate routing mistakes,
specialist failures, and interface failures separately.
""",
    "08_levels_of_generalization": r"""
### A Factorized Generalization Cube

Generalization should be indexed by held-out factors rather than labeled
zero-shot. Let \(G=(g_o,g_s,g_t,g_\ell,g_e,g_d,g_\tau)\) denote novelty in
objects, scenes, tasks, language, embodiment, dynamics, and time. A test split
is a subset of this cube. Holding out object instances while preserving category
and scene is much easier than simultaneously changing object, layout, camera,
and embodiment. Papers should publish the exact split generator and report each
axis separately before presenting a combined score.

Compositional generalization requires more than unseen instructions. The model
must recombine known entities, relations, skills, and constraints in
combinations absent from training. Design contrast sets where language changes
while the scene is fixed, the scene changes while language is fixed, and
physical feasibility contradicts semantic plausibility. This distinguishes
grounding from memorized co-occurrence.

### Adaptation Curves

For a new domain, report success as a function of target demonstrations,
gradient updates, and wall-clock interaction. Include zero-shot performance,
few-shot adaptation, and training from scratch. Area under this adaptation
curve is more informative than one arbitrary budget. Track catastrophic
forgetting on source tasks and recalibration after adaptation. A model that
adapts quickly but destroys prior safety behavior is not generally reusable.
""",
    "09_language_conditioned_control": r"""
### Grounding and Ambiguity

Language-conditioned control contains at least four subproblems: reference
resolution, goal-state inference, task decomposition, and motor execution.
An instruction such as “put the cup beside the plate” leaves reference frame,
distance tolerance, grasp choice, collision constraints, and final orientation
implicit. Dataset conventions often resolve these ambiguities consistently,
allowing a policy to succeed without representing them. Counterfactual scenes
and clarification options are needed to test genuine grounding.

A useful factorization is
\[
p(a\mid o,\ell)=\sum_g p(a\mid o,g)\,p(g\mid o,\ell),
\]
where \(g\) is an explicit or latent grounded goal. This separates language
errors from control errors and allows interventions: replace the inferred goal
with ground truth and measure the remaining motor gap. End-to-end models can be
analyzed with the same logic by probing or decoding their latent goal state.

### Pragmatic Evaluation

Test paraphrases, negation, relational swaps, distractors, impossible
instructions, and underspecified requests. Measure clarification quality and
safe refusal, not only completion. Human evaluation should use blinded raters
and a written success rubric. For interactive correction, report how many
turns and physical actions are required to recover, and whether corrections
generalize beyond the episode.
""",
    "10_embodiment_scaling_questions": r"""
### What Can Be Shared Across Bodies?

Embodiments differ in morphology, action coordinates, workspace, sensing,
compliance, and controller semantics. Shared learning is most plausible for
visual semantics, object state, task structure, and some end-effector-level
motion priors. Joint torques, balance, grasp mechanics, and latency constraints
are strongly body-specific. A scalable architecture should state where this
boundary is represented: embodiment tokens, morphology encoders, action
adapters, kinematic retargeting, or separate experts.

One can model a canonical task-space action \(u\) and embodiment-specific
decoder \(a=D_e(u,q)\). This creates a testable bottleneck: does the canonical
space preserve contact and whole-body constraints, and can a new \(D_e\) be
learned with less data than a new policy? Alternatives learn a shared latent
without explicit task-space meaning. Compare them at fixed target-embodiment
data, including bodies whose kinematics differ qualitatively rather than only
different arm brands.

### Scaling-Law Methodology

Robot scaling curves need independent axes for model parameters \(N\), number
of trajectories \(D\), task diversity \(K\), embodiments \(E\), and deployment
compute \(C\). Varying all at once cannot identify the source of improvement.
Fit curves on multiple scales, reserve out-of-mixture tasks, and report
uncertainty over dataset resampling and seeds. Measure the point at which adding
heterogeneous data causes interference. The scientifically important result may
be a boundary condition where scaling stops helping, not a smooth average trend.
""",
}


def research_depth(directory: str, slug: str, topic: str) -> str:
    formalism = DOMAIN_FORMALISM[directory].strip()
    if slug == "05_world_models_for_robotics":
        formalism = r"""
A world model separates state inference, dynamics, and decision making:
\[
z_t=E_\theta(o_{\leq t}),\qquad
p_\phi(z_{t+1}\mid z_t,a_t),\qquad
a_t=\Pi(z_t,g;p_\phi).
\]
This factorization matters because predictive accuracy and control utility are
not identical. A model can produce sharp videos while misrepresenting contact,
or predict a task-sufficient latent without reconstructing texture. The state
space, prediction target, uncertainty model, planning horizon, and mechanism
for grounding imagined trajectories in new observations are therefore part of
the formal problem.
""".strip()
    vla = VLA_DEEP_DIVES.get(slug, "") if directory == "06_vla_and_embodied_foundation_models" else ""
    return f"""
## Formal Problem Formulation

{formalism}

For **{topic}**, the paper-level specification should name the random variables,
coordinate frames, prediction horizon, and decision interface. It should also
state assumptions that are often hidden: static versus dynamic scene,
calibrated versus drifting sensors, known versus open-set objects, rigid versus
deformable interactions, and whether test-time adaptation or human correction
is allowed. These assumptions define the actual problem more precisely than the
model name.

{vla}

## Experimental Design at a CVPR / Robotics Research Standard

### Hypotheses and Baselines

Begin with a falsifiable hypothesis, not “our model improves performance.” A
strong hypothesis identifies a mechanism: temporal memory should improve
performance specifically after occlusion; metric 3D state should improve
viewpoint transfer; tactile input should help after first contact; heterogeneous
pretraining should reduce target-domain sample complexity. Select baselines that
isolate that mechanism: a matched-capacity model without the component, a
classical or modular alternative, and a strong current system evaluated through
the same observation and action interface.

Match data, optimization steps, augmentations, action horizon, and deployment
frequency wherever possible. Parameter count alone is not a sufficient control
because frozen pretraining, context length, image resolution, and sampling steps
change effective compute. Report training FLOPs or accelerator-hours and
measured inference latency. When exact matching is impossible, disclose the
asymmetry and include a resource-performance curve rather than a single point.

### Splits, Leakage, and Generalization

The experimental unit should be the factor intended to generalize: object
instance, physical scene, building, operator, task template, robot, or collection
day. Randomly splitting adjacent frames leaks appearance and state. Randomly
splitting demonstrations from the same reset can leak trajectories. Language
templates can leak task identity even when object instances are new. Construct
grouped splits before training and publish the group identifiers.

Report in-distribution performance separately from each held-out axis and from
their composition. “Unseen” must say unseen in what sense. A novel object in a
known category and pose is different from an unknown category, and an unseen
instruction paraphrase is different from a new physical skill. For pretrained
models, audit likely overlap with public datasets and avoid claiming strict
zero-shot novelty when pretraining provenance is unknown.

### Statistics and Reporting

Closed-loop trials are Bernoulli or ordinal outcomes with substantial
environmental variation. Report the numerator and denominator, not only a
percentage. Include confidence intervals such as Wilson intervals for success
rates, stratify by scene or task, and use hierarchical bootstrap when trials are
nested within objects or environments. Run enough independent seeds to expose
optimization variance and enough physical trials to expose deployment variance.
Do not treat thousands of video frames from one episode as independent samples.

Average success should be accompanied by worst-group performance, time to
completion, interventions, safety violations, recovery success, and a failure
taxonomy. Pre-register success criteria for ambiguous tasks and score videos
blind to method when human judgment is required. Preserve failed runs and
timeouts in the released logs.

## Diagnostic Ablations and Failure Analysis

Ablations should remove information or capacity in a way that tests the claimed
causal story. Useful interventions include removing temporal context, shuffling
language, withholding proprioception, perturbing calibration, delaying one
modality, replacing predicted geometry with ground truth, and replacing the
planner or controller with an oracle. Oracle studies locate the bottleneck:
ground-truth pose tests the perception gap, ground-truth subgoals test the
reasoning gap, and replay under a validated controller tests the action gap.

Stress tests should vary lighting, clutter, occlusion, camera pose, distractors,
reflective or transparent materials, actuator delay, and scene rearrangement.
For each failure, record the earliest observable precursor and whether the
system's confidence changed before the physical error. A useful taxonomy
separates sensing failure, state-estimation failure, grounding failure, planning
failure, control failure, and invalid evaluation assumptions. “Policy failed”
is not an analysis.

## Reproducibility Checklist

- Publish exact train, validation, and test episode identifiers.
- Record robot model, end effector, sensors, calibration procedure, and control interface.
- State observation rate, policy rate, action horizon, executed chunk length, and latency distribution.
- Release action normalization, coordinate-frame conventions, preprocessing, and success predicates.
- Report model initialization, frozen modules, optimizer, schedule, augmentations, seeds, and compute.
- Preserve per-trial outcomes, intervention logs, reset policy, exclusions, and representative failures.
- Distinguish simulation, replay, human teleoperation, autonomous execution, and post-selected video.
- Document licenses, privacy constraints, safety limits, and any unavailable proprietary training data.

## Thesis-Level Research Questions

1. Which latent variables are necessary and sufficient for {topic.lower()}, and
   how can sufficiency be tested through interventions rather than probes alone?
2. Under which distribution shifts does the proposed representation fail
   gracefully, become miscalibrated, or produce confidently unsafe actions?
3. What is gained by end-to-end learning after matching data, compute, control
   rate, and privileged geometric information against a modular baseline?
4. Can active perception or contact reduce uncertainty more efficiently than
   increasing model size or demonstration count?
5. How does performance scale with independent changes in task diversity,
   environment diversity, embodiment diversity, and trajectory count?
6. Which failures are detectable early enough for abstention, replanning, or
   human assistance, and what is the cost of those safeguards?
""".strip()


def title(slug: str) -> str:
    return re.sub(r"^\d+_", "", slug).replace("_", " ").title().replace("Vla", "VLA").replace("Rgbd", "RGB-D").replace("Rt1", "RT-1").replace("Rt2", "RT-2").replace("Rtx", "RT-X").replace("Pi0", "pi0").replace("Gr00T", "GR00T").replace("3D", "3D").replace("4D", "4D")


def level(directory: str) -> str:
    if directory == "10_frontier_2024_2026":
        return "Frontier"
    if directory in {"06_vla_and_embodied_foundation_models", "04_3d_and_spatial_understanding"}:
        return "Advanced"
    if directory in {"00_scope_and_map", "01_history", "02_robot_perception_foundations", "12_meta"}:
        return "Foundational"
    return "Intermediate"


def related(directory: str, slug: str) -> str:
    local = STRUCTURE[directory].split()
    i = local.index(slug)
    links = []
    for j in {max(0, i - 1), min(len(local) - 1, i + 1)}:
        if local[j] != slug:
            links.append(f"[{title(local[j])}]({local[j]}.md)")
    links.append("[Knowledge Base Index](../INDEX.md)")
    return ", ".join(links)


def topic_analysis(slug: str, topic: str) -> str:
    text = SPECIAL.get(slug, "")
    key = slug.lower()
    additions = []
    if "vla" in key or "rt1" in key or "pi0" in key or "generalist" in key or "embodiment_scaling" in key:
        additions.append("A VLA is not merely a VLM with an action head: training must align observations with temporally coherent actions, encode robot state, represent embodiment, and remain stable under closed-loop distribution shift. Discrete action tokens integrate naturally with autoregressive backbones but quantize control; continuous heads preserve precision; diffusion and flow heads represent multimodal trajectories at additional inference cost. Action chunking amortizes latency but reduces reactivity.")
    if "world_model" in key:
        additions.append("World models learn p(z_{t+1}|z_t,a_t) or longer-horizon predictive distributions. Pixel prediction retains appearance but spends capacity on irrelevant detail; latent prediction can focus on controllable state but risks discarding contact-relevant geometry. Passive video pretraining teaches dynamics priors without intervention semantics, while action-conditioned robot data identifies causal transitions. Planning can optimize imagined trajectories, retrieve skills, or train policies from synthetic rollouts, but model exploitation and compounding error remain severe.")
    if "diffusion" in key:
        additions.append("Diffusion Policy represents a conditional distribution over action sequences and handles multimodal demonstrations better than mean regression. Receding-horizon execution restores feedback, while denoising iterations create a latency-quality trade-off. Consistency models, rectified flow, and flow matching seek fewer inference steps. The method is strongest for local dexterous behavior and becomes less reliable when high-level task decomposition or persistent memory is required.")
    if "slam" in key or "odometry" in key:
        additions.append("Visual odometry estimates local motion; SLAM couples motion with a reusable map and loop closure. Feature-based systems are efficient and interpretable, direct methods exploit photometric information, and learned systems can improve priors or robustness. Dynamic objects violate static-world assumptions, while lighting change, repetitive texture, rolling shutter, and calibration drift produce catastrophic but sometimes silent failures.")
    if "gaussian" in key:
        additions.append("3D Gaussian Splatting offers fast differentiable rendering through anisotropic primitives and rasterization, often making it more practical than NeRF for visualization and map updates. Robotics still needs geometry extraction, free-space guarantees, semantic features, memory bounds, and dynamic-object handling. A photometrically excellent splat map can be unsafe for collision checking unless coupled to depth, occupancy, or meshes.")
    if "sensor" in key or "fusion" in key or "tactile" in key:
        additions.append("Fusion should be reliability-aware rather than simple concatenation. RGB contributes texture and semantics; depth or LiDAR adds range; tactile and force reveal local contact; proprioception supplies kinematic context; IMU stabilizes motion estimation. Calibration, timestamp error, unequal sampling rates, and missing modalities can dominate network architecture. Training with modality dropout and explicit uncertainty is therefore essential.")
    if "navigation" in key or "mapping" in key:
        additions.append("Metric maps answer where free space exists, topological maps encode connectivity, and semantic maps support task queries. Open-vocabulary maps attach language-aligned features to 3D locations, but similarity does not imply navigability or current object presence. Long-term robots need change detection, forgetting policies, provenance, and separate episodic from semantic memory.")
    if "grasp" in key:
        additions.append("Grasp perception progressed from planar rectangles and antipodal geometry to dense 6-DoF proposal networks. Quality depends on friction, collision, gripper width, approach path, and post-grasp task. In clutter, segmentation and pose errors interact with occlusion; foundation models can nominate objects or functional parts but still require geometric feasibility and closed-loop correction.")
    if "egocentric" in key:
        additions.append("Egocentric observations couple gaze, body motion, hands, and task intent. Wrist cameras offer precise local views but severe motion blur and self-occlusion; head cameras preserve context but may miss contact. Human datasets such as Ego4D and EPIC-KITCHENS provide rich action priors, yet embodiment, hand morphology, and action labels differ from robots.")
    if "event_camera" in key:
        additions.append("Event cameras asynchronously report brightness changes with microsecond-scale latency, high dynamic range, and little motion blur. They suit high-speed interception, drone flight, and visual servoing, but require new representations, calibration, fusion, and benchmarks. Most foundation models assume frames, so event-to-token pretraining and low-power deployment remain open.")
    if not text and not additions:
        additions.append(f"For {topic.lower()}, the central design question is which representation remains sufficient after viewpoint change, occlusion, object motion, and robot intervention. Offline perception metrics should be paired with downstream task success, latency, calibration sensitivity, and abstention quality. A model that improves average recognition but removes metric consistency or uncertainty may degrade the complete robot.")
    return (text + "\n\n" + "\n\n".join(additions)).strip()


def note(directory: str, slug: str) -> str:
    d = DOMAIN[directory]
    t = title(slug)
    recent = directory == "10_frontier_2024_2026" or any(x in slug for x in ["2024_2026", "pi0", "openvla"])
    systems = list(d["systems"])
    datasets = list(d["datasets"])
    for key, rows in TOPIC_SYSTEMS.items():
        if key in slug:
            systems.extend(rows)
    for key, rows in TOPIC_DATASETS.items():
        if key in slug:
            datasets.extend(rows)
    src = FRONTIER_SOURCES if recent or directory == "06_vla_and_embodied_foundation_models" else [
        ("Probabilistic Robotics", "https://mitpress.mit.edu/9780262201629/probabilistic-robotics/"),
        ("Modern Robotics", "https://modernrobotics.northwestern.edu/"),
        ("Annual Review of Control, Robotics, and Autonomous Systems", "https://www.annualreviews.org/journal/control"),
        ("IEEE Robotics and Automation Letters", "https://www.ieee-ras.org/publications/ra-l"),
    ]
    systems_rows = "\n".join(f"| {n} | {y} | {ty} | {why} |" for n, y, ty, why in systems)
    data_rows = "\n".join(f"| {n} | {task} | {metric} | {why} |" for n, task, metric, why in datasets)
    reading = "\n".join(f"- [{n}]({u})" for n, u in src)
    freshness = "\n\n> **Frontier note:** Very recent / subject to rapid change. Company-reported demonstrations are treated as evidence of a direction, not as independent proof of general capability." if recent else ""
    diagram = ""
    if slug == "00_overview_roadmap":
        diagram = """
```mermaid
graph TD
    A[Sensor Input: RGB, Depth, Tactile, Proprioception] --> B[Perception]
    B --> C[Scene Representation]
    C --> D[Reasoning / Prediction / Planning]
    D --> E[Action Generation]
    E --> F[Robot Control]
    F --> G[Environment Change]
    G --> A
    B --> H[Open-vocabulary semantics]
    B --> I[3D geometry]
    B --> J[Affordances]
    C --> K[World model / scene memory]
    D --> L[VLA]
    D --> M[Modular planner]
    D --> N[Diffusion policy]
```
"""
    return f"""# {t}

> **Last Updated:** {UPDATED}
> **Level:** {level(directory)}
> **Why It Matters for Robotics:** {d['frame']} {t} must be evaluated by its effect on physical decisions, not only by passive recognition accuracy.
> **Related Sections:** {related(directory, slug)}
{freshness}

## Overview

{d['core']}

The robotics-first question is not whether a model can describe an image, but whether it can maintain the right state for intervention. Relevant state includes pose, free space, articulation, support, containment, material, contact, uncertainty, and expected change under action. Because actions alter observations, perception and control form a coupled dynamical system. This makes calibration, temporal consistency, recovery, and out-of-distribution detection first-class research concerns.

{topic_analysis(slug, t)}

{diagram}
## Core Technical Ideas

1. **Task-conditioned sufficiency.** Representations should retain variables required by the controller while excluding nuisance variation. The sufficient state differs for collision avoidance, insertion, cloth folding, and language-conditioned search.
2. **Geometry plus semantics.** Metric structure supports reachability and collision checking; semantics identifies task-relevant entities and likely functions. Either alone is inadequate in open-world scenes.
3. **Temporal and causal grounding.** Tracking and memory distinguish persistent state from transient appearance. Action-conditioned observations reveal articulation, mass, friction, compliance, and hidden constraints.
4. **Uncertainty and abstention.** Robots need calibrated confidence, anomaly detection, and information-gathering actions. A plausible but wrong prediction is more dangerous than an explicit request for another view or human help.
5. **Closed-loop evaluation.** Dataset metrics isolate components, but deployment requires measuring task success, intervention rate, recovery, latency, and performance across hours, scenes, and hardware conditions.

Architecturally, modular pipelines expose intermediate state and allow geometric verification, while end-to-end policies optimize the final behavior and can exploit cues that annotations omit. Hybrid systems use pretrained visual-language features for semantics, explicit maps or object memories for persistence, learned action generators for local control, and classical safety or motion constraints around execution.

## Why This Matters in Robotics

Manipulation converts millimeter-scale pose, depth, or contact errors into missed grasps and collisions. Navigation compounds localization drift and stale semantic memory over long trajectories. Human-robot interaction adds uncertain intent and safety margins. Real robots also face reflective and transparent materials, self-occlusion, changing illumination, sensor dropout, actuator delay, and objects absent from training.

Consequently, a credible result should state the embodiment, sensors, control frequency, inference hardware, environment split, number of trials, reset policy, intervention policy, and failure taxonomy. Generalization claims should name the axis held out: objects, layouts, tasks, instructions, embodiments, dynamics, or time. Aggregating these axes into a single success number conceals where the system actually transfers.

{research_depth(directory, slug, t)}

## Key Systems / Methods / Papers

| Name | Year | Type | Why It Matters |
|------|------|------|----------------|
{systems_rows}

These systems should not be read as a linear leaderboard. They make different assumptions about calibration, data access, action spaces, environment structure, and evaluation. The most useful comparison asks which assumptions remain valid in the target robot deployment.

## Benchmarks / Datasets / Evaluation

| Benchmark or Dataset | Task | Metric | Why It Matters |
|----------------------|------|--------|----------------|
{data_rows}

Offline metrics are necessary for diagnosis but insufficient for robotics. Add closed-loop success, time-to-completion, collision or damage rate, human interventions, recovery success, calibration error, worst-group performance, and confidence calibration. Report uncertainty across trials and environments rather than selecting demonstration videos.

## Pros, Limits, and Failure Modes

| Dimension | Strength | Limitation |
|-----------|----------|------------|
| Learned representations | Transfer semantics and exploit large heterogeneous datasets | Can encode dataset shortcuts and lose metric consistency |
| Explicit geometry | Interpretable, measurable, and compatible with planning | Brittle under missing depth, dynamics, deformability, and calibration error |
| End-to-end policies | Optimize behavior and reduce hand-designed interfaces | Difficult to audit; failures couple perception, reasoning, and control |
| Modular systems | Components can be tested, replaced, and safety-checked | Interface errors and task-irrelevant objectives can cap performance |
| Simulation | Scalable labels, interventions, and rare-event generation | Appearance, contact, dynamics, and behavior gaps can compound |
| Open-vocabulary models | Recognize long-tail concepts and flexible instructions | Semantic similarity does not establish pose, reachability, or affordance |

Common failures include occlusion-induced identity switches, reference-frame confusion, stale memory after an object moves, confidently hallucinated objects, depth failure on transparent surfaces, temporal lag during contact, and policies that succeed only from narrow reset distributions. Recovery behavior is often undertrained because datasets overrepresent successful demonstrations.

## Open Problems

- Build persistent 3D/4D memory that updates after robot and human interventions without catastrophic drift.
- Calibrate semantic, geometric, and action uncertainty into a common decision-relevant quantity.
- Learn affordances and contact dynamics that transfer across object instances, materials, and embodiments.
- Evaluate long-horizon autonomy with transparent resets, interventions, failures, and confidence intervals.
- Combine web-scale priors with robot data without importing visual shortcuts or unsafe commonsense assumptions.
- Adapt online to sensor, calibration, environment, and hardware change without forgetting safety constraints.
- Develop representations for deformables, transparent objects, articulated mechanisms, and multi-agent interaction.

## Connections to Neighboring Topics

This topic sits between sensing and control. It depends on the foundations in `02_robot_perception_foundations`, gains spatial structure from `04_3d_and_spatial_understanding`, and connects semantics and contact through `05_multimodal_perception`. Its ultimate value is tested in `08_manipulation_navigation_and_control`; data and reproducibility constraints are covered in `07_data_simulation_and_training`.

## Further Reading

{reading}
- [Robotics: Science and Systems proceedings](https://www.roboticsproceedings.org/)
- [CoRL proceedings](https://proceedings.mlr.press/)
"""


def make_readme() -> str:
    return f"""# Robotics-CV Knowledge Base

> **Last Updated:** {UPDATED}

This repository is a living, robotics-first research database about the transition from passive visual recognition to actionable spatial intelligence. It focuses on manipulation, navigation, 3D/4D scene understanding, multimodal sensing, vision-language-action models, world models, robot data, and closed-loop evaluation.

The notes are written as research briefs rather than glossary entries. Each one
now includes a formal problem statement, explicit assumptions, hypothesis and
baseline design, leakage-resistant evaluation splits, statistical reporting,
diagnostic ablations, a reproducibility checklist, and thesis-level research
questions. Section 06 adds architecture-specific mathematical and experimental
analysis for VLAs, action generators, world models, language grounding, and
cross-embodiment scaling.

## What “Robotics-First CV” Means

Robotics CV is judged by whether visual state supports safe and effective action. Detection and segmentation matter when they improve pose, reachability, affordance, memory, planning, control, or recovery. The database therefore downweights generic benchmark history and emphasizes geometry, time, uncertainty, contact, embodiment, latency, and distribution shift.

## Organization

The numbered directories progress from scope and history through perception foundations, core problems, spatial and multimodal understanding, embodied foundation models, data, control, hardware, the 2024–2026 frontier, resources, and research workflow. Start with [INDEX.md](INDEX.md), then follow the PhD reading path in [12_meta/01_reading_path_for_phd_student.md](12_meta/01_reading_path_for_phd_student.md).

## Updating the Database

For a new paper, record the publication date, stable URL, task, embodiment, sensors, action representation, training data, evaluation split, trial count, and key limitations. Distinguish author-reported demonstrations from independent reproduction. Update `Last Updated`, add links in neighboring notes, and run the repository audit before committing.

Frontier files require the most discipline: verify claims against papers or official technical reports, mark very recent results, avoid extrapolating from videos, and archive benchmark protocol changes. Annual snapshots should preserve what was believed at the time rather than silently rewriting history.
"""


def make_index(paths: list[tuple[str, str]]) -> str:
    sections = []
    for directory, slugs in STRUCTURE.items():
        desc = DOMAIN[directory]["frame"]
        items = "\n".join(f"- [x] [{title(s)}]({directory}/{s}.md)" for s in slugs.split())
        sections.append(f"### `{directory}/`\n{desc}\n\n{items}")
    return f"""# Research Navigation Index

> **Last Updated:** {UPDATED}

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

{chr(10).join(sections)}
"""


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    paths = []
    for directory, slugs in STRUCTURE.items():
        out = ROOT / directory
        out.mkdir(parents=True, exist_ok=True)
        for slug in slugs.split():
            (out / f"{slug}.md").write_text(note(directory, slug), encoding="utf-8")
            paths.append((directory, slug))
    (ROOT / "README.md").write_text(make_readme(), encoding="utf-8")
    (ROOT / "INDEX.md").write_text(make_index(paths), encoding="utf-8")


if __name__ == "__main__":
    main()
