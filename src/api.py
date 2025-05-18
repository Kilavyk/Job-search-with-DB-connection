import requests
from typing import Dict, Optional


class HeadHunterAPI:
    """Класс для взаимодействия с API hh.ru для получения данных о работодателях и вакансиях."""

    def __init__(self) -> None:
        self.base_url = "https://api.hh.ru/"
        self.headers = {"User-Agent": "HH-User-Agent"}

    def get_employer(self, employer_id: str) -> Optional[Dict]:
        """Получение данных о работодателе по его ID."""
        url = f"{self.base_url}employers/{employer_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        print(f"Получены данные о работодателе '{response.json()['name']}'.")
        return response.json() if response.status_code == 200 else None

