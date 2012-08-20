import numpy as np
import numpy.testing as npt

from mullermsm.metric import EuclideanMetric


def test_0():
    m = EuclideanMetric()
    x = {'XYZList': np.random.randn(100,2)}
    y = {'XYZList': np.random.randn(100,2)}
    
    px, py = m.prepare_trajectory(x), m.prepare_trajectory(y)

    d = m.one_to_all(px, py, 0)
    d2 = np.sqrt(np.sum(np.square(py - px[0]), axis=1))
    
    npt.assert_array_almost_equal(d, d2)