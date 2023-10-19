# kidney_classifier

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?
### steps:

clone the Repository

```bash
https://github.com/VijayRamaRaju98/kidney_classifier
```

### create a conda environment after opening the repository

```bash
conda create -n NAME python=3.8 -y
```

```bash
conda activate NAME
```

### Install the requirements

```bash
pip install -r requirements.txt
```




import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "kidney_classifier"
AUTHOR_USER_NAME = "VijayRamaraju98"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "uppalapativijay98@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)