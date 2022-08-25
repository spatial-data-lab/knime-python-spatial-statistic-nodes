import logging
import knime_extension as knext
import pandas as pd
import geopandas as gp
import geo_category
LOGGER = logging.getLogger(__name__)


@knext.node(name="CRS Transformer", node_type=knext.NodeType.MANIPULATOR, icon_path="icon.png", category=geo_category.category)
@knext.input_table(name="Geo table", description="Table with geometry column to transform")
@knext.output_table(name="Transformed geo table", description="Transformed Geo input table")
class CrsTransformerNode:
    """

    This node projects the data from its original CRS to the entered CRS.
    """

    new_crs = knext.StringParameter("New CRS", "The new CRS system to use", "3857")

    def configure(self, configure_context, input_schema_1):
        return input_schema_1
 
    def execute(self, exec_context:knext.ExecutionContext, input_1):
        gdf=gp.GeoDataFrame(input_1.to_pandas())
        exec_context.set_progress(0.3, "Geo data frame loaded. Starting projection...")
        gdf=gdf.to_crs(self.new_crs)
        exec_context.set_progress(0.1, "Projection done")
        #is always raising an error even if I haven't canceled the node
#        if exec_context.is_canceled: 
#            raise RuntimeError("Execution canceled")
        LOGGER.debug("CRS converted to " + self.new_crs)
        
        #why do we need to convert the GeoDataFrame into a pandas data frame???
        return knext.Table.from_pandas(pd.DataFrame(gdf))


        
@knext.node(name="Compute Area", node_type=knext.NodeType.MANIPULATOR, icon_path="icon.png", category=geo_category.category)
@knext.input_table(name="Geo table", description="Table with geometry column to compute the area for")
@knext.output_table(name="Geo table with area", description=" Geo input table with additional area column")
class ComputeAreaNode:
    """
    This node computes the area of a geo cell.
    """

    def configure(self, configure_context, input_schema_1):
        return input_schema_1.append(knext.Column(knext.double(), "area"))
 
    def execute(self, exec_context, input_1):
        gdf=gp.GeoDataFrame(input_1.to_pandas())
        gdf['area']=gdf.area
        #why do we need to convert the GeoDataFrame into a pandas data frame???
        return knext.Table.from_pandas(pd.DataFrame(gdf))
        