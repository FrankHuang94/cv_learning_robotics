# Computer Vision for Robotics Research Database

This repository contains a PhD-level, robotics-first knowledge base on robot
perception, embodied AI, 3D/4D spatial understanding, multimodal sensing,
vision-language-action models, world models, robot data, simulation, and
closed-loop control.

Start with the [research navigation index](robotics-cv-knowledge-base/INDEX.md).
The database contains 97 populated research notes plus its own README and
completion index. Frontier claims are dated and separated from independently
reproduced evidence.

The knowledge base contains more than 200,000 words. Every research note
includes a formal problem formulation, assumptions, experimental design,
generalization and leakage controls, statistical reporting guidance, diagnostic
ablations, reproducibility requirements, and thesis-level research questions.
Section 06 receives additional architecture-specific treatment of VLA
tokenization and fusion, RT-X, open models, flow matching, diffusion policies,
world models, language grounding, generalization, and embodiment scaling.

**October 2026 refresh (last updated 2026-10-18).** Notes now include dated
"Recent Developments" sections covering mid-2025 to October 2026 research
(RL-refined VLAs, whole-body humanoid policies, world action models, latent
world models, feed-forward 3D/4D vision, SAM 3 and DINOv3, arena-style
evaluation) and a new
[industry status snapshot](robotics-cv-knowledge-base/10_frontier_2024_2026/08_industry_status_2026.md).

**简体中文版 / Simplified Chinese edition.** A reference translation with the
same structure is in [`Chinese translation/`](Chinese%20translation/INDEX.md).
Each Chinese note links back to its English original.

Both editions are reproducible with:

```bash
python3 scripts/build_kb.py      # English knowledge base
python3 scripts/build_kb_zh.py   # Simplified Chinese edition
```
