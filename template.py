import os  # For OS-level file operations
from pathlib import Path  # For path handling
import logging  # For logging steps

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')  # Logging format

project_name = "dlChurn"  # Project folder name

list_of_files = [  # All required files to initialize the project
    ".github/workflows/.gitignore",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config.yaml",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:  # Loop through each file
    filepath = Path(filepath)  # Convert to Path object
    file_dir, file_name = os.path.split(filepath)  # Get folder and file name

    if file_dir != "":  # If folder path exists
        os.makedirs(file_dir, exist_ok=True)  # Create folder if needed
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")  # Log folder creation

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # Create if file doesn't exist or is empty
        with open(filepath, "w") as f:  # Create file
            content = f"# This is the {file_name} file\n" if str(filepath).endswith(".py") else ""
            f.write(content)
        logging.info(f"Creating empty file: {filepath}")  # Log file creation
    else:
        logging.info(f"File already exists: {filepath}")  # Log if file already there

# Final log
logging.info("Project template setup completed.")

# End of file creation script
# This script initializes a project structure by creating necessary directories and files.
# It ensures that all required files are present, creating empty files if they do not exist.
# The script uses logging to provide feedback on the creation process.
