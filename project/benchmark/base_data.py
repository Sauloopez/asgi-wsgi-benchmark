import json
from os import path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class __BaseFake:
    data_filename = ''

    def __init__(self) -> None:
        self.mock_json = BASE_DIR / self.data_filename
        if not self.mock_json.exists():
            raise Exception('The directory \'%s\' does not exists :('%self.mock_json)
        pass

    def get_content(self) -> list:
        return json.load(self.mock_json.open())

class FakeUsers(__BaseFake):
    data_filename = 'users_data.json'
    pass
