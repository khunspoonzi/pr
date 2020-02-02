# -------------------------------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------------------------------

import setuptools


# -------------------------------------------------------------------------------------
# README
# -------------------------------------------------------------------------------------

with open("README.md") as f:
    README = f.read()


# -------------------------------------------------------------------------------------
# SETUP
# -------------------------------------------------------------------------------------

setuptools.setup(
    author="Khun Spoonzi",
    author_email="khunspoonzi@gmail.com",
    name="pr",
    license="MIT",
    description="A high-level shorthand print formatter for Python 3 or above",
    version="v0.1.0",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/khunspoonzi/pr",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
)
