import matplotlib.pyplot as plt


def plot_av_coop_level(coop_levels, title="Average cooperation level over time.", filename="av_coop_level.png", show=False):
    averages = []
    for i in range(len(coop_levels[0])):
        values = [sublist[i] for sublist in coop_levels]
        averages.append(sum(values) / len(values))
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Average cooperation level")
    if show:
        plt.show()
    else:
        plt.savefig(filename)
    plt.clf()


def plot_coop_prob(drives, title="Cooperation probabilities rates", filename="drive_rates.png", show=False):
    xs = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    ys = [0 for _ in xs]
    for i, val in enumerate(xs):
        for drive in drives:
            if 0.5 <= val - drive < 0.5:
                ys[i] += 1
    plt.title(title)
    plt.xlabel("Probability of cooperation")
    plt.ylabel("Number of players")
    plt.bar(xs, ys)
    if show:
        plt.show()
    else:
        plt.savefig(filename)
    plt.clf()


def plot_individual_drive(drives, title="Individual drives rates", filename="drive_rates.png", show=False):
    xs = [i for i in range(-16, 1)]
    ys = [0 for _ in xs]
    for i, val in enumerate(xs):
        for drive in drives:
            if 0.5 <= val - drive < 0.5:
                ys[i] += 1
    plt.title(title)
    plt.xlabel("Individual drive")
    plt.ylabel("Number of players")
    plt.bar(xs, ys)
    if show:
        plt.show()
    else:
        plt.savefig(filename)
    plt.clf()


def plot_normative_drive(drives, title="Normative drives rates", filename="drive_rates.png", show=False):
    xs = [i for i in range(-5, 30)]
    ys = [0 for _ in xs]
    for i, val in enumerate(xs):
        for drive in drives:
            if 0.5 <= val - drive < 0.5:
                ys[i] += 1
    plt.title(title)
    plt.xlabel("Normative drive")
    plt.ylabel("Number of players")
    plt.bar(xs, ys)
    if show:
        plt.show()
    else:
        plt.savefig(filename)
    plt.clf()
