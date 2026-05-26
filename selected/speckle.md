---
name: "Speckle"
slug: "speckle"
category: "BIM_IFC"
summary: "BIM/AEC 데이터 협업 플랫폼 구축"
github: "https://github.com/specklesystems/speckle-server"
license: "Apache-2.0"
language: "TypeScript / Vue / Python"
korean_applications:
  - "Revit / Rhino / Civil 3D 간 모델 변경분을 회사 서버에서 직접 관리"
  - "발주-설계-시공 단계별 모델 버전을 단일 진실 저장소로 통합"
added: 2026-05-25
---

Speckle Systems 가 만든 AEC 데이터 협업 플랫폼. 흔히 "BIM 을 위한 Git" 으로 비유된다.

서버 (TypeScript / Vue) + 다양한 CAD/BIM 도구 커넥터 (Revit, Rhino, Grasshopper, Blender, AutoCAD, Civil 3D) 구조.

Revit 의 객체 단위 diff, IFC 외 다양한 스키마 (USD, glTF) 변환, GraphQL API 까지 한 자리에서 다룬다.

자체 호스팅 무료 (Apache-2.0). 클라우드 호스팅도 제공.

대형 설계사 / 시공사 BIM 팀이 협업 데이터 인프라를 자체 운영하려 할 때 사실상 첫 후보.
