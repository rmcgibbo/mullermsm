import os, sys
import argparse
import mullermsm
from mullermsm import metric
from mullermsm import muller
from msmbuilder import Project, Trajectory
import numpy as np
import IPython as ip
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--n_trajs', type=int, default=10)
    parser.add_argument('-t', '--traj_length', type=int, default=10000)
    args = parser.parse_args()
    
    # these could be configured
    kT = 15.0
    dt = 0.1
    mGamma = 1000.0
    
    forcecalculator = muller.muller_force()
    

    project = Project({'ConfFilename': os.path.join(mullermsm.__path__[0], 'conf.pdb'),
              'NumTrajs': args.n_trajs,
              'ProjectRootDir': '.',
              'TrajFileBaseName': 'trj',
              'TrajFilePath': 'Trajectories',
              'TrajFileType': '.lh5',
              'TrajLengths': [args.traj_length]*args.n_trajs})
    if os.path.exists('ProjectInfo.h5'):
        print >> sys.stderr, "The file ./ProjectInfo.h5 already exists. I don't want to overwrite anything, so i'm backing off"
        sys.exit(1)
    
    
    try:
        os.mkdir('Trajectories')
    except OSError:
        print >> sys.stderr, "The directory ./Trajectores already exists. I don't want to overwrite anything, so i'm backing off"
        sys.exit(1)
        
    for i in range(args.n_trajs):
        print 'simulating traj %s' % i
        
        # select initial configs randomly from a 2D box
        initial_x = [random.uniform(-1.5, 1.2), random.uniform(-0.2, 2)]
        positions = muller.propagate(args.traj_length, initial_x, kT, dt, mGamma, forcecalculator)

        # positions is N x 2, but we want to make it N x 1 x 3 where the additional
        # column is just zeros. This way, being N x 1 x 3, it looks like a regular MD
        # trajectory that would be N_frames x N_atoms x 3
        positions3 = np.hstack((positions, np.zeros((len(positions),1)))).reshape((len(positions), 1, 3))
        t = Trajectory.LoadTrajectoryFile(project['ConfFilename'])
        t['XYZList'] = positions3
        
        t.SaveToLHDF(project.GetTrajFilename(i))
        project.LoadTraj(i)
        
    project.SaveToHDF('ProjectInfo.h5')
    print 'saved ProjectInfo.h5'
    
    
if __name__ == '__main__':
    main()