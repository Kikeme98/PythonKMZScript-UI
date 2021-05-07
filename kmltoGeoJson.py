from osgeo import ogr
import gdal

srcDS = gdal.OpenEx('084090952187.kml')
ds = gdal.VectorTranslate('output.json', srcDS, format='GeoJSON')