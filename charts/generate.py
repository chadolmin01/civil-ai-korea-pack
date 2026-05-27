"""civilai.kr pack visualizations.

Charts:
1. funnel.png    — 2108 candidates → 83 selected (filter stages)
2. category.png  — 8 categories distribution
3. sources.png   — discovery source breakdown
"""
import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl

# Korean font fallback — Windows
mpl.rcParams["font.family"] = ["Malgun Gothic", "Pretendard", "Apple SD Gothic Neo", "DejaVu Sans"]
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["pdf.fonttype"] = 42

# Pack palette (matches civilai.kr)
BG = "#fafaf9"
FG = "#171717"
MUTED = "#737373"
ACCENT = "#0f766e"

DIR = Path(__file__).parent
PACK = DIR.parent


def load_candidates():
    with open(PACK / "candidates.jsonl", "r", encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def funnel_chart():
    """Funnel: 2108 candidates → 83 selected."""
    stages = [
        ("자동 발굴", 2059),
        ("+ 수동 시드", 2108),
        ("자동 카테고리 매칭", 1471),
        ("★★★ 자동 등급", 76),
        ("수동 promotion", 83),
    ]
    labels = [s[0] for s in stages]
    values = [s[1] for s in stages]

    fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG)
    ax.set_facecolor(BG)

    from matplotlib.colors import to_rgba

    y_pos = list(range(len(stages)))[::-1]
    alphas = [1.0, 0.85, 0.65, 0.45, 1.0]
    bar_colors = [
        to_rgba(ACCENT if i == len(stages) - 1 else FG, alpha=alphas[i])
        for i in range(len(stages))
    ]
    bars = ax.barh(y_pos, values, color=bar_colors, height=0.7)

    for i, (label, val) in enumerate(stages):
        y = y_pos[i]
        ax.text(
            val + max(values) * 0.012,
            y,
            f"{val:,}",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=FG,
            family="JetBrains Mono",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11, color=FG)
    ax.tick_params(axis="x", colors=MUTED, labelsize=9)
    ax.set_xlim(0, max(values) * 1.18)
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)
    ax.grid(False)

    fig.suptitle(
        "civilai.kr 선별 펀넬",
        x=0.05,
        y=0.96,
        ha="left",
        fontsize=15,
        fontweight="bold",
        color=FG,
    )
    fig.text(
        0.05,
        0.91,
        "2,108 후보 → 83 큐레이션 (자동 2,059 + 수동 시드 49)",
        fontsize=10,
        color=MUTED,
    )

    plt.tight_layout(rect=(0, 0, 1, 0.88))
    out = DIR / "funnel.png"
    plt.savefig(out, dpi=160, facecolor=BG, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


def category_chart():
    """Category distribution of selected 83 cards."""
    cands = load_candidates()
    selected = [c for c in cands if c["status"] == "selected"]
    # Categories come from .md files — re-read selected cards
    cat_count = Counter()
    for md in (PACK / "selected").glob("*.md"):
        text = md.read_text(encoding="utf-8")
        for line in text.split("\n"):
            if line.startswith("category:"):
                cat = line.split(":", 1)[1].strip().strip('"')
                cat_count[cat] += 1
                break

    LABELS = {
        "BIM_IFC": "BIM / IFC",
        "CAD_DWG": "CAD / DWG",
        "SURVEY_GIS": "측량 / GIS",
        "VIZ_TWIN": "시각화 / 트윈",
        "STRUCTURE_SIM": "구조해석",
        "AGENT_WORKFLOW": "AI 에이전트",
        "SPEC_REVIEW": "시방 검증",
        "DRAWING_OCR": "도면 OCR",
    }
    items = sorted(cat_count.items(), key=lambda x: -x[1])
    labels = [LABELS.get(k, k) for k, _ in items]
    values = [v for _, v in items]

    fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG)
    ax.set_facecolor(BG)

    y_pos = list(range(len(items)))[::-1]
    ax.barh(y_pos, values, color=ACCENT, height=0.65)
    for i, v in enumerate(values):
        ax.text(
            v + 0.3,
            y_pos[i],
            str(v),
            va="center",
            fontsize=11,
            fontweight="bold",
            color=FG,
            family="JetBrains Mono",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11, color=FG)
    ax.tick_params(axis="x", colors=MUTED, labelsize=9)
    ax.set_xlim(0, max(values) + 5)
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    fig.suptitle(
        "큐레이션 83 카드 — 카테고리 분포",
        x=0.05,
        y=0.96,
        ha="left",
        fontsize=15,
        fontweight="bold",
        color=FG,
    )
    fig.text(0.05, 0.91, f"8 카테고리 enum 고정 · 총 {sum(values)}장", fontsize=10, color=MUTED)
    plt.tight_layout(rect=(0, 0, 1, 0.88))
    out = DIR / "category.png"
    plt.savefig(out, dpi=160, facecolor=BG, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


def sources_chart():
    """Source-type breakdown of all candidates."""
    cands = load_candidates()
    type_count = Counter()
    for c in cands:
        types = set()
        for s in c.get("sources", []):
            if ":" in s:
                types.add(s.split(":", 1)[0])
            else:
                types.add(s)
        for t in types:
            type_count[t] += 1

    labels_map = {
        "topic": "GitHub topic 검색",
        "awesome": "Awesome list",
        "query": "GitHub 풀텍스트 search",
        "manual": "수동 시드",
    }
    items = sorted(type_count.items(), key=lambda x: -x[1])
    labels = [labels_map.get(k, k) for k, _ in items]
    values = [v for _, v in items]

    fig, ax = plt.subplots(figsize=(8, 4), facecolor=BG)
    ax.set_facecolor(BG)
    from matplotlib.colors import to_rgba

    y_pos = list(range(len(items)))[::-1]
    bar_colors = [
        to_rgba(
            ACCENT if "수동" in labels[i] else FG,
            alpha=1.0 if "수동" in labels[i] else 0.75,
        )
        for i in range(len(items))
    ]
    bars = ax.barh(y_pos, values, color=bar_colors, height=0.6)
    for i, v in enumerate(values):
        ax.text(
            v + max(values) * 0.012,
            y_pos[i],
            f"{v:,}",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=FG,
            family="JetBrains Mono",
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=11, color=FG)
    ax.tick_params(axis="x", colors=MUTED, labelsize=9)
    ax.set_xlim(0, max(values) * 1.18)
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    fig.suptitle(
        "후보 발굴 출처",
        x=0.05,
        y=0.94,
        ha="left",
        fontsize=15,
        fontweight="bold",
        color=FG,
    )
    fig.text(
        0.05,
        0.88,
        "한 후보가 여러 출처에 잡힐 수 있음 (corroboration = 신호 강도)",
        fontsize=10,
        color=MUTED,
    )
    plt.tight_layout(rect=(0, 0, 1, 0.85))
    out = DIR / "sources.png"
    plt.savefig(out, dpi=160, facecolor=BG, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    funnel_chart()
    category_chart()
    sources_chart()
