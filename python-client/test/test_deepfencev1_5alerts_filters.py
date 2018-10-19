# coding: utf-8

"""
    Deepfence Runtime API v1.5

    Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container, kubernetes and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider, container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.  # noqa: E501

    OpenAPI spec version: 1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import deepfence_runtime_api
from deepfence_runtime_api.models.deepfencev1_5alerts_filters import Deepfencev15alertsFilters  # noqa: E501
from deepfence_runtime_api.rest import ApiException


class TestDeepfencev15alertsFilters(unittest.TestCase):
    """Deepfencev15alertsFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeepfencev15alertsFilters(self):
        """Test Deepfencev15alertsFilters"""
        # FIXME: construct object with mandatory attributes with example values
        # model = deepfence_runtime_api.models.deepfencev1_5alerts_filters.Deepfencev15alertsFilters()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
