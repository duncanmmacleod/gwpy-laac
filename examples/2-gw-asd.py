#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to plot the LLO h(t) spectrum

In this example we show how to de-whiten the L1 DARM channel to produce an
ASD in GW strain units.

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

# Next we can calculate the `ASD <gwpy.timeseries.TimeSeries.asd>` of the
# whitened data:
wasd = white.asd(8, 4)

# Now we can `de-whiten <gwpy.spectrum.Spectrum.zpk>` the ASD using
# the inverse of the original whitening filter:
dasd = wasd.zpk([100]*5, [1]*5, 1e-10/4000.)
# giving us an ASD in strain units.
#
# .. note::
#
#    We have chosen to de-whiten in the frequency domain, rather than the
#    the time domain, to prevent any problems with unstable filters.
#    Only when using `scipy` >= 0.16 will time-domain filtering be reliable.

# Next, we can also calculate the inspiral sensitivity using the PSD:
from gwpy.astro import inspiral_range
bns = inspiral_range(dasd**2)

# Finally, we can make a plot, and prettify it with limits and labels:
plot = dasd.plot()
ax = plot.gca()
ax.set_ylabel(r'GW sensitivity [strain/\rtHz]')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylim(5e-24, 1e-19)
ax.set_xlim(10, 4000)
ax.set_title('L1 $h(t)$ spectrum [%.3g %s BNS range]' % (bns.value, bns.unit))
plot.show()
