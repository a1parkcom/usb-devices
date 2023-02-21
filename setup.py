from setuptools import setup, find_packages
from sys import platform


requires = open('requirements.txt', 'r').read().split()
if platform.lower().find('linux') != -1:
    requires.append('evdev==1.6.1')


setup(
    name='UsbDevices',
    version='1.5.0a2',
    description='parking module',
    author='pysashapy',
    author_email='sasha.2000ibr@gmail.com',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'smartsale = UsbDevices.POSTerminals.SmartSale:install',
        ]
    }
)
