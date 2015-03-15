#####################################
Practical Data-Quality with GWpy/LDVW
#####################################

**Written for the LSC Academic Affairs Council Retreat, March 2015**

This tutorial serves as a brief introduction to the following topics:

- `GWpy <//gwpy.github.io>`_ - a python package for gravitational-wave astrophysics, and
- `LDVW <//ldvw.ligo.caltech.edu>`_ - a web service for plotting gravitational-wave interferometer data

Contained in this tutorial are a small number of practical examples, meant to expand upon the documentation to either of the projects above.

=====
Setup
=====

First things first, installing GWpy. There are `decent instructions <//gwpy.github.io/docs/stable/install.html>`_ provided as part of the `GWpy documentation <//gwpy.github.io/docs/stable>`_.

Alternatively, if you are having serious problems installing GWpy and its dependencies on your own machine, or don't want to, you can use the shared installation available on the `LIGO Data Grid <//wiki.ligo.org/LDG/>`_ computing centres at CIT, LHO, and LLO.
To use that installation, just run from the shell:

.. code-block:: bash

   source ~detchar/opt/gwpysoft/etc/gwpy-user-env.sh

The GWpySoft installation includes bleeding-edge installations of `NumPy <https://numpy.org>`_, `SciPy <https://scipy.org>`_, `matplotlib <https://matplotlib.org>`_, and `Astropy <https://astropy.org>`_ that go (far) beyond what is normally available on the LIGO Data Grid, so don't be surprised if old code doesn't work completely when you move to using the GWpySoft stack.

========
Examples
========

.. toctree::
   :numbered:
   :glob:
   :titlesonly:

   examples/*


======================
Further LIGO resources
======================

- aLog: `LHO <https://alog.ligo-wa.caltech.edu/aLOG/index.php>`_, `LLO <https://alog.ligo-la.caltech.edu/aLOG/index.php>`_
- Summary pages: `LHO <https://ldas-jobs.ligo-wa.caltech.edu/~detchar/summary/>`_, `LLO <https://ldas-jobs.ligo-la.caltech.edu/~detchar/summary/>`_, `Multi-IFO <https://ldas-jobs.ligo.caltech.edu/~detchar/summary/>`_
- Simulink web views: `LHO <https://lhocds.ligo-wa.caltech.edu/simulink/>`_, `LLO <https://llocds.ligo-la.caltech.edu/daq/simulink/>`_
- `Remote MEDM <//wiki.ligo.org/RemoteAccess/RemoteMEDM>`_
