
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

import codecs
import random
import os
import shutil

# ------------------------------------------
# FUNCTION generate_file
# ------------------------------------------


def generate_file(num_rows: int, num_columns: int, percentage_mines: int, file_name: str):
    """ Generates a file with the given parameters

    Args:
        num_rows (int): number of rows
        num_columns (int): number of columns
        percentage_mines (int): percentage of mines
        file_name (str): file name
    """

    # 1. We open the file to write
    my_input_file = codecs.open(file_name, "w", encoding='utf-8')

    # 2. We write the number of rows and columns
    my_input_file.write(str(num_rows) + " " + str(num_columns) + "\n")

    # 3. We create the minesweeper grid
    for _ in range(num_rows):
        for _ in range(num_columns):
            # 2.1. We pick a random number
            random_number = random.randint(0, 100)

            # 2.2. We check if the number is less than the percentage of mines
            if random_number < percentage_mines:
                my_input_file.write("x")
            else:
                my_input_file.write("o")

            my_input_file.write(" ")

        # 2.3. We add a new line
        my_input_file.write("\n")

    # 4. We close the file
    my_input_file.close()

# ------------------------------------------
# FUNCTION generate_benchmark
# ------------------------------------------


def generate_benchmark(directory_name: str, num_files: int, num_rows: int, num_columns: int, percentage_mines: int):
    """ Generates a benchmark with the given parameters

    Args:
        directory_name (str): directory name
        num_files (int): number of files
        num_rows (int): number of rows
        num_columns (int): number of columns
        percentage_mines (int): percentage of mines
    """
    # 1. If the directory already contained some files, we remove them
    if os.path.exists(directory_name):
        # os.remove(directory_name)
        shutil.rmtree(directory_name)
        os.mkdir(directory_name)

    # 2. We generate the benchmark by creating the desired number of files
    for index in range(num_files):
        generate_file(num_rows, num_columns, percentage_mines,
                      directory_name + "file_" + str(index + 1) + ".txt")
