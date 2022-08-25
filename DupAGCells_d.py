# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'C:\0_DATA\0_GIS\AG_WORK\0_MISC\DupAGCells\DupAGCells_SCRIPT_TEST.gdb'

# set feature class that requires processing
fc = 'DupAGCells_SCRIPT_TEST_COPY_d'
# assign to a list the fields that are to be searched and updated
fields = ['OBJECTID', 'COUNT', 'Avg_Depth', 'Min_Depth', 'Max_Depth', 'Rng_Depth', 'Std_Depth', 'LON_X', 'LAT_Y']

# instantiate cursor
with arcpy.da.SearchCursor(fc, fields) as cursor_1:
    for row_a in cursor_1:
        
        obj_ID_a = row_a[0]     # OBJECTID value of outer cursor row
        lon_a = row_a[7]        # LON_X value of outer cursor row
        lat_a = row_a[8]        # LAT_Y valueof outer cursor row       

        print obj_ID_a          # print OBJECTID of current outer cursor row

        with arcpy.da.UpdateCursor(fc, fields) as cursor_2:
            for row_b in cursor_2:
                
                obj_ID_b = row_b[0]     # OBJECTID value of inner cursor row
                lon_b = row_b[7]        # LON_X value of inner cursor row
                lat_b = row_b[8]        # LAT_Y valueof inner cursor row

                print obj_ID_b          # print OBJECTID of current inner cursor row

                if lon_a == lon_b and lat_a == lat_b:       # if the centroid coordinates are the same for ro_a and row_b
                    print 'True'    # centroid coordinates of both rows match (cells are spatially coincident)
                    if row_a[1] == None:
                        row_a[1] = row_b[1]     # set row_b COUNT value to row_a COUNT cell
                        row_a[2] = row_b[2]     # set row_b Avg_Depth value to row_a Avg_Depth cell
                        row_a[3] = row_b[3]     # set row_b Min_Depth value to row_a Min_Depth cell
                        row_a[4] = row_b[4]     # set row_b Max_Depth value to row_a Max_Depth cell
                        row_a[5] = row_b[5]     # set row_b Rng_Depth value to row_a Rng_Depth cell
                        row_a[6] = row_b[6]     # set row_b Std_Depth value to row_a Std_Depth cell

                    else:   # if row_b[1] == None
                        row_b[1] = row_a[1]     # set row_a COUNT value to row_b COUNT cell
                        row_b[2] = row_a[2]     # set row_a Avg_Depth value to row_b Avg_Depth cell
                        row_b[3] = row_a[3]     # set row_a Min_Depth value to row_b Min_Depth cell
                        row_b[4] = row_a[4]     # set row_a Max_Depth value to row_b Max_Depth cell
                        row_b[5] = row_a[5]     # set row_a Rng_Depth value to row_b Rng_Depth cell
                        row_b[6] = row_a[6]     # set row_a Std_Depth value to row_b Std_Depth cell

                else:
                    print 'False'   # centroid coordinates of both rows DO NOT match (cells are NOT spatially coincident)
            
                cursor_2.updateRow(row_b)   # update current row and proceed to next row

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!