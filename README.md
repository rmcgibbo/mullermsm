# MullerMSM : An MSMBuilder addon for dynamics on the 2D Muller Potential


<img width="400" height="400" src=https://raw.github.com/rmcgibbo/mullermsm/master/potential.png></src>


## Overview
This package allows you to sample trajectories on the Muller-Brown potential
and then use MSMBuilder to build Markov state models to describe the dynamics.

The intent is to provide a simple teaching tool illustrating the process of building
Markov state models in a simple and intuitive environment.


## Installation

The package is hosted at `https://github.com/rmcgibbo/mullermsm`. You can download
the package either with git:

    $ git cline git://github.com/rmcgibbo/mullermsm.git
  
Or by downloading a zip file from the `https://github.com/rmcgibbo/mullermsm/zipball/master`

MullerMSM requires MSMBuilder2.5.1 or later, which can be downloaded from
http://simtk.org/home/msmbuilder. It also requires theano, which can be installed
with 

    $ easy_install theano

To install the MullerMSM package, run

    $ python setupy.py install


## Using MullerMSM

The MullerMSM package installs three scripts

    mullermsm_propagate.py
    mullermsm_plot_trajectories.py
    mullermsm_voronoi.py

The first script, `mullermsm_propagate.py`, propagates trajectories on the Muller
potential energy surface using a simple Langevin integrator, and saves the
results in MSMBuilder's format.

The second script, `mullermsm_plot_trajectories.py`, plots the trajectories.

The third script, `mullermsm_voronoi.py`, helps to visualize the microstates
and macrostates of your MSMs.


### Simulating Trajectories on the Muller Potential Energy Surface


To generate trajectories on the muller potential, use the script `mullermsm_propagate.py`. 
To simulate ten trajectories of a length 10,000 steps, use the following command.
    
    $ mullermsm_propagate.py -n 10 -t 10000

This script will save the trajectories in MSMBuilder's format, and will
create a `ProjectInfo.h5` file for MSMBuilder. You can view the
trajectories with `mullermsm_plot_trajectories.py`.

To show all of the trajectories, use the command.

    $ mullermsm_plot_trajectories.py

To show only the first trajectory, you can use the command

    $ mullermsm_plot_trajectories.py -t 1


### Clustering the trajectories into a microstate MSM


Then, to use the kcenters algorithm to cluster into 100 microstates, you could
use the command

    $ Cluster.py custom -i metric.pickl kcenters -k 100


Finally, you can plot your clustering as a Veroni decompsosition using the command `mullermsm_plot_veroni.py`

    $ mullermsm_plot_veroni.py -g Data/Gens.lh5 -p ProjectInfo.h5




