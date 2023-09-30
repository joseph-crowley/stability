# Stability

This project harnesses the power of the Stability AI platform to seamlessly generate both images and text based on provided prompts, embodying a modular and extendable code structure which encourages further exploration and development in AI-driven creativity.

## Features

- Image Generation: Generate captivating images based on textual prompts.
- Text Generation: Create engaging text based on textual prompts.
- Modular Codebase: A well-organized, modular codebase that allows for easy extension and modification.
- Test Suite: A suite of tests to ensure functionality and facilitate continuous improvement.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8 or newer
- Stability SDK

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/joseph-crowley/stability.git
cd stability 
```

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Navigate to the `src` directory:

```bash
cd src
```

Run the main script:

```bash
python main.py
```

## Configuration

Configuration settings are located in `configs/config.py`. Update the `STABILITY_HOST` and `STABILITY_KEY` values with your Stability AI platform credentials.

## Testing

Navigate to the `tests` directory:

```bash
cd tests
```

Run the tests:

```bash
python -m unittest discover
```

## Contributing

Contributions are welcome! Please read the contributing guidelines to get started.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

