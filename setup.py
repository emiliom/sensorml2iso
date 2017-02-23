from setuptools import setup

kwargs = {
    "name": "sensorml2iso",
    "author": "Micah Wengren",
    "author_email": "micah.wengren@gmail.com",
    "url": "https://github.com/ioos/sensorml2iso",
    "description": "A small utility to convert IOOS SOS SensorML to ISO19115-2 for IOOS Catalog",
    "entry_points": {
        "console_scripts": [
            "sensorml2iso=sensorml2iso.command_line:main",
        ]
    },
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    "packages": ["sensorml2iso"],
    "package_data": {
        "templates": [
            "*.xml"
        ]
    },
    "install_requires": [
        "OWSLib>=0.11.0",
        "flake8>=2.5.1",
        "geopandas>=0.2.1",
        "jinja2>=2.7",
        "lxml>=3.5.0",
        "numpy>=1.11.2",
        "pandas>=0.19.0",
        "pyoos>=0.8.2",
        "shapely>=1.5.16"
    ],
    "version": "1.0.1",
}

setup(**kwargs)
