#!/usr/bin/env python

import os, sys
import argparse
import numpy as np
import IPython as ip
import matplotlib.pyplot as pp

from msmbuilder import Project, Trajectory, Serializer
from mullermsm.muller import plot_v

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project', default='ProjectInfo.h5')
    parser.add_argument('-a', '--assignments', default='Data/Assignments.h5')
    args = parser.parse_args()

    a = Serializer.LoadData(args.assignments)
    p = Project.LoadFromHDF(args.project)
    maxx, maxy, minx, miny = -np.inf, -np.inf, np.inf, np.inf
    n_states = np.max(a) + 1

    x = np.concatenate([p.LoadTraj(i)['XYZList'][:, 0, 0] for i in range(p['NumTrajs'])])
    y = np.concatenate([p.LoadTraj(i)['XYZList'][:, 0, 1] for i in range(p['NumTrajs'])])
    a = np.concatenate([a[i, :] for i in range(p['NumTrajs'])])
    
    plot_v(minx=np.min(x), maxx=np.max(x), miny=np.min(y), maxy=np.max(y))
    colors = ['b', 'r', 'm', 'c', 'g']
    for j in xrange(n_states):
        w = np.where(a == j)[0]    
        pp.scatter(x[w], y[w], marker='x', c=colors[j], label='State %d' % j,
                   edgecolor=colors[j], alpha=0.5)

    
    pp.legend()
    pp.show()
    
if __name__ == '__main__':
    main()
