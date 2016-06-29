"""
Example Configuration (config.cfg): (Can be spit out by the script itself)

    [Collector]
    target = /path/to/file.json
    token = token-example-string
"""
import argparse
import io
import json

from six.moves import configparser

import slack
import slack.users


def anonymize(data):
    for item in data['members']:
        item.pop('profile', None)
        item.pop('real_name', None)
        item.pop('name', None)

    return data


def collect(token):
    slack.api_token = token
    return slack.users.list()


def save(data, target_file):
    with io.open(target_file, 'w', encoding='utf-8') as target:
        target.write(json.dumps(data,
                                ensure_ascii=False,
                                indent=4,
                                separators=(',', ': ')))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.cfg')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    data = anonymize(collect(config.get('Collector', 'token')))
    save(data, config.get('Collector', 'target'))
