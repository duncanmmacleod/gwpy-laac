#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Duncan M. Macleod

"""How to read Omicron triggers on the LIGO Data Grid

The Omicron event-trigger generator is used to find glitches in the main
*h(t)* channel and in auxiliary channels.
In this example we show how to fetch those triggers for a given channel,
and make a plot.

.. note::

   Event triggers are typically only available on the LDG cluster at the
   relevant observatory. This example will only work from the LLO machine,
   e.g. from `ldas-pcdev1.ligo-la.caltech.edu`
"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"

# First, we get the DC readout segments for the day of March 2 2015:

from gwpy.segments import DataQualityFlag
locksegs = DataQualityFlag.query_dqsegdb(
    'L1:DMT-DC_READOUT_LOCKED:1', 'March 2 2015', 'March 3 2015',
    url='https://dqsegdb5.phy.syr.edu')

# Now, GWpy provides a :meth:`~gwpy.table.lsctables.SnglBurstTable.fetch`
# method to find and read Omicron triggers (and ExcessPower triggers) in a
# single step.
# Here we read the `L1:OAF-CAL_DARM_DQ` triggers (L1 GW readout), for the
# day of March 2, using the `filt` keyword argument to filter out those 
# triggers in one of the lock segments:

from gwpy.table.lsctables import SnglBurstTable
triggers = SnglBurstTable.fetch(
    'L1:OAF-CAL_DARM_DQ', 'omicron', 'March 2 2015', 'March 3 2015',
    filt=lambda t: float(t.get_peak()) in locksegs.active)

# Then we can plot the triggers
plot = triggers.plot('time', 'peak_frequency', color='snr', edgecolor='none')
plot.set_epoch(1109462416)
plot.set_xlim(1109462416, 1109462416+86400)
plot.set_yscale('log')
plot.set_ylabel('Frequency [Hz]')
plot.set_title('L1 gravitational-wave strain [$h(t)$]')
# and add a colour-bar
plot.add_colorbar(log=True, clim=[3, 50], label='Signal-to-noise ratio (SNR)')
# and plot the DC readout segments along the bottom:
plot.add_state_segments(locksegs, plotargs={'label': 'Lock'})
plot.show()
