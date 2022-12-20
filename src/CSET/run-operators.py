#! /usr/bin/env python3
"""
Script to chain together individual operators.

Currently it is hard coded, but in future it will take an argument specifying a
config file describing what operators to run in what order.

It takes the input file as its first argument, and the output file as the second
argument.
"""

import sys
from CSET.operators import generate_constraints, read, write, filters

# First argument is input file name, second is output file name.
# Third argument is (later optional) stash name and forth argument is
# later optional) variable name to constrain loading of model data.
# Currently using "m01s03i236" as stash name and "test" as variable name for test purposes.
input_file = sys.argv[1]
output_file = sys.argv[2]
stash = sys.argv[3]
varname = sys.argv[4]

# Hardcoded task chain to extract instantaneous air temperature.
stash_constraint = generate_constraints.generate_stash_constraints(stash)
var_constraint = generate_constraints.generate_var_constraints(varname)
cubes = read.read_cubes(input_file, stash_constraint)
cube = filters.filter_cubes(cubes, "m01s03i236", ())
write.write_cube_to_nc(cube, output_file)
