import matplotlib.pyplot as plt
from typing import Union

class Figure:
    axes = plt.gca()

    def __init__(self, color, linestyle, ratio):
        self.color = color
        self.linestyle = linestyle
        self.ratio = ratio

    def draw(self):
        """"
        Открывает окно с созданным графиком
        """
        NotImplemented()

    def set_limits(self, x: Union[list, tuple], y: Union[list, tuple]) -> None:
        """
        Устанавливает координаты границ координатной прямой отталкиваясь от координат заданных точек

        input:
            x: кортеж или список из всех координат по оси X
            y: кортеж или список из всех координат по оси Y
        output:
            plt.xlim: минимальная и максимальная граница по оси X
            plt.ylim: минимальная и максимальная граница по оси Y
        """
        x_min, x_max = min(plt.xlim()), max(plt.xlim())
        y_min, y_max = min(plt.ylim()), max(plt.ylim())
        if min(x) < min(plt.xlim()):
            x_min = min(x) - 2
        if max(x) > max(plt.xlim()):
            x_max = max(x) + 2
        if min(y) < min(plt.ylim()):
            y_min = min(y) - 2
        if max(y) > max(plt.ylim()):
            y_max = max(y) + 2
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

    def rotate(self, degree=0):
        """"
        Поворачивает фигуру на 90, 180 и 270 градусов
        """
        NotImplemented()

    def shift(self, ax, ay):
        """"
        Двигает фигуру по оси X и Y
        """
        NotImplemented()

    @staticmethod
    def mirror_point(line_coord1: tuple[int, int], line_coord2: tuple[int, int], point: tuple[int, int]) -> tuple[float, float]:
        """
        Рассчитывыет зеркальное отражение точки относительно прямой заданной двумя координатами

        Формулы, по которым проводятся вычисления:
        k_degree = (y2 - y1) / (x2 - x1) - угловой коэффициент заданной прямой
        b_shift = y1 - ((y2 - y1) / (x2 - x1)) * x1 - свободный коэффициент заданной прямой
        k_perpend = (x1 - x2) / (y2 - y1)- угловой коэффициент перпендикулярной прямой
        b_perpend = p_y - ((x1 - x2) / (y2 - y1)) * p_x - свободный коэффициент перпендикулярной прямой
        mirror_x = ((b_perpend - b_shift) / (k_degree - k_perpend)) * 2 - p_x - рассчет координаты зеркальной точки по оси X
        mirror_y = (k_perpend * crossing_point_x + b_perpend) * 2 - p_y - рассчет координаты зеркальной точки по оси Y

        input:
            line_coord1: первая координата прямой, относительно которой будет происходить отзеркаливание
            line_coord2: вторая координата прямой, относительно которой будет происходить отзеркаливание
            point: координата точки, которую будем отзеркаливать
        output:
            crossing_point_x: координата зеркальной точки по оси X
            crossing_point_y: координата зеркальной точки по оси Y
        """
        x1, x2 = line_coord1[0], line_coord2[0]
        y1, y2 = line_coord1[1], line_coord2[1]
        p_x, p_y = point[0], point[1]
        crossing_point_x = (((p_y - (x1 - x2) / (y2 - y1) * p_x) - (y1 - ((y2 - y1) / (x2 - x1)) * x1)) / (
                (y2 - y1) / (x2 - x1) - (x1 - x2) / (y2 - y1))) * 2 - p_x
        crossing_point_y = ((x1 - x2) / (y2 - y1) * (
                    ((p_y - (x1 - x2) / (y2 - y1) * p_x) - (y1 - ((y2 - y1) / (x2 - x1)) * x1)) / (
                    (y2 - y1) / (x2 - x1) - (x1 - x2) / (y2 - y1))) + (
                                    p_y - ((x1 - x2) / (y2 - y1)) * p_x)) * 2 - p_y
        return crossing_point_x, crossing_point_y

    def mirror(self, line_coord1: tuple[int, int], line_coord2: tuple[int, int], original_figure=False, draw_line=False):
        NotImplemented()

    def remove(self) -> None:
        plt.clf()


