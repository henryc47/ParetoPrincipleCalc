#python script to calculate the pareto relation from the data the provided txt,csv file, if no filename provided will default to reading from stdin

import sys
import pareto


def pareto_calc(args : list[str]):
    if len(args)==1: #eventually we shall implement reading from stdin if no filename provided
        sys.exit("ERROR : provide a file to read input from")
    if len(args)>1:
        filename = args[1]
    if len(args)>2:
        decimals = int(args[2])
        if decimals<0:
            print("WARNING : minimum number of decimal places to print is 0",sys.stderr)
            decimals = 0
    else:
        decimals = 2 #default is 2 decimal places
    if filename[-4:]!=".txt":
        sys.exit("ERROR : input file must be a .txt file")
    else:
        data = process_txt_file(filename)
        input_x,output_x = pareto.pareto_principle_even(data) #reversal not a typo, statement is still true (by the nature of the pareto principle), but the reverse order is more eye-catching
        #convert to % of 100
        output_x *= 100
        input_x *= 100
        print(f'{input_x:.{decimals}f}',r" % of the input is responsible for ",f'{output_x:.{decimals}f}',r" % of the output")
        return

    
def process_txt_file(filename : str) -> list[float]:
    data : list[float] = []
    file = open(filename)
    for line in file:
        data.append(float(line))
    file.close()
    return data

if __name__ == "__main__":
    pareto_calc(sys.argv)
    