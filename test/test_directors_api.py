# coding: utf-8

"""
    Bacularis API

    This is the Bacularis API documentation.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: marcin.haba@bacula.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.directors_api import DirectorsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDirectorsApi(unittest.TestCase):
    """DirectorsApi unit test stubs"""

    def setUp(self):
        self.api = DirectorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_directors_director_name_status_get(self):
        """Test case for api_v2_directors_director_name_status_get

        Get director status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
