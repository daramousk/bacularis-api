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
from swagger_client.api.volumes_api import VolumesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVolumesApi(unittest.TestCase):
    """VolumesApi unit test stubs"""

    def setUp(self):
        self.api = VolumesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_volumes_get(self):
        """Test case for api_v2_volumes_get

        Volume list  # noqa: E501
        """
        pass

    def test_api_v2_volumes_label_barcodes_get(self):
        """Test case for api_v2_volumes_label_barcodes_get

        Get label barcodes volume output  # noqa: E501
        """
        pass

    def test_api_v2_volumes_label_barcodes_post(self):
        """Test case for api_v2_volumes_label_barcodes_post

        Label volume using barcodes  # noqa: E501
        """
        pass

    def test_api_v2_volumes_label_get(self):
        """Test case for api_v2_volumes_label_get

        Get label volume output  # noqa: E501
        """
        pass

    def test_api_v2_volumes_label_post(self):
        """Test case for api_v2_volumes_label_post

        Label volume  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_delete(self):
        """Test case for api_v2_volumes_mediaid_delete

        Delete volume by MediaId  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_get(self):
        """Test case for api_v2_volumes_mediaid_get

        Find volume by MediaId  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_jobs_get(self):
        """Test case for api_v2_volumes_mediaid_jobs_get

        Jobs on volume  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_prune_put(self):
        """Test case for api_v2_volumes_mediaid_prune_put

        Prune volume  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_purge_put(self):
        """Test case for api_v2_volumes_mediaid_purge_put

        Purge volume  # noqa: E501
        """
        pass

    def test_api_v2_volumes_mediaid_put(self):
        """Test case for api_v2_volumes_mediaid_put

        Update volume properties  # noqa: E501
        """
        pass

    def test_api_v2_volumes_required_jobid_fileid_get(self):
        """Test case for api_v2_volumes_required_jobid_fileid_get

        Get volumes required to restore file  # noqa: E501
        """
        pass

    def test_api_v2_volumes_update_barcodes_get(self):
        """Test case for api_v2_volumes_update_barcodes_get

        Get update slots output using barcodes  # noqa: E501
        """
        pass

    def test_api_v2_volumes_update_barcodes_put(self):
        """Test case for api_v2_volumes_update_barcodes_put

        Update slots using barcodes  # noqa: E501
        """
        pass

    def test_api_v2_volumes_update_get(self):
        """Test case for api_v2_volumes_update_get

        Get update slots output  # noqa: E501
        """
        pass

    def test_api_v2_volumes_update_put(self):
        """Test case for api_v2_volumes_update_put

        Update slots  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
