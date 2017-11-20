"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        matrix = []
        zig = False
        for i in range(numRows):
            matrix.append([])

        x, y = 0, 0

        for i in range(len(s)):
            matrix[y].append(s[i])
            if zig:
                if y == 0:
                    y = 1
                    zig = not zig
                else:
                    y -= 1
                    x += 1
            else:
                if y == numRows - 1:
                    y -= 1
                    x += 1
                    zig = not zig
                else:
                    y += 1

        return ''.join([letter for row in matrix for letter in row])

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
