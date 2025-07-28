from random import random
from numpy import sqrt, exp, arange
from matplotlib.pyplot import *
def random_distribution (possible_grades) :
    preeval_rel = []
    for grade in possible_grades :
        preeval_rel.append([grade, random()])
    total = 0
    for couple in preeval_rel :
        total += couple[1]
    eval_rel = []
    for couple in preeval_rel :
        eval_rel.append([couple[0], couple[1]/total])
    return eval_rel
def expected_value (distribution_list) :
    result = 0
    for couple in distribution_list :
        result += couple[0]*couple[1]
    return result
def standard_deviation (distribution_list) :
    result = 0
    expected = expected_value(distribution_list)
    for couple in distribution_list :
        result += (couple[0]-expected)*(couple[0]-expected)*couple[1]
    return sqrt(result)
def heating (distribution_list, log_temperature = 0) :
    # we use the logarithm of the temperature rather than the temperature itself
    total = 0
    for couple in distribution_list :
        total += exp(couple[1]*exp(-log_temperature))
    result = []
    for couple in distribution_list :
        result.append([couple[0],exp(couple[1]*exp(-log_temperature))/total])
    return result
f, ax = subplots(1)
ax.set_xlim(left=0,right=72)
ax.set_ylim(bottom=0,top=50)
for _ in range(10) :
    possible_grades = [random()*20 for _ in range(_*5+5)]
    distribution = random_distribution(possible_grades)
    deviations = []
    for log_temperature in list(arange(-7-.2*_,6,.1)) :
        heated = heating(distribution,log_temperature)
        deviations.append(standard_deviation(heated))
    plot(list(exp(arange(-7-.2*_,6,.1))),deviations,"-",color=(1-.1*_,0,.1*_))
ax.set_xscale('log')
ax.set_xlim(left=.00013,right=403)
ax.set_ylim(bottom=0,top=9)
ax.grid()
xlabel("Température")
ylabel("Écart-type")
show()
