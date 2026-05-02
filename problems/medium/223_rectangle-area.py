class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate area of rectangle A
        area_a = (ax2 - ax1) * (ay2 - ay1)
        
        # Calculate area of rectangle B
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate overlap region (intersection)
        # For x-axis: overlap exists if max(left edges) < min(right edges)
        overlap_x1 = max(ax1, bx1)
        overlap_x2 = min(ax2, bx2)
        
        # For y-axis: overlap exists if max(bottom edges) < min(top edges)
        overlap_y1 = max(ay1, by1)
        overlap_y2 = min(ay2, by2)
        
        # Calculate overlap area
        # If no overlap, width or height will be negative/zero, so we use max with 0
        overlap_width = max(0, overlap_x2 - overlap_x1)
        overlap_height = max(0, overlap_y2 - overlap_y1)
        overlap_area = overlap_width * overlap_height
        
        # Total area = sum of both areas minus the overlapping part (to avoid double counting)
        return area_a + area_b - overlap_area