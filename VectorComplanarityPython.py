# No argument verification, no nothing. Spice to your taste!

import numpy.linalg as npl

def IsComplanar(*vectors):  
  #return npl.matrix_rank(vectors) <= 2 #this will work until float operation precision will screw you up
  u, s, vh = npl.svd(vectors)   
  s = [round(val, 12) for val in s]
  count = sum(map(lambda x : x > 0, s))
  return count <= 2
