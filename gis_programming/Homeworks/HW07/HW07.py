import arcpy

source = r"C:\Users\Sapir\Desktop\GEOG 392\LT05_L1TP_026039_20110819_20160831_01_T1.tar\LT05_L1TP_026039_20110819_20160831_01_T1"
band1 = arcpy.sa.Raster(source + "\LT05_L1TP_026039_20110819_20160831_01_T1_B1.TIF")
band2 = arcpy.sa.Raster(source +"\LT05_L1TP_026039_20110819_20160831_01_T1_B2.TIF")
band3 = arcpy.sa.Raster(source +"\LT05_L1TP_026039_20110819_20160831_01_T1_B3.TIF")
band4 = arcpy.sa.Raster(source +"\LT05_L1TP_026039_20110819_20160831_01_T1_B4.TIF")
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "\combined.tif")

source = r"C:\Users\Sapir\Desktop\GEOG 392"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_hillshade.tif", azimuth, altitude, shadows, z_factor)

source = r"C:\Users\Sapir\Desktop\GEOG 392"
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_slopes.tif", output_measurement, z_factor)