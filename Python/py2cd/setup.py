__author__ = 'Mark Weinreuter'

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='py2cd',
      version='0.1',
      description='Wrapper for pygame to provide a simple drawing and gaming framework in German. This project is develop for the use in the CoderDojo Karlsruhe.',
      url='http://github.com/coderdojoka/Materialien/Python/py2cd',
      author='CoderDojo Karlsruhe, Mark Weinreuter',
      packages=['py2cd'],
      install_requires=[
          'pygame'
      ],
      test_suite="tests",
      zip_safe=False)
