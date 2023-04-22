from setuptools import find_packages, setup

setup(
    name="lab1",
    packages=find_packages(exclude=["lab1_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
