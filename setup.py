import setuptools


setuptools.setup(
    name='weather',
    version='0.1',
    author='Lorenzo Bunino',
    author_email="bunino.lorenzo@gmail.com",
    description="B2B automation for music stores",
    long_description_content_type="text/markdown",
    url="https://github.com/lorenzobunino/weather",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'weather = weather.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas>=1.2.0'],
    python_requires='>=3.6'
)
