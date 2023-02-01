from setuptools import setup, find_packages

setup(
   name='UsbDevices',
   version='1.3.0',
   description='parking module',
   author='pysashapy',
   author_email='sasha.2000ibr@gmail.com',
   packages=find_packages(),
   install_requires=open('requirements.txt', 'r').read().split(),
   entry_points={
      'console_scripts': [
         'smartsale = UsbDevices.POSTerminals.SmartSale:install',
      ]
   }
)
