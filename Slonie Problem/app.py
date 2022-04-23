import numpy as np
import os
INF = 10e9
min_weight = INF

import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("print_string", help="Prints the supplied argument.")

args = parser.parse_args()
file_name = args.print_string

def calculate_result(N, weights, orignial_positions,final_positions ):
    vis = np.array([True   if (orignial_positions[i] == final_positions[i]) else False for i in range(N) ])

    result = 0 #final result initialized with 0

    for position in range(1,N+1): #for positions in the file:

        if not vis[position-1]:

            min_w_cycle = INF #minc
            effort = 0    #suma
            cur = position  #cur = pocz
            cycle_length = 0 #dl  while loop 

            while True: 
                min_w_cycle = min(min_w_cycle,weights[cur-1])

                effort += weights[cur-1] 
                cur = final_positions[cur-1]
                vis[cur-1] = True 
                cycle_length = cycle_length + 1 

                if cur == position: 
                    break 
            result += min( (effort + (cycle_length-2)*min_w_cycle), effort + ((cycle_length+1)*min_weight) )
    return result

if __name__ == '__main__':
    path = os.getcwd()
    with open( os.path.join( path , file_name ) ) as f:
        # print(input_files[file_number])
        lines = f.readlines()
        N = int(lines[0])
        weights = [ int(x)  for x in lines[1].split(' ') ]
        orignial_positions = [ int(x)  for x in lines[2].split(' ')]
        final_positions = [ int(x)  for x in lines[3].split(' ')]
        result = calculate_result(N, weights, orignial_positions,final_positions )
        print(result)
        