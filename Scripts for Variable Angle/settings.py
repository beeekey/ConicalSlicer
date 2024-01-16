from common import ConeType


#######################################################################
# General Settings
#######################################################################
CONE_ANGLE = 16                                 # Transformation angle
CONE_TYPE = ConeType.OUTWARD            # type of the cone: 'ConeType.INWARD' & 'ConeType.OUTWARD'

#######################################################################
# STL Settings
#######################################################################

STL_FILE_NAME = 'Tor_Prop_5in002'                       # Filename without extension
STL_FOLDER_NAME_UNTRANSFORMED = 'stl'
STL_FOLDER_NAME_TRANSFORMED = 'stl_transformed'   # Make sure this folder exists
REFINEMENT_ITERATIONS = 1                       # refinement iterations of the stl. 2-3 is a good start for regular stls. If its already uniformaly fine, use 0 or 1. High number cause huge models and long script runtimes
TRANSFORMATION_TYPE = CONE_TYPE                # type of the cone: 'inward' & 'outward'

#######################################################################
# GCODE Settings
#######################################################################

GCODE_FILENAME= 'Tor_Prop_5in002_outward_16deg_transformed_PLA_1h6m.gcode'      # filename including extension
GCODE_FOLDERNAME= 'gcodes/'             # name of the subfolder in which the gcode is located
FIRST_LAYER_HEIGHT = 0.2
BED_WIDTH_X = 200
BED_DEPTH_Y = 190
START_GCODE_INSERT_AFTER = "M104"
START_GCODE = '''
G28 ; home all axes
G1 Z10 ; rise head to move in middle without collision
G1 X100 Y100 ; move in middle of bed
G1 Z2 ; lower head
G92 E0 ; reset extrusion distance
M117 NG printing..
'''
END_GCODE = '''
M104 S0 T0 ; shutdown extruder T0
M104 S0 T1 ; shutdown extruder T1
M140 S0 ; shutdown bed
G1 Z200 ; lower bed
G28 X0 Y0 ; home X and Y
M84 ; communicate program end
'''