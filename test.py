from pybna import pyBNA
p = pyBNA("192.168.40.225","bna_ames","gis","gis",verbose=True)
p.addScenarioNew("base","lksjdfkd",3000,1,"neighborhood_ways_net_link","neighborhood_ways_net_vert")
blocks = p.blocks
s = p.scenarios['base']
connectivity = s.connectivity