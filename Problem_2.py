import requests
import os
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def add_catalog(self, file_path: str):
      files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
      headers = self.get_header()
      res_files_link = requests.put(f'{files_url}?path={file_path}',headers=headers)
    #   pprint (res_files_link.status_code)
    # #   return res_files_link.json()
    
    def get_header(self):
        return {
            'Content-type': 'application/json',
            'Authorization':'OAuth {}'.format(self.token)
        }
    
    def get_upload_link (self, file_path):
      upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
      headers = self.get_header()  
      self.add_catalog(file_path)
      file_path_file = file_path + 'file_test.txt'
      params = {'path':file_path_file, 'overwrite':'True'}  
      res_upload_link = requests.get(upload_url,headers=headers,params=params)
      pprint (res_upload_link.json())
      return res_upload_link.json()
        
    
    def upload(self, file_path: str):
      files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
      headers = self.get_header()
      href = self.get_upload_link(file_path=file_path).get("href","")
      response = requests.put(href,data=open('file_test.txt','rb'))
      pprint (response)
      """Метод загружает файлы по списку file_list на яндекс диск"""
                
    
        
    def get_files_list(self):
      files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
      headers = self.get_header()
      res_files_link = requests.get(files_url,headers=headers)
      return res_files_link.json()
        

if __name__ == '__main__':
    os.chdir (r"Z:\2021-09-23_PYTHON\http.requests")
    var_input_path = input ('Введите каталог, куда нужно скопировать файлы:')
    path_to_file = var_input_path + '/'
    print(path_to_file)
    with open ('token.txt', encoding='utf-8') as file_token:
       token = file_token.read()
    uploader = YaUploader(token)
    # pprint(uploader.get_files_list()) 
    # uploader.add_catalog(path_to_file)
    res1 = uploader.upload(path_to_file)
    pprint (res1)