# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RSpatstatGeom(RPackage):
    """Geometrical Functionality of the 'spatstat' Family.

    Defines spatial data types and supports geometrical operations on them.
    Data types include point patterns, windows (domains), pixel images, line
    segment patterns, tessellations and hyperframes. Capabilities include
    creation and manipulation of data (using command line or graphical
    interaction), plotting, geometrical operations (rotation, shift, rescale,
    affine transformation), convex hull, discretisation and pixellation,
    Dirichlet tessellation, Delaunay triangulation, pairwise distances,
    nearest-neighbour distances, distance transform, morphological operations
    (erosion, dilation, closing, opening), quadrat counting, geometrical
    measurement, geometrical covariance, colour maps, calculus on spatial
    domains, Gaussian blur, level sets of images, transects of images,
    intersections between objects, minimum distance matching. (Excludes spatial
    data on a network, which are supported by the package
    'spatstat.linnet'.)"""

    cran = "spatstat.geom"

    version('2.3-1', sha256='f23e58d05a6d6bfab1345951fa528a9865f2a744e162fe4456161e1b0b5172c0')

    depends_on('r@3.5.0:', type=('build', 'run'))
    depends_on('r-spatstat-data@2.0-0:', type=('build', 'run'))
    depends_on('r-spatstat-utils@2.2-0:', type=('build', 'run'))
    depends_on('r-deldir@1.0-2:', type=('build', 'run'))
    depends_on('r-polyclip@1.10-0:', type=('build', 'run'))
