# CIVIL AI Korea Pack

> 글로벌 토목·건설 AI 오픈소스 2059 후보 → 83 큐레이션. 데이터 자산.

[civilai.kr](https://civilai.kr) 의 라이브러리 카드 83장과 *선별 과정* 을 자연어 질의 가능한 형태로 정리한 OpenCrab 호환 팩.

## 무엇이 이 안에

- `selected/` — 큐레이션 83장 카드 (한국 적용 시나리오 + 메타데이터)
- `candidates.jsonl` — 발굴 후보 2059 개 (선별 / 탈락 상태 포함)
- `selection_log.md` — 4 단계 필터 + Lee 의 수동 promotion 이력
- `rejected_patterns.md` — 자주 나온 탈락 사유 패턴 7 가지

## OpenCrab 인제스트

```bash
opencrab ingest https://github.com/chadolmin01/civil-ai-korea-pack
```

## 자연어 질의 예시

- "내가 누락한 BIM 도구가 있는지 점검해줘"
- "라이센스 불명으로 탈락한 도구 중 다시 봐야 할 후보는?"
- "★1k 미만인데 83개에 포함된 도구들의 공통 선별 이유는?"
- "측량 / GIS 1차 통과했지만 최종 탈락한 도구 패턴은?"
- "한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합은?"

## 갱신

원본 사이트 ([civilai.kr](https://civilai.kr)) 의 `src/content/library/ko/` 가 source of truth.
이 팩은 사이트 repo 의 `scripts/build-pack.ts` 로 *자동 생성된 파생물*.

## 라이센스

CC BY-SA 4.0 — 콘텐츠 자유 사용, 변경 시 같은 라이센스로 공유.

## 만든 사람

- [Lee (Seongmin)](https://tryseongmin.com) · [@trySeongmin](https://www.threads.com/@tryseongmin)
- 원본 사이트: [civilai.kr](https://civilai.kr)
- 이슈 / 제안: GitHub Issues

## 영감

- [@alex_ai_mcp](https://github.com/AlexAI-MCP) 의 OpenCrab — 자연어 질의 데이터 팩 인프라
- [@logotekton](https://www.threads.com/@logotekton) — *큐레이션 자체가 데이터 자산* 관점
