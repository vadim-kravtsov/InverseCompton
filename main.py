from random import uniform
from math import sqrt
from numpy import log, mean
import matplotlib.pyplot as plt


def angle(beta):
    mu = uniform(-1, 1)
    mu_gen = uniform(0, 2)
    if mu_gen < theta_check(mu, beta):
        return [mu, beta*mu_gen]
    else:
        return [None, None]

def theta_check(mu, beta):
    return 1 - beta*mu

if __name__ == '__main__':
    beta = 0.1
    gamma = 1/sqrt(1-beta**2)
    x, y = [], []
    e_list = []
    for i in range(100000):
        mu, mu_gen = angle(beta)
        if mu:
            x.append(mu)
            y.append(mu_gen)
            e = gamma**2*(1 - beta*mu)*(1 + beta*uniform(-1, 1)) 
            e_list.append(e)
    nbins = 100
    e_min, e_max = min(e_list), max(e_list)
    bin_size = (e_max - e_min)/nbins
    bins = [e_min + i*bin_size for i in range(nbins)]
    print(bins)
    e_binned = []
    for b in bins:
        e_binned.append([])
        for e in e_list:
            if b < e < b + bin_size:
                e_binned[bins.index(b)].append(e)
    v1, v2, v3 = [], [], []
    for b in e_binned:
        numb = len(b)
        bin_pos = bins[e_binned.index(b)]+bin_size/2
        v1.append(bin_pos)
        v2.append(bin_pos*numb)
        v3.append(numb)
    plt.plot(v1, v2/mean(v2), '+', markersize = 7, c = 'k')
    plt.plot(v1, v3/mean(v3), '+', markersize = 7, c = 'r')
    
    #plt.hist(e_list, bins=100)
    plt.show()
