from setuptools import setup, find_packages

setup(
    name="PythonProject",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List dependencies here
        # e.g., "requests>=2.25.1",
    ],
    author="Kiss Máté",
    author_email="kiss.mate.4@stud.u-szeged.hu",
    url="https://github.com/KissMate04/PythonProject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)