---
name: "engineering-drawing-extractor"
slug: "engineering-drawing-extractor"
category: "DRAWING_OCR"
summary: "도면 표제란에서 메타데이터 자동 추출"
github: "https://github.com/Bakkopi/engineering-drawing-extractor"
license: "라이센스 명시 없음"
language: "Python"
korean_applications:
  - "수만 장의 발주 도서 PDF 에서 도면번호 · 작성자 · 발주처 · 일자 자동 색인"
  - "공사 마무리 시 인계 도서의 표제란 정보를 ERP / EDMS 로 일괄 등록"
added: 2026-05-25
---

엔지니어링 청사진에서 도면번호 · 작성자 · 제목 같은 표제란 정보를 OCR 로 자동 추출하는 파이프라인.

도면 영역과 표제표 영역을 분리한 뒤, 표제표에 OCR 을 적용한다.

pdf2image + OpenCV + Tesseract 조합. 표제 레이아웃 표준이 정해진 한국 토목 도서에 잘 맞다.

> 라이센스 명시 없음 — 코드 차용 시 저자에게 확인 필요.

수년치 도서가 정리 없이 쌓여있는 한국 시공사 / 설계사 가 색인화·디지털화 작업의 초안으로 쓰기 좋음.
