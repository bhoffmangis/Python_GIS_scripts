# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!!
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_062221\BOEM_Fisheries_GDB.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAMES!!!
fc = 'fishing_closures_westcoast_UTM10_FOR_ST'


new_field = ['Unique_ID']

with arcpy.da.UpdateCursor(fc, new_field) as cursor:

    feature_num = 10001

    for row in cursor:  
        row[0] = feature_num
        feature_num += 1
        
        cursor.updateRow(row)

print 'Finished...'