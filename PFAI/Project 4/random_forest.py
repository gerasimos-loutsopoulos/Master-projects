'''
random_forest.py

Author Korbinian Randl
'''
from decision_tree import BinaryDecisionTree
import random

class BinaryRandomForest:
    def __init__(self, X:dict, y:list, n_trees:int, bias:float=.5, max_depth:int=float('inf')) -> None:
        '''Creates and trains a binary random forest.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.

            n_trees:    number of trees in the forest.

            bias:       decision bias for non-pure leaves.

            max_depth:  max_depth of the tree.
        '''
        self.trees = [BinaryDecisionTree(*self.get_sample(X, y), **{'bias':bias, 'max_depth':max_depth}) for _ in range(n_trees)]

    def predict(self, X:dict) -> bool:
        '''Predict the class of the input.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

        
        returns:        predicted boolean class
        '''
        predictions = [tree.predict(X) for tree in self.trees]

        return random.choice(predictions)

    def get_sample(self, X, y):
        '''Implements feature bagging for X.
    
        inputs:
            X: dictionary str->list[float] of attributes and their values.
    
            y: list[bool] of labels.
    
        returns: a bootstrap sample of X and y
        '''
        num_samples = len(X)
        sampled_indices = [random.randint(0, num_samples - 1) for _ in range(num_samples)]  # Randomly select indices with replacement
        sampled_X = {key: [X[key][i] for i in sampled_indices] for key in X}
        sampled_y = [y[i] for i in sampled_indices]

        return sampled_X, sampled_y