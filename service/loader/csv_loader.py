# !/usr/bin/env python
# -*-coding:utf-8 -*-
# File       : csv_loader.py
# Time       ：2023/8/18 09:59
# Author     ：feiandxs
# version    ：python 3.10.10
# Description：
import csv


def process_csv(file_path: str) -> str:
    """
    从给定的 CSV 文件中读取数据并将其拼接成一个字符串返回。

    Args:
        file_path (str): CSV 文件的路径。

    Returns:
        str: 拼接后的字符串，如果读取失败则返回空字符串。
    """
    try:
        data = []
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)

        # 将数据拼接成字符串
        merged_text = ""
        for row in data:
            merged_text += ",".join(row) + "\n"

        return merged_text
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")
        return ""
