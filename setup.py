from setuptools import setup, find_packages

setup(
    name='condensa_frontend',
    version='0.4',
    packages=find_packages("."),
    url='https://github.com/stormymcstorm/condensa_frontend/',
    install_requires=[
        'condensa', 'flask'
    ],
    platforms='any',
)