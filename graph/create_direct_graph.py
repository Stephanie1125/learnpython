# create graph for small, medium, large data
import doctest

def direct_graph(input_file):
    """
    >>> direct_graph('small_data.txt')
    {'A': ['C'], '10': [], 'C': ['D', 'E'], 'B': ['F', 'G'], 'E': ['B'], 'D': ['E', 'G'], 'G': ['A'], 'F': ['D'], '7': []}
    """
    g = {}
    f = open(input_file, "r")
    for line in f.readlines():
        tmp = line.strip().split()
        if len(tmp) == 1: # node
            g[tmp[0]] = []
        elif len(tmp) == 2: # edges
            if tmp[0] in g:
                g[tmp[0]] += tmp[1]
        else:
            print "error"
    return g

g1 = direct_graph("small_data.txt")
print g1
for i in g1:
    print "%s: %s" % (i, len(g1[i]))

g2 = direct_graph("medium_data.txt")
print g2
g3 = direct_graph("large_data.txt")
print g3


doctest.testmod(verbose=1)

