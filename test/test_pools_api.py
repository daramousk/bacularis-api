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
from swagger_client.api.pools_api import PoolsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPoolsApi(unittest.TestCase):
    """PoolsApi unit test stubs"""

    def setUp(self):
        self.api = PoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_pools_get(self):
        """Test case for api_v2_pools_get

        Pool list  # noqa: E501
        """
        pass

    def test_api_v2_pools_poolid_get(self):
        """Test case for api_v2_pools_poolid_get

        Find pool by PoolId  # noqa: E501
        """
        pass

    def test_api_v2_pools_poolid_show_get(self):
        """Test case for api_v2_pools_poolid_show_get

        Show pool  # noqa: E501
        """
        pass

    def test_api_v2_pools_poolid_update_put(self):
        """Test case for api_v2_pools_poolid_update_put

        Update pool properties  # noqa: E501
        """
        pass

    def test_api_v2_pools_poolid_update_volumes_put(self):
        """Test case for api_v2_pools_poolid_update_volumes_put

        Update properties all volumes in pool  # noqa: E501
        """
        pass

    def test_api_v2_pools_poolid_volumes_get(self):
        """Test case for api_v2_pools_poolid_volumes_get

        Get all volumes in pool  # noqa: E501
        """
        pass

    def test_api_v2_pools_show_get(self):
        """Test case for api_v2_pools_show_get

        Show pools  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
