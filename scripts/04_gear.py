ext_r = 4
height = 1
int_r = 1
holes_r = ext_r - (ext_r - int_r) / 2
hole_r = 0.3

solid = (
    cq.Workplane("front")
    .circle(ext_r)
    .circle(int_r)
    .pushPoints(
        [
            (holes_r, 0),
            (holes_r**(1/2), holes_r**(1/2)),
            (0, holes_r),
            (-holes_r**(1/2), holes_r**(1/2)),
            (-holes_r, 0),
            (holes_r**(1/2), -holes_r**(1/2)),
            (0, -holes_r),
            (-holes_r**(1/2), -holes_r**(1/2))
        ]
    )
    .circle(hole_r)
    .extrude(height)
)

show_object(solid)

cq.exporters.export(solid, "04_gear.stl")