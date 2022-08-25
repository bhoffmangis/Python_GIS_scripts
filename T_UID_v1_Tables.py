# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!!
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_WORK\BOEM_Fisheries_GDB_3.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAMES!!!
fc = 'Rec_Closures_PHASE3'


new_field = ['T_UID']

with arcpy.da.UpdateCursor(fc, new_field) as cursor:

    feature_num = 70001

    for row in cursor:  
        row[0] = feature_num
        feature_num += 1
        
        cursor.updateRow(row)

print 'Finished...'