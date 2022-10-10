import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiopaystack",
    version="1.0.0",
    author="IchingaSamuel",
    author_email="ichingasamuel@gmail.com",
    description="Asynchronous PayStack library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ichinga-Samuel/aiopaystack",
    project_urls={
        "Bug Tracker": "https://github.com/Ichinga-Samuel/aiopaystack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['httpx'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)
