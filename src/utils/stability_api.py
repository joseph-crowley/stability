# utils/stability_api.py
import logging
from stability_sdk import client
from configs import Config

class StabilityAPI:
    def __init__(self):
        self.config = Config()
        self.stability_api = client.StabilityInference(
            key=self.config.STABILITY_KEY,
            verbose=True,
            engine="stable-diffusion-xl-1024-v1-0",
        )

    def generate_images(self, prompt, **kwargs):
        try:
            answers = self.stability_api.generate(prompt, **kwargs)
            return answers
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None

