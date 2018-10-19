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
from deepfence_runtime_api.api.compliance_api import ComplianceApi  # noqa: E501
from deepfence_runtime_api.rest import ApiException


class TestComplianceApi(unittest.TestCase):
    """ComplianceApi unit test stubs"""

    def setUp(self):
        self.api = deepfence_runtime_api.api.compliance_api.ComplianceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_applicable_compliance_scans(self):
        """Test case for applicable_compliance_scans

        Compliance API - Get Applicable Compliance Scans  # noqa: E501
        """
        pass

    def test_check_compliance_scan_status(self):
        """Test case for check_compliance_scan_status

        Compliance API - Check Compliance Scan Status  # noqa: E501
        """
        pass

    def test_find_compliance_scan_results(self):
        """Test case for find_compliance_scan_results

        Compliance API - Get/Delete Compliance Scan Results with filters  # noqa: E501
        """
        pass

    def test_start_compliance_scan(self):
        """Test case for start_compliance_scan

        Compliance API - Start Compliance Scan  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
