from build123d import *
from ocp_vscode import show

# Units in mm
SCREW_DIAMETER = 4
SCREW_LENGTH = 10
GLUE_AREA_LENGTH = 25


class WallAnchor(Compound):
    """A basic adhesive wall anchor for keyhole slots"""
    def __init__(self, screw_diameter: int, screw_length:int, glue_area:int):
        with BuildPart() as bp:
            with BuildSketch:
                RectangleRounded(glue_area, glue_area, 2)
        super().__init__(bp.part.wrapped)




if __name__=="__main__":
    pass
