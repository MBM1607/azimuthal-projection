import cartopy
import matplotlib.pyplot as plt


def main():
    kabah_longitude, kabah_latitude = 39.826206, 21.422487
    plt.figure()
    ax = plt.axes(
        projection=cartopy.crs.AzimuthalEquidistant(
            central_latitude=kabah_latitude, central_longitude=kabah_longitude
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
        kabah_longitude,
        kabah_latitude,
        color="#ED2939",
        marker="o",
        transform=cartopy.crs.Geodetic(),
    )

    plt.show()


if __name__ == "__main__":
    main()
