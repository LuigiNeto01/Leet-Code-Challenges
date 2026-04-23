from __future__ import annotations
import random
import math
from typing import List

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        # store circle parameters for use by randPoint
        # radius may be zero; handle that in randPoint
        self.radius = float(radius)
        self.xc = float(x_center)
        self.yc = float(y_center)

    def randPoint(self) -> List[float]:
        # If radius is zero, always return the center (degenerate circle)
        if self.radius == 0.0:
            return [self.xc, self.yc]

        # Generate a uniformly random angle in [0, 2*pi)
        theta = random.random() * 2.0 * math.pi

        # Generate radius with distribution proportional to r (area element).
        # Use sqrt(u) where u ~ U(0,1) so that PDF of r is uniform over area.
        r = self.radius * math.sqrt(random.random())

        # Convert polar coordinates (r, theta) to Cartesian coordinates
        x = self.xc + r * math.cos(theta)
        y = self.yc + r * math.sin(theta)

        return [x, y]