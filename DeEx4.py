import numpy as np
import matplotlib.pyplot as plt

# cons_fnDeJongs = lambda x: sum(x**2)/len(x)
cons_fnDeJongs = lambda minLimite, maxLimite, x, tamanhoDopulacao: np.argmin(minLimite+x*(minLimite-(maxLimite))/(pow(2,tamanhoDopulacao)-1))
cons_limites = [(-5-12, 5.12), (-5.12, 5.12), (-5.12, 5.12)]
cons_mutacao = 0.7
cons_cross = 0.7
cons_populacaoTamanho = 15
cons_iteracoes=200
results = []

def de(fnDeJongs, limites, mutacao, cross, populacaoTamanho, iteracoes):
    dimensoes = len(limites)
    populacao = np.random.rand(populacaoTamanho, dimensoes)
    minLimite, maxLimite = np.asarray(limites).T
    diff = np.fabs(minLimite - maxLimite)
    pop_denorm = minLimite + populacao * diff
    fitness = np.asarray([fnDeJongs(ind, minLimite, maxLimite, populacaoTamanho) for ind in pop_denorm])
    # fitness = np.asarray([fnDeJongs(ind) for ind in pop_denorm])

    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    for i in range(iteracoes):
        for j in range(populacaoTamanho):
            idxs = [idx for idx in range(populacaoTamanho) if idx != j]
            a, b, c = populacao[np.random.choice(idxs, 3, replace = False)]
            mutado = np.clip(a + mutacao * (b - c), 0, 1)
            cross_points = np.random.rand(dimensoes)<cross
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimensoes)] = True
            trial = np.where(cross_points, mutado, populacao[j])
            trial_denorm = minLimite + trial * diff
            print(trial_denorm)
            # f = fnDeJongs(trial_denorm, minLimite, maxLimite, populacaoTamanho)
            f = fnDeJongs(trial_denorm, minLimite, maxLimite, populacaoTamanho)

            # f = sum(trial_denorm)
            print("fitness J ", fitness[j])
            print("f ", f)
            if f < fitness[j]:
                fitness[j] = f
                populacao[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
        # yield best, fitness[best_idx]
        results.append(np.argmin(best))

        print("best %s fitness %s " % (best, fitness[best_idx]))

    # x = np.linspace(0, 10, cons_iteracoes)
    # y = np.cos(x) + np.random.normal(0, 0.2, cons_iteracoes)
    # plt.scatter(x, y)
    # plt.plot(x, np.cos(x), label='cos(x)')
    # plt.legend()

    # plt.show()

if __name__ == '__main__':
    de(cons_fnDeJongs, cons_limites, cons_mutacao, cons_cross, cons_populacaoTamanho, cons_iteracoes)