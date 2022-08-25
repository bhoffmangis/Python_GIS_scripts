# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!!
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_WORK\BOEM_Fisheries_GDB_2.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAME!!!
fc_list = ['rec_Closures_PHASE2']

# loop through feature classes to add fields
for fc in fc_list:
    arcpy.AddField_management(fc, "T_UID", "LONG", "", "", 50, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "RC_UID", "SHORT", "", "", 50, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "Recreational_Closure_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Prohibit_Allow_Restrict_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "type_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "spp_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "gear_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "gear_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "location_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")

    arcpy.AddField_management(fc, "Editor_Initials", "TEXT", "", "", 3, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "Att_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Att_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "BIO_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")

    arcpy.AddField_management(fc, "QC_Initials", "TEXT", "", "", 5, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "AttQC_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")
    arcpy.AddField_management(fc, "AttQC_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "GIS_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")


# Add default 'no' values to update/checked fields
    new_fields = ["Recreational_Closure_U", "Prohibit_Allow_Restrict_U", "type_U", "spp_U",
                  "gear_U", "location_U", "Att_U"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 7:
                row[index] = 'no'
                index += 1

                cursor.updateRow(row)

# Add default 'not started' values to status fields
    new_fields = ["BIO_Status", "AttQC_Status", "GIS_Status"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 3:
                row[index] = 'not started'
                index += 1

                cursor.updateRow(row)

print 'Finished...'