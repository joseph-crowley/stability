# models/image_model.py
import io
import warnings
from PIL import Image
from utils import StabilityAPI
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

class ImageModel:
    def __init__(self):
        self.stability_api = StabilityAPI()

    def generate_and_save_images(self, prompt, **kwargs):
        answers = self.stability_api.generate_images(prompt, **kwargs)
        if answers is None:
            return

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    img.save(str(artifact.seed) + ".png")

