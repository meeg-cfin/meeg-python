# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same
try:
    from setuptools import setup
    scripts = []
except ImportError:
    from distutils.core import setup

setup(name='meeg',
      version='0.1',
      description='Utilities for meeg-cfin',
      long_description=open('README.md').read(),
      author='Chris Bailey',
      author_email='cjb@cfin.au.dk',
      license='BSD',
      url='https://github.com/meeg-cfin/meeg-python',
      packages=['meeg'],
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: BSD License'])
