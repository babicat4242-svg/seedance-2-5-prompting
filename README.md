# Seedance 2.5 Prompting Skill

Seedance 2.5와 명시적 Seedance 2.0 Fast 영상 프롬프트를 작성·검토·수정하는 Codex용 커뮤니티 스킬입니다. 멀티모달 레퍼런스 바인딩, R2V/화이트 모델, 30초 및 커스텀 15초 구성, 지역 수정·연장, 그리고 물리적으로 일관된 카메라 모션 설계에 초점을 둡니다.

> Unofficial community skill; not affiliated with ByteDance or Dreamina.

이 저장소는 v1 스킬로 별도 관리합니다. v2의 추가 연출 규칙과 통합하지 않습니다.

프롬프트 출력 순서: **참조 → 피사체 → 배경 → 타임라인 → 카메라 → 스타일 → 오디오 → 제약 조건**. 참조에는 이미지·영상 자료를, 오디오에는 음원 참조·대사·효과음·BGM을 구분해서 배치합니다.

## 주요 기능

- Seedance 2.5와 명시적 Seedance 2.0 Fast를 처리하고, 그 밖의 2.0 레거시는 기존 2.0 스킬로 라우팅
- `@Image1`, `@Video1`, `@Audio1` 등 레퍼런스 태그와 역할·우선순위 보존
- 인물 정체성, 동작, 공간/카메라 경로, 오디오 리듬의 독립 바인딩
- 원테이크, 멀티숏, 제품 광고, R2V, 화이트 모델, 지역 수정, 연장 패턴
- 30개 카메라 모션 정의와 충돌 규칙
- 시작 구도 → 물리 경로 → 방향축 → 속도/이징 → 렌즈/초점 → 종료 구도로 이어지는 카메라 컴파일러
- 현재 UI와 계정에 따라 달라질 수 있는 기능은 `Beta/UI-dependent`로 명시
- Seedance 2.5: 권장 4,300–4,800자, 공백·줄바꿈 포함 하드 리밋 5,000자
- Seedance 2.0 Fast 커스텀 프로필: 15초, 약 3,500자 목표, 하드 리밋 4,000자, 2.5와 동일한 프롬프트 구조
- 활성 프로필의 하드 리밋 초과 시 중국어 간체 폴백

## 설치

### macOS / Linux

```bash
git clone https://github.com/babicat4242-svg/seedance-2-5-prompting.git \
  ~/.codex/skills/seedance-2-5-prompting
```

### Windows PowerShell

```powershell
git clone https://github.com/babicat4242-svg/seedance-2-5-prompting.git `
  "$env:USERPROFILE\.codex\skills\seedance-2-5-prompting"
```

Codex가 이미 실행 중이라면 새 작업을 시작하거나 앱을 다시 열어 스킬 목록을 갱신하세요.

## 사용 예시

```text
씨댄스 2.5로 12초 복도 원테이크 프롬프트를 만들어줘.
@Image1은 인물 정체성, @Video1은 걷기와 문 열기 동작만 사용해.
카메라는 후방 3/4 팔로우에서 왼쪽으로 아크한 뒤 문을 통과해 느린 돌리 인으로 끝내줘.
```

```text
Seedance 2.5로 30초 럭셔리 향수 광고 프롬프트를 작성해줘.
@Video1은 제품 회전이 아니라 카메라 반원 오빗 경로만 참조해.
```

```text
Seedance 2.0 Fast로 15초 제품 광고 프롬프트를 작성해줘.
2.5와 같은 자산 역할표·타임라인·카메라 시작/경로/도착·오디오·최종 프레임 구조를 유지해.
약 3,500자를 목표로 하고 4,000자를 넘기지 마.
```

## 파일 구성

```text
SKILL.md
agents/openai.yaml
references/camera-motion.md
references/community-api-prompts-analysis.md
references/model-differences.md
references/prompt-patterns.md
references/sources.md
scripts/count_prompt_chars.py
tests/test_count_prompt_chars.py
```

- [`SKILL.md`](SKILL.md): 트리거, 작성 절차, 출력 계약
- [`camera-motion.md`](references/camera-motion.md): 카메라 모션 사전과 충돌 매트릭스
- [`model-differences.md`](references/model-differences.md): 2.0 → 2.5 마이그레이션 기준
- [`prompt-patterns.md`](references/prompt-patterns.md): 실전 프롬프트 패턴
- [`sources.md`](references/sources.md): 공식 출처와 근거 우선순위
- [`count_prompt_chars.py`](scripts/count_prompt_chars.py): 기본 5,000자 및 `--limit 4000` Fast 하드 리밋 검사
- [`test_count_prompt_chars.py`](tests/test_count_prompt_chars.py): 경계값 및 줄바꿈 정규화 회귀 테스트

## 검증

- Codex 공식 `skill-creator` validator 통과: `Skill is valid!`
- 복도 원테이크, 30초 제품 광고, 화이트 모델 R2V, 15초 Seedance 2.0 Fast 시나리오로 포워드 테스트
- 기존 Seedance 2.0 스킬과 독립적으로 설치하며, 명시적 2.0 Fast만 이 스킬의 커스텀 프로필로 처리

Seedance 2.0 Fast의 15초·3,500자 목표·4,000자 하드 리밋은 이 저장소의 커스텀 제작 프로필이며 공식 사양으로 제시하지 않습니다.

## Seedance 2.5 주요 공식 출처

- [Seedance 2.5](https://dreamina.capcut.com/seedance/seedance-2-5)
- [Seedance 2.5 vs Seedance 2.0](https://dreamina.capcut.com/seedance/seedance-2-5-vs-seedance-2-0)
- [Seedance 2.5 Motion Reference Guide](https://dreamina.capcut.com/seedance/seedance-2-5-motion-reference-guide)
- [Seedance 2.5 Prompt Guide](https://dreamina.capcut.com/seedance/seedance-2-5-prompt)

## 커뮤니티 참고 자료

- [Anil-matcha/awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — 간결한 프롬프트 순서, 타임코드 샷 스크립트, 멀티모달 태그 관례, 카메라 용어를 교차검사했습니다. README에는 MIT로 표시되어 있으나 검토 당시 독립 라이선스 파일은 확인되지 않아 예제 전체를 복사하지 않고 패턴만 재서술했습니다.
- [고정 커밋 분석 문서](references/community-api-prompts-analysis.md) — 채택한 원칙, 제외한 제3자 API 주장, 기존 2.5/Fast 구조와의 대응표를 기록합니다.

기능 제공 여부와 한도는 Dreamina의 현재 UI, 계정, 지역, 베타 상태를 우선합니다.

## License

[MIT](LICENSE)
