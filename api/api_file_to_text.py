from fastapi import APIRouter
from scheme import APIJsonResponse, DataResponse, ConvertRequest
from utils.file_type_check import detect_file_type, FileType
from utils.file_download import FileDownloader


from service.loader.csv_loader import process_csv
from service.loader.excel_loader import process_excel
from service.loader.html_loader import process_html
from service.loader.markdown_loader import process_markdown
from service.loader.pdf_loader import process_pdf
from service.loader.text_loader import process_text
from service.loader.word_loader import process_word

from typing import Optional

router = APIRouter()


@router.post(
    path="/",
    summary="文件提取文本",
    response_model=APIJsonResponse,
)
async def handle_inference(request: ConvertRequest):

    file_downloader = FileDownloader()

    url_to_download: str = request.file_url

    downloaded_file_path: Optional[str] = file_downloader.download_file(url_to_download)
    print("downloaded_file_path:", downloaded_file_path)
    if not downloaded_file_path:
        return APIJsonResponse(code=-1, message="文件下载失败", data=None)

    file_type = detect_file_type(downloaded_file_path)
    if not file_type:
        return APIJsonResponse(code=-1, message="文件类型不支持", data=None)

    print("file_type:", file_type)

    result = None  # Initialize with a default value

    # 根据文件类型执行相应的处理函数
    if file_type == FileType.PDF:
        print("File type is pdf")
        result = process_pdf(downloaded_file_path)
    elif file_type == FileType.WORD:
        print("File type is word")
        result = process_word(downloaded_file_path)
    elif file_type == "excel":
        print("File type is excel")
        result = process_excel(downloaded_file_path)
    elif file_type == "ppt":
        response = APIJsonResponse()
        response.code = -1
        response.message = "不支持的文件类型"
        return response
    elif file_type == "csv":
        print("File type is csv")
        result = process_csv(downloaded_file_path)
    elif file_type == "html":
        print("File type is html")
        result = process_html(downloaded_file_path)
    elif file_type == "markdown":
        print("File type is markdown")
        result = process_markdown(downloaded_file_path)
    elif file_type == "text":
        print("File type is text")
        result = process_text(downloaded_file_path)

    print("result:", result)

    # remove download files
    file_downloader.delete_file(downloaded_file_path)
    response = APIJsonResponse()
    if result is None:
        response.code = -1
        response.message = "文件处理失败"
        return response
    else:
        response.code = 0
        response.message = "success"
        response.data = DataResponse(file_url=request.file_url, text=result)
        return response
