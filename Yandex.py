class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        import requests
        resp1 = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                             params={"path": file_path, "overwrite": "true"},
                             headers={"Authorization": token})
        resp1.raise_for_status()
        data = resp1.json()
        s = data["href"]
        with open(file_path, "rb") as f:
            resp2 = requests.put(s, files={"file": f})

    if __name__ == "__main__":
        uploader = YaUploader(token)
        result = uploader.upload("C:/Users/Asus/Desktop/Липецк, блоки")