import os, sys
import argparse
import numpy as np
import IPython as ip
import matplotlib.pyplot as pp

from msmbuilder import Project, Trajectory
from mullermsm.muller import plot_v

pp.ion()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project', default='ProjectInfo.h5')
    parser.add_argument('-t', '--trajectories', nargs='+',
        help='''Supply either the path to a trajectory file (i.e. Data/Gens.lh5),
         or an integer, which will be interepreted as a trajectory index
         into the trajectories that accompany the project. default: plot all
         of the trajectories''', default=['-1'])
    args = parser.parse_args()
    
    p = Project.LoadFromHDF(args.project)
    
    # record the bounding box of the points so that we know
    # what to render for the background
    maxx, minx, maxy, miny = 1.2, -1.5, 2, -0.2
    
    # if -1 is included, add in ALL of the trajectories
    if '-1' in args.trajectories:
        args.trajectories.remove('-1')
        args.trajectories.extend(range(p['NumTrajs']))
    # remove duplicates
    args.trajectories = set(args.trajectories)
    
    for requested in args.trajectories:
        if os.path.exists(str(requested)):
            traj = Trajectory.LoadTrajectoryFile(str(requested))
            print 'plotting %s' % requested
            markersize = 50
        else:
            try:
                i = int(requested)
                traj = p.LoadTraj(i)
                print 'plotting %s' % i
                markersize=5
            except ValueError:
                print >> sys.stderr, 'I couldnt figure out how to deal with the argument %s' % requested
                continue
            except IOError as e: 
                print >> sys.stderr, str(e)
                continue
    
        xyz = traj['XYZList']
        x = xyz[:,0,0]
        y = xyz[:,0,1]
        
        maxx, maxy = max(np.max(x), maxx), max(np.max(y), maxy)
        minx, miny = min(np.min(x), minx), min(np.min(y), miny)
        pp.plot(x, y, '.', markersize=markersize, alpha=0.5)
    
    print maxx, minx, maxy, miny
    plot_v(minx=minx, maxx=maxx, miny=miny, maxy=maxy)
    ip.embed()
    
if __name__ == '__main__':
    main()
