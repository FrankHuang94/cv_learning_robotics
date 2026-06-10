# Multimodal And Foundation Models

> **Last Updated:** 2026-06-10
> **Level:** Foundational
> **Why It Matters for Robotics:** The history matters because today's foundation policies inherit unresolved assumptions from calibration, stereo, SLAM, recognition, and behavior cloning. Multimodal And Foundation Models must be evaluated by its effect on physical decisions, not only by passive recognition accuracy.
> **Related Sections:** [Deep Robot Perception](04_deep_robot_perception.md), [Embodied Ai 2024 2026](06_embodied_ai_2024_2026.md), [Knowledge Base Index](../INDEX.md)


## Overview

Robot vision evolved through overlapping regimes rather than clean replacement: engineered geometry and control; probabilistic state estimation; RGB-D reconstruction; deep discriminative perception; self-supervised representation learning; and multimodal policies. Classical methods remain inside modern systems as coordinate transforms, optimization, tracking, collision checks, and safety monitors. The decisive shift is from estimating a static world for a downstream planner toward learning representations jointly with language and action.

The robotics-first question is not whether a model can describe an image, but whether it can maintain the right state for intervention. Relevant state includes pose, free space, articulation, support, containment, material, contact, uncertainty, and expected change under action. Because actions alter observations, perception and control form a coupled dynamical system. This makes calibration, temporal consistency, recovery, and out-of-distribution detection first-class research concerns.

For multimodal and foundation models, the central design question is which representation remains sufficient after viewpoint change, occlusion, object motion, and robot intervention. Offline perception metrics should be paired with downstream task success, latency, calibration sensitivity, and abstention quality. A model that improves average recognition but removes metric consistency or uncertainty may degrade the complete robot.


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

## Key Systems / Methods / Papers

| Name | Year | Type | Why It Matters |
|------|------|------|----------------|
| Shakey | 1969 | mobile robot | Linked perception, symbolic planning, and action |
| SIFT | 1999 | feature method | Enabled robust correspondence and localization |
| KinectFusion | 2011 | RGB-D mapping | Made dense online reconstruction practical |
| AlexNet | 2012 | deep vision | Accelerated learned perception |
| RT-1 | 2022 | robot transformer | Demonstrated broad multi-task policy scaling |

These systems should not be read as a linear leaderboard. They make different assumptions about calibration, data access, action spaces, environment structure, and evaluation. The most useful comparison asks which assumptions remain valid in the target robot deployment.

## Benchmarks / Datasets / Evaluation

| Benchmark or Dataset | Task | Metric | Why It Matters |
|----------------------|------|--------|----------------|
| KITTI | autonomous driving perception | ATE, AP | Standardized real mobile perception |
| NYU Depth V2 | indoor RGB-D | depth error, mIoU | Supported indoor geometry and semantics |
| ImageNet | visual pretraining | top-1 | Supplied transferable visual features, though not embodied supervision |

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

- [Probabilistic Robotics](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/)
- [Modern Robotics](https://modernrobotics.northwestern.edu/)
- [Annual Review of Control, Robotics, and Autonomous Systems](https://www.annualreviews.org/journal/control)
- [IEEE Robotics and Automation Letters](https://www.ieee-ras.org/publications/ra-l)
- [Robotics: Science and Systems proceedings](https://www.roboticsproceedings.org/)
- [CoRL proceedings](https://proceedings.mlr.press/)
