#!/usr/bin/env python3

from pwn import *

{bindings}

### debug / info / warn / error
### cf) default option == info
context.log_level='info'
context.binary = {bin_name}

def slog(name, addr):
    return success(": ".join([name, hex(addr)]))


def conn():
    ### [*] Local Environment
    p = process([{bin_name}.path])
    
    ### [*] Docker Environment
    # p = remote("localhost", 13337)
    
    ### [*] Wargame Server Environment
    ### [*] "WARGAME_HOST" and "PORT" are variable.
    # p = remote("WARGAME_HOST", PORT)
    
    ### [+] GDB (Optional)
    # gdb.attach(p)

    return p


def main():
    p = conn()
    
    # good luck pwning :)
    
    p.interactive()


if __name__ == "__main__":
    main()
