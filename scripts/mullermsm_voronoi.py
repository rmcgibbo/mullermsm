#!/usr/bin/env python

import matplotlib.pyplot as pp
from matplotlib.collections import LineCollection
import argparse
import scipy.stats
import numpy as np
from scipy.spatial import Delaunay

from msmbuilder import Project, Conformation, MSMLib, Serializer, Trajectory
from mullermsm import Voronoi
from mullermsm.muller import plot_v


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generators', default='Data/Gens.lh5', help='Path to Gens.lh5')
    parser.add_argument('-p', '--project', default='ProjectInfo.h5', help='Path to ProjectInfo.h5')
    parser.add_argument('-s', '--stride', default=5, type=int, help='Stride to plot the data at')
    args = parser.parse_args()
    
    
    gens = Trajectory.LoadTrajectoryFile(args.generators)
    gens_x = gens['XYZList'][:,0,0]
    gens_y =  gens['XYZList'][:,0,1]
    points = np.array([gens_x, gens_y]).transpose()
    
    
    
    tri = Delaunay(points)

    PL = []
    for p in points:
        PL.append(Voronoi.Site(x=p[0],y=p[1]))

    v,eqn,edges,wtf = Voronoi.computeVoronoiDiagram(PL)

    edge_points=[]
    for (l,x1,x2) in edges:
        if x1>=0 and x2>=0:
            edge_points.append((v[x1],v[x2]))

    lines = LineCollection(edge_points, linewidths=0.5, color='k')
    
    fig = pp.figure()
    ax = fig.add_subplot(111)
    
    fig.gca().add_collection(lines)

    maxx, minx= np.max(gens_x), np.min(gens_x)
    maxy, miny = np.max(gens_y), np.min(gens_y)
    # plot the background
    plot_v(minx=minx, maxx=maxx, miny=miny, maxy=maxy, ax=ax)
    pp.xlim(minx, maxx)
    pp.ylim(miny, maxy)

    # plot a single trajectory
    p = Project.LoadFromHDF(args.project)
    t = p.LoadTraj(0)
    x = t['XYZList'][:,0,0][::args.stride]
    y = t['XYZList'][:,0,1][::args.stride]
    cm = pp.get_cmap('spectral')

    n_points = len(x)
    ax.set_color_cycle([cm(1.*i/(n_points-1)) for i in range(n_points-1)])
    for i in range(n_points-1):
        ax.plot(x[i:i+2],y[i:i+2])

    pp.title('Voronoi Microstate Decomposition, with first trajectory')
    


    pp.show()
    
if __name__ == '__main__':
    main()
