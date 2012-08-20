from msmbuilder import metrics
import numpy as np

class EuclideanMetric(metrics.Vectorized):
    def prepare_trajectory(self, traj):
        xyzlist = traj['XYZList']
        n_frames, n_atoms, n_dims = xyzlist.shape
        
        # result needs to be n_frames x n_features
        return xyzlist.reshape(n_frames, n_atoms * n_dims).astype(np.double)

        

