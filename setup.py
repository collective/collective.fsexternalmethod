from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='collective.fsexternalmethod',
      version=version,
      description='A small shim that allows external methods to be present in skin layers.',
      long_description=open(os.path.join('README.md')).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='cmf externalmethod',
      author='Matthew Wilkes',
      author_email='matthew@matthewwilkes.co.uk',
      url='',
      license='GPL',
      package_dir = {'':'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFCore',
          'Products.ExternalMethod',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
