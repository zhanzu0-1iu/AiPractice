#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File    : 1-匹配单个字符.py
@Author  : 刘展佐 (zhanzu0_1iu@outlook.com)
@Time    : 2026/9/28 下午2:26
@Desc    : 
"""

# 匹配单个字符示例
import re
result = re.match("wangdao", "wangdao.cn")
print(result.group())
ret = re.match('.', "aaaaa")  # 匹配任意单个字符
print(ret.group())

# 匹配邮箱示例
email_pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'

test_emails = [
    "zhanzu0_1iu@outlook.com",   # 合法邮箱
    "hello123@qq.com",            # 合法邮箱
    "test@163.com",               # 合法邮箱
    "invalid-email",              # 无 @ 符号
    "@outlook.com",               # 缺少用户名
    "user@.com",                  # 缺少域名
]

for email in test_emails:
    result = re.match(email_pattern, email)
    if result:
        print(f"✓ 匹配成功: {email}")
    else:
        print(f"✗ 匹配失败: {email}")

