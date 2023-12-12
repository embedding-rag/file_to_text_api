import os
import sys
import uuid
from typing import Optional

import requests

class FileDownloader:
    def __init__(self) -> None:
        self.sys_info: str = self.get_system_info()

    @staticmethod
    def get_system_info() -> str:
        """返回系统信息字符串"""
        print("系统信息:", sys.platform)
        return sys.platform

    def get_download_directory(self) -> str:
        """返回下载目录路径"""
        directory: str = (
            "./tmp/download_files"
            if self.sys_info == "win32"
            else "/tmp/download_files"
        )
        print("下载目录:", directory)
        return directory

    def create_download_directory(self) -> None:
        """根据系统信息创建下载目录"""
        os.makedirs(self.get_download_directory(), exist_ok=True)

    def download_file(self, url: str) -> Optional[str]:
        self.create_download_directory()  # 调用创建目录的方法

        try:
            response = requests.get(url)
            response.raise_for_status()  # 如果下载失败，会抛出异常

            original_filename: str = os.path.basename(url)  # 获取原始文件名
            ext: str = os.path.splitext(original_filename)[1]  # 获取原始文件的扩展名

            new_filename: str = str(uuid.uuid4()) + ext  # 使用新的UUID和扩展名生成文件名

            # 构建文件路径
            download_path: str = os.path.join(
                self.get_download_directory(), new_filename
            )

            with open(download_path, "wb") as file:
                file.write(response.content)  # 将下载的内容写入文件

            print("文件下载成功！")
            print("文件名:", new_filename)
            print("下载到了:", download_path)

            return download_path  # 返回保存文件的路径
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"文件下载失败: {e}")
            return None

    def delete_file(self, file_path: str) -> bool:
        """删除本地文件，并返回删除结果"""
        try:
            os.remove(file_path)
            print(f"文件删除成功: {file_path}")
            return True
        except FileNotFoundError:
            print(f"文件不存在: {file_path}")
            return False
        except Exception as e:
            print(f"文件删除失败: {e}")
            return False

    def clear_download_directory(self) -> None:
        """清空下载目录中的所有内容"""
        try:
            for filename in os.listdir(self.get_download_directory()):
                file_path = os.path.join(self.get_download_directory(), filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            print("下载目录已清空。")
        except Exception as e:
            print(f"清空下载目录失败: {e}")



# 示例用法
# file_downloader = FileDownloader()
# url_to_download: str = "https://example.com/sample.pdf"
# downloaded_file_path: Optional[str] = file_downloader.download_file(url_to_download)

# 外部逻辑处理完文件后，调用删除文件的方法
# if downloaded_file_path:
#     file_downloader.delete_file(downloaded_file_path)

# 清空下载目录
# file_downloader.clear_download_directory()
