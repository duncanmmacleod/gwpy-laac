#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to plot the LLO h(t) spectrum

In this example we show how to de-whiten the L1 DARM channel to produce an
ASD in GW strain units.

.. note::

   This example will only reliably work when using `scipy` >= 0.16, which
   at the time of writing is only available by installing `scipy` directly
   from its git repository:

   .. code-block:: bash

      pip install --user git+https://github.com/scipy/scipy

"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__currentmodule__ = 'gwpy.timeseries'

# First, we `fetch() <gwpy.timeseries.TimeSeries.fetch>` the whitened data
# for 30 minutes of a recent lock stretch:
from gwpy.timeseries import TimeSeries
white = TimeSeries.fetch(
    'L1:OAF-CAL_DARM_DQ', 'March 2 2015 12:00', 'March 2 2015 12:30')

# .. note::
#
#    We used the NDS2 service to get the data, however, we could have
#    read the data directly from frames, see `here
#    <//gwpy.github.io/docs/stable/timeseries/gwf.html>`_ for more details.

# Now we can `de-whiten <gwpy.timeseries.TimeSeries.zpk>` the data using
# the inverse of the whitening filter, after applying a
# `~gwpy.timeseries.TimeSeries.highpass` filter to prevent low-frequency
# noise from causing problems
hp = white.highpass(4)
displacement = hp.zpk([100]*5, [1]*5, 1e-10/4000.)

# Next we can calculate the `ASD <gwpy.timeseries.TimeSeries.asd>`:
asd = displacement.asd(8, 4)

# Finally, we can make a plot, and prettify it with limits and labels:
plot = asd.plot()
ax = plot.gca()
ax.set_ylabel(r'GW sensitivity [strain/\rtHz]')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylim(5e-24, 1e-19)
ax.set_xlim(10, 4000)
ax.set_title('L1 $h(t)$ spectrum')
plot.show()
