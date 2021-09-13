from setuptools import setup, find_packages

setup(
    name='pysmarthome-yeelight',
    description='Yeelight plugin for pysmarthome',
    version='1.1.1',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome~=3.0',
        'yeelight',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome-yeelight',
    zip_zafe=False,
)
