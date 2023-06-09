from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="algeria",
    version="0.1.0",
    author="Mohammed BADI",
    author_email="badi.mohammed@univ-oran2.dz",
    description="Python library which gives you a (clé) and (rip) of a given (ccp) CCP number account, additional features may be added to the library in the future",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mouh2020/algeria",
    packages=["algeria"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
