# knime-python-spatial-statistic-nodes

Spatial statistic nodes plugin for Knime. See the document [here](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html#introduction).


## Installation





## Usage






## How to contribute

### General suggestions

- Create one repository per Python node extension
- If the extension contains several nodes create a file for each node group e.g., IO, analysis,
views

### Clone the repository

```bash
git clone https://github.com/spatial-data-lab/knime-python-spatial-statistic-nodes.git
```

### Setup the developing environment

See [here](https://docs.google.com/presentation/d/1lZh2QeJ0kcU82CSokTQlLnFwjFE4V57Q/edit?usp=sharing&ouid=102101640576662100418&rtpof=true&sd=true) or the materials folder in the repository
### Understand the structure of the project


    .
    ├── LICENSE
    ├── README.md
    ├── config.yml
    ├── docs
    ├── icons
    │   └── icon.png
    ├── materials
    │   ├── Build KNIME Python Geospatial tools.pptx
    │   └── DevSetup.pdf
    ├── my_conda_env.yml
    ├── src
    │   ├── LICENSE.TXT
    │   ├── __init__.py
    │   ├── category.py
    │   ├── icon.png
    │   ├── knime.yml
    │   ├── spatial_statistic.py (should import user defined python module here)
    │   ├── spatial_weights_nodes.py (user defined code here, different contributors can have different module, each module can have several nodes)
    │   └── transformer_nodes.py (user defined code here)
    └── tests
        ├── GeoExtensionNodes_v0.1.knwf
        └── data
            └── baltim.gpkg


### Test

[Test guideline ](https://docs.google.com/document/d/1XrJFvqVCreyBGRcP9M-M9afq0l5gFGIMxk_SUpno1yc/edit?usp=sharing)
## Todo

- [ ] Add Installation and usage instructions
- [ ] Add structure details of the project
## License


## References

[KNIMEGeoNodes20220603.xlsx](https://docs.google.com/spreadsheets/d/1qXoCPaJtxtbdXp7wjqliCQ7hAWkyBObF/edit?usp=sharing&ouid=102101640576662100418&rtpof=true&sd=true)

[CGAtransfer - Google Drive](https://drive.google.com/drive/folders/1WhZ6lURlsPx4YbSZWPyv2QRGDPnkofdk?usp=sharing)


[Spatiotemporal Simulation Analysis](http://129.174.21.126:8080/knime/webportal/space/)

