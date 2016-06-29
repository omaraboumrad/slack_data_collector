import json
import os
import unittest

from slackcollector import collector


class TestCollector(unittest.TestCase):

    def test_anonymize_data_success(self):
        """
        Test whether the data anonymizer works by removing sensitive
        JSON objects
        """
        test_json_file = os.path.join(os.path.dirname(__file__),
                                      '_test_data/sensitive_json.json')

        with open(test_json_file) as data_file:
            json_data = json.load(data_file)

        clean_json_data = collector.anonymize(json_data)
        sensitive_keys_set = set(['profile', 'real_name', 'name'])

        for item in clean_json_data['members']:
            # If the intersection of the "sensitive_keys_set" and keys sets is
            # empty the we have cleared these keys and their values
            self.assertFalse(sensitive_keys_set.intersection(set(item.keys())))

if __name__ == '__main__':
    unittest.main()
