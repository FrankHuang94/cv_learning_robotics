# Computer Vision for Robotics Research Database

This repository contains a PhD-level, robotics-first knowledge base on robot
perception, embodied AI, 3D/4D spatial understanding, multimodal sensing,
vision-language-action models, world models, robot data, simulation, and
closed-loop control.

Start with the [research navigation index](robotics-cv-knowledge-base/INDEX.md).
The database contains 96 populated research notes plus its own README and
completion index. Frontier claims are dated and separated from independently
reproduced evidence.

The knowledge base contains more than 200,000 words. Every research note
includes a formal problem formulation, assumptions, experimental design,
generalization and leakage controls, statistical reporting guidance, diagnostic
ablations, reproducibility requirements, and thesis-level research questions.
Section 06 receives additional architecture-specific treatment of VLA
tokenization and fusion, RT-X, open models, flow matching, diffusion policies,
world models, language grounding, generalization, and embodiment scaling.

The generated knowledge base is reproducible with:

```bash
python3 scripts/build_kb.py
```
