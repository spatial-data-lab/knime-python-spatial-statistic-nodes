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

1. [Download](https://www.knime.com/nightly-build-downloads) and install the knime4.7
2.  Install Knime extension. Open Knime and click KNIME -> File-> Install KNIME Extensions, Search for Python and select `KNIME Python Extension Development (Labs)`,`KNIME Python Integration (Labs) `, Disable the “Group items by category” option Search for geo and select  `KNIME Geospatial Nodes`.
3. Build New Python Environment for Geospatial Nodes
```bash
conda create -n my_python_env python=3.9 knime-python-base knime-extension geopandas -c knime -c conda-forge 

conda activate my_python_env

conda install libpysal scipy # if you use these packages, please install here too

conda info
# Record the env location path such as D:\ProgramData\Anaconda3\envs\my_python_env 

```
4. Configure the Knime python setting.  
KNIME -> File-> Preference> KNIME> Conda  Choose anaconda directory
KNIME -> File-> Preference> KNIME> Python(Labs) Choose my_python_env
KNIME -> File-> Preference> KNIME> Python(Labs) Choose my_python_env
* This step is not necessary unless you installed KNIME Python Integration
5. Clone this repository

```bash
git clone  https://github.com/spatial-data-lab/knime-python-spatial-statistic-nodes.git

```
6. Configure the project settings

`my_conda_env.yml` contains the dependencies of our python code, if we use some python package, we need add the information here

`config.yml` is the main configuration of our project.  

7. Configure knime.ini and All set. Add the following line to your knime.ini file which should point to config.yml file within the extracted folder.

`-Dknime.python.extension.config=D:\Software\knime_470\knimespace\geo\config.yml`

8. Reopen the Knime and you should see the extension in your Knime node repository.



More details see [here](https://docs.google.com/presentation/d/1lZh2QeJ0kcU82CSokTQlLnFwjFE4V57Q/edit?usp=sharing&ouid=102101640576662100418&rtpof=true&sd=true) or the materials folder in the repository

9. Add new file in src folder

10. Make sure you have install all the package you used in your python script too (for example `libpysal`  )

### Build



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
