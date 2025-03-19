import threading
import requests

class download_thread(threading.Thread):
    def download(self,url,callback_world_count):
        print(f"Thread: {threading.get_ident()} downloading {url}")
        response = requests.get(url)
        response.encoding = 'utf-8'
        callback_world_count(url,response.text) # callback


    def start_download(self,url,callback_world_count):
        thread = threading.Thread(target=self.download,args=(url,callback_world_count))
        thread.start()


def world_count(url,result):

    print(f"{url}:{len(result)} -> {result[:5]}")


def main():
    download = download_thread()
    
    download.start_download("http://127.0.0.1:8000/C2_3/novel1.txt",world_count)
    download.start_download("http://127.0.0.1:8000/C2_3/novel2.txt",world_count)
    download.start_download("http://127.0.0.1:8000/C2_3/novel3.txt",world_count)