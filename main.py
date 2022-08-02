import matplotlib.pyplot as plt
import cartopy

my_lon, my_lat = 39.826206, 21.422487
plt.figure()
ax = plt.axes(
    projection=cartopy.crs.AzimuthalEquidistant(
        central_latitude=my_lat, central_longitude=my_lon
    )
)

ax.stock_img()
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle="dotted")
ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
ax.add_feature(cartopy.feature.RIVERS)

ax.set_global()
ax.gridlines()

plt.plot(
    my_lon,
    my_lat,
    color="#ED2939",
    marker="o",
    transform=cartopy.crs.Geodetic(),
)

plt.show()
