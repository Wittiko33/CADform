from build123d import *
from ocp_vscode import show

# Units in mm
SCREW_DIAMETER = 4
SCREW_LENGTH = 10
GLUE_AREA_LENGTH = 25


class WallAnchor(Compound):
    """A basic adhesive wall anchor for keyhole slots"""
    def __init__(self, screw_diameter: int, screw_length:int, glue_area:int, plate_thickness:int, corner_radius:int=2):
        with BuildPart() as bp:
            with BuildSketch():
                RectangleRounded(glue_area, glue_area, corner_radius)
            extrude(amount=plate_thickness)
        super().__init__(bp.part.wrapped)




if __name__=="__main__":
    my_anchor = WallAnchor(screw_diameter=SCREW_DIAMETER, screw_length=SCREW_LENGTH, glue_area=GLUE_AREA_LENGTH, plate_thickness=2)
    show(my_anchor)
