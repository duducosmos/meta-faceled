import sys
from setuptools import setup

setup(
        name="FaceLed",
        version="1.0",
        packages=["faceledapp"],
        package_data={"":["model/*"]},
        author="Eduardo S. Pereira",
        author_email="pereira.somoza@gmail.com",
        description="Liga led ao reconhecer face",
        license="MIT",
        keywords= "opencv",
        url="",
        entry_points = {"console_scripts":["faceled = faceledapp.main:main"]},
        )
