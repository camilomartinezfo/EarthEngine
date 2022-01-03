import ee

# Initialize the Earth Engine module.
ee.Initialize()

# Acceso a la colección de imágenes de Planet
nicfi = ee.ImageCollection('projects/planet-nicfi/assets/basemaps/americas')

# Filtra la primera imagen con el método first 
basemap = nicfi.filter(ee.Filter.date('2021-03-01','2021-07-01')).first()
print(type(basemap))

# Resolución espacial de las imágenes Planet
print(nicfi.get('spatial_resolution').getInfo())