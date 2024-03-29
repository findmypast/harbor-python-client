# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.chart_repository_api import ChartRepositoryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestChartRepositoryApi(unittest.TestCase):
    """ChartRepositoryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.chart_repository_api.ChartRepositoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chartrepo_charts_post(self):
        """Test case for chartrepo_charts_post

        Upload a chart file to the defult 'library' project.  # noqa: E501
        """
        pass

    def test_chartrepo_health_get(self):
        """Test case for chartrepo_health_get

        Check the health of chart repository service.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_get(self):
        """Test case for chartrepo_repo_charts_get

        Get all the charts under the specified project  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_delete(self):
        """Test case for chartrepo_repo_charts_name_delete

        Delete all the versions of the specified chart  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_get(self):
        """Test case for chartrepo_repo_charts_name_get

        Get all the versions of the specified chart  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_delete(self):
        """Test case for chartrepo_repo_charts_name_version_delete

        Delete the specified chart version  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_get(self):
        """Test case for chartrepo_repo_charts_name_version_get

        Get the specified chart version  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_labels_get(self):
        """Test case for chartrepo_repo_charts_name_version_labels_get

        Return the attahced labels of chart.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_labels_id_delete(self):
        """Test case for chartrepo_repo_charts_name_version_labels_id_delete

        Remove label from chart.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_name_version_labels_post(self):
        """Test case for chartrepo_repo_charts_name_version_labels_post

        Mark label to chart.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_charts_post(self):
        """Test case for chartrepo_repo_charts_post

        Upload a chart file to the specified project.  # noqa: E501
        """
        pass

    def test_chartrepo_repo_prov_post(self):
        """Test case for chartrepo_repo_prov_post

        Upload a provance file to the specified project.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
