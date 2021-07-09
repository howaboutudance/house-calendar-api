import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dc-demo-fastapi", # Replace with your own username
    version="0.0.1",
    author="Micahel Penhallegon",
    author_email="mike@hematite.tech",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpenhall-celgene/dc-fast-example",
    project_urls={
        "Bug Tracker": "https://github.com/mpenhall-celgene/dc-fast-example/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)