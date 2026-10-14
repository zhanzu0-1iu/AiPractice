#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File    : 2-匹配多个字符.py
@Author  : 刘展佐 (zhanzu0_1iu@outlook.com)
@Time    : 2026/9/28 下午2:50
@Desc    : 
"""

# 匹配多个字符示例
import re

ret = re.match('.', "aaaaa")  # 匹配任意单个字符
print(ret.group())
