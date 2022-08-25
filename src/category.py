#This defines the Geospatial KNIME category that is displayed in the node repository
import knime_extension as knext
category = knext.category(
    path="/",
    level_id="spatialstatistic",
    name="spatial statistic",
    description="spatial statistic nodes",
    icon="../icons/icon.png",
)