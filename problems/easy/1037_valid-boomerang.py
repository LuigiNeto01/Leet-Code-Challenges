class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        # Extract coordinates for readability
        p1, p2, p3 = points[0], points[1], points[2]
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        # Step 1: Check if all three points are distinct
        # If any two points are the same, they cannot form a boomerang
        if p1 == p2 or p2 == p3 or p1 == p3:
            return False
        
        # Step 2: Check collinearity using cross product (determinant method)
        # Compute the area of the triangle formed by the three points
        # If area == 0, points are collinear (in a straight line)
        # Avoid floating point division: use cross product formula directly
        # (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1)
        # This compares slopes: (y2-y1)/(x2-x1) == (y3-y1)/(x3-x1) without division
        area_twice = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        
        # Return True only if area is non-zero (not collinear)
        return area_twice != 0