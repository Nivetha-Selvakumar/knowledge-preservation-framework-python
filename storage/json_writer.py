import json
import os


class JsonWriter:

    def __init__(self):

        self.base_path = "storage/data"

        os.makedirs(self.base_path, exist_ok=True)

    def write(self, filename, data):

        file_path = os.path.join(self.base_path, filename)

        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

        return file_path
