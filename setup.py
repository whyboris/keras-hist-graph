import setuptools

long_description = open('README.md', 'r').read()

setuptools.setup(
    author="Boris Yakubchik",
    author_email="yboris@yahoo.com",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    description="Graph Keras training history object",
    install_requires=['Keras', 'matplotlib'],
    keywords=['keras', 'jupyter'],
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="keras-hist-graph",
    packages=setuptools.find_packages(),
    url="https://github.com/whyboris/keras-hist-graph",
    version="0.0.1"
)
