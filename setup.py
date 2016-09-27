"""Mission Pinball Framework Media Controller (mpf-mc) setup.py"""

import re

from setuptools import setup

import sys
# import re
#
# from os import environ
# from os.path import join, dirname, exists, isdir
# from distutils.version import LooseVersion
# from setuptools import setup, Extension
#
platform = sys.platform
#
#
# def ver_equal(self, other):
#     return self.version == other
#
# LooseVersion.__eq__ = ver_equal
#
# # Detect 32/64bit for OSX (http://stackoverflow.com/a/1405971/798575)
# if sys.platform == 'darwin':
#     if sys.maxsize > 2 ** 32:
#         osx_arch = 'x86_64'
#     else:
#         osx_arch = 'i386'

# Get the version number of mpfmonitor and the required version of MPF by
# reading the file directly. We can't import it because that would import mpf
# and # break the setup. Details here:
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
version_file = "mpfmonitor/_version.py"
version_file_content = open(version_file, "rt").read()
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(version_re, version_file_content, re.M)
if mo:
    mon_version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in %s." % (version_file,))

# This section pulls the MPF required version from the mpf-mc version file so
# we can write that as a requirement below
mpf_version_re = r"^__mpf_version_required__ = ['\"]([^'\"]*)['\"]"
mo = re.search(mpf_version_re, version_file_content, re.M)
if mo:
    mpf_version = mo.group(1)
else:
    raise RuntimeError("Unable to find MPF version string in %s." % (
        version_file,))

install_requires = ['ruamel.yaml>=0.10,<0.11',
                    'mpf>={}'.format(mpf_version),
                    ]

if platform == 'win32':
    install_requires += ['pypiwin32',
                         'kivy.deps.sdl2',
                         'kivy.deps.sdl2_dev',
                         'kivy.deps.glew',
                         'kivy',
                         ]

setup(

    name='mpf-monitor',
    version=mon_version,
    description='MPF Monitor',
    long_description='''GUI Monitoring & Troubleshooting app for the Mission
Pinball Framework.

MPF Monitor is built on Kivy.''',

    url='https://missionpinball.org',
    author='The Mission Pinball Framework Team',
    author_email='brian@missionpinball.org',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Artistic Software',
        'Topic :: Games/Entertainment :: Arcade'
    ],

    keywords='pinball',

    include_package_data=True,

    package_data={},

    packages=['mpfmonitor'],

    zip_safe=False,

    install_requires=install_requires,

    tests_require=[],

    entry_points="""
    [mpf.command]
    monitor=mpfmonitor.commands.monitor:get_command
    """,
)