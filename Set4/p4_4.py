class Vector:
    def __init__(self, lst):
        self.lst = lst

    def as_list(self):
        return self.lst
    
    def size(self):
        return len(self.lst)
    
    def magnitude(self):
        total = 0

        for vectors in self.as_list():
            total += vectors ** 2

        return total ** 0.5
    
    def euclidean_distance(self, other):
        total = 0

        for i, j in zip(self.lst, other.lst):
            total += (j - i) ** 2
        
        return total ** 0.5
    
    def normalized(self):
        normalized_vector = []
        for nums in self.lst:
            normalized_vector.append(nums / self.magnitude())
        
        return Vector(normalized_vector)

    def cosine_similarity(self, other):
        dot_product = 0
        for i, j in zip(self.as_list(), other.as_list()):
            dot_product += i * j

        return dot_product / (self.magnitude() * other.magnitude())
    
    # Dunder Methods
    def __add__(self, other):
        sum_of_vectors = []
        if self.size() == other.size():
            for i, j in zip(self.as_list(), other.as_list()):
                sum_of_vectors.append(i + j)
            return Vector(sum_of_vectors)
        else:
            return None
    
    def __sub__(self, other):
        sub_of_vectors = []
        if self.size() == other.size():
            for i, j in zip(self.as_list(), other.as_list()):
                sub_of_vectors.append(i - j)
            return Vector(sub_of_vectors)
        else:
            return None

    def __mul__(self, other):
        dot_product = 0
        _list_ = []
        if isinstance(other, Vector) and self.size() == other.size():
            for i, j in zip(self.as_list(), other.as_list()):
                dot_product += i * j
            return dot_product
        elif isinstance(other, Vector) and self.size() != other.size():
            return None
        elif isinstance(other, (int, float)):
            for nums in self.as_list():
                _list_.append(nums * other)
            return Vector(_list_)
        else:
            return None

    def __truediv__(self, other):
        _list_ = []
        if isinstance(other, (int, float)):
            for nums in self.as_list():
                _list_.append(nums / other)
            return Vector(_list_)
        else:
            return None


num_one = Vector([1, 2, 3, 4])
num_two = Vector([5, 6, 7, 8])

print(num_one.euclidean_distance(num_two))
print(num_one.normalized().as_list())