from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code-generation-system",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A powerful code generation system for Laravel and Vue.js",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/code-generation-system",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Jinja2>=2.11.3,<3.0.0",
        "PyYAML>=5.4.1,<6.0.0",
        "click>=7.1.2,<8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "code-gen=code_generation_system.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "code_generation_system": ["templates/*"],
    },
)