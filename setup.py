from setuptools import setup, find_packages

setup(
    name="PythonProject",
    version="0.1.0",
    packages=find_packages(include=["pythonproject", "pythonproject.*"]),
    package_data={
        "pythonproject": ["sprites/*.png"],
    },
    include_package_data=True,
    install_requires=[
        "pygame~=2.6.1",
        "setuptools~=80.3.1",
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