from distutils.core import setup

setup(name='mullermsm',
      version='0.1',
      license='GPLv3',
      include_package_data=True,
      package_data = {'': ['conf.pdb']},
      packages=['mullermsm'],
      package_dir={'mullermsm':'lib'})