
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

import shutil
import time
import os
import codecs
import math
import multiprocessing
import problem_algorithms


# ------------------------------------------
# FUNCTION run_file
# ------------------------------------------
def run_file(file, num_cores, use_distribution, result_dir):

    # 1. Check if result directory exists

    # 1.1. We open the file for reading
    my_input_file = codecs.open(file, "r", encoding='utf-8')

    # 1.2. We read it
    grid_size = my_input_file.readline().split()
    mine_data = []
    hor = int(grid_size[0])
    ver = int(grid_size[1])
    for _ in range(hor):
        hor_data = my_input_file.readline().split()
        mine_data_row = []
        for mine in hor_data:
            mine_data_row.append(mine)
        mine_data.append(mine_data_row)

    my_input_file.close()

    # 2.2. We solve the problem using the desired algorithm
    if (use_distribution == True):
        sol = problem_algorithms.solve_distribution(
            ((hor, ver), mine_data), num_cores)
    else:
        sol = problem_algorithms.solve_sequential(((hor, ver), mine_data))

    my_output_file = codecs.open(
        result_dir + "/" + file.split("/")[-1], "w", encoding='utf-8')
    for row in range(len(sol)):
        for col in range(len(sol[row])):
            my_output_file.write(f"{sol[row][col]} ")
        my_output_file.write("\n")


# --------------------------------------------------
# my_divide_stage
# --------------------------------------------------
def my_divide_stage(game_files, num_cores, use_distribution, result_dir):
    # 1. We create the output variable
    res = []

    # 2. We get the amount of people in the population benchmark
    size = len(game_files)

    # 3. We get the size of each people_subset to be assigned to a different core
    sub_size = math.ceil((size * 1.0) / (num_cores * 1.0))

    # 4. We assign res

    # Divide Policy 1
    res = [(game_files[slice_lb:(slice_lb + sub_size)], num_cores, use_distribution,
            result_dir) for slice_lb in range(0, size, sub_size)]

    # Divide Policy 2
    # res = [ [] for index in range(num_cores) ]
    # bucket = 0
    # for index in range(size):
    #     res[bucket].append(population_files[index])
    #     bucket = bucket + 1
    #     if (bucket == num_cores):
    #         bucket = 0

    # 5. We return res
    return res

# --------------------------------------------------
# FUNCTION core_workload
# --------------------------------------------------


def core_workload(slice):
    # 1. We create the output variable
    res = []

    # 2. We unpack the variables
    game_files = slice[0]
    num_cores = slice[1]
    use_distribution = slice[2]
    result_dir = slice[3]

    # 3. We assign res
    res = [run_file(file, num_cores, use_distribution, result_dir)
           for file in game_files]

    # 4. We return res
    return res

# --------------------------------------------------
# FUNCTION my_map_stage
# --------------------------------------------------


def my_map_stage(game_slices):
    # 1. We create the output variable
    res = []

    # 2. We setup the object for enabling parallel computation among the different cores
    pool = multiprocessing.Pool()

    # 3. We use pool to trigger the parallel execution of each people subset (slice) in a different process
    res = pool.map(core_workload, game_slices)

    # 4. We return res
    return res

# --------------------------------------------------
# FUNCTION my_reduce_stage
# --------------------------------------------------


def my_reduce_stage(game_slices_results):
    # 1. We create the output variable
    res = ()

    # 1.1. We output the inversions and elapsed time per person in the population
    game_results = [
        game for slice in game_slices_results for game in slice]
    return game_results

    # # 1.2. Additionally, we output as well the total working time per core (which is relevant to our analysis)
    # time_per_core = [sum(person[1] for person in slice)
    #                  for slice in population_slices_results]

    # # 1.3. Additionally, we output the total time spent by all cores all together
    # total_time = sum(time_per_core)

    # # 2. We assign res to its final value
    # res = (population_results, total_time, time_per_core)

    # # 3. We return res
    # return res

# ------------------------------------------
# FUNCTION run_benchmark
# ------------------------------------------


def run_benchmark(input_files_dir: str, result_dir: str, execution_mode: int, num_files: int, num_cores: int):
    """ run benchmark

    Args:
        input_files_dir (str): input files directory
        result_dir (str): result directory
        execution_mode (int): execution mode
        num_files (int): number of files
        num_cores (int): number of cores

        Execution Mode 1. Benchmark -> Sequential; Single_File -> Sequential.
        Execution Mode 2. Benchmark -> Sequential; Single_File -> Distributed.
        Execution Mode 3. Benchmark -> Distributed; Single_File -> Sequential.
        Execution Mode 4. Benchmark -> Distributed; Single_File -> Distributed.
    """
    # 1. We create the result directory if it does not exist
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
        os.mkdir(result_dir)

    # 2. We get the list of files to be processed
    game_files = [input_files_dir +
                  file_name for file_name in os.listdir(input_files_dir)]

    # 3. We run the benchmark
    # 3.1. We run the benchmark in sequential mode
    if execution_mode == 1:
        assert num_cores == 1
        for file in game_files:
            run_file(file, num_cores, False, result_dir)

    # 3.2. We run the benchmark in distributed mode
    elif execution_mode == 2:
        assert num_cores > 1
        for game in game_files:
            run_file(game, num_cores, True, result_dir)

    elif execution_mode == 3:
        assert num_cores > 1
        # 4.1. We apply our problem-specific divide function:
        game_slices = my_divide_stage(
            game_files, num_cores, False, result_dir)

        # 4.2. We apply our problem-specific map function:
        game_slices_results = my_map_stage(game_slices)

        # 4.3. We apply our problem-specific reduce function:
        # my_reduce_stage(game_slices_results)

    # elif execution_mode == 4:
    #     assert num_cores > 1
    #     # 4.1. We apply our problem-specific divide function:
    #     game_slices = my_divide_stage(
    #         game_files, num_cores, True, result_dir)

    #     # 4.2. We apply our problem-specific map function:
    #     game_slices_results = my_map_stage(game_slices)

    #     # 4.3. We apply our problem-specific reduce function:
    #     # my_reduce_stage(game_slices_results)
