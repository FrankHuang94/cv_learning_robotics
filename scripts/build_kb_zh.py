#!/usr/bin/env python3
"""Build the Simplified Chinese reference translation of the knowledge base.

The Chinese edition mirrors ``robotics-cv-knowledge-base/`` file for file and is
written to ``Chinese translation/``. It reuses the English structure from
``build_kb.py`` and the translated text stored in the ``kb_zh`` package. Run
``python3 scripts/build_kb.py`` first, then this script. Missing translations
raise an error so the two editions cannot silently drift apart.
"""

from __future__ import annotations

from pathlib import Path

import build_kb as en
from kb_zh.domain import DOMAIN_ZH
from kb_zh.formalism import DOMAIN_FORMALISM_ZH, WORLD_MODEL_FORMALISM_ZH
from kb_zh.pages import INDEX_ZH, README_ZH
from kb_zh.phrases import PHRASE_ZH, SOURCE_ZH
from kb_zh.recent import RECENT_HEADING_ZH, RECENT_UPDATES_ZH
from kb_zh.special import SPECIAL_ZH
from kb_zh.templates import (
    FALLBACK_ADDITION_ZH,
    FRESHNESS_ZH,
    LEVEL_ZH,
    MERMAID_ZH,
    NOTE_TEMPLATE_ZH,
    RESEARCH_DEPTH_TEMPLATE_ZH,
    TOPIC_ADDITIONS_ZH,
)
from kb_zh.titles import DIR_ZH, TITLE_ZH
from kb_zh.vla_deep_dives_a import VLA_DEEP_DIVES_ZH_A
from kb_zh.vla_deep_dives_b import VLA_DEEP_DIVES_ZH_B


REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "Chinese translation"
EN_DIR = "robotics-cv-knowledge-base"
VLA_DEEP_DIVES_ZH = {**VLA_DEEP_DIVES_ZH_A, **VLA_DEEP_DIVES_ZH_B}


def fill(template: str, **values: str) -> str:
    for key, value in values.items():
        template = template.replace(f"<<{key}>>", value)
    assert "<<" not in template, template[template.index("<<"):][:80]
    return template


def zh(phrase: str) -> str:
    if phrase not in PHRASE_ZH:
        raise KeyError(f"Missing Chinese translation for phrase: {phrase!r}")
    return PHRASE_ZH[phrase]


def zh_title(directory: str, slug: str) -> str:
    return TITLE_ZH[f"{directory}/{slug}"]


def related(directory: str, slug: str) -> str:
    local = en.STRUCTURE[directory].split()
    i = local.index(slug)
    links = []
    for j in {max(0, i - 1), min(len(local) - 1, i + 1)}:
        if local[j] != slug:
            links.append(f"[{zh_title(directory, local[j])}]({local[j]}.md)")
    links.append("[知识库索引](../INDEX.md)")
    return "、".join(links)


def topic_analysis(slug: str, topic: str) -> str:
    text = SPECIAL_ZH[slug].strip() if slug in en.SPECIAL else ""
    key = slug.lower()
    conditions = [
        ("vla", "vla" in key or "rt1" in key or "pi0" in key or "generalist" in key or "embodiment_scaling" in key),
        ("world_model", "world_model" in key),
        ("diffusion", "diffusion" in key),
        ("slam", "slam" in key or "odometry" in key),
        ("gaussian", "gaussian" in key),
        ("fusion", "sensor" in key or "fusion" in key or "tactile" in key),
        ("navigation", "navigation" in key or "mapping" in key),
        ("grasp", "grasp" in key),
        ("egocentric", "egocentric" in key),
        ("event_camera", "event_camera" in key),
    ]
    additions = [TOPIC_ADDITIONS_ZH[name].strip() for name, hit in conditions if hit]
    if not text and not additions:
        additions.append(fill(FALLBACK_ADDITION_ZH, TOPIC=topic).strip())
    return (text + "\n\n" + "\n\n".join(additions)).strip()


