# 탈락 패턴

자동 발굴 풀 2059개 중 2025개 미선별. 주요 사유 패턴.

## 1. 라이센스 불명 (NOASSERTION)

GitHub API 가 `NOASSERTION` 반환 — LICENSE 파일 없음 / 비표준 / 다중 라이센스 mixing.

사례: `mageaustralia/FloorPlanAnalyzer`, `Bakkopi/engineering-drawing-extractor`, `jianboqi/CSFTools`.

→ 학습 / 개인 연구용으로는 OK 지만 *사내 / 상용* 활용 시 변호사 검토 부담. 비용 대비 활용성 낮음.
일부는 그래도 promotion (수동 카드에 `license: "라이센스 명시 없음"` 명시).

## 2. 카테고리 추정 매칭하지만 도메인 비매칭

자동 키워드 매칭은 8 카테고리 enum 으로 분류했지만, 실제 도메인이 토목 / 건설 / 건축 영역 밖.

사례:
- `topic:lidar` 매칭 → 자율주행 LiDAR (Waymo / 자율주행 SDK) 다수
- `topic:bim` 매칭 → 비즈니스 인텔리전스 모델 (전혀 다른 BIM)
- `topic:cad` 매칭 → 회로 설계 CAD (KiCAD / Eagle 등 PCB)
- `topic:construction` 매칭 → 영어 *건설 메타포* 사용한 SaaS ("Build")

→ 카테고리 추정은 *키워드 1차 필터* 일 뿐, 도메인 적합성은 Lee 의 수동 판단.

## 3. 활동 정체 (STALE / ARCHIVED)

마지막 `pushed_at` > 2 년 또는 명시적 archived.

사례: `oddworldng/dwg_to_dxf` (2019-11 마지막 push) 같은 *실용적이지만 멈춘* repo 는 promotion (STALE 라벨 명시).
의존성으로 누군가 쓰는 게 가치 있으면 살림, 그렇지 않으면 폐기.

## 4. 학술 / 토이 / 미완

★ ≤ 5 이거나 README 한 줄, 코드 미완.

→ 대부분 자동 ★ 등급에서 ★ (최하) 로 분류 → 큐레이션 안 됨.

## 5. 중복 / 파생

이미 포함된 repo 의 파생 / 학습용 fork / mirror.

사례: `amrit3701/FreeCAD-Reinforcement` 는 promotion 했지만 `flowwie/flowwie-freecad`, `ghbalf/freecad-ai` 등 다수 파생 fork 는 폐기.

## 6. 외부 환경 종속이 너무 큼

ROS 풀스택, Unity / Unreal 라이브빌드, 특정 클라우드 (AWS Lambda 전용) 종속 등 *사내 환경에서 바로 시도* 가 어려운 도구.

토목 실무자의 *환경 진입 비용* 이 도구 가치를 압도하면 폐기.

## 7. 일반 generic agent / LLM 도구

`topic:mcp-server` 매칭하지만 토목 도메인 무관한 일반 LLM 인프라.

사례: `octelium` (zero trust auth), 일반 RAG 프레임워크, 일반 코드 리뷰 봇 등.
COMPAS / RevitMCPBridge / Bonsai_mcp 처럼 *AEC 명시* 한 것만 promotion.
