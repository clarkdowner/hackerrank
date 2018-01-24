"""
https://www.codewars.com/kata/coloured-lattice-points-forming-coloured-triangles
"""


def count_col_triang(input_pts):
    color_map, triangles = {}, {}

    def get_num_triangles(pts):
        tot, ct = 0, len(pts)
        for i in range(ct-2):
            for j in range(i+1, ct-1):
                for k in range(j+1, ct):
                    if is_valid_triangle(pts[i], pts[j], pts[k]):
                        tot += 1
        return tot

    def is_valid_triangle(coord1, coord2,coord3):
        return three_by_det(coord1[0], coord1[1], 1, coord2[0], coord2[1], 1, coord3[0], coord3[1], 1) != 1

    def three_by_det(a, b, c, d, e, f, g, h, i):
        # return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
        return a*(two_by_det(e, f, h, i)) - b*(two_by_det(d, f, g, i)) + c*(two_by_det(d, e, g, h))

    def two_by_det(a, b, c, d):
        return a*d - b*c

    for point in input_pts:
        if point[1] in color_map:
            color_map[point[1]].append(point[0])
        else:
            color_map[point[1]] = [point[0]]

    for color in color_map:
        if len(color_map[color]) > 2:
            triangles[color] = get_num_triangles(color_map[color])

    tri_ct, tri_tot, tri_colors = 0, 0, []
    for color in triangles:
        c = triangles[color]
        if c > tri_ct:
            tri_colors, tri_ct = [color], c
        elif c == tri_ct:
            tri_colors.append(color)
        tri_tot += c
    print(sorted(tri_colors))
    s_colors = sorted(tri_colors)
    print(type(s_colors))
    points = len(input_pts)
    colors = len(color_map.keys())
    most = s_colors.append(tri_ct)
    print(tri_ct)
    return [points, colors, tri_tot, most]


print(count_col_triang(
    [
        [[3, -4], 'blue'],
        [[-7, -1], 'red'],
        [[7, -6], 'yellow'],
        [[2, 5], 'yellow'],
        [[1, -5], 'red'],
        [[1, 1], 'red'],
        [[1, 7], 'red'],
        [[1, 4], 'red'],
        [[-3, -5], 'blue'],
        [[4, 1], 'blue']
    ]))

