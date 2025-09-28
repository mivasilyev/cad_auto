height = 30.0
width = 20.0
thickness = 10.0
diameter = 22.0
edge = 1.0

solid = (
    cq.Workplane('XY')
    .box(height, width, thickness)
    .edges('|X')
    .fillet(edge)
    .edges('|Y')
    .fillet(edge)
)

show_object(solid)

cq.exporters.export(solid, "01_basic_rounded_box.stl")