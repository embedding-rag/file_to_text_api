# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : excel_loader.py
# Time       ：2023/8/18 09:13
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
import pandas as pd
import xlrd


def process_excel(file_path: str) -> str:
    """
    从给定的 Excel 文件中提取所有工作表的内容并将其拼接为一个完整的字符串。

    Args:
        file_path (str): Excel 文件的路径。

    Returns:
        str: 处理结果，如果处理失败则返回空字符串。
    """
    try:
        # 打开 Excel 文件
        xls = pd.ExcelFile(file_path)

        # 获取所有工作表的名称
        sheet_names = xls.sheet_names

        # 创建一个空字符串用于存储拼接后的内容
        merged_text = ""

        # 遍历每个工作表
        for sheet_name in sheet_names:
            # 读取工作表的内容
            sheet_data = pd.read_excel(xls, sheet_name=sheet_name)

            # 将工作表内容拼接到字符串中
            merged_text += str(sheet_data)

        return merged_text  # 返回拼接后的字符串
    except Exception as e:
        print(f"An error occurred while processing Excel file: {str(e)}")
        return ""
