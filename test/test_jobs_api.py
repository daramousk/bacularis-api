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
from swagger_client.api.jobs_api import JobsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_jobs_estimate_get(self):
        """Test case for api_v2_jobs_estimate_get

        Get estimate output  # noqa: E501
        """
        pass

    def test_api_v2_jobs_estimate_post(self):
        """Test case for api_v2_jobs_estimate_post

        Estimate job bytes and files  # noqa: E501
        """
        pass

    def test_api_v2_jobs_files_get(self):
        """Test case for api_v2_jobs_files_get

        Search jobs by file criteria  # noqa: E501
        """
        pass

    def test_api_v2_jobs_get(self):
        """Test case for api_v2_jobs_get

        Job list  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_bandwidth_put(self):
        """Test case for api_v2_jobs_jobid_bandwidth_put

        Set Job bandwidth limit  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_cancel_put(self):
        """Test case for api_v2_jobs_jobid_cancel_put

        Cancel job  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_delete(self):
        """Test case for api_v2_jobs_jobid_delete

        Delete job  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_files_get(self):
        """Test case for api_v2_jobs_jobid_files_get

        Show job files and directories  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_get(self):
        """Test case for api_v2_jobs_jobid_get

        Find job by JobId  # noqa: E501
        """
        pass

    def test_api_v2_jobs_jobid_show_get(self):
        """Test case for api_v2_jobs_jobid_show_get

        Show job  # noqa: E501
        """
        pass

    def test_api_v2_jobs_recent_jobname_get(self):
        """Test case for api_v2_jobs_recent_jobname_get

        Get most recent jobids for job to restore  # noqa: E501
        """
        pass

    def test_api_v2_jobs_resnames_get(self):
        """Test case for api_v2_jobs_resnames_get

        Job resource names  # noqa: E501
        """
        pass

    def test_api_v2_jobs_restore_post(self):
        """Test case for api_v2_jobs_restore_post

        Restore job  # noqa: E501
        """
        pass

    def test_api_v2_jobs_run_post(self):
        """Test case for api_v2_jobs_run_post

        Run job  # noqa: E501
        """
        pass

    def test_api_v2_jobs_show_get(self):
        """Test case for api_v2_jobs_show_get

        Show jobs  # noqa: E501
        """
        pass

    def test_api_v2_jobs_totals_get(self):
        """Test case for api_v2_jobs_totals_get

        Show job total bytes and files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
