"""Summarize OpenCrab query results — civilai.kr pack."""
import json
from pathlib import Path

QUERIES = {
    1: "내가 누락한 BIM 도구가 있는지 점검",
    2: "라이센스 불명으로 탈락한 도구 중 다시 봐야 할 후보",
    3: "별 1000 미만인데 큐레이션에 포함된 도구들의 공통 선별 이유",
    4: "측량 GIS 1차 통과했지만 최종 탈락한 도구 패턴",
    5: "한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합",
}

DIR = Path(__file__).parent
out_md = []

for i, q in QUERIES.items():
    path = DIR / f"q{i}.json"
    out_md.append(f"## Q{i}. {q}\n")
    if not path.exists():
        out_md.append("_(no file)_\n")
        continue
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            out_md.append("_(invalid JSON)_\n")
            continue
    out_md.append("| # | source | score | node | snippet |")
    out_md.append("|---|---|---|---|---|")
    for idx, r in enumerate(data[:5], 1):
        node = r["node_id"].replace("\\", "/").split("/")[-1]
        snippet = r.get("text", "")[:80].replace("\n", " ").replace("|", "\\|")
        out_md.append(
            f"| {idx} | {r['source']} | {r['score']:.3f} | `{node}` | {snippet}… |"
        )
    out_md.append("")

result = "\n".join(out_md)
with open(DIR / "RESULTS.md", "w", encoding="utf-8") as f:
    f.write("# OpenCrab Query Results — civilai.kr pack\n\n")
    f.write(
        "Local LocalCrab (SQLite + ChromaDB) 인제스트 (87 files) 후 hybrid retrieval (vector + BM25 + graph) 결과.\n\n"
        "총 후보 2108 (자동 발굴 2059 + 수동 시드 49) → 선별 83 / 탈락 2025.\n\n"
    )
    f.write(result)

print(result)
