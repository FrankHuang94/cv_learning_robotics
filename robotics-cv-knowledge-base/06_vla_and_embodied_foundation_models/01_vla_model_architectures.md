# VLA Model Architectures

> **Last Updated:** 2026-06-10
> **Level:** Advanced
> **Why It Matters for Robotics:** Embodied foundation models place visual representation learning inside a perception-memory-reasoning-action loop, where errors alter the next observation and can cause physical failure. VLA Model Architectures must be evaluated by its effect on physical decisions, not only by passive recognition accuracy.
> **Related Sections:** [Overview Roadmap](00_overview_roadmap.md), [RT-1 RT-2 RT-X](02_rt1_rt2_rtx.md), [Knowledge Base Index](../INDEX.md)


## Overview

A VLA maps visual observations, language, and robot state to actions, often by adapting a pretrained VLM and adding an action decoder. Architectures differ in action tokenization, continuous regression, diffusion or flow heads, action chunking, memory, and control hierarchy. The central constraint is multi-timescale operation: semantic reasoning can run at a few hertz, while stable contact and whole-body control may require tens to hundreds of hertz. World models instead learn predictive state transitions and can support imagination or planning; hybrid systems increasingly combine both.

The robotics-first question is not whether a model can describe an image, but whether it can maintain the right state for intervention. Relevant state includes pose, free space, articulation, support, containment, material, contact, uncertainty, and expected change under action. Because actions alter observations, perception and control form a coupled dynamical system. This makes calibration, temporal consistency, recovery, and out-of-distribution detection first-class research concerns.

A VLA consumes images, language instructions, and usually proprioceptive state, then predicts robot actions. It differs from a VLM with an action head because the training distribution is sequential and intervention-dependent: actions change camera pose, contact, object state, and future observations. The model must learn temporal alignment, embodiment conventions, controller semantics, and closed-loop correction, none of which follows automatically from image-text pretraining.

Common architectures pair a ViT or VLM visual encoder with a language backbone and one of four action decoders. Discrete token decoders quantize action dimensions and reuse autoregressive next-token training, as in RT-2-style formulations; continuous regression heads are efficient but average incompatible strategies; diffusion heads represent multimodal action sequences through iterative denoising; flow-matching heads learn a continuous transport field. Action chunking predicts several future controls at once, improving throughput at the cost of feedback frequency.

Short-horizon control asks the network to react locally, often at 10-50 Hz or faster. Long-horizon behavior additionally needs task decomposition, memory, termination prediction, and recovery. Humanoids sharpen the constraint: vision-language inference may run below 10 Hz while balance, fingers, and contact loops require 100-1000 Hz. Helix addresses this through an asynchronous 7-9 Hz semantic system and 200 Hz visuomotor system; other stacks place a VLA above conventional whole-body controllers.

Internally, VLAs must resolve referring expressions, parse object parts and support relations, infer occlusion and depth, identify grasp regions, track state changes, and distinguish reachable from merely visible objects. Internet pretraining supplies semantic breadth, but metric pose, force, friction, and embodiment-specific reachability still come primarily from robot data, geometry modules, or interaction.


A VLA is not merely a VLM with an action head: training must align observations with temporally coherent actions, encode robot state, represent embodiment, and remain stable under closed-loop distribution shift. Discrete action tokens integrate naturally with autoregressive backbones but quantize control; continuous heads preserve precision; diffusion and flow heads represent multimodal trajectories at additional inference cost. Action chunking amortizes latency but reduces reactivity.


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
| RT-1 | 2022 | robot transformer | Scaled multi-task real-robot behavior |
| RT-2 | 2023 | VLA | Represented actions as language-like tokens |
| OpenVLA | 2024 | open VLA | Released a reproducible 7B VLA |
| Octo | 2024 | open policy | Generalist transformer trained across robot datasets |
| pi0 | 2024 | flow VLA | Used a flow-matching action expert |
| Helix | 2025 | humanoid VLA | Separated 7-9 Hz semantics from 200 Hz control |

These systems should not be read as a linear leaderboard. They make different assumptions about calibration, data access, action spaces, environment structure, and evaluation. The most useful comparison asks which assumptions remain valid in the target robot deployment.

## Benchmarks / Datasets / Evaluation

| Benchmark or Dataset | Task | Metric | Why It Matters |
|----------------------|------|--------|----------------|
| Open X-Embodiment | cross-embodiment policy learning | per-task success | Aggregates heterogeneous robot experience |
| LIBERO | lifelong manipulation | task success | Tests transfer and interference |
| CALVIN | language-conditioned long horizon | sequence completion | Measures chained skill execution |

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

- [Open X-Embodiment / RT-X](https://robotics-transformer-x.github.io/)
- [OpenVLA](https://openvla.github.io/)
- [Octo](https://octo-models.github.io/)
- [Physical Intelligence pi0](https://www.pi.website/blog/pi0)
- [Physical Intelligence pi0.5](https://www.pi.website/blog/pi05)
- [Figure Helix](https://www.figure.ai/news/helix)
- [Gemini Robotics](https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/)
- [NVIDIA GR00T](https://developer.nvidia.com/isaac/gr00t)
- [Robotics: Science and Systems proceedings](https://www.roboticsproceedings.org/)
- [CoRL proceedings](https://proceedings.mlr.press/)