def research_depth(directory: str, slug: str, topic: str) -> str:
    formalism = DOMAIN_FORMALISM_ZH[directory].strip()
    if slug == "05_world_models_for_robotics":
        formalism = WORLD_MODEL_FORMALISM_ZH.strip()
    vla = VLA_DEEP_DIVES_ZH.get(slug, "") if directory == "06_vla_and_embodied_foundation_models" else ""
    return fill(RESEARCH_DEPTH_TEMPLATE_ZH, FORMALISM=formalism, TOPIC=topic, VLA=vla.strip()).strip()


def recent_updates(directory: str, slug: str) -> str:
    key = f"{directory}/{slug}"
    if not en.RECENT_UPDATES.get(key, "").strip():
        return ""
    return f"\n{RECENT_HEADING_ZH}\n\n{RECENT_UPDATES_ZH[key].strip()}\n"


def system_rows(rows: list[tuple]) -> str:
    return "\n".join(f"| {n} | {y} | {zh(ty)} | {zh(why)} |" for n, y, ty, why in rows)


def dataset_rows(rows: list[tuple]) -> str:
    return "\n".join(f"| {n} | {zh(task)} | {zh(metric)} | {zh(why)} |" for n, task, metric, why in rows)


def note(directory: str, slug: str) -> str:
    d = DOMAIN_ZH[directory]
    t = zh_title(directory, slug)
    systems, datasets, sources, recent = en.note_inputs(directory, slug)
    reading = "\n".join(f"- [{SOURCE_ZH.get(n, n)}]({u})" for n, u in sources)
    diagram = MERMAID_ZH if slug == "00_overview_roadmap" else ""
    return fill(
        NOTE_TEMPLATE_ZH,
        TITLE=t,
        TITLE_EN=en.title(slug),
        SOURCE_LINK=f"../../{EN_DIR}/{directory}/{slug}.md",
        UPDATED=en.UPDATED,
        LEVEL=LEVEL_ZH[en.level(directory)],
        FRAME=d["frame"],
        RELATED=related(directory, slug),
        FRESHNESS=FRESHNESS_ZH if recent else "",
        CORE=d["core"],
        TOPIC_ANALYSIS=topic_analysis(slug, t),
        DIAGRAM=diagram,
        RESEARCH_DEPTH=research_depth(directory, slug, t),
        RECENT_UPDATES=recent_updates(directory, slug),
        SYSTEMS_ROWS=system_rows(systems),
        DATA_ROWS=dataset_rows(datasets),
        READING=reading,
    )


def make_index() -> str:
    sections = []
    for directory, slugs in en.STRUCTURE.items():
        items = "\n".join(
            f"- [x] [{zh_title(directory, s)}]({directory}/{s}.md)（[英文原文](../{EN_DIR}/{directory}/{s}.md)）"
            for s in slugs.split()
        )
        sections.append(f"### `{directory}/` — {DIR_ZH[directory]}\n{DOMAIN_ZH[directory]['frame']}\n\n{items}")
    return fill(INDEX_ZH, UPDATED=en.UPDATED, SECTIONS="\n".join(sections))


def main() -> None:
    missing = [f"{d}/{s}" for d, slugs in en.STRUCTURE.items() for s in slugs.split() if f"{d}/{s}" not in TITLE_ZH]
    missing += [k for k in en.SPECIAL if k not in SPECIAL_ZH]
    missing += [k for k, v in en.RECENT_UPDATES.items() if v.strip() and k not in RECENT_UPDATES_ZH]
    missing += [k for k in en.DOMAIN if k not in DOMAIN_ZH or k not in DOMAIN_FORMALISM_ZH]
    if missing:
        raise SystemExit(f"Missing Chinese translations: {missing}")
    ROOT.mkdir(parents=True, exist_ok=True)
    for directory, slugs in en.STRUCTURE.items():
        out = ROOT / directory
        out.mkdir(parents=True, exist_ok=True)
        for slug in slugs.split():
            (out / f"{slug}.md").write_text(note(directory, slug), encoding="utf-8")
    (ROOT / "README.md").write_text(fill(README_ZH, UPDATED=en.UPDATED), encoding="utf-8")
    (ROOT / "INDEX.md").write_text(make_index(), encoding="utf-8")


if __name__ == "__main__":
    main()
