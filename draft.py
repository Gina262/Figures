# def a(line_coord1, line_coord2, point):
#     k_degree = (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0])
#     b_shift = line_coord1[1] - k_degree * line_coord1[0]
#     k_perpend = (-1) / k_degree
#     b_perpend = point[1] - k_perpend * point[0]
#     crossing_point_x = (b_perpend - b_shift) / (k_degree - k_perpend)
#     crossing_point_y = k_perpend * crossing_point_x + b_perpend
#     mirror_x = crossing_point_x * 2 - point[0]
#     mirror_y = crossing_point_y * 2 - point[1]
#     print(mirror_x, mirror_y)
#     return mirror_x, mirror_y
#
#
# def b(line_coord1, line_coord2, point):
#     x1, x2 = line_coord1[0], line_coord2[0]
#     y1, y2 = line_coord1[1], line_coord2[1]
#     p_x, p_y = point[0], point[1]
#     print(x1, x2, y1, y2, p_x, p_y)
#     k_degree = (y2 - y1) / (x2 - x1)
#     b_shift = y1 - ((y2 - y1) / (x2 - x1)) * x1
#     k_perpend = (x1 - x2) / (y2 - y1)
#     b_perpend = p_y - ((x1 - x2) / (y2 - y1)) * p_x
#     crossing_point_x = (((p_y - (x1 - x2) / (y2 - y1) * p_x) - (y1 - ((y2 - y1) / (x2 - x1)) * x1)) / (
#                 (y2 - y1) / (x2 - x1) - (x1 - x2) / (y2 - y1))) *2 - p_x
#     crossing_point_y = ((x1 - x2) / (y2 - y1) * (((p_y - (x1 - x2) / (y2 - y1) * p_x) - (y1 - ((y2 - y1) / (x2 - x1)) * x1)) / (
#                 (y2 - y1) / (x2 - x1) - (x1 - x2) / (y2 - y1))) + (
#                                    p_y - ((x1 - x2) / (y2 - y1)) * p_x)) *2 - p_y
#     print(crossing_point_x, crossing_point_y)
#     return crossing_point_x, crossing_point_y
#
# a((-3, -1), (-1, -2), (2, 3))
# b((-3, -1), (-1, -2), (2, 3))