import arcpy
arcpy.env.workspace = r'C:\Users\Sapir\Documents\ArcGIS\Projects\392_Lab4_Workspace'

# Define our geodatabase
myGDB = '392_Lab4_GDB.gdb'

# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))
garageName = input('Please enter garage name: ')

# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if building exists
structures = myGDB + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False

for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

# If we shouldProceed do so
if shouldProceed:
    # Generate the name for our generated buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, myGDB + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, myGDB + buildingBuff, bufferSize_input)
    # Clip the structures to our buffered feature
    arcpy.Clip_analysis(structures, myGDB + buildingBuff, myGDB + "/clip_%s" % (buildingNumber_input))

    
else:
    print("Seems we couldn't find the building you entered")