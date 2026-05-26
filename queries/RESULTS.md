# OpenCrab Query Results — civilai.kr pack

Local LocalCrab (SQLite + ChromaDB) 위에서 hybrid retrieval (vector + BM25 + graph). 5 질의의 top-5 결과.

## Q1. 내가 누락한 BIM 도구가 있는지 점검

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 0.929 | `assimp.md` | --- name: "Open Asset Import Library (assimp)" slug: "assimp" category: "BIM_IFC… |
| 2 | vector | 0.910 | `ifcopenshell.md` | --- name: "IfcOpenShell" slug: "ifcopenshell" category: "BIM_IFC" summary: "IFC … |
| 3 | vector | 0.849 | `selection_log.md` | # 선별 과정 로그  원본 후보 **2059** 개 → 최종 큐레이션 **83** 장. (후보 중 ko/ 에 promotion 된 카드: 34 … |
| 4 | vector | 0.783 | `revitlookup.md` | --- name: "RevitLookup" slug: "revitlookup" category: "BIM_IFC" summary: "Revit … |
| 5 | vector | 0.776 | `hypar-elements.md` | --- name: "Hypar Elements" slug: "hypar-elements" category: "BIM_IFC" summary: "… |

## Q2. 라이센스 불명으로 탈락한 도구 중 다시 봐야 할 후보

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.000 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 2059 후보 → 83 큐레이션. 데이터 자산.  [civilai.… |
| 2 | vector | 0.842 | `rejected_patterns.md` | # 탈락 패턴  후보 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitHub AP… |
| 3 | vector | 0.769 | `floorplan-analyzer.md` | --- name: "FloorPlanAnalyzer" slug: "floorplan-analyzer" category: "DRAWING_OCR"… |
| 4 | vector | 0.745 | `engineering-drawing-extractor.md` | --- name: "engineering-drawing-extractor" slug: "engineering-drawing-extractor" … |
| 5 | vector | 0.742 | `selection_log.md` | # 선별 과정 로그  원본 후보 **2059** 개 → 최종 큐레이션 **83** 장. (후보 중 ko/ 에 promotion 된 카드: 34 … |

## Q3. 별 1000 미만인데 큐레이션에 포함된 도구들의 공통 선별 이유

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.056 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 2059 후보 → 83 큐레이션. 데이터 자산.  [civilai.… |
| 2 | vector | 0.793 | `rejected_patterns.md` | # 탈락 패턴  후보 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitHub AP… |
| 3 | vector | 0.716 | `csftools.md` | --- name: "CSFTools" slug: "csftools" category: "SURVEY_GIS" summary: "LiDAR 점군에… |
| 4 | vector | 0.679 | `dynamo.md` | --- name: "Dynamo" slug: "dynamo" category: "BIM_IFC" summary: "Revit / Civil 3D… |
| 5 | vector | 0.659 | `floorplan-analyzer.md` | --- name: "FloorPlanAnalyzer" slug: "floorplan-analyzer" category: "DRAWING_OCR"… |

## Q4. 측량 GIS 1차 통과했지만 최종 탈락한 도구 패턴

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 0.901 | `rejected_patterns.md` | # 탈락 패턴  후보 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitHub AP… |
| 2 | vector | 0.846 | `selection_log.md` | # 선별 과정 로그  원본 후보 **2059** 개 → 최종 큐레이션 **83** 장. (후보 중 ko/ 에 promotion 된 카드: 34 … |
| 3 | vector | 0.788 | `maptalks.md` | --- name: "maptalks.js" slug: "maptalks" category: "SURVEY_GIS" summary: "2D/3D … |
| 4 | vector | 0.779 | `blender-gis.md` | --- name: "BlenderGIS" slug: "blender-gis" category: "SURVEY_GIS" summary: "Blen… |
| 5 | vector | 0.762 | `mapshaper.md` | --- name: "mapshaper" slug: "mapshaper" category: "SURVEY_GIS" summary: "SHP/Geo… |

## Q5. 한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.056 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 2059 후보 → 83 큐레이션. 데이터 자산.  [civilai.… |
| 2 | vector | 0.900 | `mcp4ifc.md` | --- name: "MCP4IFC" slug: "mcp4ifc" category: "BIM_IFC" summary: "자연어로 IFC 모델 검증… |
| 3 | vector | 0.847 | `text-to-cad.md` | --- name: "Text-to-CAD" slug: "text-to-cad" category: "AGENT_WORKFLOW" summary: … |
| 4 | vector | 0.787 | `hollowrc.md` | --- name: "HollowRC" slug: "hollowrc" category: "STRUCTURE_SIM" summary: "중공 철근콘… |
| 5 | vector | 0.772 | `structuralcodes.md` | --- name: "structuralcodes" slug: "structuralcodes" category: "STRUCTURE_SIM" su… |
