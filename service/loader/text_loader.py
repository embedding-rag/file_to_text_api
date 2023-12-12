# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : text_loader.py
# Time       ：2023/8/18 11:02
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
def process_text(file_path: str) -> str:
    """
    从给定的文本文件中读取内容并返回。

    Args:
        file_path (str): 文本文件的路径。

    Returns:
        str: 读取到的文本内容，如果读取失败则返回空字符串。
    """
    try:
        with open(file_path, "r") as file:
            text = file.read()
            return text
    except Exception as e:
        print(f"An error occurred while reading the text file: {str(e)}")
        return ""
