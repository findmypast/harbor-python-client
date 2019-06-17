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
from swagger_client.api.products_api import ProductsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.products_api.ProductsApi()  # noqa: E501

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

    def test_configurations_get(self):
        """Test case for configurations_get

        Get system configurations.  # noqa: E501
        """
        pass

    def test_configurations_put(self):
        """Test case for configurations_put

        Modify system configurations.  # noqa: E501
        """
        pass

    def test_configurations_reset_post(self):
        """Test case for configurations_reset_post

        Reset system configurations.  # noqa: E501
        """
        pass

    def test_email_ping_post(self):
        """Test case for email_ping_post

        Test connection and authentication with email server.  # noqa: E501
        """
        pass

    def test_health_get(self):
        """Test case for health_get

        Health check API  # noqa: E501
        """
        pass

    def test_internal_syncregistry_post(self):
        """Test case for internal_syncregistry_post

        Sync repositories from registry to DB.  # noqa: E501
        """
        pass

    def test_jobs_replication_get(self):
        """Test case for jobs_replication_get

        List filters jobs according to the policy and repository  # noqa: E501
        """
        pass

    def test_jobs_replication_id_delete(self):
        """Test case for jobs_replication_id_delete

        Delete specific ID job.  # noqa: E501
        """
        pass

    def test_jobs_replication_id_log_get(self):
        """Test case for jobs_replication_id_log_get

        Get job logs.  # noqa: E501
        """
        pass

    def test_jobs_replication_put(self):
        """Test case for jobs_replication_put

        Update status of jobs. Only stop is supported for now.  # noqa: E501
        """
        pass

    def test_jobs_scan_id_log_get(self):
        """Test case for jobs_scan_id_log_get

        Get job logs.  # noqa: E501
        """
        pass

    def test_labels_get(self):
        """Test case for labels_get

        List labels according to the query strings.  # noqa: E501
        """
        pass

    def test_labels_id_delete(self):
        """Test case for labels_id_delete

        Delete the label specified by ID.  # noqa: E501
        """
        pass

    def test_labels_id_get(self):
        """Test case for labels_id_get

        Get the label specified by ID.  # noqa: E501
        """
        pass

    def test_labels_id_put(self):
        """Test case for labels_id_put

        Update the label properties.  # noqa: E501
        """
        pass

    def test_labels_id_resources_get(self):
        """Test case for labels_id_resources_get

        Get the resources that the label is referenced by.  # noqa: E501
        """
        pass

    def test_labels_post(self):
        """Test case for labels_post

        Post creates a label  # noqa: E501
        """
        pass

    def test_ldap_groups_search_get(self):
        """Test case for ldap_groups_search_get

        Search available ldap groups.  # noqa: E501
        """
        pass

    def test_ldap_ping_post(self):
        """Test case for ldap_ping_post

        Ping available ldap service.  # noqa: E501
        """
        pass

    def test_ldap_users_import_post(self):
        """Test case for ldap_users_import_post

        Import selected available ldap users.  # noqa: E501
        """
        pass

    def test_ldap_users_search_get(self):
        """Test case for ldap_users_search_get

        Search available ldap users.  # noqa: E501
        """
        pass

    def test_logs_get(self):
        """Test case for logs_get

        Get recent logs of the projects which the user is a member of  # noqa: E501
        """
        pass

    def test_policies_replication_get(self):
        """Test case for policies_replication_get

        List filters policies by name and project_id  # noqa: E501
        """
        pass

    def test_policies_replication_id_delete(self):
        """Test case for policies_replication_id_delete

        Delete the replication policy specified by ID.  # noqa: E501
        """
        pass

    def test_policies_replication_id_get(self):
        """Test case for policies_replication_id_get

        Get replication policy.  # noqa: E501
        """
        pass

    def test_policies_replication_id_put(self):
        """Test case for policies_replication_id_put

        Put modifies name, description, target and enablement of policy.  # noqa: E501
        """
        pass

    def test_policies_replication_post(self):
        """Test case for policies_replication_post

        Post creates a policy  # noqa: E501
        """
        pass

    def test_projects_get(self):
        """Test case for projects_get

        List projects  # noqa: E501
        """
        pass

    def test_projects_head(self):
        """Test case for projects_head

        Check if the project name user provided already exists.  # noqa: E501
        """
        pass

    def test_projects_post(self):
        """Test case for projects_post

        Create a new project.  # noqa: E501
        """
        pass

    def test_projects_project_id_delete(self):
        """Test case for projects_project_id_delete

        Delete project by projectID  # noqa: E501
        """
        pass

    def test_projects_project_id_get(self):
        """Test case for projects_project_id_get

        Return specific project detail infomation  # noqa: E501
        """
        pass

    def test_projects_project_id_logs_get(self):
        """Test case for projects_project_id_logs_get

        Get access logs accompany with a relevant project.  # noqa: E501
        """
        pass

    def test_projects_project_id_members_get(self):
        """Test case for projects_project_id_members_get

        Get all project member information  # noqa: E501
        """
        pass

    def test_projects_project_id_members_mid_delete(self):
        """Test case for projects_project_id_members_mid_delete

        Delete project member  # noqa: E501
        """
        pass

    def test_projects_project_id_members_mid_get(self):
        """Test case for projects_project_id_members_mid_get

        Get the project member information  # noqa: E501
        """
        pass

    def test_projects_project_id_members_mid_put(self):
        """Test case for projects_project_id_members_mid_put

        Update project member  # noqa: E501
        """
        pass

    def test_projects_project_id_members_post(self):
        """Test case for projects_project_id_members_post

        Create project member  # noqa: E501
        """
        pass

    def test_projects_project_id_metadatas_get(self):
        """Test case for projects_project_id_metadatas_get

        Get project metadata.  # noqa: E501
        """
        pass

    def test_projects_project_id_metadatas_meta_name_delete(self):
        """Test case for projects_project_id_metadatas_meta_name_delete

        Delete metadata of a project  # noqa: E501
        """
        pass

    def test_projects_project_id_metadatas_meta_name_get(self):
        """Test case for projects_project_id_metadatas_meta_name_get

        Get project metadata  # noqa: E501
        """
        pass

    def test_projects_project_id_metadatas_meta_name_put(self):
        """Test case for projects_project_id_metadatas_meta_name_put

        Update metadata of a project.  # noqa: E501
        """
        pass

    def test_projects_project_id_metadatas_post(self):
        """Test case for projects_project_id_metadatas_post

        Add metadata for the project.  # noqa: E501
        """
        pass

    def test_projects_project_id_put(self):
        """Test case for projects_project_id_put

        Update properties for a selected project.  # noqa: E501
        """
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

    def test_replications_post(self):
        """Test case for replications_post

        Trigger the replication according to the specified policy.  # noqa: E501
        """
        pass

    def test_repositories_get(self):
        """Test case for repositories_get

        Get repositories accompany with relevant project and repo name.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_delete(self):
        """Test case for repositories_repo_name_delete

        Delete a repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_labels_get(self):
        """Test case for repositories_repo_name_labels_get

        Get labels of a repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_labels_label_id_delete(self):
        """Test case for repositories_repo_name_labels_label_id_delete

        Delete label from the repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_labels_post(self):
        """Test case for repositories_repo_name_labels_post

        Add a label to the repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_put(self):
        """Test case for repositories_repo_name_put

        Update description of the repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_signatures_get(self):
        """Test case for repositories_repo_name_signatures_get

        Get signature information of a repository  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_get(self):
        """Test case for repositories_repo_name_tags_get

        Get tags of a relevant repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_post(self):
        """Test case for repositories_repo_name_tags_post

        Retag an image  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_delete(self):
        """Test case for repositories_repo_name_tags_tag_delete

        Delete a tag in a repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_get(self):
        """Test case for repositories_repo_name_tags_tag_get

        Get the tag of the repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_labels_get(self):
        """Test case for repositories_repo_name_tags_tag_labels_get

        Get labels of an image.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_labels_label_id_delete(self):
        """Test case for repositories_repo_name_tags_tag_labels_label_id_delete

        Delete label from the image.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_labels_post(self):
        """Test case for repositories_repo_name_tags_tag_labels_post

        Add a label to image.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_manifest_get(self):
        """Test case for repositories_repo_name_tags_tag_manifest_get

        Get manifests of a relevant repository.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_scan_post(self):
        """Test case for repositories_repo_name_tags_tag_scan_post

        Scan the image.  # noqa: E501
        """
        pass

    def test_repositories_repo_name_tags_tag_vulnerability_details_get(self):
        """Test case for repositories_repo_name_tags_tag_vulnerability_details_get

        Get vulnerability details of the image.  # noqa: E501
        """
        pass

    def test_repositories_scan_all_post(self):
        """Test case for repositories_scan_all_post

        Scan all images of the registry.  # noqa: E501
        """
        pass

    def test_repositories_top_get(self):
        """Test case for repositories_top_get

        Get public repositories which are accessed most.  # noqa: E501
        """
        pass

    def test_search_get(self):
        """Test case for search_get

        Search for projects, repositories and helm charts  # noqa: E501
        """
        pass

    def test_statistics_get(self):
        """Test case for statistics_get

        Get projects number and repositories number relevant to the user  # noqa: E501
        """
        pass

    def test_system_gc_get(self):
        """Test case for system_gc_get

        Get gc results.  # noqa: E501
        """
        pass

    def test_system_gc_id_get(self):
        """Test case for system_gc_id_get

        Get gc status.  # noqa: E501
        """
        pass

    def test_system_gc_id_log_get(self):
        """Test case for system_gc_id_log_get

        Get gc job log.  # noqa: E501
        """
        pass

    def test_system_gc_schedule_get(self):
        """Test case for system_gc_schedule_get

        Get gc's schedule.  # noqa: E501
        """
        pass

    def test_system_gc_schedule_post(self):
        """Test case for system_gc_schedule_post

        Create a gc schedule.  # noqa: E501
        """
        pass

    def test_system_gc_schedule_put(self):
        """Test case for system_gc_schedule_put

        Update gc's schedule.  # noqa: E501
        """
        pass

    def test_systeminfo_get(self):
        """Test case for systeminfo_get

        Get general system info  # noqa: E501
        """
        pass

    def test_systeminfo_getcert_get(self):
        """Test case for systeminfo_getcert_get

        Get default root certificate.  # noqa: E501
        """
        pass

    def test_systeminfo_volumes_get(self):
        """Test case for systeminfo_volumes_get

        Get system volume info (total/free size).  # noqa: E501
        """
        pass

    def test_targets_get(self):
        """Test case for targets_get

        List filters targets by name.  # noqa: E501
        """
        pass

    def test_targets_id_delete(self):
        """Test case for targets_id_delete

        Delete specific replication's target.  # noqa: E501
        """
        pass

    def test_targets_id_get(self):
        """Test case for targets_id_get

        Get replication's target.  # noqa: E501
        """
        pass

    def test_targets_id_policies_get(self):
        """Test case for targets_id_policies_get

        List the target relevant policies.  # noqa: E501
        """
        pass

    def test_targets_id_put(self):
        """Test case for targets_id_put

        Update replication's target.  # noqa: E501
        """
        pass

    def test_targets_ping_post(self):
        """Test case for targets_ping_post

        Ping validates target.  # noqa: E501
        """
        pass

    def test_targets_post(self):
        """Test case for targets_post

        Create a new replication target.  # noqa: E501
        """
        pass

    def test_usergroups_get(self):
        """Test case for usergroups_get

        Get all user groups information  # noqa: E501
        """
        pass

    def test_usergroups_group_id_delete(self):
        """Test case for usergroups_group_id_delete

        Delete user group  # noqa: E501
        """
        pass

    def test_usergroups_group_id_get(self):
        """Test case for usergroups_group_id_get

        Get user group information  # noqa: E501
        """
        pass

    def test_usergroups_group_id_put(self):
        """Test case for usergroups_group_id_put

        Update group information  # noqa: E501
        """
        pass

    def test_usergroups_post(self):
        """Test case for usergroups_post

        Create user group  # noqa: E501
        """
        pass

    def test_users_current_get(self):
        """Test case for users_current_get

        Get current user info.  # noqa: E501
        """
        pass

    def test_users_current_permissions_get(self):
        """Test case for users_current_permissions_get

        Get current user permissions.  # noqa: E501
        """
        pass

    def test_users_get(self):
        """Test case for users_get

        Get registered users of Harbor.  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Creates a new user account.  # noqa: E501
        """
        pass

    def test_users_user_id_delete(self):
        """Test case for users_user_id_delete

        Mark a registered user as be removed.  # noqa: E501
        """
        pass

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Get a user's profile.  # noqa: E501
        """
        pass

    def test_users_user_id_password_put(self):
        """Test case for users_user_id_password_put

        Change the password on a user that already exists.  # noqa: E501
        """
        pass

    def test_users_user_id_put(self):
        """Test case for users_user_id_put

        Update a registered user to change his profile.  # noqa: E501
        """
        pass

    def test_users_user_id_sysadmin_put(self):
        """Test case for users_user_id_sysadmin_put

        Update a registered user to change to be an administrator of Harbor.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
