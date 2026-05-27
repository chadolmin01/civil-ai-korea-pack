# 기여 가이드

CIVIL AI Korea Pack 에 관심 주셔서 감사합니다.

이 저장소는 [civilai.kr](https://civilai.kr) 의 *큐레이션 결과 + 과정* 을 데이터 자산화한 것입니다. 사이트가 single source of truth 이고, 이 팩은 [`scripts/build-pack.ts`](https://github.com/chadolmin01/civil-ai-korea/blob/main/scripts/build-pack.ts) 로 자동 생성됩니다.

따라서 **이 저장소에 직접 PR 을 보내지 마세요** — 변경은 사이트 repo 에서 일어나야 합니다.

---

## 어떤 종류의 기여가 가능한가

### 1. 새 라이브러리 / repo 제보

이슈로 받습니다 — *Pack 에 누락된 토목·건설 AI 오픈소스가 있다면*.

**이슈 템플릿**:
```
- Repo URL: https://github.com/...
- 카테고리: BIM_IFC | CAD_DWG | SURVEY_GIS | VIZ_TWIN | STRUCTURE_SIM | AGENT_WORKFLOW | SPEC_REVIEW | DRAWING_OCR
- 한국 적용 시나리오: (KDS / KCS / BF / KOSHA 조항 또는 실무 상황)
- 왜 큐레이션 가치가 있는가: (1-2 문장)
```

Lee 가 직접 검토 후 사이트 repo 에 promotion 합니다 (자동 발행 안 함).

### 2. 큐레이션 오류 신고

- `selected/*.md` 의 사실 오류 (라이센스 / 언어 / 한국 적용 매핑 등)
- `rejected_patterns.md` 의 분류 오류
- `selection_log.md` 의 수치 불일치

→ 이슈로 신고. 본문에 *어느 파일의 어느 줄* 명시.

### 3. 자신의 도메인으로 fork

**환영합니다.** Pack 의 데이터 자산화 패턴은 토목·건설 외 도메인 (전기 / 기계 / 화공 / 의료 / 디자인 / 법률 등) 에도 그대로 적용 가능합니다.

Fork 후:
1. `candidates.jsonl` 의 schema 유지 (`repo / sources / stars / status` 등)
2. `selected/*.md` frontmatter 의 `category` enum 을 본인 도메인 분류로 (8개 enum 권장)
3. `selection_log.md` 에 본인 필터 기준 단계별 기록
4. `rejected_patterns.md` 에 본인 도메인의 탈락 사유
5. `charts/generate.py` 의 카테고리 라벨 교체

fork 한 repo URL 을 이슈로 알려주시면 README 의 "관련 fork" 섹션에 링크합니다.

### 4. 번역 / 다국어

본 팩은 현재 한국어만. 영문 / 일문 / 중문 등 번역 fork 환영. CC BY-SA 4.0 라이센스 준수 + 원본 출처 표기 필수.

---

## 무엇이 *받지 않는* 기여인가

- ❌ **카드 본문 직접 수정 PR** — 사이트 repo (civilai.kr) 에서 변경하세요.
- ❌ **새 카테고리 추가 제안** — 8 enum 고정입니다 (decisions.md D3 결정).
- ❌ **자동 발행 / 봇 PR** — 자동 발굴된 후보는 Lee 의 수동 검수 후에만 큐레이션됩니다 (CLAUDE.md 절대 금지 5).
- ❌ **광주 화정 아이파크 / 모바일 ID / 감리 서명 콘텐츠 제안** — 본 팩의 scope 가 아닙니다 (CLAUDE.md 절대 금지 9, 10).

---

## 라이센스 동의

기여 시 본 저장소의 라이센스에 동의한 것으로 간주합니다:
- 콘텐츠 (이슈 / 제보) → CC BY-SA 4.0
- 스크립트 → MIT

자세한 내용은 [LICENSE](./LICENSE).

---

## 행동 강령

- 마케팅 톤 금지 ("혁신적인", "최고의", "강력한") — README 와 동일한 절제된 문체
- 영어 그대로 복붙 / Repo README 직역 금지
- 광고성 repo 제보 금지

---

## 만든 사람

- [Lee (Seongmin)](https://tryseongmin.com) · [@trySeongmin](https://www.threads.com/@tryseongmin)
- 이슈: [GitHub Issues](https://github.com/chadolmin01/civil-ai-korea-pack/issues)
