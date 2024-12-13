import requests

class SkolverketAPI:
    BASE_URL = "https://api.skolverket.se/syllabus/v1/"

    def __init__(self):
        pass

    def get_subjects(self):
        """Hämta en lista över alla ämnen."""
        endpoint = "subjects"
        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching subjects: {e}")
            return None

