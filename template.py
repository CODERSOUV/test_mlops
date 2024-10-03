import os

from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",  # Added .py extension
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]


def create_files():
    for file_path in list_of_files:
        # Convert the string path to a Path object
        file = Path(file_path)
        
        # Create the parent directories if they do not exist
        if not file.parent.exists():
            file.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the file if it does not exist
        if not file.exists():
            file.touch()
            print(f"Created: {file}")
        else:
            print(f"Already exists: {file}")



create_files()