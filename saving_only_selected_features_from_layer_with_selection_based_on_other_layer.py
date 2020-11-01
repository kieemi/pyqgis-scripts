mc= iface.mapCanvas()
import processing

#extract name of currently selected layer
lyr = mc.currentLayer()
lyr_name = lyr.name()

#name of layer to compare
layer_to_select_name ="warstwa_do_zaznaczania"

output_path="D:/testy"+"/"

while processing.run("native:selectbylocation", {
    'INPUT': '{lyr_name}'.format(**vars()),
    'PREDICATE': 0,
    'INTERSECT': '{layer_to_select_name}'.format(**vars()),
    'METHOD': 0}):
#    check for empty selection
    if temp_lyr.selectedFeatureCount()<1:
        break
    else:
#        write a shapefile on disk
        QgsVectorFileWriter.writeAsVectorFormat(
            lyr,
            output_path +'{lyr_name}'.format(**vars()),
            "utf-8",
            lyr.crs(),
            "ESRI Shapefile",
            True)
#       add new layer to 
        new_layer = QgsVectorLayer('{output_path}'.format(**vars())+'{lyr_name}'.format(**vars())+".shp",'{lyr_name}'.format(**vars())+"_only_selected","ogr")
        if not new_layer.isValid():
            print("Layer failed to load!")
        else:
            QgsProject.instance().addMapLayer(new_layer)
        break