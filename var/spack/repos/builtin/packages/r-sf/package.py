# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RSf(RPackage):
    """Simple Features for R.

    Support for simple features, a standardized way to encode spatial vector
    data. Binds to 'GDAL' for reading and writing data, to 'GEOS' for
    geometrical operations, and to 'PROJ' for projection conversions and datum
    transformations. Optionally uses the 's2' package for spherical geometry
    operations on geographic coordinates."""

    cran = "sf"

    version('1.0-7', sha256='d0731fab9438d73a55af7232f0474b36f4b2a4e6d66adaa141632f4a60265453')
    version('1.0-5', sha256='290c28fa5ea777d555e70962c59079c134f02f7bdf60259a72eea79a064a1ac4')
    version('0.9-7', sha256='4acac2f78badf9d252da5bf377975f984927c14a56a72d9f83d285c0adadae9c')
    version('0.7-7', sha256='d1780cb46a285b30c7cc41cae30af523fbc883733344e53f7291e2d045e150a4')
    version('0.7-5', sha256='53ed0567f502216a116c4848f5a9262ca232810f82642df7b98e0541a2524868')
    version('0.5-5', sha256='82ad31f98243b6982302fe245ee6e0d8d0546e5ff213ccc00ec3025dfec62229')

    depends_on('r@3.3.0:', type=('build', 'run'))
    depends_on('r-classint@0.2-1:', type=('build', 'run'))
    depends_on('r-classint@0.4-1:', type=('build', 'run'), when='@0.9-7:')
    depends_on('r-dbi@0.8:', type=('build', 'run'))
    depends_on('r-magrittr', type=('build', 'run'))
    depends_on('r-rcpp@0.12.18:', type=('build', 'run'))
    depends_on('r-s2@1.0.7:', type=('build', 'run'), when='@1.0-5:')
    depends_on('r-units@0.6-0:', type=('build', 'run'), when='@1.0-5:')
    depends_on('gdal@2.0.1:')
    depends_on('geos@3.4.0:')
    depends_on('proj@4.8.0:5', when='@:0.7-3')
    depends_on('proj@4.8.0:6', when='@0.7-4:0.7-7')
    depends_on('proj@4.8.0:')
    depends_on('sqlite', when='@0.9-7')

    depends_on('r-units@0.6-0:', type=('build', 'run'), when='@:9.9-7')
