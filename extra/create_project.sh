#!/bin/bash

## Define the project name
#PROJECT_NAME="project_name"
#
## Create the main project directory
#mkdir $PROJECT_NAME
#
## Navigate to the project directory
#cd $PROJECT_NAME

# Create the source, tests, configs, and assets directories
mkdir -p src/models src/utils tests configs assets

# Create the necessary Python files
touch src/__init__.py src/models/__init__.py src/models/language_model.py src/models/image_model.py \
      src/utils/__init__.py src/utils/stability_api.py \
      src/setup_logging.py src/main.py \
      tests/__init__.py tests/test_models.py \
      configs/config.py \
      setup.py requirements.txt

# Print a message indicating that the project structure has been created
echo "Project structure for $PROJECT_NAME has been created successfully!"


