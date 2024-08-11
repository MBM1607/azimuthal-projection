# Introduction

Azimuthal equidistant projection centered on the holy Kabbah, created using cartopy.

Cartopy is a Python package designed for geospatial data processing in order to produce maps and
other geospatial data analyses.

Cartopy makes use of the powerful **PROJ.4**, **NumPy** and **Shapely** libraries and includes a
programmatic interface built on top of Matplotlib for the creation of publication quality maps.

## Development

First we setup a virtual environment to avoid conflicts with other python packages.

```bash
python -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

After that we install the required packages

```bash
pip install -r requirements.txt
```

## Running the code

To run the code, simply execute the following command

```bash
python main.py
```

## Projection Around Kabbah

![projection](projection.png)
