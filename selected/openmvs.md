---
name: "OpenMVS"
slug: "openmvs"
category: "SURVEY_GIS"
summary: "다중 뷰 스테레오 사진측량 (점군·메시)"
github: "https://github.com/cdcseacave/openMVS"
license: "AGPL-3.0"
language: "C++"
korean_applications:
  - "드론 사진측량 (오쏘 이미지 + 다중각 사진) → 정밀 점군 + 메시 자동 생성"
  - "LiDAR 부재 시 사진 기반 모델링 — 소규모 현장 / 도시 보존 / 문화재"
added: 2026-05-25
---

OpenMVS = open Multi-View Stereo 의 줄임말. 사진측량 (Photogrammetry) 파이프라인의 *후반부* (Dense Reconstruction) 표준 도구. ★4k.

워크플로우: SfM (Structure from Motion, COLMAP / Meshroom) → 점군 → OpenMVS → 정밀 메시 + 텍스처.

LiDAR 가 없거나 비용 부담될 때, *사진만으로 3D 모델* 만드는 경로. 드론 + 일반 카메라 결합 가능.

핵심 단계: Dense Point Cloud (DensifyPointCloud) → Mesh (ReconstructMesh) → Refine (RefineMesh) → Texture (TextureMesh).

CLI 파이프라인 — 사내 자동화 통합 쉬움. PDAL / Open3D / MeshLab 와 자연스러운 후처리 연결.

AGPL-3.0 — 사내 무료, 외부 서비스화 시 라이센스 의무.

한국 토목 현장의 *사진 기반 측량* — 드론 LiDAR 비용 부담될 때, 소규모 현장 / 부분 측량 / 문화재 보존에 적합.
