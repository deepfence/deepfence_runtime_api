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
from deepfence_runtime_api.api.node_control_api import NodeControlApi  # noqa: E501
from deepfence_runtime_api.rest import ApiException


class TestNodeControlApi(unittest.TestCase):
    """NodeControlApi unit test stubs"""

    def setUp(self):
        self.api = deepfence_runtime_api.api.node_control_api.NodeControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_node_details(self):
        """Test case for node_details

        Node Details API  # noqa: E501
        """
        pass

    def test_packet_capture_status(self):
        """Test case for packet_capture_status

        Node Control API - Packet Capture Status  # noqa: E501
        """
        pass

    def test_pause_node(self):
        """Test case for pause_node

        Node Control API - Pause Node  # noqa: E501
        """
        pass

    def test_restart_node(self):
        """Test case for restart_node

        Node Control API - Restart Node  # noqa: E501
        """
        pass

    def test_scale_down(self):
        """Test case for scale_down

        Node Control API - Scale Down  # noqa: E501
        """
        pass

    def test_scale_up(self):
        """Test case for scale_up

        Node Control API - Scale Up  # noqa: E501
        """
        pass

    def test_start_node(self):
        """Test case for start_node

        Node Control API - Start Node  # noqa: E501
        """
        pass

    def test_start_packet_capture(self):
        """Test case for start_packet_capture

        Node Control - Start Packet Capture  # noqa: E501
        """
        pass

    def test_stop_node(self):
        """Test case for stop_node

        Node Control API - Stop Node  # noqa: E501
        """
        pass

    def test_stop_packet_capture(self):
        """Test case for stop_packet_capture

        Node Control API - Stop Packet Capture  # noqa: E501
        """
        pass

    def test_unpause_node(self):
        """Test case for unpause_node

        Node Control API - Unpause Node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
