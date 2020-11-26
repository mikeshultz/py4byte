import re
from pathlib import Path
from setuptools import setup, find_packages

this_dir = Path(__file__).parent.absolute()
meta_py = open('py4byte/meta.py').read()
metadata = dict(re.findall("__([a-z]+)__ = \"([^\"]+)\"", meta_py))

# Get the long description from the README file
with this_dir.joinpath('README.md').open(encoding='utf-8') as f:
    long_description = f.read()


def requirements_to_list(filename):
    return [dep for dep in this_dir.joinpath(filename).open().read().split('\n') if (
        dep and not dep.startswith('#')
    )]

setup(
    name='py4byte',
    version=metadata['version'],
    description='Python library that leverages the 4byte.directory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikeshultz/py4byte',
    author=metadata['author'],
    author_email=metadata['email'],
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
    packages=find_packages(exclude=['docs', 'build', 'test', 'dist']),
    install_requires=requirements_to_list('requirements.txt'),
    package_data={
        '': [
            'README.md',
        ],
    }
)
