---
name: "segment-geospatial"
slug: "segment-geospatial"
category: "SURVEY_GIS"
summary: "위성 영상 객체를 SAM 으로 자동 분할"
github: "https://github.com/opengeos/segment-geospatial"
license: "MIT"
language: "Python"
korean_applications:
  - "위성 영상에서 *건물 / 도로 / 농지 / 산림* 자동 분할 + 면적 자동 산정"
  - "재난 (산불 / 홍수) 사후 영향 면적 자동 산출 (사전/사후 영상 비교)"
added: 2026-05-25
---

Meta 의 Segment Anything Model (SAM) 을 *위성 / 항공 영상* 에 특화한 Python 라이브러리. ★4k.

기존 위성 영상 분할은 *클래스별 학습 데이터 필요* — segment-geospatial 은 SAM 의 *제로샷* 능력을 활용해 학습 없이 객체 분할.

GeoTIFF / WMS 직접 입력. 결과 = GeoJSON / Shapefile (QGIS / leafmap 호환).

leafmap / geemap 자매 라이브러리 (같은 저자) — Jupyter 친화.

한국 환경 / 도시 / 임야 / 재난 관련 *위성 데이터 활용* 자동화. NGII / Sentinel / Landsat 데이터에서 객체 단위 추출이 한 줄로 가능.
