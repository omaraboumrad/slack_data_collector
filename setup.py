from setuptools import setup

setup(
    name='slack_collector',
    version='0.0.1',
    description='Slack Data Collector',
    url='http://mena-devs.com',
    author='Bassem Dghaidi',
    author_email='bassem@interop.link',
    license='MIT',
    packages=['slackcollector'],
    install_requires=[
        'six',
        'requests',
        'pyslack',
    ],
    zip_safe=False,
)
