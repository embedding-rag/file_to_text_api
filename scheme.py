from typing import Optional
from pydantic import BaseModel

class ConvertRequest(BaseModel):
    """用于推理请求的 Pydantic 模型"""
    file_url: str

class DataResponse(BaseModel):
    """用于 API 响应中的 data 字段的 Pydantic 模型"""
    file_url: str
    text: Optional[str] = None

class APIJsonResponse(BaseModel):
    """API 响应的 Pydantic 模型"""
    code: int = 0
    message: str = "success"
    data: Optional[DataResponse] = None
