# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!!
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_WORK\BOEM_Fisheries_GDB_2.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAMES!!!
fc_list = ['RCA_Comm_NonTrawl_Groundfish_UTM10_PHASE2', 'RCA_Comm_Trawl_Groundfish_UTM10_PHASE2', 'RCA_Comm_Trawl_NonGroundfish_UTM10_PHASE2']

# loop through feature classes to add fields
for fc in fc_list:
    arcpy.AddField_management(fc, "region_id_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")

# Add default 'no' values to update/checked fields
    new_fields = ["region_id_U"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 1:
                row[index] = 'no'
                index += 1

                cursor.updateRow(row)

print 'Finished...'