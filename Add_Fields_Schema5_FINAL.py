# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!! 
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_WORK\BOEM_Fisheries_GDB_2.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAME!!!
fc_list = ['BOEM_Fisheries_Editor_MarkUp_PHASE2']

# loop through feature classes to add fields
for fc in fc_list:
    arcpy.AddField_management(fc, "MU_UID", "LONG", "", "", 50, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "FC_UID", "LONG", "", "", 50, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "BIO_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")

    arcpy.AddField_management(fc, "Editor_Initials", "TEXT", "", "", 3, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "Comment", "TEXT", "", "", 255, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "QC_Initials", "TEXT", "", "", 5, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "QC_Comment", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "GIS_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")

# Cannot assign default values as no features yet exist...

print 'Finished...'