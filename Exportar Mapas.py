mxd = arcpy.mapping.MapDocument ("CURRENT")
for pageNum in range (1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    arcpy.mapping.ExportToJPEG(mxd,r"C:\Mapas\Reforestacion"+str(pageNum)+".jpeg")
    

