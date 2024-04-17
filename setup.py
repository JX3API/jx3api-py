from setuptools import find_packages, setup

setup(
    name="jx3api",
    version="20240416",
    description="The Python SDK to the JX3API",
    long_description="The Python SDK to the JX3API",
    author="JX3API",
    url="https://www.jx3api.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=["aiohttp"],
)
