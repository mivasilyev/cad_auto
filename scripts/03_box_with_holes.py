height = 30.0
width = 5.0
thickness = 20.0
diameter1 = 4.0
diameter2 = 3.0

solid = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">X")
    .workplane()
    .hole(diameter1)
    .faces(">Z")
    .workplane()
    .center(-10, 0)
    .hole(diameter2)
)

show_object(solid)

cq.exporters.export(solid, "03_box_with_holes.stl")