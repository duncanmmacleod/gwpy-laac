#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to make a spectrogram over multiple segments

In this example we demonstrate how to make a multi-segment
`~gwpy.spectrogram.Spectrogram` plot, showing the H1 **h(t)** data over
multiple locks.

"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__currentmodule__ = 'gwpy.timeseries'

# First, we can download the lock segments for the H1 interferometer:
from gwpy.segments import DataQualityFlag
locksegs = DataQualityFlag.query_dqsegdb(
    'H1:DMT-DC_READOUT_LOCKED:1', 'March 14 2015 12:00', 'March 14 2015 16:00',
    url='https://dqsegdb5.phy.syr.edu')

# then we loop over each segment, performing the following steps:
#
# - `~gwpy.timeseries.TimeSeries.fetch` the data
# - calculate an ASD `~gwpy.spectrogram.Spectrogram` for those data
# - de-whiten the data into units of strain/rtHz
#
from gwpy.timeseries import TimeSeries
specgrams = []
for segment in locksegs.active:
    data = TimeSeries.fetch('H1:CAL-DELTAL_EXTERNAL_DQ', segment[0], segment[1])
    sg = data.spectrogram(30, fftlength=8, overlap=4) ** (1/2.)
    specgrams.append(sg.zpk([100.]*5, [1.]*5, 1e-10/4000.))

# To make a plot using multiple data sets, we first generate a blank plot:
from gwpy.plotter import SpectrogramPlot
plot = SpectrogramPlot()
ax = plot.gca()

# then `~gwpy.plotter.SpectrogramAxes.plot` each data set in turn:
for sg in specgrams:
    ax.plot(sg)
    print(sg)

# To finish off, we customise the plot to make it look better
ax.grid(which='both')
ax.set_xlim(locksegs.known[0][0], locksegs.known[-1][-1])
ax.set_epoch(locksegs.known[0][0])
ax.set_yscale('log')
ax.set_ylim(40, 4000)
ax.set_title('LIGO Hanford $h(t)$')
plot.add_colorbar(log=True, clim=[1e-24, 1e-19], label=r'[strain/\rtHz]')
plot.add_state_segments(locksegs, plotargs={'label': 'Lock'})
plot.show()
