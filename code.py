import itertools

def surfaceArea(A):
    area = H * W * 2
    for row in itertools.chain(A, zip(*A)): #It groups all the iterables together and produces a single iterable as output.
        for a, b in pairwise((0, *row, 0)):
            area += abs(a-b)
    return area
  
"for Python 3.10+ -> itertools.pairwise"
def pairwise(iter): 
    return zip(iter, iter[1:])
  



