from setuptools import setup, find_packages

setup(
   name='UsbDevices',
   version='1.1.1a',
   description='parking module',
   author='pysashapy',
   author_email='sasha.2000ibr@gmail.com',
   packages=find_packages(),
   install_requires=open('requirements.txt', 'r').read().split(),
)
