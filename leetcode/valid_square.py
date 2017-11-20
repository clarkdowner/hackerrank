"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        self.x_hash = {}
        self.y_hash = {}
        self.x_keys = []
        self.y_keys = []

        self.add_to_hash(p1)
        self.add_to_hash(p2)
        self.add_to_hash(p3)
        self.add_to_hash(p4)

        for key in self.x_hash:
            if self.x_hash[key] != 2:
                return False
            self.x_keys.append(key)

        for key in self.y_hash:
            if self.y_hash[key] != 2:
                return False
            self.y_keys.append(key)

        if abs(self.x_keys[0] - self.x_keys[1]) != abs(self.y_keys[0] - self.y_keys[1]):
            return False
        return True

    def add_to_hash(self, coord):
        if coord[0] in self.x_hash:
            self.x_hash[coord[0]] += 1
        else:
            self.x_hash[coord[0]] = 1

        if coord[1] in self.y_hash:
            self.y_hash[coord[1]] += 1
        else:
            self.y_hash[coord[1]] = 1
