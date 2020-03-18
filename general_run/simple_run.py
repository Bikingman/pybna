

import bikingman.pybna as pybna
i = pybna.Importer(config='C:\\Users\\dpatterson\\OneDrive - Toole Design Group\\BNA Training\\apbp\\apbp_config.yaml', verbose=False, debug=False, host=None, db_name=None, user=None, password=None)

i.import_boundary(fpath='C:\\Users\\dpatterson\\OneDrive - Toole Design Group\\BNA Training\\apbp\\boundary.shp', srid=None,table=None,overwrite=True)

i.import_census_blocks(fips=41,keep_water=False,overwrite=False)
#
# i.import_census_jobs("received.neighborhood_census_block_jobs",state="OR", url_main=None, url_aux=None, fpath_main=None, fpath_aux=None,overwrite=True)
#
# i.import_osm_network(roads_table=None,ints_table=None,  boundary_file=None,boundary_buffer=None, osm_file=None,keep_holding_tables=False,srid=None, overwrite=False)
#
# i.import_osm_destinations(osm_file=None,schema=None,boundary_file=None, srid=None,destination_tags=None,overwrite=False, keep_intermediates=False)
#
# # stress
# s = pybna.Stress(config=None, create_lookups=True, verbose=False)
#
# s.segment_stress(table=None,table_filter=None,dry=None)
#
# s.crossing_stress(table=None,angle=20,table_filter=None,dry=None)
#
# # connectivity
# bna = pybna.pyBNA(config=None, force_net_build=False, verbose=False, debug=False,  host=None, db_name=None, user=None, password=None)
#
# bna.calculate_connectivity(scenario_id=None,origin_blocks=None, destination_blocks=None,network_filter=None, road_ids=None,append=False,subtract=False, dry=None)
#
# bna.score_destinations("automated.bna_score_destinations")
