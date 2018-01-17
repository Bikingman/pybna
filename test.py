from pybna import pyBNA
p = pyBNA("192.168.40.225","bna_ames","gis","gis",tilesTableName='tiles',verbose=True)
p.addScenarioNew("base","lksjdfkd")
s = p.scenarios['base']
blocks = s.blocks
tiles = p.tiles
connectivity = s.connectivity
a = s.getConnectivity(p.tiles[p.tiles.index==113])







from graphutils import *
import psycopg2
conn = psycopg2.connect('host=192.168.40.225 dbname=bna_ames user=gis')
g = buildNetwork(conn,"neighborhood_ways_net_link","neighborhood_ways_net_vert",
    "link_id","vert_id","source_vert","target_vert","link_cost","link_stress")

targets = [g.vertex(100),g.vertex(101)]
dist, pred = astar_search(
    g, g.vertex(0), g.ep.cost,
    VisitorExample(targets),
    heuristic=lambda v: heuristic(v, targets, g.vp.pos)
)
