# Copyright (C) 2018 Caio Carrara <eu@caiocarrara.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import setuptools


with open('README.rst', 'r') as readme:
    long_description = readme.read()


setuptools.setup(
    name='dojo-referee',
    version='0.0.2',
    author='Caio Carrara',
    author_email='eu@caiocarrara.com.br',
    description='Just another Coding Dojo assistant tool (but with GUI)',
    long_description=long_description,
    url='https://github.com/cacarrara/dojo-referee',
    packages=setuptools.find_packages(),
    package_data={
        'dojo_referee': [
            'logging.conf',
        ]
    },
    entry_points={
        'console_scripts': [
            'dojo-referee=dojo_referee.__main__:main',
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
    ],
)
