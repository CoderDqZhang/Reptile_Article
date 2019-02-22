#!/usr/bin/env python
# -*- coding:utf-8 -*-     
# constants for chinese_to_arabic

def is_number(s):
    try:
        float(s)
        s.isdigit()
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        int(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
