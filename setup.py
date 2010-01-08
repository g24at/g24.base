__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='thet.grak.base',
      version=version,
      description="plone integration package for gruene akademie graz website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='Johannes Raggam',
      author_email='johannes@raggam.co.at',
      url='http://github.com/thet/thet.grak.base',
      license='GPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['thet', 'thet.grak'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.dancing',
          'z3c.unconfigure',
          'collective.portlet.flickr',
          # 'Products.slideshowfolder',
          # 'collective.gallery',
          # 'Products.pipbox',
          # 'collective.plonetruegallery[all]',
          # 'p4a.plonecalendar',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
