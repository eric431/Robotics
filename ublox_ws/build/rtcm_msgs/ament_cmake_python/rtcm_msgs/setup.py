from setuptools import find_packages
from setuptools import setup

setup(
    name='rtcm_msgs',
    version='1.1.0',
    packages=find_packages(
        include=('rtcm_msgs', 'rtcm_msgs.*')),
)
