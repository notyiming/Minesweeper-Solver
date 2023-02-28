
# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

# ------------------------------------------------
#
#   ALGORITHM 1: count_inversions_n2
#
#   COMPLEXITY: n2
#
# ------------------------------------------------

# ------------------------------------------
# FUNCTION count_inversions_n2
# ------------------------------------------
import math
import multiprocessing


# def count_inversions_n2(my_rank_list):
#     # 1. We create the output variable
#     res = 0

#     # 2. We compute the length of the list
#     size = len(my_rank_list)

#     # 3. We iterate to compute the number of inversions
#     for i in range(size):
#         for j in range(i+1, size):
#             # 3.1. If A[i] > A[j] we increase the number of inversions
#             if my_rank_list[i] > my_rank_list[j]:
#                 res = res + 1

#     # 4. We return res
#     return res

# # ------------------------------------------------
# #
# #   ALGORITHM 2: mergesort_and_count_inversions
# #
# #   COMPLEXITY: n logn
# #
# # ------------------------------------------------

# # ------------------------------------------
# # FUNCTION: merge_count_inversions
# # ------------------------------------------
# def merge_count_inversions(l1, l2):
#     # 1. We create the output variable
#     res = ()

#     # 1.1. We create the sort_list
#     sort_list = []

#     # 1.2. We create the num_inversions
#     num_inversions = 0

#     # 2. Auxiliary variables

#     # 2.1. size_l1: Size of sub-list l1
#     size_l1 = len(l1)

#     # 2.2. size_l2: Size of sub-list l2
#     size_l2 = len(l2)

#     # 2.3. i: index being explored in sub-list l1
#     i = 0

#     # 2.4. j: index being explored in sub-list l2
#     j = 0

#     # 3. We merge both lists and count
#     while (size_l1 > 0) or (size_l2 > 0):
#         # 3.1. Case where both l1 and l2 have elements
#         if (size_l1 > 0) and (size_l2 > 0):
#             # 3.1.1. If the first element is the smallest
#             if (l1[i] <= l2[j]):
#                 # I. We add it to the list
#                 sort_list.append(l1[i])
#                 # II. We get one element less in the first list
#                 size_l1 = size_l1 - 1
#                 # III. We increase the index for the first list
#                 i = i + 1

#             # 3.1.2. If the second element is the smallest
#             else:
#                 # I. We add it to the list
#                 sort_list.append(l2[j])
#                 # II. We get one element less in the first list
#                 size_l2 = size_l2 - 1
#                 # III. We increase the index for the second list
#                 j = j + 1
#                 # IV. We increase the amount of inversions found
#                 num_inversions = num_inversions + size_l1

#         # 3.2. Case where one of the lists is empty
#         else:
#             # 3.2.1. When l1 is non-empty
#             if (size_l1 > 0):
#                 # I. We concatenate the result with the rest of the list
#                 sort_list = sort_list + l1[i:]

#                 # II. We set the remaining unexplored part of the list to zero
#                 size_l1 = 0

#             # 3.2.2. When l2 is non-empty
#             else:
#                 # I. We concatenate the result with the rest of the list
#                 sort_list = sort_list + l2[j:]

#                 # II. We set the remaining unexplored part of the list to zero
#                 size_l2 = 0

#     # 4. We assign res
#     res = (sort_list, num_inversions)

#     # 5. We return res
#     return res

# # ------------------------------------------
# # FUNCTION mergesort_and_count_inversions
# # ------------------------------------------
# def mergesort_and_count_inversions(l):
#     # 1. We create the output variable
#     res = ()

#     # 1.1. We create the sort_list
#     sort_list = []

#     # 1.2. We create the num_inversions
#     num_inversions = 0

#     # 2. We get the length of the list
#     length = len(l)

#     # 3. If the list is empty or contains just one item
#     if (length <= 1):
#         # 3.1. We get a fresh (deep) copy of the list
#         sort_list = l[:]

#         # 3.2. The number of inversions is 0
#         num_inversions = 0

#     # 4. If the list contains two or more elements
#     else:
#         # 4.1. We get the middle index of the list
#         half = length // 2

#         # 4.2. We get a fresh (deep) copy of each half of the list
#         f = l[:half]
#         s = l[half:]

#         # 4.3. We solve recursively the 2 sub-problems
#         (sort_list_1, num_inversions_1) = mergesort_and_count_inversions(f)
#         (sort_list_2, num_inversions_2) = mergesort_and_count_inversions(s)

#         # 4.4. We merge the two results and count the flipped inversions
#         (sort_list, num_inversions_3) = merge_count_inversions(sort_list_1, sort_list_2)

#         # 4.5. We count the total number of inversions
#         num_inversions = num_inversions_1 + num_inversions_2 + num_inversions_3

#     # 5. We assign res
#     res = (sort_list, num_inversions)




