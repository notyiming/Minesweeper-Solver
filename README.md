# Minesweeper-Solver
Exploring ways to solve a minesweeper problem in a distributed and sequential manner

- Execution Mode 1:   
  - Solve the benchmark files in sequential order (using 1 single core). 
  - Solve each file in sequential order (using 1 single core).   
- Execution Mode 2:   
  - Solve the benchmark files in sequential order (using 1 single core). 
  - Solve each file in distributed order (using more than 1 core).  
 
- Execution Mode 3:   
  - Solve the benchmark files in distributed order (using more than 1 core). 
  - Solve each file in sequential order (using 1 single core).   
- Execution Mode 4:   
  - Solve the benchmark files in distributed order (using more than 1 core). 
  - Solve each file in distributed order (using more than 1 core). 
  - Unfortunately, the execution mode 4 is not supported by the multi-threading library of 
  Python 3, which triggers the following exception:  
  ``AssertionError: daemonic processes are not allowed to have children.``
  
  # Results
  ![image](https://user-images.githubusercontent.com/55159184/221833323-4a01df27-943f-4d6c-a2a4-ea5da51ed786.png)
