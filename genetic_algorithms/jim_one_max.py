"""My attempt to build a genetic algorithm from scratch to solve the onemax problem"""

# %%
import random

## Constants

NUM_GENES=10
POP_SIZE=10
P_MUTATION=.3
P_CROSSOVER=.7


# %%
class Individuals():
    """Random generated Binary chromosomes. Each chromsome has 10 genes."""
    def __init__(self):
        self.ind=[]

        
    def make_individual(self):
        i=[random.randint(0,1) for i in range(NUM_GENES)]
        return i

        # print(i)

# %%
class Population():

    def __init__(self):
        self.a=Individuals()
        self.the_population=[]
        self.make_population()

    def make_population(self):
        for i in range(POP_SIZE):
            self.the_population.append(self.a.make_individual())

        print(self.the_population)

        return self.the_population


    
# %%
def fitness_score(x):
    s=sum(x)
    print(f'Fitness Scores: {s}')

    return s

# %%

def populationSum(fitness):
    s=sum(fitness)
    print(f'\nPopulation Sum: {s}')

    return s


# %%

def roulette_weights(fitness):
    
    s=sum(fitness)

    w=[round((i/s),2)*100 for i in fitness]
    print(f'Relative Portion: {w}')
    return w

def roulette_selection():
    pass


def tornament_select(gen_stat,pool_size=len(gen_stat),k=2):

    mating_pool=[]

    for i in range(pool_size):
        tornament=[gen_stat[random.randint(0,len(gen_stat)-1)] for i in range(k)]

        mating_pool.append(max(tornament))

    return mating_pool


def single_point_crossover():

    # Input: mating_pool
    # Randomly Choose 2 binary strings (chromosones) from the mating pool

    # Crossover of two parents occurs with propability (pb)

    # Randomly choose the crossover site

    # perform the crossover if crossover probability is met

    # Return the offspring or the parents if crossover probability is not met

def mutation():

    # Input: receive the offspring

    # generate random number between 0 and 1 len(chromosome) times.
    # Where each random number (r) is assigned to an index (gene) of the chromsome

    # if r<P_MUTATION then bit flip the gene at that index.

    # Return the offspring with mutation

    

    pass


# %%

p=Population()

fitness=[fitness_score(i) for i in p.the_population]

population_sum=populationSum(fitness)

w=roulette_weights(fitness)

gen_stat=sorted(list(zip(fitness,p.the_population,w)),reverse=True)

# print(gen_stat)

mating_pool=tornament_select(gen_stat)



# %%
