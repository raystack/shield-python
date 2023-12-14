# coding: utf-8

"""
    Frontier Administration API

    The Frontier APIs adhere to the OpenAPI specification, also known as Swagger, which provides a standardized approach for designing, documenting, and consuming RESTful APIs. With OpenAPI, you gain a clear understanding of the API endpoints, request/response structures, and authentication mechanisms supported by the Frontier APIs. By leveraging the OpenAPI specification, developers can easily explore and interact with the Frontier APIs using a variety of tools and libraries. The OpenAPI specification enables automatic code generation, interactive API documentation, and seamless integration with API testing frameworks, making it easier than ever to integrate Frontier into your existing applications and workflows.

    The version of the OpenAPI document: 0.2.0
    Contact: hello@raystack.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from frontier_api.models.v1beta1_list_project_service_users_response import V1beta1ListProjectServiceUsersResponse

class TestV1beta1ListProjectServiceUsersResponse(unittest.TestCase):
    """V1beta1ListProjectServiceUsersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1ListProjectServiceUsersResponse:
        """Test V1beta1ListProjectServiceUsersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1ListProjectServiceUsersResponse`
        """
        model = V1beta1ListProjectServiceUsersResponse()
        if include_optional:
            return V1beta1ListProjectServiceUsersResponse(
                serviceusers = [
                    frontier_api.models.v1beta1_service_user.v1beta1ServiceUser(
                        id = '', 
                        title = 'Order Service', 
                        metadata = frontier_api.models.metadata.metadata(), 
                        created_at = '2023-06-07T05:39:56.961Z', 
                        updated_at = '2023-06-07T05:39:56.961Z', 
                        state = '', 
                        org_id = '', )
                    ],
                role_pairs = [
                    frontier_api.models.v1beta1_list_project_service_users_response_role_pair.v1beta1ListProjectServiceUsersResponseRolePair(
                        serviceuser_id = '', 
                        roles = [
                            frontier_api.models.v1beta1_role.v1beta1Role(
                                id = '', 
                                name = '', 
                                permissions = [
                                    ''
                                    ], 
                                title = '', 
                                metadata = frontier_api.models.metadata.metadata(), 
                                created_at = '2023-06-07T05:39:56.961Z', 
                                updated_at = '2023-06-07T05:39:56.961Z', 
                                org_id = '', 
                                state = '', 
                                scopes = [
                                    ''
                                    ], )
                            ], )
                    ]
            )
        else:
            return V1beta1ListProjectServiceUsersResponse(
        )
        """

    def testV1beta1ListProjectServiceUsersResponse(self):
        """Test V1beta1ListProjectServiceUsersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
