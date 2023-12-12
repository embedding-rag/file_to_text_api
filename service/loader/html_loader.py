# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : html_loader.py
# Time       ：2023/8/18 10:17
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
import re

from bs4 import BeautifulSoup


def remove_html_tags(html):
    # 创建 BeautifulSoup 对象并指定解析器
    soup = BeautifulSoup(html, "html.parser")

    # 移除所有的标签
    text = soup.get_text()

    return text


def limit_newlines(text):
    # 将连续的换行符限制为最多两个
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def process_html(file_path: str) -> str:
    """
    从给定的HTML文件中读取内容并返回。

    Args:
        file_path (str): HTML文件的路径。

    Returns:
        str: 读取到的HTML内容，如果读取失败则返回空字符串。
    """
    try:
        with open(file_path, "r") as file:
            html_content = file.read()
            res = remove_html_tags(html_content)
            res = limit_newlines(res)
            return res
    except Exception as e:
        print(f"An error occurred while reading the HTML file: {str(e)}")
        return ""
