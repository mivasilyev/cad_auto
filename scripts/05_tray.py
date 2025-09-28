thickness = 1.0
length = 9.0
width = 6.0
height = 1.0

solid = (
    cq.Workplane("front")
    .rect(length, width)
    .rect(length - thickness, width - thickness)
    .extrude(height)
)

show_object(solid)

cq.exporters.export(solid, "05_tray.stl")