class Line(Figure):
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    def __init__(self, coord1, coord2, color, linestyle='--', ratio='auto'):
        super().__init__(color, linestyle, ratio)
        self.coord1 = coord1
        self.coord2 = coord2

    def create(self, point_1: tuple[int, int]=(), point_2: tuple[int, int]=()) -> None:
        """
                Создает отрезок на оси координат
        input:
            point_1: первая точка отрезка
            point_2: вторая точка отрезка
        output:
            plt.plot:
        """
        if not point_1 and not point_2:
            point_1 = self.coord1
            point_2 = self.coord2
        self.set_limits(point_1, point_2)
        plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], color=self.color)

    def set_limits(self, coord1: tuple[int, int], coord2: tuple[int, int]) -> None:
        """
        Устанавливает координаты границ координатной прямой отталкиваясь от координат заданных точек

        input:
            x: кортеж координат по оси X
            y: кортеж координат по оси Y
        output:
            plt.xlim: минимальная и максимальная граница по оси X
            plt.ylim: минимальная и максимальная граница по оси Y
        """
        x_min, x_max = min(plt.xlim()), max(plt.xlim())
        y_min, y_max = min(plt.ylim()), max(plt.ylim())
        if min(coord1[0], coord2[0]) < min(plt.xlim()):
            x_min = min(coord1[0], coord2[0]) - 2
        if max(coord1[0], coord2[0]) > max(plt.xlim()):
            x_max = max(coord1[0], coord2[0]) + 2
        if min(coord1[1], coord2[1]) < min(plt.ylim()):
            y_min = min(coord1[1], coord2[1]) - 2
        if max(coord1[1], coord2[1]) > max(plt.ylim()):
            y_max = max(coord1[1], coord2[1]) + 2
        plt.xlim(x_min, x_max)
        plt.xlim(y_min, y_max)

    def draw(self) -> None:
        """"
        Открывает окно с созданным графиком
        """
        self.create()
        plt.show()

    def mirror(self, line_coord1: tuple[int, int], line_coord2: tuple[int, int], original_figure: [bool]=False, draw_line: [bool]=False) -> None:
        """
        Отзеркаливает линию относительно заданной прямой
        input:
            line_coord1: первая координата прямой, относительно которой будет происходить отзеркаливание
            line_coord2: вторая координата прямой, относительно которой будет происходить отзеркаливание
            original_figure: переменная, указывающая нужно ли отражать на оси координат изначальную фигуру
            draw_line: переменная, указывающая нужно ли отражать на оси координат линию относительно, которой будет
                    отражаться фигура
        output:
            plt.show: открывает созданный график
        Описание:
            С помощью заданных точек прямой(line_coord1, line_coord2) вызывается функция mirror_point, чтобы отразить
            каждую точку поочередно.
            Если условие с draw_line соблюдено, будет отображена линия, относительно которой будет идти отражение
            Если условие с original_figure соблюдено, будет отображена линия, которую нужно отразить
        """
        mirror_point_1 = self.mirror_point(line_coord1, line_coord2, self.coord1)
        mirror_point_2 = self.mirror_point(line_coord1, line_coord2, self.coord2)
        self.create(mirror_point_1, mirror_point_2)
        if draw_line:
            y_1 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * max(plt.xlim())
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            y_2 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * min(plt.xlim())
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            self.create((max(plt.xlim()), y_1), ((min(plt.xlim()), y_2)))
        if original_figure:
            self.draw()
        plt.show()


