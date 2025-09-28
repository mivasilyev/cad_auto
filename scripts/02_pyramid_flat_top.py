base_side = 110.0
height = 45.0

solid = (
    cq.Workplane("XY")
    .rect(1.4 * base_side, base_side)
    .extrude(height, taper=40)
)

show_object(solid)

cq.exporters.export(solid, "02_pyramid_with_flat_top.stl")
