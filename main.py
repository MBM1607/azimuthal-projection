import matplotlib.pyplot as plt
import cartopy.crs as ccrs

my_lon, my_lat = 39.826206, 21.422487
plt.figure(figsize=(3, 3))
ax = plt.axes(
    projection=ccrs.AzimuthalEquidistant(
        central_latitude=my_lat, central_longitude=my_lon
    )
)
ax.coastlines(resolution="110m")
ax.gridlines()
ax.stock_img()

plt.plot(
    my_lon,
    my_lat,
    color="green",
    marker="o",
    transform=ccrs.Geodetic(),
)

plt.text(
    my_lon - 5,
    my_lat + 4,
    "Makkah",
    horizontalalignment="left",
    transform=ccrs.Geodetic(),
)

plt.show()
