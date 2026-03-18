# system-hacking-cheatsheet

DreamHack System Hacking 공부 정리 자료

## Assembly 작동 조건

1. Ubuntu, x64 아키텍쳐

## 어셈블리어 함수 특징

1. syscall은 항상 마지막에 `rax`
2. **함수 1~3번째 인자는 순서대로 `rdi`, `rsi`, `rdx`**
    - **이 내용은 정보보안기사 기출문제이기도 함!!!!!!!**

```text
syscall:{rax}(args0:{rdi}, args1:{rsi}, args2:{rdx})
```

## Cyberchef 레시피

바로 Little Endian으로 만들어 `0x`만 앞에 넣으면 꽂아넣을 수 있는 레시피임!

```json
[
  { "op": "To Hex",
    "args": ["Space", 8] },
  { "op": "Swap endianness",
    "args": ["Hex", 8, true] },
  { "op": "From Hex",
    "args": ["Space"] },
  { "op": "To Hex",
    "args": ["None", 8] },
  { "op": "Reverse",
    "args": ["Line"] }
]
```

입력 예시

```text
/home/shell_basic/flag_name_is_loooooong
```

출력 예시

```hex
676e6f6f6f6f6f6f
6c5f73695f656d61
6e5f67616c662f63
697361625f6c6c65
68732f656d6f682f
```
