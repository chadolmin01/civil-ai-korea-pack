---
name: "ThingsBoard"
slug: "thingsboard"
category: "VIZ_TWIN"
summary: "IoT 센서 데이터 + 디지털 트윈 통합"
github: "https://github.com/thingsboard/thingsboard"
license: "Apache-2.0"
language: "Java"
korean_applications:
  - "교량 / 터널 / 댐 의 변위 / 응력 센서 실시간 수집 + 디지털 트윈 위 오버레이"
  - "시설물 IoT 모니터링 자체 호스팅 (외부 클라우드 의존 회피, 국가 보안 시설 관리)"
added: 2026-05-25
---

벨라루스 ThingsBoard 가 만든 오픈소스 IoT 플랫폼. ★21.8k.

핵심: 디바이스 관리 + 데이터 수집 (MQTT / CoAP / HTTP / LwM2M / SNMP) + 룰 엔진 + 위젯 대시보드 + 알람 + 자체 호스팅.

디지털 트윈 시각화 (Cesium / xeokit) 와 짝지어 *시설물 상태* 를 실시간으로 표현. 변위 임계 초과 시 자동 알람.

Java 백엔드 + Angular 프론트엔드. PostgreSQL / Cassandra DB. Docker / K8s 배포.

한국 도로공사 / K-water / 한전 의 시설물 모니터링, 지자체 스마트시티 부서의 센서 통합, 보안 시설 (외부 클라우드 금지) 의 자체 IoT 플랫폼.
