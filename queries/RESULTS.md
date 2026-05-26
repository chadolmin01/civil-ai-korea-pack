# OpenCrab Query Results — civilai.kr pack

Local LocalCrab (SQLite + ChromaDB) 인제스트 (87 files) 후 hybrid retrieval (vector + BM25 + graph) 결과.

총 후보 2108 (자동 발굴 2059 + 수동 시드 49) → 선별 83 / 탈락 2025.

## Q1. 내가 누락한 BIM 도구가 있는지 점검

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 0.938 | `assimp.md` | --- name: "Open Asset Import Library (assimp)" slug: "assimp" category: "BIM_IFC… |
| 2 | vector | 0.919 | `ifcopenshell.md` | --- name: "IfcOpenShell" slug: "ifcopenshell" category: "BIM_IFC" summary: "IFC … |
| 3 | vector | 0.794 | `revitlookup.md` | --- name: "RevitLookup" slug: "revitlookup" category: "BIM_IFC" summary: "Revit … |
| 4 | vector | 0.778 | `hypar-elements.md` | --- name: "Hypar Elements" slug: "hypar-elements" category: "BIM_IFC" summary: "… |
| 5 | vector | 0.777 | `xeokit-bim-viewer.md` | --- name: "xeokit BIM Viewer" slug: "xeokit-bim-viewer" category: "VIZ_TWIN" sum… |

## Q2. 라이센스 불명으로 탈락한 도구 중 다시 봐야 할 후보

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.000 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 **2108** 후보 → **83** 큐레이션. 데이터 자산.  (… |
| 2 | vector | 0.826 | `rejected_patterns.md` | # 탈락 패턴  자동 발굴 풀 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitH… |
| 3 | vector | 0.771 | `floorplan-analyzer.md` | --- name: "FloorPlanAnalyzer" slug: "floorplan-analyzer" category: "DRAWING_OCR"… |
| 4 | vector | 0.753 | `selection_log.md` | # 선별 과정 로그  총 후보 **2108** 개 → 최종 큐레이션 **83** 장.  \| 풀 \| 개수 \| 출처 \| \|---\|---\|---\| \|… |
| 5 | vector | 0.746 | `engineering-drawing-extractor.md` | --- name: "engineering-drawing-extractor" slug: "engineering-drawing-extractor" … |

## Q3. 별 1000 미만인데 큐레이션에 포함된 도구들의 공통 선별 이유

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.056 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 **2108** 후보 → **83** 큐레이션. 데이터 자산.  (… |
| 2 | vector | 0.796 | `rejected_patterns.md` | # 탈락 패턴  자동 발굴 풀 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitH… |
| 3 | vector | 0.717 | `csftools.md` | --- name: "CSFTools" slug: "csftools" category: "SURVEY_GIS" summary: "LiDAR 점군에… |
| 4 | vector | 0.679 | `dynamo.md` | --- name: "Dynamo" slug: "dynamo" category: "BIM_IFC" summary: "Revit / Civil 3D… |
| 5 | vector | 0.659 | `floorplan-analyzer.md` | --- name: "FloorPlanAnalyzer" slug: "floorplan-analyzer" category: "DRAWING_OCR"… |

## Q4. 측량 GIS 1차 통과했지만 최종 탈락한 도구 패턴

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 0.901 | `rejected_patterns.md` | # 탈락 패턴  자동 발굴 풀 2059개 중 2025개 미선별. 주요 사유 패턴.  ## 1. 라이센스 불명 (NOASSERTION)  GitH… |
| 2 | vector | 0.799 | `maptalks.md` | --- name: "maptalks.js" slug: "maptalks" category: "SURVEY_GIS" summary: "2D/3D … |
| 3 | vector | 0.790 | `blender-gis.md` | --- name: "BlenderGIS" slug: "blender-gis" category: "SURVEY_GIS" summary: "Blen… |
| 4 | vector | 0.771 | `mapshaper.md` | --- name: "mapshaper" slug: "mapshaper" category: "SURVEY_GIS" summary: "SHP/Geo… |
| 5 | vector | 0.724 | `freecad-road.md` | --- name: "Road (FreeCAD Workbench)" slug: "freecad-road" category: "CAD_DWG" su… |

## Q5. 한국 KDS 검증 워크플로우에 묶을 수 있는 도구 조합

| # | source | score | node | snippet |
|---|---|---|---|---|
| 1 | vector | 1.056 | `README.md` | # CIVIL AI Korea Pack  > 글로벌 토목·건설 AI 오픈소스 **2108** 후보 → **83** 큐레이션. 데이터 자산.  (… |
| 2 | vector | 0.907 | `mcp4ifc.md` | --- name: "MCP4IFC" slug: "mcp4ifc" category: "BIM_IFC" summary: "자연어로 IFC 모델 검증… |
| 3 | vector | 0.853 | `text-to-cad.md` | --- name: "Text-to-CAD" slug: "text-to-cad" category: "AGENT_WORKFLOW" summary: … |
| 4 | vector | 0.790 | `hollowrc.md` | --- name: "HollowRC" slug: "hollowrc" category: "STRUCTURE_SIM" summary: "중공 철근콘… |
| 5 | vector | 0.774 | `structuralcodes.md` | --- name: "structuralcodes" slug: "structuralcodes" category: "STRUCTURE_SIM" su… |
