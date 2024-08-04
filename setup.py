from setuptools import find_packages, setup

with open("README.md", "r+") as f:
    readme = f.read()

setup(
    name="jx3api",
    version="2024.08.04",
    description="The Python SDK to the JX3API",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="JX3API",
    url="https://www.jx3api.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=["aiohttp"],
)
