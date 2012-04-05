from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='g24.base',
      version=version,
      description="plone integration package for g24.at",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='Johannes Raggam',
      author_email='johannes@raggam.co.at',
      url='http://github.com/g24at/g24.base',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['g24',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Plone',
          'Pillow',
          'g24.elements',
          'g24.theme',
          'plone.app.event[dexterity]',
          'collective.embedly',
          'jarn.xmpp.core',
          'jarn.xmpp.collaboration',
      ],
)
