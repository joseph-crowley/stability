# src/models/language_model.py
from utils import StabilityAPI

class LanguageModel:
    def __init__(self):
        self.stability_api = StabilityAPI()

    def generate_text(self, prompt, **kwargs):
        try:
            answers = self.stability_api.generate_text(prompt, **kwargs)
            return answers
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None

