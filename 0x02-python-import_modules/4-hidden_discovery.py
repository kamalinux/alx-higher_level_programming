#!/usr/bin/python3
# Author: @kamalinux

if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)
