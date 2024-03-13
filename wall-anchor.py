from build123d import *
from ocp_vscode import show
import os

# Units in mm
SCREW_DIAMETER = 4
SCREW_LENGTH = 10
GLUE_AREA_LENGTH = 25


class WallAnchor(Compound):
    """A basic adhesive wall anchor for keyhole slots"""

    def __init__(
        self,
        screw_diameter: int,
        screw_length: int,
        glue_area: int,
        plate_thickness: int,
        corner_radius: int = 2,
    ):
        with BuildPart() as bp:
            with BuildSketch():
                RectangleRounded(glue_area, glue_area, corner_radius)
            extrude(amount=plate_thickness)
            plate_edges=bp.faces().filter_by(Axis.Z).sort_by(Axis.Z).edges()
            with BuildSketch(bp.faces().filter_by(Axis.Z).sort_by(Axis.Z)[-1]):
                Circle(radius=screw_diameter/2 + 3)
            extrude(amount=screw_length-plate_thickness)
            boss_outer_edges = bp.edges(Select.LAST).filter_by(Plane.XY).sort_by(Axis.Z)
            with BuildSketch(bp.faces().filter_by(Axis.Z).sort_by(Axis.Z)[-1]):
                Circle(radius=screw_diameter/2)
            extrude(amount=-screw_length,mode=Mode.SUBTRACT)
            chamfer(bp.edges(Select.LAST).sort_by(Axis.Z)[0], length=0.4)
            top_edge = bp.faces().filter_by(Axis.Z).sort_by(Axis.Z)[-1].edges()
            chamfer(top_edge, length=0.6)
            fillet(boss_outer_edges[0], radius=3)          
            chamfer(plate_edges, length=0.4)

            
        super().__init__(bp.part.wrapped)


if __name__ == "__main__":
    my_anchor = WallAnchor(
        screw_diameter=SCREW_DIAMETER,
        screw_length=SCREW_LENGTH,
        glue_area=GLUE_AREA_LENGTH,
        plate_thickness=2,
    )
    show(my_anchor)
    try:
        os.mkdir("./output")
    except FileExistsError:
        pass
    my_anchor.export_step("output/wall_anchor.step")
