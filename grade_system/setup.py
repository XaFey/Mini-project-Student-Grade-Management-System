from setuptools import setup, find_packages

setup(
    name = "grade_system",
    version= "0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires =["typer"],
    entry_points={
        "console_scripts": [
            "grade-system = grade_system.cli:app",
        ],
    },
    author = "Xa'Nah Greene",
    author_email="xanah.greene@students.cau.edu",
    description = "Student Grade Management System",

    )