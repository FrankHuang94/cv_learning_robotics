# Robotics-CV Knowledge Base

> **Last Updated:** 2026-06-11

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
