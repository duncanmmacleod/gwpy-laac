#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to get the L1 'observation intent' segments

In this example we show how to download segments from the Advanced LIGO
Data Quality Segment DataBase (DQSegDB), and plot them.

Using GWpy
==========
"""

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'
__currentmodule__ = 'gwpy.segments'

# First, import the `~gwpy.segments.DataQualityFlag` object
from gwpy.segments import DataQualityFlag

# Then call the `DataQualityFlag.query_dqsegdb()
# <gwpy.segments.DataQualityFlag.query_dqsegdb>` `classmethod` to query
# for a specific flag between a start time and an end time (UTC date strings
# get converted to GPS internally):
intent = DataQualityFlag.query_dqsegdb(
    'L1:DMT-SCIENCE:1', 'Mar 1', 'now', url='https://dqsegdb5.phy.syr.edu')

# And that's it.
#

# Finally, we can plot the segments downloaded in GWpy by calling the
# :meth:`~gwpy.segments.DataQualityFlag.plot` method:
plot = intent.plot(label='LLO')
plot.show()

# On the command-line
# ===================
#
# Alternatively, you could have done the same from the command-line, using
# the `ligolw_segment_query_dqsegdb <https://ldas-jobs.ligo.caltech.edu/~rfisher/dqsegdb_doc/ligolw_segment_query_dqsegdb.html>`_ script provided by the
# `DQSegDB <https://www.lsc-group.phys.uwm.edu/daswg/projects/dqsegdb.html>`_
# package:
#
# .. code-block:: bash
#
#    ligolw_segment_query_dqsegdb --query-segments --segment-url https://dqsegdb5.phy.syr.edu -s 1109203216 -e 1109808016 --include-segments L1:DMT-SCIENCE:1
#
# Which would return a `LIGO_LW` XML document complete with a set of segment
# tables (`segment_definer`, `segment_summary`, and `segment`).
#
# You could then print whichever data you wanted directly using `ligolw_print`:
#
# .. code-block:: bash
#
#    $ ligolw_segment_query_dqsegdb --query-segments --segment-url https://dqsegdb5.phy.syr.edu -s 1109203216 -e 1109808016 --include-segments L1:DMT-SCIENCE:1 | ligolw_print -t segment -c start_time -c end_time -d ' '
#    1109326141 1109326666
#    1109326668 1109347336
#
# .. note::
#
#    In case you care, the DQSegDB package is the official client interface
#    for the Advanced LIGO segment database(s), and is what is used by GWpy
#    internally.
