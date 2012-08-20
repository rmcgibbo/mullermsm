MullerMSM : An MSMBuilder addon for dynamics on the 2D Muller Potential
=========

<img width="400" height="400" src=https://raw.github.com/rmcgibbo/mullermsm/master/potential.png></src>


Overview
--------
This package allows you to sample trajectories on the Muller potential
and then use MSMBuilder to build MSMs for the dynamics.


Using MullerMSM
---------------

To generate trajectories on the muller potential, use the script `mullermsm_propagate.py`.

This script will save the trajectories in MSMBuilder's format, and will
create a `ProjectInfo.h5` file for MSMBuilder. You can view the
trajectories with `mullermsm_plot_trajectories.py`.

To cluster the trajectories using MSMBuilder, you need to give MSMBuilder
an appropriate distance metric. For a toy 2D potential like this, there's
really no concept of rotation and translational invariance, so something like
RMSD -- MSMBuilder's default -- is too complicated.

To build the appropriate distance metric, use `mullermsm_metric.py`. This will
save a file called `metric.pickl`, which can be used as a "custom" distance metric
for msmbuilder.

Then, to use the kcenters algorithm to cluster into 100 microstates, you could
use the command

    Cluster.py custom -i metric.pickl kcenters -k 100

From here on, it's basically a standard msmbuilder project.

Have fun!

Installation
------------

Run

    python setupy.py install
    
In addition to the library, it installs three scripts: `mullermsm_metric.py`
`mullermsm_plot_trajectories.py` and `mullermsm_propagate.py`

Requirements 
-----------

This package requires MSMBuilder, which can be downloaded from http://simtk.org/home/msmbuilder.
MSMBuilder 2.5.1 or greater is required.

Other requirements include theano, numpy, matplotlib, and ipython.

theano can be installed with

    pip install theano
    
or, if you prefer `easy_install`

    easy_install theano

