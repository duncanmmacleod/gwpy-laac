#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2015)

"""How to get state segments from the Guardian

This example explains how to get state information from the Guardian system.
Specifically we will be finding the times of 'DC readout' locking, and
of locklosses, from the H1 `ISC_LOCK` Guardian node.

"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__currentmodule__ = 'gwpy.timeseries'

# First of, a bit of Guardian info. Each 'node' represents a single,
# controlled system, with a set of non-overlapping, connected states.
# More simply put, each node can be in only one state at any given time,
# and there are hand-defined conditions allowing transitions from one state
# to another (but not any other).
# For more details on the aLIGO Guardian system,
# `click here <https://awiki.ligo-wa.caltech.edu/aLIGO/Guardian>`_.
#
# Now, for any node, the state record for that node is written to the frames
# as `<ifo>:GRD-<node>_STATE_N`, e.g. `H1:GRD-ISC_LOCK_STATE_N` for the
# H1 locking node, and `L1:GRD-IFO_LOCK_STATE_N` for the L1 locking node,
# note the slight difference in names.
# With that knowledge, we can `~gwpy.timeseries.StateVector.fetch` the data
# for the H1 locking node for a few hours of recent commissioning, and store
# it in a `~gwpy.timeseries.StateVector`:

from gwpy.timeseries import TimeSeries
lockstate = TimeSeries.fetch(
    'H1:GRD-ISC_LOCK_STATE_N', 'March 10 2015', 'March 10 2015 12:00')

# Now, our Jeff told us that the 'DC readout' state was defined as state
# 500 in their locking guardian, so all we have to do is find those
# segments when `lockstate` was equal to 500.
#
# .. note::
#
#    On March 14 2015, the DC readout state was redefined to index 501,
#    with index 500 used for the transition to DC readout.
#
# First, we find the samples that are equal to 500:

dcreadout = lockstate == 500

# This gives us a `~gwpy.timeseries.StateTimeSeries`, just a `~gwpy.timeseries.TimeSeries` that has only `boolean <bool>` values.
# We can then convert that to a `~gwpy.segments.DataQualityFlag` by calling
# the `~gwpy.timeseries.StateTimeSeries.to_dqflag` method:

dcsegs = dcreadout.to_dqflag(name='DC')

# Similarly, we were told that locklosses are recorded as state `2` in the same
# node, so we can get those segments as well:

locklosssegs = (lockstate == 2).to_dqflag(name='Lockloss')

# It's only really useful to know the time of the start of the lockloss segment,
# so we extract those from our `~gwpy.segments.DataQualityFlag`:
locklosses = [seg[0] for seg in locklosssegs.active]
print(locklosses)
#[1109983042.0, 1109983063.3125, 1109983313.375, 1109983716.1875, 1109985581.5625, 1109986598.375, 1109986696.3125, 1109986754.375, 1109991413.3125, 1109991605.375, 1109993712.5, 1109993732.375, 1109994694.8125, 1109996012.125, 1110000870.4375, 1110002655.25, 1110002900.3125, 1110005279.375, 1110005839.0625, 1110009341.125, 1110009382.375, 1110011323.5, 1110012373.25, 1110023041.9375]

# Now, this shows us that there are lots of locklosses, this is because a
# lockloss segment is recorded whenever lock is broken at any point in the
# locking sequence, so can happen before a full DC-readout lock is recorded.
#
# But, we can easily work out which locklosses were at the end of a DC-readout
# segment:

enddcreadout = [seg[1] for seg in dcsegs.active]
reallocklosses = [t for t in locklosses if t in enddcreadout]
print(reallocklosses)
#[1109983042.0, 1109991413.3125, 1110023041.9375]

# Just for fun, we can plot the DC readout segments alongside the lockloss
# segments:

from gwpy.plotter import SegmentPlot
plot = SegmentPlot(dcsegs, locklosssegs, known=None)
plot.set_title('H1 lock segments and locklosses')
plot.show()
