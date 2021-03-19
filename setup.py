from distutils.core import setup
setup(
  name = 'OMDriver',
  packages = ['OMDriver'], # this must be the same as the name above
  version = '1.3',
  description = 'Simplify3x Object Picker Data Retrieval',
  author = 'Simplify3x',
  author_email = 'simplifyom@simplify3x.com',
  keywords = ['string', 'reverse'],
  url='https://github.com/Simplify3x/OMDriver',
  classifiers = [],
  install_requires=['requests']
)