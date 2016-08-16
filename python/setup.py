# Liblouis Python ctypes bindings
#
# Copyright (C) 2009 Eitan Isaacson <eitan@ascender.com>
# Copyright (C) 2010 James Teh <jamie@jantrid.net>
#
# This file is part of liblouis.
# 
# liblouis is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
# 
# liblouis is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with liblouis. If not, see <http://www.gnu.org/licenses/>.
# 

r"""Python bindings for liblouis
"""

from setuptools import setup, find_packages
import louis

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Programming Language :: Python',
    'Topic :: Text Processing :: Linguistic',
    ]

setup(name="louis",
      description=__doc__,
      download_url = "http://code.google.com/p/liblouis/",
      license="LGPLv2.2",
      classifiers=classifiers,
      test_suite='nose.collector',
      tests_require=['nose'],
      version=louis.version().split(',')[0].split('-',1)[-1],
      packages=["louis"])
