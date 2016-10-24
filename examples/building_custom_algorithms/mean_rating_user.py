"""
This module descibes how to build your own prediction algorithm. Please refer
to User Guide for more insight.
"""

from recsys import AlgoBase
from recsys import Dataset
from recsys import evaluate

from statistics import mean

class MyOwnAlgorithm(AlgoBase):

    def __init__(self):

        # Always call base method before doing anything.
        AlgoBase.__init__(self)

    def estimate(self, u, i):

        return mean(r for (_, r) in self.trainset.ur[u])


data = Dataset.load_builtin('ml-100k')
algo = MyOwnAlgorithm()

evaluate(algo, data)
