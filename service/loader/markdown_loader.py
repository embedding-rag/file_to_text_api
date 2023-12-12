# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : markdown_loader.py
# Time       ：2023/8/18 10:54
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
def process_markdown(file_path: str) -> str:
    """
    从给定的Markdown文件中读取内容并返回。

    Args:
        file_path (str): Markdown文件的路径。

    Returns:
        str: 读取到的Markdown内容，如果读取失败则返回空字符串。
    """
    try:
        with open(file_path, "r") as file:
            markdown_content = file.read()
            return markdown_content
    except Exception as e:
        print(f"An error occurred while reading the Markdown file: {str(e)}")
        return ""
