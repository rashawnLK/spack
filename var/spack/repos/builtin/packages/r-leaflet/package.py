# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RLeaflet(RPackage):
    """Create Interactive Web Maps with the JavaScript 'Leaflet' Library.

    Create and customize interactive maps using the 'Leaflet' JavaScript
    library and the 'htmlwidgets' package. These maps can be used directly from
    the R console, from 'RStudio', in Shiny apps and R Markdown documents."""

    cran = "leaflet"

    version('2.0.4.1', sha256='b0f038295f1de5d32d9ffa1d0dbc1562320190f2f1365f3a5e95863fff88901f')
    version('2.0.2', sha256='fa448d20940e01e953e0706fc5064b0fa347e69fa967792599eb03c52b2e3114')
    version('2.0.1', sha256='9876d5adf3235ea5683db79ec2435d3997c626774e8c4ec4ef14022e24dfcf06')
    version('1.0.1', sha256='f25a8e10c9616ccb5504bb874c533bc44fb7e438e073d4fe4484dee0951a9bc3')

    depends_on('r@3.1.0:', type=('build', 'run'))
    depends_on('r-base64enc', type=('build', 'run'))
    depends_on('r-crosstalk', type=('build', 'run'), when='@2.0.0:')
    depends_on('r-htmlwidgets', type=('build', 'run'))
    depends_on('r-htmltools', type=('build', 'run'))
    depends_on('r-magrittr', type=('build', 'run'))
    depends_on('r-markdown', type=('build', 'run'))
    depends_on('r-png', type=('build', 'run'))
    depends_on('r-rcolorbrewer', type=('build', 'run'))
    depends_on('r-raster', type=('build', 'run'))
    depends_on('r-scales@1.0.0:', type=('build', 'run'))
    depends_on('r-sp', type=('build', 'run'))
    depends_on('r-viridis@0.5.1:', type=('build', 'run'), when='@2.0.0:')
    depends_on('r-leaflet-providers@1.8.0:', type=('build', 'run'), when='@2.0.4.1:')
