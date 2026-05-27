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
        0.89,
        "2,108 후보 → 83 큐레이션 (자동 2,059 + 수동 시드 49)",
        fontsize=10,
        color=MUTED,
    )

    fig.subplots_adjust(top=0.82, bottom=0.10, left=0.18, right=0.96)
    out = DIR / "funnel.png"
    plt.savefig(out, dpi=160, facecolor=BG)
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
    fig.text(0.05, 0.89, f"8 카테고리 enum 고정 · 총 {sum(values)}장", fontsize=10, color=MUTED)
    fig.subplots_adjust(top=0.82, bottom=0.10, left=0.20, right=0.96)
    out = DIR / "category.png"
    plt.savefig(out, dpi=160, facecolor=BG)
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
        y=0.95,
        ha="left",
        fontsize=15,
        fontweight="bold",
        color=FG,
    )
    fig.text(
        0.05,
        0.86,
        "한 후보가 여러 출처에 잡힐 수 있음 (corroboration = 신호 강도)",
        fontsize=10,
        color=MUTED,
    )
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.22, right=0.96)
    out = DIR / "sources.png"
    plt.savefig(out, dpi=160, facecolor=BG)
    plt.close()
    print(f"wrote {out}")


def social_preview():
    """GitHub social preview — 한국 표준 ↔ 오픈소스 매핑 우선 (1280x640)."""
    fig = plt.figure(figsize=(12.8, 6.4), facecolor=BG)
    ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
    ax.set_facecolor(BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Header — title + tagline
    ax.text(
        0.05, 0.90,
        "CIVIL AI Korea Pack",
        fontsize=30,
        fontweight="bold",
        color=FG,
        family="Malgun Gothic",
    )
    ax.text(
        0.05, 0.82,
        "글로벌 토목·건설 AI 오픈소스  ↔  한국 표준 1:1 매핑",
        fontsize=14,
        color=MUTED,
        family="Malgun Gothic",
    )

    # 5 매핑 rows
    mappings = [
        ("KDS 14 20 50",        "콘크리트 철근상세 자동 검증",   "MCP4IFC + IfcOpenShell"),
        ("KDS 41 17 00",        "내진 비선형 시간이력 해석",     "OpenSees"),
        ("조달청 BIM 납품",      "IFC 일괄 검수",                "IfcOpenShell"),
        ("BF 인증",             "출입구 / 경사로 자동 점검",     "MCP4IFC"),
        ("드론 LiDAR → 토공",   "지표면 추출 + DEM 생성",        "CSFTools"),
    ]

    # row 영역: y = 0.10 ~ 0.72 (0.62 단위)
    n = len(mappings)
    row_h = 0.62 / n
    top_y = 0.72

    # Column x positions
    x_std = 0.05      # 한국 표준 코드 (좌)
    x_scenario = 0.30 # 시나리오 설명 (중-좌)
    x_arrow = 0.58    # 화살표
    x_repo = 0.63     # 오픈소스 (우)

    for i, (std, scenario, repo) in enumerate(mappings):
        y = top_y - (i + 0.5) * row_h
        # left: 표준 코드 (bold accent)
        ax.text(
            x_std, y,
            std,
            fontsize=15,
            fontweight="bold",
            color=ACCENT,
            family="Malgun Gothic",
            va="center",
        )
        # middle: 시나리오 설명
        ax.text(
            x_scenario, y,
            scenario,
            fontsize=12,
            color=FG,
            family="Malgun Gothic",
            va="center",
        )
        # arrow
        ax.text(
            x_arrow, y,
            "→",
            fontsize=18,
            color=MUTED,
            family="Malgun Gothic",
            va="center",
        )
        # right: 오픈소스 repo
        ax.text(
            x_repo, y,
            repo,
            fontsize=14,
            fontweight="bold",
            color=FG,
            family="Malgun Gothic",
            va="center",
        )

    # Footer
    ax.text(
        0.05, 0.04,
        f"83 카드  ·  KDS / KCS / BF / KOSHA  ·  자연어 질의 가능 (OpenCrab)",
        fontsize=11,
        color=MUTED,
        family="Malgun Gothic",
    )
    ax.text(
        0.95, 0.04,
        "civilai.kr",
        fontsize=11,
        color=MUTED,
        family="Malgun Gothic",
        ha="right",
        fontweight="bold",
    )

    out = DIR / "social-preview.png"
    plt.savefig(out, dpi=100, facecolor=BG)
    plt.close()
    print(f"wrote {out}")


if __name__ == "__main__":
    funnel_chart()
    category_chart()
    sources_chart()
    social_preview()
