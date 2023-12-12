# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : word_loader.py
# Time       ：2023/8/18 09:10
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
from docx import Document


def process_word(file_path: str) -> str:
    """
    从给定的DOCX文件中提取文本。

    Args:
        file_path (str): DOCX文件的路径。

    Returns:
        str: 提取到的文本，如果提取失败则返回空字符串。
    """
    try:
        print("file_path:", file_path)
        document = Document(file_path)
        text = ""
        for p in document.paragraphs:
            print(p.text)
            text += p.text + "\n"
        print("text:", text)
        return text
    except Exception as e:
        print(f"An error occurred while extracting text from DOCX: {str(e)}")
        return None
