# tests/test_models.py
from models import ImageModel

def test_image_generation():
    image_model = ImageModel()
    # assuming a valid prompt
    prompt = "A serene landscape with a calm lake under a clear blue sky"
    assert image_model.generate_and_save_images(prompt) is not None

