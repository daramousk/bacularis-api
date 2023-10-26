# coding: utf-8

"""
    Bacularis API

    This is the Bacularis API documentation.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: marcin.haba@bacula.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "bacularis-api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Bacularis API",
    author_email="marcin.haba@bacula.pl",
    url="",
    keywords=["Swagger", "Bacularis API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Bacularis API documentation.  # noqa: E501
    """
)