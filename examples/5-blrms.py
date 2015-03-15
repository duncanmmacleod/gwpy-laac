#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to read band-limited RMS seismic trends and plot them

In this example, we look at the impact of a massive earthquake in the
Atlantic Ocean that had an impact on LIGO operations
"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__currentmodule__ = 'gwpy.timeseries'

# First: we import the objects we need, one for getting the data:
from gwpy.timeseries import TimeSeriesDict
# and one for plotting the data:
from gwpy.plotter import TimeSeriesPlot

# Next we define the channels we want, namely the 0.03Hz-1Hz ground motion
# band-limited RMS channels (1-second average trends).
# We do this using string-replacement so we can substitute the interferometer
# prefix easily when we need to:
channels = [
    '%s:ISI-BS_ST1_SENSCOR_GND_STS_X_BLRMS_30M_100M.mean,s-trend',
    '%s:ISI-BS_ST1_SENSCOR_GND_STS_Y_BLRMS_30M_100M.mean,s-trend',
    '%s:ISI-BS_ST1_SENSCOR_GND_STS_Z_BLRMS_30M_100M.mean,s-trend',
]

# At last we can fetch 12 hours of data for each interferometer using the
# `TimeSeriesDict.fetch() <gwpy.timeseries.TimeSeries.fetch>` method:
lho = TimeSeriesDict.fetch([c % 'H1' for c in channels],
                           'Feb 13 2015 16:00', 'Feb 14 2015 04:00')
llo = TimeSeriesDict.fetch([c % 'L1' for c in channels],
                           'Feb 13 2015 16:00', 'Feb 14 2015 04:00')

# Next we can plot the data, with a separate `~gwpy.plotter.Axes` for each
# instrument:
plot = TimeSeriesPlot(lho, llo)
for ifo, ax in zip(['H1', 'L1'], plot.axes):
   ax.legend(['X', 'Y', 'Z'])
   ax.yaxis.set_label_position('right')
   ax.set_ylabel(ifo, rotation=0, va='center', ha='left')
   ax.set_yscale('log')
plot.text(0.1, 0.5, '$1-3$\,Hz motion [nm/s]', rotation=90, fontsize=24,
          ha='center', va='center')
plot.axes[0].set_title('Magnitude 7.1 earthquake impact on LIGO', fontsize=24)
plot.show()

# Here we have also customised the output by manually setting the legend
# entries, putting the interferometer label on the right-hand side, setting
# a logarithmic y-axis scale, adding a shared y-axis label on the left-hand
# side, and setting a title.

# As we can see, the earthquake had a huge impact on the observatories, severly
# imparing operations for several hours.