# # ------------------------------------------
# # FUNCTION count_inversions_nlogn
# # ------------------------------------------
# def count_inversions_nlogn(my_rank_list):
#     # 1. We create the output variable
#     res = 0

#     # 2. We create an auxiliary variable to host the sort_list
#     sort_list = None

#     # 3. We call to mergesort_and_count_inversions
#     (sort_list, res) = mergesort_and_count_inversions(my_rank_list)

#     # 4. We return res
#     return res

def mine_divide_stage(mine_data, num_cores):
    # 1. create res variable
    res = []

    # 2. get the amount of rows
    num_rows = len(mine_data)
    num_cols = num_rows


    # 3. get the size of each mine cell to be assigned to each core
    sub_size = math.ceil((num_rows* 1.0) / (num_cores * 1.0))

    # 4. assign res
    for i in range(num_cores):
        # 4.1. get the starting and ending indices
        start_index = i * sub_size
        end_index = start_index + sub_size

        # 4.2. get the sub-list
        sub_list = mine_data[start_index:end_index]

        # 4.3. check if end_index is out of bounds
        if end_index > num_rows:
            end_index = num_rows

        # 4.4. append sub-list to res
        res.append(((end_index - start_index, num_cols), sub_list))
    
    # 5. return res
    return res

def mine_core_workload(slice):
    num_rows = slice[0][0]
    num_cols = slice[0][1]
    mine_data = slice[1]

    # assign res
    res = [solve_sequential(((num_rows, num_cols), mine_data))]

    # return res
    return res




def mine_map_stage(mine_slices):
    # 1. setup the pool of workers
    pool = multiprocessing.Pool()

    # 2. use pool to trigger the parallel execution of the function
    res = pool.map(mine_core_workload, mine_slices)

    # 3. close the pool
    pool.close()

    # 4. return res
    return res

def mine_reduce_stage(mine_slices_results):
    # 1. create return variable
    mine_results = []

    # 2. iterate throught mine_slices_results
    for i, mine_slice in enumerate(mine_slices_results):

        # 3. iterate through mine_slice
        for j, mine_row in enumerate(mine_slice[0]):

            # 4. check if we are in the first row
            if j == 0 and i != 0:

                # 4.1. get the previous row
                previous_row = mine_slices_results[i - 1][0][-1]

                # 4.2. amalgamate and update mine_row with previous_row
                for k, mine_cell in enumerate(mine_row):
                    if mine_cell != "x":
                        for m in range(k - 1, k + 2):

                            # 4.2.1. check if m is out of bounds
                            if (m < 0 or m > len(mine_row) - 1):
                                continue

                            # 4.2.2. update mine_row
                            if previous_row[m] == "x":
                                mine_row[k] += 1


            
            # 5. check if we are in the last row
            elif j == len(mine_slice[0]) - 1 and i != len(mine_slices_results) - 1:
                    
                # 5.1. get the next row
                next_row = mine_slices_results[i + 1][0][0]

                # 5.2 amalgamate and update mine_row with next_row
                for k, mine_cell in enumerate(mine_row):
                    if mine_cell != "x":
                        for m in range(k - 1, k + 2):

                            # 5.2.1. check if m is out of bounds
                            if (m < 0 or m > len(mine_row) - 1):
                                continue

                            # 5.2.2. update mine_row
                            if next_row[m] == "x":
                                mine_row[k] += 1

            # 6. append mine_row to mine_results
            mine_results.append(mine_row)

    # 7. return mine_results
    return mine_results


def solve_distribution(my_data, num_cores):
    # 1. We get the dimensions of the board
    hor = my_data[0][0]
    ver = my_data[0][1]

    # 2. We get the board
    mine_data = my_data[1]

    mine_data_slices = mine_divide_stage(mine_data, num_cores)
    mine_slices_results = mine_map_stage(mine_data_slices)
    return mine_reduce_stage(mine_slices_results)


def solve_sequential(my_data):

    # 1. We get the dimensions of the board
    hor = my_data[0][0]
    ver = my_data[0][1]

    # 2. We get the board
    mine_data = my_data[1]

    # 3. We create the solution matrix
    sol = []
    for i in range(hor):
        sol_row = []
        for j in range(ver):
            sol_row.append(0)
        sol.append(sol_row)

    # 4. We traverse the board
    for i in range(hor):
        for j in range(ver):
            # 5.1. If we find a mine
            if mine_data[i][j] == 'x':
                # 5.1.1. We update the solution matrix
                for row in range(i - 1, i + 2):
                    if (row < 0 or row > hor - 1):
                        continue
                    for col in range(j - 1, j + 2):
                        if (col < 0 or col > ver - 1):
                            continue
                        sol[row][col] = sol[row][col] + 1

    # 5. We traverse the solution matrix
    for i in range(hor):
        for j in range(ver):
            # 6.1. If we find a mine
            if mine_data[i][j] == 'x':
                # 6.1.1. We update the solution matrix
                sol[i][j] = 'x'

    # 8. We return sol
    return sol
