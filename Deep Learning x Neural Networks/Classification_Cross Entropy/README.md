# Cross-Entropy?
Cross-entropy is a measure of the difference between two probability distributions for a given random variable or set of events.ry Cross Entropy is the negative average of the log of corrected predicted probabilities.
 * Entropy is the number of bits required to transmit a randomly selected event from a probability distribution. A skewed distribution has a low entropy, whereas a distribution where events have equal probability has a larger entropy.

![image](https://github.com/ThisIs-Developer/Python/assets/109382325/34b2c1d1-7739-4882-954a-b10c42c4db2c)

## When fitting a neural network for classification, Keras provide the following three different types of cross entropy loss function:
1. binary_crossentropy
2. categorical_crossentropy
3. sparse_categorical_crossentropy
## binary_crossentropy
Used as a loss function for binary classification model. The binary_crossentropy function computes the cross-entropy loss between true labels and predicted labels.
## categorical_crossentropy
Used as a loss function for multi-class classification model where there are two or more output labels. The output label is assigned one-hot category encoding value in form of 0s and 1. The output label, if present in integer form, is converted into categorical encoding using keras.utils to_categorical method.
## sparse_categorical_crossentropy
Used as a loss function for multi-class classification model where the output label is assigned integer value (0, 1, 2, 3…). This loss function is mathematically same as the categorical_crossentropy. It just has a different interface.
