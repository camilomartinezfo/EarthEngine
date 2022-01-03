import ee

# Initialize the Earth Engine module.
ee.Initialize()

# Print metadata for a DEM dataset.
nicfi = ee.ImageCollection('projects/planet-nicfi/assets/basemaps/americas')