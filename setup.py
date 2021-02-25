from setuptools import setup

setup(
    name = 'calculator_2',
    version = '0.1',
    description = 'scientific calculator in orange beacuse that is better',
    author = 'brice',
    url = '',
    license = 'MIT',
    packages = ['calculator_2.py'],
    entry_points = {'console_scripts': ['prog = calculator_2.calculator_2',],},
)