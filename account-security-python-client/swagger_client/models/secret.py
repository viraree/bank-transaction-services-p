# coding: utf-8

"""
    bank-access-api

    This is an example of using OAuth2 Access Code Flow in a specification to describe security to your API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Secret(object):
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
        'id': 'int',
        'message': 'str',
        'public_key': 'object',
        'token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'public_key': 'publicKey',
        'token': 'token'
    }

    def __init__(self, id=None, message=None, public_key=None, token=None):  # noqa: E501
        """Secret - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._message = None
        self._public_key = None
        self._token = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if public_key is not None:
            self.public_key = public_key
        if token is not None:
            self.token = token

    @property
    def id(self):
        """Gets the id of this Secret.  # noqa: E501


        :return: The id of this Secret.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Secret.


        :param id: The id of this Secret.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this Secret.  # noqa: E501


        :return: The message of this Secret.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Secret.


        :param message: The message of this Secret.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def public_key(self):
        """Gets the public_key of this Secret.  # noqa: E501


        :return: The public_key of this Secret.  # noqa: E501
        :rtype: object
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Secret.


        :param public_key: The public_key of this Secret.  # noqa: E501
        :type: object
        """

        self._public_key = public_key

    @property
    def token(self):
        """Gets the token of this Secret.  # noqa: E501


        :return: The token of this Secret.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Secret.


        :param token: The token of this Secret.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(Secret, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
