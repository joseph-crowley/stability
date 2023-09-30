# src/main.py
from models import ImageModel, LanguageModel
from setup_logging import setup_logging

def main():
    setup_logging()

    # Image Model Usage
    image_model = ImageModel()
    image_prompt = "A beautiful sunset over the ocean"
    image_model.generate_and_save_images(image_prompt)

    # Language Model Usage (hypothetical)
    language_model = LanguageModel()
    text_prompt = "Describe a peaceful countryside."
    language_model.generate_text(text_prompt)

if __name__ == "__main__":
    main()

