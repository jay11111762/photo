# Foreedom editorial photo library

150장의 포리덤 행사·공간 사진을 선별하고 비생성 색보정한 에셋 라이브러리입니다.

- Key visual: 12장 — 사이트·캠페인 첫 장면
- Signature: 23장 — 반복 노출할 관계·브랜드 모티프
- Editorial: 96장 — 서비스·브랜드 이야기 본문
- Archive: 19장 — 행사 기록·연혁·뉴스

[온라인 갤러리](https://jay11111762.github.io/photo/)에서, 또는 `index.html`을 열면 용도·장면·행사명으로 검색하고 보정 전후를 비교할 수 있습니다. 사진을 누르면 각 컷의 선정 이유와 크롭 가이드가 표시됩니다.

`assets/master/`: sRGB JPG, 긴 변 최대 4096px, 원본 비율 유지. 작은 원본은 확대하지 않습니다.

`assets/web/`: sRGB WebP, 긴 변 최대 2400px. 실제 웹 에셋에 권장합니다.

`assets/thumbs/`: JPG, 긴 변 최대 640px. 목록·검수용입니다.

`manifest.json`, `selection.csv`: 원본 상대 경로, 용도, 선정 이유, 보정 프로파일·노출·화이트밸런스, 출력 크기와 체크섬을 기록합니다.

`review/original/`: 보정 전 sRGB 미리보기입니다. 원본 사진 파일 전체를 저장소에 복제한 것은 아닙니다.

원본 `/Volumes/jw/##photo`에는 아무 변경도 하지 않았습니다. 출력은 색·명암만 변경하고 얼굴, 로고, 문구, 물체, 구도를 재생성하지 않았습니다. 보정은 픽셀 색상값을 바꾸며 JPG/WebP는 손실 압축됩니다. EXIF 촬영·GPS 정보는 출력에 포함하지 않습니다.

## Direction

포리덤의 사진 문법은 **대화하는 얼굴 → 함께 쓰는 손 → 이동하는 뒷모습 → 브랜드의 작은 물성**입니다. 큰 공간 컷 하나와 가까운 관계 컷 둘을 묶어 편집하면 일관성이 생깁니다. 단체사진은 캠페인 히어로보다 행사 본문에 사용합니다.

[Monocle](https://monocle.com/), [BRUTUS](https://brutus.jp/), [POPEYE](https://popeyemagazine.jp/)의 장소·문화·생활 중심 편집을 참고한 해석입니다. 매체의 공식 LUT나 동일한 보정값을 사용한 것은 아닙니다. 노출 보정은 −0.08~+0.23 EV로 제한했고 주간·실내·야간의 분위기를 유지했습니다. 상세 방향은 갤러리의 편집 기준에서 확인할 수 있습니다.

브릿지 폴더의 PNG는 서비스 소개 그래픽이어서 행사 사진 선별에서 제외했습니다. UNIVijob와 Vijob가 함께 등장하는 행사·부스는 공동 활용 맥락으로 표시했습니다. 브랜드 표기는 참가자 소속·국적의 판정이 아닙니다.

## Rebuild

Python 3.12 / Pillow / numpy / pillow-heif. `python -m pip install -r tools/requirements.txt`로 의존성을 설치합니다. `tools/rebuild.py`에 원본 루트와 별도 출력 디렉터리를 지정하면 manifest의 보정값으로 다시 출력합니다. 원본 SHA-256을 검사합니다. HDR/RAW 현상과 인쇄용 CMYK 분판은 별도 작업이며 이 패키지는 화면용 sRGB입니다.

사진의 공개 게시 여부와 별개로 사진 사용 권한은 원 권리자의 조건을 따릅니다. 이 저장소는 사진의 오픈 라이선스를 부여하지 않습니다.

## Asset URLs

웹에서 바로 사용할 경로 예시: `https://jay11111762.github.io/photo/assets/web/foreedom-p00528.webp`

전체 경로·선정 이유·크롭 지침은 [manifest.json](manifest.json)에서 확인합니다. 라이브러리의 상대 경로에 갤러리 URL을 붙이면 됩니다.
