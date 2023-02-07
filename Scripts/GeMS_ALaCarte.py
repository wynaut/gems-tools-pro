﻿"""Add GeMS objects a la carte to a geodatabase

    Create or augment a GeMS or GeMS-like file geodatabase by adding one or more
    objects as needed

    Attributes:
        gdb (string): path to an existing file geodatbase. Use the new file
        geodatabase context menu option when browsing to a folder to create 
        an new empty geodatabase

        gdb_items (list): a list of new GeMS ojbects to add to the gdb. Each list
        can have three items;
        [[new or existing feature dataset, spatial reference of fd, table]]
"""

import arcpy
import GeMS_Definition as gdef
from pathlib import Path


def process(gdb, value_table):
    # if gdb doesn't exist, make it
    if not Path(gdb).exists:
        folder = Path(gdb).parent
        name = Path(gdb).stem
        arcpy.CreateFileGDB_management(folder, name)

    arcpy.AddMessage(value_table)

    # collect the values from the valuetable
    for i in range(0, value_table.rowCount):
        fd = value_table.getValue(i, 0)
        sr_prj = value_table.getValue(i, 1)
        fc = value_table.getValue(i, 2)

        # if not fd in ['', ' ', '#', None:

        sr = arcpy.SpatialReference()
        sr.loadFromString(value_table.getValue(i, 1))


if __name__ == "__main__":
    gdb = sys.argv[1]
    # gdb_items = sys.argv[2]
    value_table = arcpy.GetParameter(1)
    process(gdb, value_table)
