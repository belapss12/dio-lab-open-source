from setuptools import setup, find_packages

setup(
    name="image_processor",
    version="1.0.0",
    description="Pacote de processamento de imagens em Python",
    author="Bela",
    author_email="bela@example.com",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
    ],
)
