import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np

band3 = rasterio.open('LE07_L1TP_195021_20000929_20170209_01_T1_B3.TIF') #red
band4 = rasterio.open('LE07_L1TP_195021_20000929_20170209_01_T1_B4.TIF') #nir

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.tight_layout()

#generate nir and red objects as arrays in float64 format
red = band3.read(1).astype('float64')
nir = band4.read(1).astype('float64')

np.seterr(divide='ignore', invalid='ignore')
#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where(
    (nir+red)==0.,
    0,
    (nir-red)/(nir+red))
#export ndvi image
ndviImage = rasterio.open('ndviImage.tiff','w',driver='Gtiff',
                          width=band3.width,
                          height = band3.height,
                          count=1, crs=band3.crs,
                          transform=band3.transform,
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()
#plot ndvi
ndvi = rasterio.open('ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)
