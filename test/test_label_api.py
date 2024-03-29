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
from swagger_client.api.label_api import LabelApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLabelApi(unittest.TestCase):
    """LabelApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.label_api.LabelApi()  # noqa: E501

    def tearDown(self):
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


if __name__ == '__main__':
    unittest.main()
