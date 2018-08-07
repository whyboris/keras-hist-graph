# Keras History Graph

Uses `matplotlib` to generate a simple graph of the history object. Particularly useful with _Jupyter_

It will show the _accuracy_ and _loss_ for both _training data_ and _validation data_.
It will also print the maximum _validation accuracy_ reached during the training.

![Example output](https://user-images.githubusercontent.com/17264277/43170872-5ff85946-8f75-11e8-86e8-d08a0fa79f15.png)

# Installation

`pip install keras-hist-graph`

# Usage

assuming you are using _Keras_

```
from keras_hist_graph import plot_history

history = model.fit(x, y, ...)

plot_history(history)
```
