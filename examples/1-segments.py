#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to get the L1 'observation intent' segments

In this example we show how to download segments from the Advanced LIGO
Data Quality Segment DataBase (DQSegDB), and plot them.
"""

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'
__currentmodule__ = 'gwpy.segments'

# First, import the `DataQualityFlag` object
from gwpy.segments import DataQualityFlag

# Then call the `~DataQualityFlag.query_dqsegdb` `classmethod` to query
# for a specific flag between a start time and an end time (UTC date strings
# get converted to GPS internally):
intent = DataQualityFlag.query_dqsegdb(
    'L1:DMT-SCIENCE:1', 'Mar 1', 'now', url='https://dqsegdb5.phy.syr.edu')

# And that's it.
#
# Now, we can plot them for sanity by calling the `~DataQualityFlag.plot`
# method:
plot = intent.plot(label='LLO')
plot.show()
