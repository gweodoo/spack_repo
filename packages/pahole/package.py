# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pahole
#
# You can edit this file again by typing:
#
#     spack edit pahole
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pahole(CMakePackage):
    """FIXME: ."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://lwn.net/Articles/335942/"
    url      = "https://github.com/gweodoo/pahole/archive/v1.12.tar.gz"

    # FIXME: Add proper versions and checksums here.
    version('1.12',    sha256='2452464cbfdbaece6187d7860000fe8ef24b7271f88122cf540d3e0ab4a644d1')
    version('1.11',    sha256='3b2a413f1a6d6b1c329e1664c8b146cc341d48b68428ee5d21d21336a6cc2545')
    version('1.10',    sha256='c84cb855ae9fa13ec875d47cad6cb91134331f53a784c1a9c80979927e45b3bd')
    version('1.9',     sha256='e27297b863d242471573aec2451fb794c6d8399345cacf15528ba8b465390d90')
    version('1.8pre1', sha256='1e617735409ea642e59b8e2f535a8a4edb445c3b3d75a039f5749334a53257d5')
    version('1.8',     sha256='230265c1590aac5c775cb47605c65c07bc41e87a06685d34d1b221673bd15eee')
    version('1.7',     sha256='2b5a05b21d60adad1accaacaf109fdadfe0ccb99de8365cc7260c012d8eac06c')
    version('1.6',     sha256='d4e79cdf60e94feb5ee938045dcd8f45628c735d13da9ce457d54622862badd4')
    version('1.5',     sha256='a0b14ecf2405714aa569a99cbd67a616de53b2a8e9cd5fe46a6999c19b669765')
    version('1.4',     sha256='1cb15f783a0b9cabb95ce7a44fccc0c88802dcf167d62613540f36a980c2214a')

    # FIXME: Add dependencies if required.
    depends_on('libdwarf')

    def cmake_args(self):
        args = ["-D__LIB=lib"]
        return args
    
