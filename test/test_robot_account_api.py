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
from swagger_client.api.robot_account_api import RobotAccountApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRobotAccountApi(unittest.TestCase):
    """RobotAccountApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.robot_account_api.RobotAccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_project_id_robots_get(self):
        """Test case for projects_project_id_robots_get

        Get all robot accounts of specified project  # noqa: E501
        """
        pass

    def test_projects_project_id_robots_post(self):
        """Test case for projects_project_id_robots_post

        Create a robot account for project  # noqa: E501
        """
        pass

    def test_projects_project_id_robots_robot_id_delete(self):
        """Test case for projects_project_id_robots_robot_id_delete

        Delete the specified robot account  # noqa: E501
        """
        pass

    def test_projects_project_id_robots_robot_id_get(self):
        """Test case for projects_project_id_robots_robot_id_get

        Return the infor of the specified robot account.  # noqa: E501
        """
        pass

    def test_projects_project_id_robots_robot_id_put(self):
        """Test case for projects_project_id_robots_robot_id_put

        Update status of robot account.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
