# This is the setup.py file
import setuptools  # Core module to define and install Python packages

# Load README content for long project description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Basic project metadata
__version__ = "0.0.0"
REPO_NAME = "Customer-Churn-Classification-Deep-Learning-Project"  # GitHub repo name
AUTHOR_USER_NAME = "Tiwari666"  # Your GitHub username
SRC_REPO = "dlChurn"            # Actual Python package name inside src/
AUTHOR_EMAIL = "narendra76052@gmail.com"  # Your contact email

# Setup function to register the package
setuptools.setup(
    name=SRC_REPO,  # Package name
    version=__version__,  # Initial version
    author=AUTHOR_USER_NAME,  # Author name
    author_email=AUTHOR_EMAIL,  # Author email
    description="A small Python package for a deep learning churn prediction app",  # Short description
    long_description=long_description,  # Full description from README.md
    long_description_content="text/markdown",  # Format of long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Project homepage
    project_urls={  # Optional additional links
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Root folder for packages is 'src'
    packages=setuptools.find_packages(where="src"),  # Find all packages inside src/
    install_requires=[],  # Use requirements.txt for dependencies
)


