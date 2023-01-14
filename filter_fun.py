import numpy as np
def filter_func(raw,threshold):
  if(raw<threshold):
    return 1
  else:
    return 0
