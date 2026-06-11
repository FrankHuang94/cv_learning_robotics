# Robotics Cv Open Problems

> **Last Updated:** 2026-06-11
> **Level:** Frontier
> **Why It Matters for Robotics:** This is a very recent, rapidly changing area; claims here are dated and should be distinguished from independently reproduced evidence. Robotics Cv Open Problems must be evaluated by its effect on physical decisions, not only by passive recognition accuracy.
> **Related Sections:** [World Model Vs VLA](05_world_model_vs_vla.md), [Future Roadmaps](07_future_roadmaps.md), [Knowledge Base Index](../INDEX.md)


> **Frontier note:** Very recent / subject to rapid change. Company-reported demonstrations are treated as evidence of a direction, not as independent proof of general capability.

## Overview

The frontier is converging on heterogeneous co-training, continuous action generators, hierarchical reasoning, cross-embodiment transfer, open-world semantics, and predictive scene models. Demonstrations have improved faster than standardized evaluation. Key unknowns include whether scaling curves persist outside curated setups, how much autonomy is present in company videos, whether learned policies recover from rare contact failures, and how reliability changes over hours rather than short episodes. 2026 evidence should therefore be read as provisional unless accompanied by methods, data, and repeatable tests.

The robotics-first question is not whether a model can describe an image, but whether it can maintain the right state for intervention. Relevant state includes pose, free space, articulation, support, containment, material, contact, uncertainty, and expected change under action. Because actions alter observations, perception and control form a coupled dynamical system. This makes calibration, temporal consistency, recovery, and out-of-distribution detection first-class research concerns.

The hardest open problems are coupled. Cluttered manipulation combines occlusion, long-tail objects, collision, and uncertain support. Deformables require topology and contact state beyond rigid pose. Persistent memory must survive viewpoint change and update after humans or robots move objects. Contact-rich uncertainty requires fusing vision, force, touch, and controller state at different rates. Spatial reasoning must resolve frames, containment, support, and reachability rather than produce plausible language.

Safety-aware perception needs calibrated detection of people, tools, fragile objects, forbidden regions, and model uncertainty under domain shift. Multi-agent scenes add intent prediction, communication, and mutual occlusion. Lifelong adaptation must incorporate new objects and sensor conditions without erasing validated behavior. Open-world perception must map semantic novelty to action relevance: an unknown object may be ignorable, graspable after inspection, or a reason to stop.

Research protocols should emphasize adversarial rearrangement, transparent and reflective objects, lighting and calibration drift, long unattended runs, recovery after induced errors, and worst-group performance. The key metric is a reliability profile: probability and severity of failure, detectability before harm, recovery probability, and human intervention burden.


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

## Formal Problem Formulation

Frontier evidence should be represented as a set of dated claims
\(C=\{(c_i,s_i,t_i,r_i)\}\), where \(s_i\) is the source, \(t_i\) the date, and
\(r_i\) a reproducibility level. A peer-reviewed paper, an open checkpoint, a
company technical report, and a demonstration video provide different evidence.
They should not be collapsed into a single capability ranking. Claims about
generality require explicit train-test boundaries and claims about autonomy
require accounting for resets, interventions, remote operation, and selection.

For **Robotics Cv Open Problems**, the paper-level specification should name the random variables,
coordinate frames, prediction horizon, and decision interface. It should also
state assumptions that are often hidden: static versus dynamic scene,
calibrated versus drifting sensors, known versus open-set objects, rigid versus
deformable interactions, and whether test-time adaptation or human correction
is allowed. These assumptions define the actual problem more precisely than the
model name.



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

1. Which latent variables are necessary and sufficient for robotics cv open problems, and
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

## Key Systems / Methods / Papers

| Name | Year | Type | Why It Matters |
|------|------|------|----------------|
| OpenVLA | 2024 | open VLA | Made VLA training and adaptation inspectable |
| pi0 | 2024 | flow VLA | Joined pretrained semantics with continuous action generation |
| Gemini Robotics | 2025 | VLA | Extended a multimodal model toward dexterous physical action |
| Helix | 2025 | humanoid VLA | Demonstrated asynchronous semantic and 200 Hz control |
| pi0.5 | 2025 | VLA | Targeted unseen-home generalization with heterogeneous co-training |

These systems should not be read as a linear leaderboard. They make different assumptions about calibration, data access, action spaces, environment structure, and evaluation. The most useful comparison asks which assumptions remain valid in the target robot deployment.

## Benchmarks / Datasets / Evaluation

| Benchmark or Dataset | Task | Metric | Why It Matters |
|----------------------|------|--------|----------------|
| SimplerEnv | VLA evaluation | real-to-sim correlation and success | Attempts scalable policy comparison |
| LIBERO | knowledge transfer | task success | Tests several generalization regimes |
| BEHAVIOR-1K | household activities | task and predicate success | Moves evaluation toward long-horizon physical state change |

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
