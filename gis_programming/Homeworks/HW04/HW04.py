import arcpy

arcpy.env.workspace = r'C:\Users\Sapir\Documents\ArcGIS\Projects\392_Lab4_Workspace' 

arcpy.CreateFileGDB_management(arcpy.env.workspace, '392_Lab4_GDB.gdb') 
print('GDB Created')

garages = arcpy.management.MakeXYEventLayer('garages.csv', 'X', 'Y', 'garages_layer') 
print('Garages Table Created')

arcpy.FeatureClassToGeodatabase_conversion(garages, '392_Lab4_GDB.gdb') 
print('Garages Layer Created')

structures = arcpy.env.workspace + '/Campus.gdb/Structures'
arcpy.FeatureClassToGeodatabase_conversion(structures, '392_Lab4_GDB.gdb') 
print('Structures Layer Imported')

spatial_ref = arcpy.Describe(arcpy.env.workspace + '/Campus.gdb/Structures').spatialReference
arcpy.Project_management(arcpy.env.workspace + '/392_Lab4_GDB.gdb/garages_layer', arcpy.env.workspace + '/392_Lab4_GDB.gdb/garages_proj', spatial_ref)
print('Projection Complete')

mygdb = '392_Lab4_GDB.gdb'

arcpy.analysis.Near(mygdb + '/Structures', mygdb + r'/garages_layer')
arcpy.Buffer_analysis(mygdb + '/garages_layer', mygdb + '/garages_buffer', '100 Meters')
print('Buffer Created')

arcpy.Intersect_analysis([mygdb + '/garages_buffer', mygdb + '/Structures'], mygdb + '/intersection', 'ALL')
arcpy.TableToTable_conversion(mygdb + '/intersection.dbf', arcpy.env.workspace, 'intersection.csv')
print('successfully found the nearest garage within 100 meters!')