from setuptools import setup, find_packages

setup(
    name="chunkelize",
    version="0.1.0",
    description="Facilita updates em chunk para vários ORMs",
    author="Christian Silva",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "django": [
            "django~=3.0"
        ],
        "sqlalchemy": [
            "sqlalchemy>=1.3,<3.0"
        ],
        "dev": [
            "pytest~=7.0",
            "Faker~=14.0",
            "pytest-django~=4.0",
            "factory-boy~=3.0",
            "pytest-cov~=4.0"
        ]
    },
    python_requires=">=3.6,<3.13",
)
