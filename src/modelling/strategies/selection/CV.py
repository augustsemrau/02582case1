'''
Notes from slides

Permute data before splitting in folds - the data set might be
sorted in some way.

Normalize training data separately for each fold.

Impute missing values separately for each training set.

Be careful to perform ALL pre-processing within the CV folds

Be extremely careful with data sampled from dynamic systems
(time-dependent data).

Use K = 5 or 10 as a good compromise between bias and variance.
'''