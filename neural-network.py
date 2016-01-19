from sklearn.neural_network importMLPRegressor
import numpy as np
import csv



# Multi-layer Perceptron Regressor (neural network)
# http://scikit-learn.org/dev/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor
mlpr = MLPRegressor(hidden_layer_sizes=(8, ), activation='logistic', 
	algorithm='adam', alpha=0.0001, batch_size=200, learning_rate='constant', 
	learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, 
	random_state=None, tol=0.0001, verbose=False, warm_start=False, 
	momentum=0.9, nesterovs_momentum=True, early_stopping=False, 
	validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)




# http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM
# n_components = binary hidden units
# batch_size = number of example per minibatch
# n_iter = iterations over trainingset (10)
# rbm = BernoulliRBM(n_components=1, 
# 	learning_rate=0.06, n_iter=10, verbose=True)



###############################################################################
# Training

# Hyper-parameters. These were set by cross-validation,
# using a GridSearchCV. Here we are not performing cross-validation to
# save time.
rbm.learning_rate = 0.06
rbm.n_iter = 20
# More components tend to give better prediction performance, but larger
# fitting time
rbm.n_components = 100
