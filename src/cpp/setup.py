from distutils.core import setup, Extension

module = Extension('fast_parser', sources=['fast_parser.cpp'])

setup(
    name='fast_parser',
    version='1.0',
    description='Fast log parser for SIEM tool',
    ext_modules=[module]
)
