from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="sempretestando-triksm", 
    version="0.0.1",
    author="TRIKSM",
    author_email="tariktasima@gmail.com",
    description="Um pacote simples para processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown", # [cite: 87]
    url="https://github.com/triksm/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8', # [cite: 87]
)