import processing

#extract some groups of layers for input
root = QgsProject.instance().layerTreeRoot()
pzo = root.findGroup("PZO")
wzs = root.findGroup("WZS")

layer_to_select_name ="warstwa_do_zaznaczania"

output_path="D:/testy"+"/"
 
#check whole group of layers for features  that interescts layer_to_select
for child in pzo.children():
    child_name = child.name()
    temp_lyr = QgsProject.instance().mapLayersByName(child.name())[0]
    processing.run("native:selectbylocation", {
        'INPUT': '{child_name}'.format(**vars()),
        'PREDICATE': 0,
        'INTERSECT': '{layer_to_select_name}'.format(**vars()),
        'METHOD': 0})
    if temp_lyr.selectedFeatureCount()<1:
        continue
    else:
        QgsVectorFileWriter.writeAsVectorFormat(
            temp_lyr,
            output_path +'{child_name}'.format(**vars()),
            "utf-8",
            layer.crs(),
            "ESRI Shapefile",
            True)