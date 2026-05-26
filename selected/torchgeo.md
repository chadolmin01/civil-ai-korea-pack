---
name: "TorchGeo"
slug: "torchgeo"
category: "SURVEY_GIS"
summary: "PyTorch 위 지리공간 ML"
github: "https://github.com/torchgeo/torchgeo"
license: "MIT"
language: "Python"
korean_applications:
  - "Sentinel / Landsat 위성 영상 기반 *한국 토지피복 분류* / 건물 추출 / 변화 검출 학습"
  - "한국 환경공단 / NGII 데이터로 사전학습 모델 미세조정 (transfer learning)"
added: 2026-05-25
---

Microsoft AI for Good Lab 가 시작한 *지리공간 데이터를 위한 PyTorch 라이브러리*. ★4k.

기존 PyTorch + torchvision 의 *지리 데이터 버전*. GeoTIFF / Shapefile 데이터셋 로더, 좌표계 변환, 패치 샘플러, 사전학습 모델 (위성 영상용).

지원 데이터셋 50+ (Sentinel, Landsat, NAIP, EuroSAT, BigEarthNet 등). 사전학습 모델 (Resnet18-Sentinel2 등).

segment-geospatial 이 *제로샷 분할* 이라면 TorchGeo 는 *학습 + 미세조정* 흐름.

한국 환경 / 도시 / 임야 / 재난 관리에서 *학습 데이터 + 사전모델* 결합 머신러닝 흐름의 첫 후보. 영어 / 글로벌 데이터셋과 한국 데이터 결합 가능.
