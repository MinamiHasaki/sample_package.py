import setuptools

with open("README.md", "r") as ld:
    long_description = ld.read()

setuptools.setup(
    name="samplepackage.py",
    version="0.0.1",
    author="MinamiHasaki",
    author_email="MinamiHasaki620@Gmail.com",
    description="A sample package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinamiHasaki/samplepackage.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.0',
)