class Rectangle(Figure):
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    def __init__(self, coord1, width, height, color, linestyle='--', ratio='equal'):
        super().__init__(color, linestyle, ratio)
        self.coord1 = coord1
        self.width = width
        self.height = height

    def count_coord_x(self) -> tuple[int, int]:
        """
        Считает все координаты по оси X с помощью начальной координаты(self.coord1[0]) и прибавлением к ней
        ширины прямогугольника(self.width)

        output:
            point_x: создает кортеж со всеми координатами по оси X
        """
        point_x = (self.coord1[0], self.coord1[0] + self.width)
        return point_x

    def count_coord_y(self) -> tuple[int, int]:
        """
        Считает все координаты по оси Y с помощью начальной координаты(self.coord1[1]) и прибавлением к ней
        длины прямогугольника(self.height)

        output:
            point_y: создает кортеж со всеми координатами по оси Y
        """
        point_y = (self.coord1[1], self.coord1[1] + self.height)
        return point_y

    def create(self, x: [tuple[int, int]]=(), y: [tuple[int, int]]=(), point_1: [bool]=False) -> None:
        """
        Создает прямоугольник на координатной прямой
        input:
            x: кортеж со всеми координатами по оси X
            y: кортеж со всеми координатами по оси Y
            point_1: координаты точки начала построения
        output:
            plt.plot: создает график
        Описание:
            Если x и y не заданы, функция создает значения с помощью функциий: count_coord_x, count_coord_y. На основе точек
            на осях создается прямоугольник с точкой начала по координатам point_1
        """
        if not x and not y and not point_1:
            x = self.count_coord_x()
            y = self.count_coord_y()
            point_1 = x[0], y[0]
        self.set_limits(x, y)
        for coord in y:
            point_2 = x[0], coord
            plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], color=self.color)
            point_1 = point_2
        for coord in reversed(y):
            point_2 = x[1], coord
            plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], color=self.color)
            point_1 = point_2
        plt.plot([point_1[0], x[0]], [point_1[1], y[0]], color=self.color)

    def draw(self) -> None:
        self.create()
        plt.show()

    def mirror(self, line_coord1: tuple[int, int], line_coord2: tuple[int, int], original_figure: [bool]=False, draw_line: [bool]=False) -> None:
        """
        Отзеркаливает прямоугольник относительно заданной прямой
        input:
            line_coord1: первая координата прямой, относительно которой будет происходить отзеркаливание
            line_coord2: вторая координата прямой, относительно которой будет происходить отзеркаливание
            original_figure: переменная, указывающая нужно ли отражать на оси координат изначальную фигуру
            draw_line: переменная, указывающая нужно ли отражать на оси координат линию относительно, которой будет
                    отражаться фигура
        output:
            plt.show: открывает созданный график
        Описание:
            Создает кортеж изначальных координат на осях X, Y с помощью функций: count_coord_x, self.count_coord_y.
            С помощью заданных точек прямой(line_coord1, line_coord2) вызывается функция mirror_point, чтобы отразить
            точку начала построения прямоугольника.
            На основе отраженной точки начала построения и self.width рассчитывается вторая точка по оси X
            На основе отраженной точки начала построения и self.height рассчитывается вторая точка по оси Y
            Вызывается функция create для отображения на оси координат.
            Если условие с draw_line соблюдено, будет отображена линия, относительно которой будет идти отражение
            Если условие с original_figure соблюдено, будет отображена линия, которую нужно отразить
        """
        x = self.count_coord_x()
        y = self.count_coord_y()
        mirror_point1 = self.mirror_point(line_coord1, line_coord2, (x[0], y[0]))
        x_mirror = mirror_point1[0], mirror_point1[0] + self.width
        y_mirror = mirror_point1[1], mirror_point1[1] + self.height
        self.create(x_mirror, y_mirror, (x_mirror[0], y_mirror[0]))
        if draw_line:
            x_1 = max(x[0], x[1])
            x_2 = min(x[0], x[1])
            y_1 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * x_1
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            y_2 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * x_2
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            plt.plot((x_1, y_1), (x_2, y_2))
        if original_figure:
            self.draw()
        plt.show()


