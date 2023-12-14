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

from frontier_api.models.v1beta1_describe_preferences_response import V1beta1DescribePreferencesResponse

class TestV1beta1DescribePreferencesResponse(unittest.TestCase):
    """V1beta1DescribePreferencesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1DescribePreferencesResponse:
        """Test V1beta1DescribePreferencesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1DescribePreferencesResponse`
        """
        model = V1beta1DescribePreferencesResponse()
        if include_optional:
            return V1beta1DescribePreferencesResponse(
                traits = [
                    frontier_api.models.preference_trait_is_a_trait_that_can_be_used_to_add_preferences_to_a_resource
it_explains_what_preferences_are_available_for_a_resource.PreferenceTrait is a trait that can be used to add preferences to a resource
it explains what preferences are available for a resource(
                        resource_type = '', 
                        name = '', 
                        title = '', 
                        description = '', 
                        long_description = '', 
                        heading = '', 
                        sub_heading = '', 
                        breadcrumb = '', 
                        default = '', 
                        input_hints = '', 
                        text = '', 
                        textarea = '', 
                        select = '', 
                        combobox = '', 
                        checkbox = '', 
                        multiselect = '', 
                        number = '', )
                    ]
            )
        else:
            return V1beta1DescribePreferencesResponse(
        )
        """

    def testV1beta1DescribePreferencesResponse(self):
        """Test V1beta1DescribePreferencesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
