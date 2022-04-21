# No argument verification, no nothing. Spice to your taste!

import numpy.linalg as npl

def IsComplanar(*vectors, precision = 12):  
  #return npl.matrix_rank(vectors) <= 2 #this will work until float operation precision will screw you up
  u, s, vh = npl.svd(vectors)   
  s = [round(val, precision) for val in s]  #{only) 12 significant digits are accounted for
  count = sum(map(lambda x : x != 0, s))
  return count <= 2
