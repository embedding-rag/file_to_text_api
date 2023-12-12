import os
from enum import Enum

import filetype


class FileType(Enum):
    PDF = "pdf"
    WORD = "word"
    EXCEL = "excel"
    PPT = "ppt"
    HTML = "html"
    MARKDOWN = "markdown"
    TEXT = "text"
    CSV = "csv"


# 检测文件类型mimetype
def detect_file_type(file_path: str) -> FileType:
    kind = filetype.guess_mime(file_path)
    ext = filetype.guess_extension(file_path)
    print("current file type, kind:", kind)
    print("current file type, ext:", ext)

    # 如果是 pdf, word, excel, ppt, html, markdown, text 就对应合理返回缩写，否则就返回 None
    if kind == "application/pdf":
        return FileType.PDF
    elif (
        kind == "application/msword"
        or kind
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ):
        return FileType.WORD
    elif kind == "application/vnd.ms-excel":
        return FileType.EXCEL
    elif kind == "application/vnd.ms-powerpoint":
        return FileType.PPT
    elif kind == "text/html":
        return FileType.HTML
    elif kind == "text/markdown":
        return FileType.MARKDOWN
    elif kind == "text/plain":
        return FileType.TEXT
    elif ext == ".csv" or os.path.splitext(file_path)[1] == ".csv":
        # 如果文件扩展名是 .csv，调用 process_csv
        return FileType.CSV
    else:
        return None
