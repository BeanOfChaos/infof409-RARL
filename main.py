import numpy as np


# Final values settled in the paper
alpha = 0.21
beta = 0.31
h = 0.31
wi = 3.2
wc = 1
wo = 0.33


# payoff matrix definition
T = 10
R = 7
P = 0
S = 0

payoffs = {"C": {"C": R,
                 "D": S},
           "D": {"C": T,
                 "D": P}
           }



def play_square(pop):
    """Plays one iteration of the Prisoner's dilemma.
    Return score matrix.
    """
    scores = zeros(pop.shape, dtype=int)
    for coord, player in np.ndenumerate(pop):

    return scores

def update_square(pop, , scores):
    """Update players' strategy and preferences, given their scores, preferences and observations.
    """
    for coord, strat in np.ndenumerate(pop):
        pass


def square_static():
    """Runs an experiment for static lattice.
    """
    pop = np.empty((25,25), dtype=unicode)
    prefs = np.full_like(pop, 0.6, dtype=float64)


def square_dynamic():
    """Runs an experiment for dynamic lattice.
    """
    pop = np.empty((25,25), dtype=object)


def random_net():
    """Runs an experiment for random static networks.
    """
    pop = np.empty((625,) dtype=object)



if __name__ == "__main__":
    print("Hello, World!")
