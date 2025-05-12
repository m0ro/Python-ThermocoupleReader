from setuptools import setup, find_packages

setup(
    name='thermocouple-reader',
    version='0.1.1',
    description='Read temperatures from a 4-channel thermocouple module via serial.',
    author='steffen-w, moro',
    packages=find_packages(),
    install_requires=[
        'pyserial',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
