from setuptools import setup

setup(
   name='UsbDevices',
   version='1.0.0',
   description='parking module',
   author='pysashapy',
   author_email='sasha.2000ibr@gmail.com',
   packages=['UsbDevices'],
   install_requires=open('requirements.txt', 'r').read().split(),
)
