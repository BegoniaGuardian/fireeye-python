# coding: utf-8

"""
    Detection On Demand

    FireEye offers a best-in-class virtual execution engine in many of its core products, including our Network Security, Email Security, and File Analysis solutions. Now our customers can interact with and consume those capabilities directly via a scalable and performant web service. Use the new RESTful API to submit files for malware analysis, search hash values for past analysis results, get full reports for your file submissions, and integrate into your existing toolsets and workflows.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: developers@fireeye.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import feye_detection
from feye_detection.api.reports_api import ReportsApi  # noqa: E501
from feye_detection.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = feye_detection.api.reports_api.ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_report(self):
        """Test case for get_report

        Get single report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
