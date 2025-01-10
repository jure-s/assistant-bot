from setuptools import setup, find_packages

setup(
    name="personal_assistant",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Personal Assistant Bot for managing contacts and notes",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "assistant-bot=personal_assistant.main:main",
        ],
    },
    python_requires=">=3.8",
)