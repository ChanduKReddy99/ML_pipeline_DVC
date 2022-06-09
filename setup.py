from setuptools import setup

with open("README.md", "r", encoding= "utf-8") as fh:
    long_description = fh.read()

setup(
    name="src",
    version="0.0.2",    
    author="ChanduKReddy99",
    author_email="chanduk.amical@gmail.com",
    description="A smaall dvc ml pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChanduKReddy99/ML_pipeline_DVC",
    license="GNU",
    packages=["src"],
    python_requirement=">=3.6",
    install_requires=[
        "dvc",
        "dvc[gdrive]",
        "dvc[s3]",
        "pandas",
        "scikit-learn",

    ]

)