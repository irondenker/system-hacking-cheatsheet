# how-to-setup

## vscode WSL 설정

> 목표: WSL 환경에서 Local과 동일한 개발환경 조성

1. vscode 좌측 하단 `><` 버튼 클릭
1. `connect to WSL` 클릭
1. 좌측 하단 `remote:WSL` 문구 확인(접속 성공 시도)
1. local에서 쓰던 Extension 전부 다운로드
1. 다운로드 완료 후 필요 시 vscode 재시작

## `.asm` 개발환경 설정

### WSL

> 목표: vscode에서 쾌적한 어셈블리어 작성 환경 조성

1. `pwntools` 설치

    ``` bash
    sudo apt-get update
    sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade pwntools
    ```

    - `externally-managed-environment...`오류 발생 시

        ```bash
        python3 -m pip config set global.break-system-packages true
        ```

2. `gdb` 설치

    ```bash
    sudo apt-get update
    sudo apt-get gdb
    ```

### vscode

> 목표: vscode에서 쾌적한 어셈블리어 작성 환경 조성

1. vscode Extension Marketplace 열기 (`Ctrl+X`)
1. **`ASM Code Lens`** 검색 후 다운로드
    - publisher:"maziac"
    - Github 링크: [https://github.com/maziac/asm-code-lens-issues](https://github.com/maziac/asm-code-lens-issues)
    - Marketplace 링크: [https://marketplace.visualstudio.com/items?itemName=maziac.asm-code-lens](https://marketplace.visualstudio.com/items?itemName=maziac.asm-code-lens)
1. 임의의 경로에 `file.asm` 등의 방식으로 테스트 파일 생성
1. `mov rax, 0x0` 등 어셈블리어 작성 후 문법/형식 오류 발생 여부 확인
