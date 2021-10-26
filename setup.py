import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='py_area_codes',
    version='0.1.1',
    description='Lightweight package to simplify dealing with area codes',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/jbirdvegas/py_area_codes',
    author='Jon Stanford',
    author_email='jbirdvegas@gmail.com',
    license='Creative Commons',
    packages=find_packages(exclude=("tests",)),
    install_requires=["phonenumbers"],
    include_package_data=True,
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
