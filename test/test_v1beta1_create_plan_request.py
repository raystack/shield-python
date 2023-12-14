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

from frontier_api.models.v1beta1_create_plan_request import V1beta1CreatePlanRequest

class TestV1beta1CreatePlanRequest(unittest.TestCase):
    """V1beta1CreatePlanRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1CreatePlanRequest:
        """Test V1beta1CreatePlanRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1CreatePlanRequest`
        """
        model = V1beta1CreatePlanRequest()
        if include_optional:
            return V1beta1CreatePlanRequest(
                body = frontier_api.models.v1beta1_plan_request_body.v1beta1PlanRequestBody(
                    name = '', 
                    title = '', 
                    description = '', 
                    features = [
                        frontier_api.models.v1beta1_feature.v1beta1Feature(
                            id = '', 
                            name = '', 
                            title = '', 
                            description = '', 
                            plan_ids = [
                                ''
                                ], 
                            state = '', 
                            prices = [
                                frontier_api.models.v1beta1_price.v1beta1Price(
                                    id = '', 
                                    feature_id = '', 
                                    provider_id = '', 
                                    name = '', 
                                    interval = '', 
                                    usage_type = '', 
                                    billing_scheme = '', 
                                    state = '', 
                                    currency = '', 
                                    amount = '', 
                                    metered_aggregate = '', 
                                    tier_mode = '', 
                                    metadata = frontier_api.models.metadata.metadata(), 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            credit_amount = '', 
                            metadata = frontier_api.models.metadata.metadata(), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    interval = '', 
                    metadata = frontier_api.models.metadata.metadata(), )
            )
        else:
            return V1beta1CreatePlanRequest(
        )
        """

    def testV1beta1CreatePlanRequest(self):
        """Test V1beta1CreatePlanRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
