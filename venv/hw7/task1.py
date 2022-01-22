# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        for row in self.m_list:
            for i in row:
                print(f"{i:4}", end='')
                print()
            return ''

    def __add__(self, other):
        for i in range(len(self.m_list)):
            for i_2 in range(len(other.m_list[i])):
                self.m_list[i][i_2] = self.m_list[i][i_2] + other.m_list[i][i_2]
        return Matrix.__str__(self)


mx = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_mx = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(mx.__add__(new_mx))
