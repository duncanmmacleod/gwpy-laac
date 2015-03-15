#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Duncan M. Macleod

"""How to read triggers from ASCII files

The most used library for trigger manipulations in LIGO is the `glue.ligolw`
library.
This requires that the input data are stored in `LIGO_LW` XML files.
In this example we demonstrate how to read columnar data from ASCII (`txt`)
files into the same objects we use for `LIGO_LW` XML data.
"""

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"

# First, we grab an example of such data from a recent run of
# `Hveto <//wiki.ligo.org/DetChar/Hveto>`_ from `March 4 2015
# <//ldas-jobs.ligo-la.caltech.edu/~hveto/daily/201503/20150304/latest/>`_:

import os
os.system(
    'gsiscp ldas-pcdev2.ligo-la.caltech.edu:~hveto/public_html/daily/'
    '201503/20150304/latest/'
    'L1-HVETO_WINNERS_TRIGS_ROUND_1-1109462416-86400.txt .')

# Now we can read these using the :meth:`SnglBurstTable.read()
# <gwpy.table.lsctables.SnglBurstTable.read>` method:

from gwpy.table.lsctables import SnglBurstTable
triggers = SnglBurstTable.read(
    'L1-HVETO_WINNERS_TRIGS_ROUND_1-1109462416-86400.txt',
    columns=['time', 'peak_frequency', 'snr'])

# The columns we give have to match up to valid columns of the
# `~gwpy.table.lsctables.SnglBurstTable`, with the exception of `'time'`,
# which is handled separately by GWpy for each type of table.
#
# Now we have the same object as if we had just read the same data from
# a `LIGO_LW` XML file.
# As such, we can then plot the triggers to show which data they represent:

plot = triggers.plot('time', 'peak_frequency', color='snr', edgecolor='none')
plot.set_epoch(1109462416)
plot.set_xlim(1109462416, 1109462416+86400)
plot.set_yscale('log')
plot.set_ylabel('Frequency [Hz]')
plot.add_colorbar(log=True, clim=[3, 50], label='Signal-to-noise ratio (SNR)')
plot.set_title('HVeto round 1 winner [March 4 2015]')
plot.show()
