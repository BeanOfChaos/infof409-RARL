from math import e
import numpy as np

strats = ["C", "D"]

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


def softmax(x, b):
    return 1 / (1 + e**(-b * x))


def generate_net():
    drive = np.full((625,), 0.6, dtype=np.float64)
    pop = np.random.choice(strats, size=625, replace=True, p=[0.6, 0.4])
    adjmat = np.empty((625,), dtype=object)
    adjmat.fill([])

    for i, adj in np.ndenumerate(adjmat[:-1]):
        if len(adj) < 4:
            sample = np.random.randint(i, 625, size=4-len(adj))
            while not all(len(adjmat[other]) < 4 for other in sample):
                sample = np.random.randint(i+1, 625, size=4-len(adj))
            adj.extend(sample)
            for other in sample:
                adjmat[other].append(i[0])

    return pop, drive, adjmat


def simulate_play(index, pop, adjmat, val="C"):
    """Simulates the score of an agent at index if he were to play val.
    """
    score = 0
    for other in adjmat[index]:
        score += payoffs[val][pop[other]]
    return score


def update(pop, drive, adjmat):
    updated_pop = np.empty_like(pop)
    for i in range(pop.size):
        ot = sum([pop[j] == "C" for j in adjmat[i]])
        ct = int(pop[i] == "C")
        dnt = wc * (ct - 1) + wo * ot + wi * ct * ot
        dit = simulate_play(i, pop, adjmat, val="C") - simulate_play(i, pop, adjmat, val="D")
        drive[i] = drive[i] * (1 - alpha) + dit + h * dnt
        if np.random.random() < softmax(drive[i], beta):
            updated_pop[i] = "C"
        else:
            updated_pop[i] = "D"
    return updated_pop


if __name__ == "__main__":
    pop, drive, adjmat = generate_net()
    for i in range(1000):
        update(pop, drive, adjmat)
