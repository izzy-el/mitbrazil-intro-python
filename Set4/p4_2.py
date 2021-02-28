import math


def compare_result(x, y):
    if abs(x - y) <= 10 ** -6:
        return True
    else:
        return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)


class Triangle:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def side_lengths(self):
        first_side = ((self.first.x - self.second.x) ** 2 +
                      (self.first.y - self.second.y) ** 2) ** 0.5
        second_side = ((self.third.x - self.second.x) ** 2 +
                       (self.third.y - self.second.y) ** 2) ** 0.5
        third_side = ((self.third.x - self.first.x) ** 2 +
                      (self.third.y - self.first.y) ** 2) ** 0.5

        return(first_side, second_side, third_side)

    def angles(self):
        side_one, side_two, side_three = self.side_lengths()

        first_angle = math.acos(
            (side_one ** 2 + side_two ** 2 - side_three ** 2) / (2 * side_one * side_two))
        second_angle = math.acos(
            (side_two ** 2 + side_three ** 2 - side_one ** 2) / (2 * side_two * side_three))
        third_angle = math.acos(
            (side_three ** 2 + side_one ** 2 - side_two ** 2) / (2 * side_three * side_one))

        return (first_angle, second_angle, third_angle)

    def side_classification(self):
        list_sides = self.side_lengths()

        if compare_result(list_sides[0], list_sides[1]) and compare_result(list_sides[1], list_sides[2]) and compare_result(list_sides[2], list_sides[0]):
            return 'equilateral'
        if compare_result(list_sides[0], list_sides[1]) or compare_result(list_sides[1], list_sides[2]) or compare_result(list_sides[2], list_sides[0]):
            return 'isosceles'
        return 'scalene'

    def angle_classification(self):
        if self.is_right():
            return 'right'
        else:
            if math.pi / 3 in self.angles():
                return 'equiangular'
            else:
                for angle in self.angles():
                    if angle > math.pi / 2:
                        return 'obtuse'
                return 'acute'

    def is_right(self):
        for nums in self.angles():
            if compare_result(nums, math.pi / 2):
                return True
        return False

    def area(self):
        semi_perimeter = 0
        first_side, second_side, third_side = self.side_lengths()

        for lengths in self.side_lengths():
            semi_perimeter += lengths
        semi_perimeter *= 0.5

        result = (semi_perimeter * (semi_perimeter - first_side) *
                  (semi_perimeter - second_side) * (semi_perimeter - third_side)) ** 0.5

        return result

    def perimeter(self):
        perimeter = 0
        for numbers in self.side_lengths():
            perimeter += numbers

        return perimeter


test = Triangle(Point(2, 4), Point(4, 4), Point(3, 8))
print(test.angles())
print(test.is_right())
print(test.angle_classification())
print(test.side_lengths())
print(test.side_classification())
