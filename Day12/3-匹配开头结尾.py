#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File    : 3-匹配开头结尾.py
@Author  : 刘展佐 (zhanzu0_1iu@outlook.com)
@Time    : 2026/9/28 下午3:05
@Desc    : 
"""
#匹配开头结尾
import re

# ^ 匹配开头，$ 匹配结尾
# 用 ^ 和 $ 确保整个字符串都是合法邮箱，而非部分匹配
email_pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'

test_emails = [
    "zhanzu0_1iu@outlook.com",
    "hello123@qq.com",
    "test@163.com",
    "invalid-email",
    "@outlook.com",
    "user@.com",
]

for email in test_emails:
    if re.match(email_pattern, email):
        print(f"✓ 匹配成功: {email}")
    else:
        print(f"✗ 匹配失败: {email}")


