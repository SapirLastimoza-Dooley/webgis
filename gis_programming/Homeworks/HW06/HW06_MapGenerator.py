import arcpy
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:\Users\Sapir\Documents\ArcGIS\Projects\GEOG_392\Lab_6" + r"\Lab_6.aprx")

# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]

# Loop through available layers in the map
for layer in campus.listLayers():

    # Check that the layer is a feature layer
    if layer.isFeatureLayer:

        # Obtain a copy of the layer's symbology
        symbology = layer.symbology

        # Makes sure symbology has an attribute "renderer"
        if hasattr(symbology, 'renderer'):

            # Check if the layer's name is "Structures"
            if layer.name == "GarageParking":

                # Update the copy's renderer to be "UniqueValueRenderer"
                symbology.updateRenderer('UniqueValueRenderer')

                # Tells arcpy that we want to use "Type" as our unique value
                symbology.renderer.fields = ["Type"]

                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("No garage")
project.saveACopy(r"C:\Users\Sapir\Documents\ArcGIS\Projects\GEOG_392\Lab_6" + r"\Lab_6.aprx")