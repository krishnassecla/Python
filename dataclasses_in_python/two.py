from dataclasses import dataclass
import dataclasses


@dataclass
class Point:
    x: float
    _: dataclasses.KW_ONLY
    # any field below it are keywords only field
    y: float
    z: float


p = Point(1, y=2, z=3)
