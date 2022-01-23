from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "twine>=3", "wheel", "pip", "pandas"]

setup(
    name="schrutepy",
    version="0.1.3",
    author="Brad Lindblad",
    author_email="bradley.lindblad@gmail.com",
    description="The Entire Transcripts from the Office in Tidy Format",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/bradlindblad/schrutepy",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
