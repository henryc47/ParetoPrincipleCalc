#python library to calculate the pareto principle for a provided list
import sys

#calculate what fraction of the outcome comes from what fraction of the input
#we are after the relation for input_fraction + output_fraction = 1
#input is output per unit input (input is evenly divided between entries on list)
#return tuple of (caused_output_fraction,input_fraction)
def pareto_principle_even(data_output : list[float]) -> tuple[float,float]:
    data_output.sort() #sort the data if it is not already sorted
    amount_data_input : int = len(data_output)
    data_input = [1]*amount_data_input
    output_x,input_x = calc_pareto_principle(data_output,data_input)
    return output_x,input_x


#calculate what fraction of the outcome comes from what fraction of the input
#we are after the relation for input_fraction + output_fraction = 1
#input is output per unit input (input is evenly divided between entries on list)
#return tuple of (caused_output_fraction,input_fraction)
def calc_pareto_principle(data_output : list[float],data_input : list[float],crossover_strategy : str = 'linear') -> tuple[float,float]:
    #check input and output data are the same shape
    if(len(data_output))!=(len(data_input)): 
        sys.exit("ERROR : input and output data are not of equal length")
    #we assume input + output is sorted by output/input 
    #normalise input and output
    data_output = normalise(data_output)
    data_input = normalise(data_input)
    input_sum : float = 0
    output_sum : float = 0
    #calculate the pareto principle
    for i,this_input_data in enumerate(data_input):
        input_sum += this_input_data
        output_sum += data_output[i]
        if (output_sum+input_sum)>=1: #once we have passed the pareto point
            break
    
    if(output_sum+input_sum==1): #if we reached it exactly, output immediately
        return output_sum,input_sum
    else: #we need to go back and calculate precisely the crossover point
        previous_input_sum = input_sum-this_input_data
        previous_output_sum = output_sum-data_output[i]
        output_x,input_x = calculate_crossover(input_sum,output_sum,previous_input_sum,previous_output_sum,crossover_strategy)
        return output_x,input_x

#calculate the crossover point using the linear assumption
def linear_crossover(input_sum : float,output_sum : float,previous_input_sum : float,previous_output_sum : float) -> tuple[float,float]:
    delta_input = input_sum-previous_input_sum
    delta_output = output_sum-previous_output_sum
    x = (1-previous_input_sum-previous_output_sum)/(delta_input+delta_output)
    x_input = previous_input_sum + delta_input*x
    x_output = previous_output_sum + delta_output*x
    return x_output,x_input

#calculate the crossover point using the requested strategy
def calculate_crossover(input_sum : float,output_sum : float,previous_input_sum : float,previous_output_sum : float,crossover_strategy : str = 'linear') -> tuple[float,float]:
    strategy_dict = {'linear' : linear_crossover}
    if crossover_strategy not in strategy_dict:
        error_message : str = "ERROR : " + crossover_strategy + " is not a valid crossover strategy "
        sys.exit(error_message)
    else:
        strategy_func = strategy_dict[crossover_strategy]
        (x_output,x_input) = strategy_func(input_sum,output_sum,previous_input_sum,previous_output_sum)
    return x_output,x_input


#normalise data, so the sum is 1
def normalise(data :list[float]) -> list[float]:
    sum_data = sum(data)
    norm_data = [x/sum_data for x in data]
    return norm_data


    


