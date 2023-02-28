
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

import create_benchmark
import solve_benchmark
import sys
import codecs
import time

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------


def my_main(new_benchmark,
            execution_mode,
            num_files,
            num_cores,
            num_rows,
            num_columns,
            percentage_mines
            ):

    # 1. If a new benchmark is required we generate it
    if (new_benchmark == True):
        create_benchmark.generate_benchmark("input_files/",
                                            num_files,
                                            num_rows,
                                            num_columns,
                                            percentage_mines
                                            )

    # 2. We solve the benchmark under the required parameters
    start_time = time.time()

    solve_benchmark.run_benchmark("input_files/",
                                  "results/",
                                  execution_mode,
                                  num_files,
                                  num_cores,
                                  )

    total_time = time.time() - start_time
    print("execution_mode = " + str(execution_mode))
    print("num_files = " + str(num_files))
    print("num_cores = " + str(num_cores))
    print("num_rows = " + str(num_rows))
    print("num_columns = " + str(num_columns))
    print("percentage_mines = " + str(percentage_mines))
    print("Total Time = " + str(total_time))


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values

    # 1.1. If we call the program from the console then we collect the arguments from it
    if (len(sys.argv) > 1):

        # I. We get if there is a new benchmark to be generated
        my_arg1 = sys.argv[1]
        if (my_arg1 == "True"):
            new_benchmark = True
        else:
            new_benchmark = False

        # II. We get the execution mode:
        # Value 1. Benchmark -> Sequential; Single_File -> Sequential.
        # Value 2. Benchmark -> Sequential; Single_File -> Distributed.
        # Value 3. Benchmark -> Distributed; Single_File -> Sequential.
        # Value 4. Benchmark -> Distributed; Single_File -> Distributed.
        execution_mode = int(sys.argv[2])

        # III. We get the number of files and number of cores
        num_files = int(sys.argv[3])
        num_cores = int(sys.argv[4])

        # IV. We get the structure of each file
        num_rows = int(sys.argv[5])
        num_columns = int(sys.argv[6])
        percentage_mines = int(sys.argv[7])

    # 1.2. If we call the program from PyCharm then we hardcode the arguments to the values we want
    else:
        # I. We get if there is a new benchmark to be generated
        new_benchmark = True

        # II. We get the execution mode:
        # Value 1. Benchmark -> Sequential; Single_File -> Sequential.
        # Value 2. Benchmark -> Sequential; Single_File -> Distributed.
        # Value 3. Benchmark -> Distributed; Single_File -> Sequential.
        # Value 4. Benchmark -> Distributed; Single_File -> Distributed.
        # This mode is not supporting by multi-threading in Python, as it triggers the following exception:
        # AssertionError: daemonic processes are not allowed to have children
        execution_mode = 3

        # III. We get the number of files and number of cores
        num_files = 20
        num_cores = 4

        # IV. We get the structure of each file
        num_rows = 400
        num_columns = 400
        percentage_mines = 30

    # 2. We assert that the entries were correct
    assert (execution_mode >= 1)
    assert (execution_mode <= 4)
    assert (num_files > 0)
    assert (num_cores > 0)
    assert (num_rows > 0)
    assert (num_columns > 0)
    assert (percentage_mines >= 0)
    assert (percentage_mines <= 100)


    # 3. We call to my_main
    my_main(new_benchmark,
            execution_mode,
            num_files,
            num_cores,
            num_rows,
            num_columns,
            percentage_mines
            )
