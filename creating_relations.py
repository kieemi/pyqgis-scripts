
'''
This script serve as relation creator in QGIS project for shapefiles and
data base files created according to "Standard to collect spatial data for Plans 
of Protective Actions on Natura 2000 sites" which can be dowloaded from:
https://github.com/kieemi/environment-database-app/blob/master/Standard%20to%20collect%20spatial%20data%20for%20Plans%20of%20Protective%20Actions%20on%20Natura%202000%20sites%20(polish%20version).zip
You need to follow two steps before runing the script:
1. Load shapefiles and data tables you want to create relation between
into the project e.g. for habitats (as presented below in code)
2. Write proper layer_prefix

Then run the script and relations will be created
'''

#layer prefix, very helpfull in fast changing input data
layer_prefix = "siedn2k"

#lines below will select only one layer with descripted name, so be careful to
#have no duplicates in layer list
base_layer = QgsProject.instance().mapLayersByName(layer_prefix+'_aft')[0]
base_layer_id = base_layer.id()
rates = (QgsProject.instance().mapLayersByName(layer_prefix+'wsk')[0])
protective_actions = (QgsProject.instance().mapLayersByName(layer_prefix+'dziaochr')[0])
exiting_threats = QgsProject.instance().mapLayersByName(layer_prefix+'zagr_ist')[0]
potential_threats = QgsProject.instance().mapLayersByName(layer_prefix+'zagr_pot')[0]

#relation for rates
rates_relation = QgsRelation()
rates_relation.setReferencingLayer(rates.id())
rates_relation.setReferencedLayer(base_layer_id)
rates_relation.addFieldPair('GUID_', 'GUID_')
rates_relation.setId(layer_prefix+'wsk')
rates_relation.setName(layer_prefix + " wskaźniki")
QgsProject.instance().relationManager().addRelation(rates_relation)

#relation for protective actions
protective_actions_relation = QgsRelation()
protective_actions_relation.setReferencingLayer(protective_actions.id())
protective_actions_relation.setReferencedLayer(base_layer_id)
protective_actions_relation.addFieldPair('GUID_', 'GUID_')
protective_actions_relation.setId(layer_prefix+'dziaochr')
protective_actions_relation.setName(layer_prefix + " działania ochronne")
QgsProject.instance().relationManager().addRelation(protective_actions_relation)

#relation for existing threats
exiting_threats_relation = QgsRelation()
exiting_threats_relation.setReferencingLayer(exiting_threats.id())
exiting_threats_relation.setReferencedLayer(base_layer_id)
exiting_threats_relation.addFieldPair('GUID_', 'GUID_')
exiting_threats_relation.setId(layer_prefix+'zagr_ist')
exiting_threats_relation.setName(layer_prefix + " zagrożenia istniejące")
QgsProject.instance().relationManager().addRelation(exiting_threats_relation)

#relation for potential threats
potential_threats_relation = QgsRelation()
potential_threats_relation.setReferencingLayer(exiting_threats.id())
potential_threats_relation.setReferencedLayer(base_layer_id)
potential_threats_relation.addFieldPair('GUID_', 'GUID_')
potential_threats_relation.setId(layer_prefix+'zagr_pot')
potential_threats_relation.setName(layer_prefix + " zagrożenia potencjalne")
QgsProject.instance().relationManager().addRelation(potential_threats_relation)