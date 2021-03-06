"""
A toy example to demonstrate how to convert python arrays into cuSpatial inputs and call 
GPU-accelerated directed Hausdorff distance computation
"""

import numpy as np
import time
from cudf.core import column
import cuspatial.bindings.spatial as gis

pnt_x=column.as_column(np.array([0,-8,6],dtype=np.float64))
pnt_y=column.as_column(np.array([0,-8,6],dtype=np.float64))
cnt=column.as_column(np.array([1,2],dtype=np.int32))
num_set=len(cnt)
matrix=gis.cpp_directed_hausdorff_distance(pnt_x,pnt_y,cnt)
d=matrix.data.to_array().reshape((num_set,num_set))
print(d)
