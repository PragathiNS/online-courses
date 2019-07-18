**A neural network is basically a set of functions which can learn patterns.**

keras - API in TF. Its really easy to define Neural Networks using Keras.\
In keras, you use the word dense to define a layer of connected neurons. There's only one dense here. So there's only one layer and there's only one unit in it, so it's a single neuron. Successive layers are defined in sequence, hence the word sequential.\
`model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])`

Loss functions and optimizers\
`model.compile(optimizer='sgd', loss='mean_squared_error')`

The neural network has no idea of the relationship between X and Y, so it makes a guess. Say it guesses Y equals 10X minus 10. It will then use the data that it knows about, that's the set of Xs and Ys that we've already seen to measure how good or how bad its guess was. The loss function measures this and then gives the data to the optimizer which figures out the next guess. So the optimizer thinks about how good or how badly the guess was done using the data from the loss function. Then the logic is that each guess should be better than the one before. As the guesses get better and better, an accuracy approaches 100 percent, the term convergence is used. In this case, the loss is mean squared error and the optimizer is SGD which stands for stochastic gradient descent. 

Known data\
`xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)`\
`ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)`

Training loop -  The epochs equals 500 value means that it will go through the training loop 500 times.\
`model.fit(xs, ys, epochs=500)`

Make a guess, measure how good or how bad the guesses with the loss function, then use the optimizer and the data to make another guess and repeat this.

After tranining the model, you can print the prediction values using the command below\
`print (model.predict([10,0]))`
