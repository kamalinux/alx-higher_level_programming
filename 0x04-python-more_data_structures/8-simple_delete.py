#!/usr/bin/python3
# Author: @kamalinux

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]

    return (a_dictionary)
