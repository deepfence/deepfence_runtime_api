# coding: utf-8

"""
    Deepfence Runtime API v1.5

    Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container, kubernetes and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider, container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.  # noqa: E501

    OpenAPI spec version: 1.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Deepfencev15usersquarantineProtectionPolicyLogFilters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'list[str]',
        'alert_count_threshold': 'int',
        'alert_id': 'list[str]',
        'host_name': 'list[str]',
        'node_type': 'list[str]',
        'policy_created_by': 'list[str]',
        'severity': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'alert_count_threshold': 'alert_count_threshold',
        'alert_id': 'alert_id',
        'host_name': 'host_name',
        'node_type': 'node_type',
        'policy_created_by': 'policy_created_by',
        'severity': 'severity'
    }

    def __init__(self, action=None, alert_count_threshold=None, alert_id=None, host_name=None, node_type=None, policy_created_by=None, severity=None):  # noqa: E501
        """Deepfencev15usersquarantineProtectionPolicyLogFilters - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._alert_count_threshold = None
        self._alert_id = None
        self._host_name = None
        self._node_type = None
        self._policy_created_by = None
        self._severity = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if alert_count_threshold is not None:
            self.alert_count_threshold = alert_count_threshold
        if alert_id is not None:
            self.alert_id = alert_id
        if host_name is not None:
            self.host_name = host_name
        if node_type is not None:
            self.node_type = node_type
        if policy_created_by is not None:
            self.policy_created_by = policy_created_by
        if severity is not None:
            self.severity = severity

    @property
    def action(self):
        """Gets the action of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        What policy action was performed  # noqa: E501

        :return: The action of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        What policy action was performed  # noqa: E501

        :param action: The action of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["pause", "stop", "restart"]  # noqa: E501
        if not set(action).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `action` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(action) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._action = action

    @property
    def alert_count_threshold(self):
        """Gets the alert_count_threshold of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Policy was executed when number of alerts (threshold) was this  # noqa: E501

        :return: The alert_count_threshold of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: int
        """
        return self._alert_count_threshold

    @alert_count_threshold.setter
    def alert_count_threshold(self, alert_count_threshold):
        """Sets the alert_count_threshold of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Policy was executed when number of alerts (threshold) was this  # noqa: E501

        :param alert_count_threshold: The alert_count_threshold of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: int
        """
        if alert_count_threshold is not None and alert_count_threshold > 999999999:  # noqa: E501
            raise ValueError("Invalid value for `alert_count_threshold`, must be a value less than or equal to `999999999`")  # noqa: E501
        if alert_count_threshold is not None and alert_count_threshold < 1:  # noqa: E501
            raise ValueError("Invalid value for `alert_count_threshold`, must be a value greater than or equal to `1`")  # noqa: E501

        self._alert_count_threshold = alert_count_threshold

    @property
    def alert_id(self):
        """Gets the alert_id of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Alert id for which the policies got executed  # noqa: E501

        :return: The alert_id of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Alert id for which the policies got executed  # noqa: E501

        :param alert_id: The alert_id of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """

        self._alert_id = alert_id

    @property
    def host_name(self):
        """Gets the host_name of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Host names  # noqa: E501

        :return: The host_name of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Host names  # noqa: E501

        :param host_name: The host_name of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """

        self._host_name = host_name

    @property
    def node_type(self):
        """Gets the node_type of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Node type  # noqa: E501

        :return: The node_type of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Node type  # noqa: E501

        :param node_type: The node_type of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["host", "container"]  # noqa: E501
        if not set(node_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `node_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(node_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._node_type = node_type

    @property
    def policy_created_by(self):
        """Gets the policy_created_by of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Email address of user who created this quarantine protection policy  # noqa: E501

        :return: The policy_created_by of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._policy_created_by

    @policy_created_by.setter
    def policy_created_by(self, policy_created_by):
        """Sets the policy_created_by of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Email address of user who created this quarantine protection policy  # noqa: E501

        :param policy_created_by: The policy_created_by of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """

        self._policy_created_by = policy_created_by

    @property
    def severity(self):
        """Gets the severity of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501

        Severity set in quarantine protection policy  # noqa: E501

        :return: The severity of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Deepfencev15usersquarantineProtectionPolicyLogFilters.

        Severity set in quarantine protection policy  # noqa: E501

        :param severity: The severity of this Deepfencev15usersquarantineProtectionPolicyLogFilters.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["critical", "high", "medium", "low"]  # noqa: E501
        if not set(severity).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `severity` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(severity) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._severity = severity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Deepfencev15usersquarantineProtectionPolicyLogFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other