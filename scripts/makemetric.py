import argparse
import pickle

from mullermsm import metric

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', help='name of output file. default: metric.pickl', default='metric.pickl')
args = parser.parse_args()

metric = metric.EuclideanMetric()
pickle.dump(metric, open(args.output, 'w'))
print 'saved %s' % args.output