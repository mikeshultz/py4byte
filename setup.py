import sys
import shutil
import py4byte

from pathlib import Path
from setuptools import Command, setup, find_packages
from subprocess import check_call, CalledProcessError

this_dir = Path(__file__).parent.absolute()

# Get the long description from the README file
with this_dir.joinpath('README.md').open(encoding='utf-8') as f:
    long_description = f.read()


def requirements_to_list(filename):
    return [dep for dep in this_dir.joinpath(filename).open().read().split('\n') if (
        dep and not dep.startswith('#')
    )]


setup(
    name='py4byte',
    version=py4byte.__version__,
    description='Python library that leverages the 4byte.directory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikeshultz/py4byte',
    author=py4byte.__author__,
    author_email=py4byte.__email__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='ethereum blockchain topic function event signature 4byte',
    packages=find_packages(exclude=['docs', 'build']),
    install_requires=requirements_to_list('requirements.txt'),
    # entry_points={
    #     'console_scripts': [
    #         'py4byte=py4byte.cli:main',
    #     ],
    # },
    package_data={
        '': [
            'README.md',
        ],
    }
)