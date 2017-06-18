# random raffle selection process. the winner is chosen by process of random elimination.
# 17-06-2017

import random as rn
import numpy as np

def print_candidates(candidates):
    """
    Print the candidate names entering the competition
    
    Parameters:
    candidates: A list of strings of candidate names
    
    """
    
    # print header
    
    print('Candidates')
    print('#\tName')
    
    i = 0
    for candidate in candidates:
        i += 1
        
        # print candidate number and name, tab delimited
        print(str(i) + '\t' + candidate)

def tournament(candidates):
    """
    Decide on the winner of a raffle by process of a tournament with random 'survivor'-style elimination until
    one winner remains. 
    
    Parameters:
    candidates: List of strings of candidate names
    
    Returns:
    string: Name of the winning candidate
    """
    
    # import the randomly selected seed which has been saved to preserve state for future inspection
    with open('seed.txt','r') as f:
        seed = int(f.read())  
    
    # set the random seed. you can generate your own
    # using random.randrange(sys.maxsize) after doing "import sys"
    # and using Python's native random library which has the randrange function
    rn.seed(seed)
    
    # repeat process of elimination until only one winner remains
    while len(candidates) > 1:
        # shuffle the candidate names
        rn.shuffle(candidates)
        # remove candidate at the head of the shuffled list
        candidates = candidates[1:]
        
    return candidates[0]

def main():
    """
    Main driver function. Reads in the candidates from file and prints output to console
    """
    
    print('-----SAS Competition-----\n')
    # create empty list for the candidate names
    candidates = []
    
    # read in the contestants from a file
    f = open('contestants.txt','r')
    for line in f:
        candidates.append(line.strip())
    candidates = np.array(candidates)
    
    print_candidates(candidates)
    
    # retrieve the winner and print to console
    print('\nWinner selected is: ' + tournament(candidates))
 
if __name__ == "__main__":
    main()