class Heart(Figure):
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    def __init__(self, coord1, coord2, coord3, coord4, coord5, coord6, color="r", linestyle='--', ratio='equal'):
        super().__init__(color, linestyle, ratio)
        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3
        self.coord4 = coord4
        self.coord5 = coord5
        self.coord6 = coord6

    def create_coord_lists(self) -> tuple[list, list]:
        """
        Создает списки координат по осям X, Y
        output:
            x_points: список координат по оси X
            y_points: список координат по оси Y
        Описание:
            На основе заданных точек считается вторая половина фигуры
                """
        list_of_points = [self.coord1, self.coord2, self.coord3, self.coord4, self.coord5, self.coord6]
        x_points = []
        y_points = []
        for point in list_of_points:
            x_points.append(point[0])
            y_points.append(point[1])
        for number in range((len(x_points)-2), -1, -1):
            mirror_point = -(x_points[number])
            x_points.append(mirror_point)
        for number in range((len(y_points)-2), -1, -1):
            y_points.append(y_points[number])
        return x_points, y_points

    def create(self, x: [list]=[], y: [list]=[]) -> None:
        """
        Создает сердце на координатной прямой
        input:
            x: список координат по оси X
            y: список координат по оси Y
        output:
            plt.plot: создает график
        Описание:
            Если x и y не заданы, функция создает значения с помощью функции create_coord_lists. На основе точек
            на осях с помощью цикла поочередно строятся линии.
                """
        if not x and not y:
            x = self.create_coord_lists()[0]
            y = self.create_coord_lists()[1]
        self.set_limits(x, y)
        for point in range(len(x)-1):
            plt.plot([x[point], x[point+1]], [y[point], y[point+1]], color=self.color, linestyle='--')

    def draw(self) -> None:
        self.create()
        plt.show()

    def mirror(self, line_coord1: tuple[int, int], line_coord2: tuple[int, int], original_figure: [bool]=False, draw_line: [bool]=False) -> None:
        """
        Отзеркаливает сердце относительно заданной прямой
        input:
            line_coord1: первая координата прямой, относительно которой будет происходить отзеркаливание
            line_coord2: вторая координата прямой, относительно которой будет происходить отзеркаливание
            original_figure: переменная, указывающая нужно ли отражать на оси координат изначальную фигуру
            draw_line: переменная, указывающая нужно ли отражать на оси координат линию относительно, которой будет
                    отражаться фигура
        output:
            plt.show: открывает созданный график
        Описание:
            Создает список изначальных координат на осях X, Y с помощью функции create_coord_lists.
            Создаются пустые списки, в которых будут находится отраженные точки на осях X, Y(x_mirror, y_mirror)
            С помощью заданных точек прямой(line_coord1, line_coord2) вызывается функция mirror_point, чтобы отразить
            каждую точку поочередно и добавить ее в созданные списки.
            Вызывается функция create для отображения на оси координат.
            Если условие с draw_line соблюдено, будет отображена линия, относительно которой будет идти отражение
            Если условие с original_figure соблюдено, будет отображена линия, которую нужно отразить
        """
        x = self.create_coord_lists()[0]
        y = self.create_coord_lists()[1]
        x_mirror, y_mirror = [], []
        for point in range(0, len(x)):
            mirror_point = self.mirror_point(line_coord1, line_coord2, (x[point], y[point]))
            x_mirror.append(mirror_point[0])
            y_mirror.append(mirror_point[1])
        self.create(x_mirror, y_mirror)
        if draw_line:
            x_1 = max(self.create_coord_lists()[0]) * 100
            x_2 = min(self.create_coord_lists()[0]) * 100
            y_1 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * x_1
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            y_2 = ((line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * x_2
                   + line_coord1[1] - (line_coord2[1] - line_coord1[1]) / (line_coord2[0] - line_coord1[0]) * line_coord1[0])
            plt.plot((x_1, y_1), (x_2, y_2))
        if original_figure:
            self.draw()
        plt.show()


if __name__ == "__main__":
    line = Line([3, 4], [7, 5], "r")
    line.draw()
    line.mirror((2, 3), (4, -3), True, True)
    rect = Rectangle((2, 3), 2, 1, "r")
    rect.draw()
    rect.mirror((-1, 7), (6, 8), True, True)
    heart = Heart((0, -6), (-3, -4), (-3, 2), (-2, 3), (-1, 3), (0, 2))
    heart.draw()
    heart.mirror((-2, -8), (1, -10), True, True)
