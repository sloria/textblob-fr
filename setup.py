import sys
import subprocess
import re
from setuptools import setup

packages = ['textblob_fr']
requires = ["textblob>=0.8.0"]

def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("textblob_fr/__init__.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='textblob-fr',
    version=__version__,
    description='French language support for TextBlob.',
    long_description=(read("README.rst") + '\n\n' +
                        read("HISTORY.rst")),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/textblob-fr',
    packages=packages,
    package_dir={'textblob_fr': 'textblob_fr'},
    include_package_data=True,
    package_data={
        "textblob_fr": ["*.txt", "*.xml"]
    },
    install_requires=requires,
    license=read("LICENSE"),
    zip_safe=False,
    keywords='textblob_fr',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=['nose'],
)
