from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

with open("maui/_version.py") as versionfile:
    exec(versionfile.read())

setup(
    name="maui-tools",
    version=__version__,
    description="Multi-omics Autoencoder Integration",
    author="Jonathan Ronen",
    license="GPLv3",
    author_email="yablee@gmail.com",
    url="https://github.com/BIMSBbioinfo/maui",
    packages=["maui"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pytest",
        "numpy>=1.19.5",
        "pandas>=1.3.4",
        "scipy>=1.7.2",
        "scikit-learn>=1.0.1",
        "keras>=2.6.0",
        "tensorflow>2.6.2",
        "pytest>=3.6.0",
    ],
)
