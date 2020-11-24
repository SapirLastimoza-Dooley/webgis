import arcpy
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "lab6_toolbox.pyt"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [MapGenerator]


class MapGenerator(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab 6 Toolbox"
        self.description = "To color element on map"
        self.canRunInBackground = False
        self.category = 'Color Tools'

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName = 'File',
            name = 'File',
            datatype = 'DEFile',
            parameterType = 'Required',
            direction = 'Input'
        )
        param1 = arcpy.Parameter(
            displayName = 'Layer',
            name = 'Layer',
            datatype = 'GPString',
            parameterType = 'Required',
            direction = 'Input'
        )
        param2 = arcpy.Parameter(
            displayName = 'Output',
            name = 'Output',
            datatype = 'DEType',
            parameterType = 'Required',
            direction = 'Input'
        )

        params = [param0, param1, param2]
        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""

        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        arcpy.SetProgressor("step", "Creating Color Map...", start, maximum, step)
        time.sleep(readTime)
        arcpy.AddMessage("Creating Color Map...")

        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        # Grab the first map in the .aprx
        campus = project.listMaps('Map')[0]

        arcpy.SetProgressorPosition(start+step)
        arcpy.SetProgressorLabel("Validating building...")
        time.sleep(readTime)
        arcpy.AddMessage("Validating building...")

        arcpy.SetProgressorPosition(start+step)
        arcpy.SetProgressorLabel("Confirming building...")
        time.sleep(readTime)
        arcpy.AddMessage("Confirming building...")

        arcpy.SetProgressorPosition(start+step)
        arcpy.SetProgressorLabel("Coloring Map...")
        time.sleep(readTime)
        arcpy.AddMessage("Coloring Map...")

        arcpy.SetProgressorPosition(maximum)
        arcpy.SetProgressorLabel("Done...")
        time.sleep(readTime)
        arcpy.AddMessage("Done...")

        # Loop through available layers in the map
        for layer in campus.listLayers():

         # Check that the layer is a feature layer
            if layer.isFeatureLayer:

             # Obtain a copy of the layer's symbology
                symbology = layer.symbology

             # Makes sure symbology has an attribute "renderer"
                if hasattr(symbology, 'renderer'):

                 # Check if the layer's name is "Structures"
                    if layer.name == parameters[1].valueAsText:

                    # Update the copy's renderer to be "UniqueValueRenderer"
                        symbology.updateRenderer('UniqueValueRenderer')

                    # Tells arcpy that we want to use "Type" as our unique value
                        symbology.renderer.fields = ["Type"]

                    # Set the layer's actual symbology equal to the copy's
                    layer.symbology = symbology # Very important step
                    project.saveACopy(parameters[2].valueAsText + r"\NewMyLab6.aprx")

            else:
                print("No garage")
            return None
