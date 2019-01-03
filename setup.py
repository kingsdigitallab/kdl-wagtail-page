from distutils.core import setup

from kdl_wagtail_page import __version__

setup(
    name='kdl-wagtail-page',
    version=__version__,
    packages=['kdl_wagtail_page', ],
    license='MIT',
    description='Basic but reusable Wagtail page models for KDL projects',
    install_requires=['wagtail>=2.0'],
    description=open('README.txt').read(),
    long_description=open('README.rst').read(),
    python_requires='>3.5',
)
