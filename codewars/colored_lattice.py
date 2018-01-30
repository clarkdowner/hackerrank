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

    def is_valid_triangle(c1, c2, c3):
        return th_det(c1[0], c1[1], 1, c2[0], c2[1], 1, c3[0], c3[1], 1) != 0

    def th_det(a, b, c, d, e, f, g, h, i):
        return a*(tw_det(e, f, h, i)) - b*(tw_det(d, f, g, i)) + c*(tw_det(d, e, g, h))

    def tw_det(a, b, c, d):
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

    s_colors = sorted(tri_colors)
    s_colors.append(tri_ct)

    points = len(input_pts)
    colors = len(color_map.keys())

    return [points, colors, tri_tot, [] if tri_tot == 0 else s_colors]
