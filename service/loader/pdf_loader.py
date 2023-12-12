# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : pdf_loader.py
# Time       ：2023/8/18 08:54
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
from pdfminer.high_level import extract_text


def process_pdf(file_path: str) -> str:
    """
    从给定的PDF文件中提取文本。

    Args:
        file_path (str): PDF文件的路径。

    Returns:
        str: 提取到的文本，如果提取失败则返回空字符串。
    """
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"An error occurred while extracting text from PDF: {str(e)}")
        return None
