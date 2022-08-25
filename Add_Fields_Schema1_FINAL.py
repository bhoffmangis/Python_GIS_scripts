# import arcpy site package
import arcpy

# set workspace --> NEED TO UPDATE GEODATABASE!!!
arcpy.env.workspace = r'D:\0_DATA\Fisheries\BOEM_Fisheries_GDB_WORK\BOEM_Fisheries_GDB_2.gdb'

# create feature class list object --> NEED TO UPDATE FEATURE CLASS NAMES!!!
fc_list = ['fishing_closures_westcoast_UTM10_PHASE2', 'PLCA_Drift_Gillnet_Closures_UTM10_PHASE2', 'RCA_Comm_NonTrawl_Groundfish_UTM10_PHASE2',
           'RCA_Comm_Trawl_Groundfish_UTM10_PHASE2', 'RCA_Comm_Trawl_NonGroundfish_UTM10_PHASE2']

# loop through feature classes to add fields
for fc in fc_list:
    arcpy.AddField_management(fc, "FC_UID", "LONG", "", "", 50, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "Area_Name_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Type_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Comm_Closure_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Rec_Closure_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Comm_Fishing_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Rec_Fishing_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Gen_Rest_Level", "TEXT", "", "", 255, "", "NULLABLE", "", "Restrict_Level")
    arcpy.AddField_management(fc, "Gov_Level_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")

    arcpy.AddField_management(fc, "Closure_Yr_GenRef", "TEXT", "", "", 255, "", "NULLABLE", "", "Closure_Yr_GenRef")
    arcpy.AddField_management(fc, "Closure_Yr_Active", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "Closure_Jan", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Feb", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Mar", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Apr", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_May", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_Jun", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_Jul", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Aug", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Sep", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_Oct", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_Nov", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active") 
    arcpy.AddField_management(fc, "Closure_Dec", "TEXT", "", "", 10, "", "NULLABLE", "", "Closure_Mon_Active")
    arcpy.AddField_management(fc, "Closure_Start_M", "SHORT", "", "", 3, "", "NULLABLE", "", "Closure_M") 
    arcpy.AddField_management(fc, "Closure_Start_D", "SHORT", "", "", 3, "", "NULLABLE", "", "Closure_D")
    arcpy.AddField_management(fc, "Closure_End_M", "SHORT", "", "", 3, "", "NULLABLE", "", "Closure_M")
    arcpy.AddField_management(fc, "Closure_End_D", "SHORT", "", "", 3, "", "NULLABLE", "", "Closure_D")

    arcpy.AddField_management(fc, "Estab_Yr_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Review_Mod_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Regulation_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Mgt_Agency_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "URL_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "State_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")

    arcpy.AddField_management(fc, "CC_UID", "SHORT", "", "", 50, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "RC_UID", "SHORT", "", "", 50, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "Priority", "TEXT", "", "", 1, "", "NULLABLE", "", "Priority_Flag")

    arcpy.AddField_management(fc, "Editor_Initials", "TEXT", "", "", 3, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "SourceFound", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Geo_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Geo_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "Geo_NEW", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    
    arcpy.AddField_management(fc, "Att_U", "TEXT", "", "", 3, "", "NULLABLE", "", "Update_Flag")
    arcpy.AddField_management(fc, "Att_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "BIO_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")

    arcpy.AddField_management(fc, "QC_Initials", "TEXT", "", "", 5, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "AttQC_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")
    arcpy.AddField_management(fc, "AttQC_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")

    arcpy.AddField_management(fc, "GeoEdit_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag_wNA")
    arcpy.AddField_management(fc, "GeoAdd_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag_wNA")
    arcpy.AddField_management(fc, "GeoQC_Comm", "TEXT", "", "", 255, "", "NULLABLE", "", "")
    arcpy.AddField_management(fc, "GIS_Status", "TEXT", "", "", 15, "", "NULLABLE", "", "Status_Flag")


# Add default 'no' values to update/checked fields
    new_fields = ["Area_Name_U", "Type_U", "Comm_Closure_U", "Rec_Closure_U", "Comm_Fishing_U", "Rec_Fishing_U",
                  "Gov_Level_U", "Estab_Yr_U", "Review_Mod_U", "Regulation_U", "Mgt_Agency_U", "URL_U", "State_U",
                  "SourceFound", "Geo_U", "Geo_NEW", "Att_U"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 17:
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

# Add default 'NA' values to status w/NA fields
    new_fields = ["GeoEdit_Status", "GeoAdd_Status"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 2:
                row[index] = 'NA'
                index += 1

                cursor.updateRow(row)

# Add default '3 - low' value to priority field
    new_fields = ["Priority"]

    with arcpy.da.UpdateCursor(fc, new_fields) as cursor:

        for row in cursor:
            index = 0
            while index < 1:
                row[index] = '3'
                index += 1

                cursor.updateRow(row)

print 'Finished...'