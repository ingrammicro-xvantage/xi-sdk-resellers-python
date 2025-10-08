# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
with open('README.md', 'r') as f:
    DESCRIPTION = f.read()



NAME = "xi.sdk.resellers"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

CLASSIFIERS = [
    
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',  # Adjusted for developers interested in trying out the beta version
]


setup(
    name=NAME,
    version="1.3.0",
    description="Ingram Micro - Xvantage Integration (XI) Python Server-side SDK.",
    author="Ingram Micro Xvantage Integration(XI)",
    author_email="xi_support@ingrammicro.com",
    url="https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python",
    keywords=["xvantage", "ingrammicro", "resellerapi","xvantage integration"],
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=DESCRIPTION,
    package_data={"xi.sdk.resellers": ["py.typed", "docs/*"]},
    license='MIT',
    project_urls={
        'GitHub Repo': 'https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python',
        'Download': 'https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/archive/1.3.0.tar.gz',
        'Release Notes': 'https://github.com/ingrammicro-xvantage/xi-sdk-resellers-python/releases/',
    },
)
