from setuptools import setup, find_packages
from sys import platform


requires = open('requirements.txt', 'r').read().split('\n')
if platform.lower().find('linux') != -1:
    requires.append('evdev==1.6.1')


setup(
    name='UsbDevices',
    version='1.5.0a14',
    description='parking module',
    author='pysashapy',
    author_email='sasha.2000ibr@gmail.com',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'smartsale = UsbDevices.POSTerminals.SmartSale:install',
        ]
    },
    dependency_links=[
        'git+https://github.com/pysashapy/python-escpos.git@a1park_master'
    ]
)
