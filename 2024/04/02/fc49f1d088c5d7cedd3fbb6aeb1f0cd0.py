import base64
import requests

url = 'https://alist.xxlgenius.com/dav/file2222222.txt'
file_path = 'file.txt'
username = 'sharexupload'
password = '69LxkmawqE3gZv'
credentials = f'{username}:{password}'
base64_credentials = base64.b64encode(credentials.encode()).decode()

with open(file_path, 'rb') as file:
    headers = {'Authorization': f'Basic {base64_credentials}'}
    response = requests.put(url, data=file, headers=headers)

print("Request Headers:")
print(response.request.headers)  # 检查请求头是否正确
print("\nRequest Body:")
print(response.request.body)  # 检查请求体是否正确

print(response.status_code)  # 检查上传是否成功
