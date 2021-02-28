#I developed this based on an answer the instructor wrote on Piazza

def hailstone_sequence(a_0):
    if a_0 == 1:
        return [a_0] #in case a_0 == 1
    elif a_0 % 2 == 0:
        return [a_0] + hailstone_sequence(a_0 / 2)
    else:
        return [a_0] + hailstone_sequence(a_0 * 3 + 1)
        
# print(hailstone_sequence(21))

'''Recursion'''
# def hailstone_sequence(a_0):
#     _list.append(int(a_0))
#     if a_0 == 1:
#         return _list
#     elif a_0 % 2 == 0:
#         a_0 = int(a_0 // 2)
#         return hailstone_sequence(a_0)
#     else:
#         a_0 = int((3 * a_0) + 1)
#         return hailstone_sequence(a_0)

# print(hailstone_sequence(21))

'''Iteration'''
# def hailstone_sequence(a_0):
#     while a_0 != 1:
#         _list.append(a_0)
#         if a_0 % 2 == 0:
#             a_0 /= 2
#         elif a_0 % 2 != 0:
#             a_0 = (3 * a_0) + 1
#     _list.append(1.0)
#     return _list

# print(hailstone_sequence(21))