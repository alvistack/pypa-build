#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['build', 'build._compat']

package_data = \
{'': ['*']}

package_dir = \
{'': 'src'}

install_requires = \
['packaging >= 19.1', 'pyproject_hooks']

extras_require = \
{':os_name == "nt"': ['colorama'],
 ':python_version < "3.10"': ['importlib-metadata >= 4.6'],
 ':python_version < "3.11"': ['tomli >= 1.1.0'],
 'docs': ['furo >= 2023.08.17',
          'sphinx ~= 7.0',
          'sphinx-argparse-cli >= 1.5',
          'sphinx-autodoc-typehints >= 1.10',
          'sphinx-issues >= 3.0.0'],
 'test': ['build[uv, virtualenv]',
          'filelock >= 3',
          'pytest >= 6.2.4',
          'pytest-cov >= 2.12',
          'pytest-mock >= 2',
          'pytest-rerunfailures >= 9.1',
          'pytest-xdist >= 1.34',
          'wheel >= 0.36.0'],
 'test:python_version < "3.10"': ['setuptools >= 42.0.0'],
 'test:python_version == "3.10"': ['setuptools >= 56.0.0'],
 'test:python_version == "3.11"': ['setuptools >= 56.0.0'],
 'test:python_version >= "3.12"': ['setuptools >= 67.8.0'],
 'typing': ['build[uv]',
            'importlib-metadata >= 5.1',
            'mypy ~= 1.9.0',
            'tomli',
            'typing-extensions >= 3.7.4.3'],
 'uv': ['uv >= 0.1.18'],
 'virtualenv': ['virtualenv >= 20.0.35']}

entry_points = \
{'console_scripts': ['pyproject-build = build.__main__:entrypoint'],
 'pipx.run': ['build = build.__main__:entrypoint']}

setup(name='build',
      version='1.2.2',
      description='A simple, correct Python build frontend',
      author=None,
      author_email='Filipe Laíns <lains@riseup.net>, Bernát Gábor <gaborjbernat@gmail.com>, layday <layday@protonmail.com>, Henry Schreiner <henryschreineriii@gmail.com>',
      url=None,
      packages=packages,
      package_data=package_data,
      package_dir=package_dir,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>= 3.8',
     )
