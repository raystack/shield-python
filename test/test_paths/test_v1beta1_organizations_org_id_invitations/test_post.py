# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import frontier_api
from frontier_api.paths.v1beta1_organizations_org_id_invitations import post  # noqa: E501
from frontier_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1beta1OrganizationsOrgIdInvitations(ApiTestMixin, unittest.TestCase):
    """
    V1beta1OrganizationsOrgIdInvitations unit test stubs
        Invite user  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
