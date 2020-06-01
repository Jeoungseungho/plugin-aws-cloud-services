import os
import logging

from spaceone.core import config
from spaceone.tester import TestCase, print_json
from google.protobuf.json_format import MessageToDict

_LOGGER = logging.getLogger(__name__)

AKI = os.environ.get('AWS_ACCESS_KEY_ID', None)
SAK = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
ROLE_ARN = os.environ.get('ROLE_ARN', None)


if AKI == None or SAK == None:
    print("""
##################################################
# ERROR 
#
# Configure your AWS credential first for test
##################################################
example)

export AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>

""")
    exit


class TestCloudServiceAPIs(TestCase):
    config = config.load_config('./config.yml')
    endpoints = config.get('ENDPOINTS', {})
    secret_data = {
        'aws_access_key_id': AKI,
        'aws_secret_access_key': SAK,
    }

    if ROLE_ARN is not None:
        secret_data.update({
            'role_arn': ROLE_ARN
        })

    def test_verify(self):
        options = {
            'domain': 'mz.co.kr'
        }
        v_info = self.inventory.Collector.verify({'options': options, 'secret_data': self.secret_data})
        print_json(v_info)

    def test_collect(self):
        options = {}
        filter = {}

        res_stream = self.inventory.Collector.collect(
            {'options': options, 'secret_data': self.secret_data, 'filter': filter}
        )

        for res in res_stream:
            self.assertIsNotNone(res)
            # self.assertEqual('CLOUD_SERVICE', res.resource_type)
