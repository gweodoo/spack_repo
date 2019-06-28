##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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
from spack import *


class Malp(AutotoolsPackage):
    """
        MALP stands for Multi-Application on-Line Profiling
        it is an online performance tracing tool aiming at
        overcoming common file-system limitations by relying
        on runtime coupling between running applications.
    """
    force_autoreconf = True
    homepage = "http://malp.hpcframework.paratools.com"
    url = "https://france.paratools.com/MALP/MALP_2.1.tar.gz"

    version('2.2', 'd86f84214c772dfff07bad63624182f6')
    version('2.1', '7131ddf6d6523dbf802d4f705eb357932ab5ff18')
    version('2.0.0', '18d386726478144bed601c74ae079195')

    depends_on('mpi', type=('build', 'link', 'run'))
    depends_on('libgd', type=('build', 'link'))
    depends_on('node-js')

    depends_on('graphviz +gts', type=('build', 'run'), when="+gts")
    depends_on('graphviz ~gts', type=('build', 'run'), when="-gts")

    variant('mpit', default=True, description='Enable MPIT support')
    variant('gts', default=True,
            description='Enable GNU Triangulation Support for graphviz support')
    variant('ompt', default=True,
            description='Enable OMPT support')
    variant('mpmdcomp', default=False,
            description='Enable MPMD legacy support (process stealing)')
    variant('mpc', default=False,
            description='Enable MPC compatibility mode')

    conflicts('+ompt', when="@2.1")
    conflicts('+mpit', when="@2.1")

    # Version URL
    def url_for_version(self, version):
        url = "https://france.paratools.com/MALP/MALP_{0}.tar.gz".format(
            version)
        return url

    def configure_args(self):
        spec = self.spec

        config_args = [
            '--with-gd2={0}'.format(spec['libgd'].prefix)
        ]

        if '+mpit' in spec:
            config_args.append('--enable-mpit')

        if '+ompt' in spec:
            config_args.append('--enable-ompt')

        if '+mpmdc' in spec:
            config_args.append('--enable-mpmdcompat')

        if '+mpc' in spec:
            config_args.append('--enable-mpmdcompat')
            config_args.append('--disable-posix')
            config_args.append('--with-mpi-compiler=mpc_cc')

        return config_args
