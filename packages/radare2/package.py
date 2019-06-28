##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install radare2
#
# You can edit this file again by typing:
#
#     spack edit radare2
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Radare2(AutotoolsPackage):
    """
    r2 is a rewrite from scratch of radare in order to provide a set of libraries and tools to work with binary files.
    Radare project started as a forensics tool, a scriptable command-line hexadecimal editor able to open disk files,
    but later added support for analyzing binaries, disassembling code, debugging programs, attaching to remote gdb servers...
    """
    homepage = "https://www.rada.re"
    url      = "https://github.com/radare/radare2/archive/3.1.3.tar.gz"

    depends_on('git', type='build')
    
    version('3.1.3', sha256='e3198565b02b95c67da5c45e7f157b5a9e1c7d8afe0238bd5631459b0e7731fb')
    version('3.1.2', sha256='1fd1643c865322460e883e5fa0e59095ecac99add6262bc9aaf6cdd718423b7b')
    version('3.1.1', sha256='f04deec626ea0b57c7d3f0b4a936932ebfcbd0a62a13768702d85363d0148330')
    version('3.1.0', sha256='b6e74f29cc36ff25400376726e1315b37fe5876a1c82cf7bf75b39e6e5bbe41f')
    version('3.0.1', sha256='2de7c54f723b8439f899a86cb9e5142e7b62664994cea60aefdd9c2a69a3f9fe')
    version('3.0.0', sha256='6ac70860d2335ad4e1fdf79de38f5f4ed7642983c3349c722375ccd2a2ca5fa6')
    version('2.9.0', sha256='423ced52355daeaa12a6abbd6735f93c1eb19af728ecb359a6074f49abacc8a2')
    version('2.8.0', sha256='633c1b59e8935f6157142e7bd134b262f07595263c31c6ca3a194dd987a46360')
    version('2.7.0', sha256='624074a3edf55ee1d24e7ab05d65cb88f9672f6689f8fcc8bdd4e95faf35dce0')
    version('2.6.9', sha256='2838a8c83f1b32f8d5a13264580ff37788b3c0ac072e7f6408e9f7adbef84ba2')


    def configure_args(self):
        args = []
        return args
