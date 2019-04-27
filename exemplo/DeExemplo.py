import numpy as np


FOBJ = lambda x: sum(x**2)/len(x)
BOUNDS = [(-5, 5), (-5, 5), (-5, 5), (-5, 5)]


def de(fobj, bounds, mut=0.8, crossp=0.7, popsize=4, its=1):
    print ("EDEADFAD")
    dimensions = len(bounds)
    pop = np.random.rand(popsize, dimensions)
    min_b, max_b = np.asarray(bounds).T
    diff = np.fabs(min_b - max_b)
    pop_denorm = min_b + pop * diff
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])
    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    for i in range(its):
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = pop[np.random.choice(idxs, 3, replace = False)]
            mutant = np.clip(a + mut * (b - c), 0, 1)
            cross_points = np.random.rand(dimensions) < crossp
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimensions)] = True
            trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = min_b + trial * diff

            print("testes", trial_denorm)

            f = fobj(trial_denorm)

            print("fitness J ", fitness[j])
            print("f ", f)

            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
        # yield best, fitness[best_idx]
    print("Best - ", best)
    print("Best fitness - ", fitness[best_idx])

if __name__ == '__main__':
    print("DE")
    de(FOBJ, BOUNDS)
