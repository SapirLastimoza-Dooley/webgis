import arcpy 

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        def getParameterInfo(self):
            """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
    )
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
    )
        param2 = arcpy.Parameter(
            displayName="GDB Folder",
            name="gdbFolder",
            datatype="DEFolder",
            parameterType="Optional",
            direction="Input"
    )
        param3 = arcpy.Parameter(
            displayName="GDB Name",
            name="gdbName",
            datatype="GPString",
            parameterType="Optional",
            direction="Input"
    )
        param4 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="garageCSV",
            datatype="DETable",
            parameterType="Optional",
            direction="Input"
    )
        param5 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="garageName",
            datatype="GPString",
            parameterType="Optional",
            direction="Input"
    )
        param6 = arcpy.Parameter(
            displayName="Campus GBD",
            name="campusGDB",
            datatype="DEFolder",
            parameterType="Optional",
            direction="Input"
    )
        params = [param0, param1, param2, param3, param4, param5, param6]
        return params

    def execute(self, parameters, messages):
        arcpy.env.workspace = r'C:\Users\Sapir\Documents\ArcGIS\Projects\392_Lab4_Workspace'
        """The source code of the tool."""
        HW04 = r"C:\Users\Sapir\Documents\ArcGIS\Projects\392_Lab4_Workspace\392_Lab4_GDB.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferRadius_input = int(parameters[1].value)
        gdbFolder_input = parameters[2].valueAsText
        gdbName_input = parameters[3].valueAsText
        garageCSV_input = parameters[4].valueAsText
        garageName_input = parameters[5].valueAsText
        campusGDB_input = parameters[6].valueAsText

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = HW04 + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:
            # Generate the name for our generated buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferRadius_input)
            # Get reference to building
            buildingFeature = arcpy.Select_analysis(structures, HW04 + "/building_%s" % (buildingNumber_input), where_clause)
            # Buffer the selected building
            arcpy.Buffer_analysis(buildingFeature, HW04 + buildingBuff, bufferRadius_input)
            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(structures, HW04 + buildingBuff, HW04 + "/clip_%s" % (buildingNumber_input))

        else:
            print("Seems we couldn't find the building you entered")
        return None