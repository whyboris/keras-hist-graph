# Keras History Graph

Uses `matplotlib` to generate a simple graph of the history object. Particularly useful with _Jupyter_

It will show the _accuracy_ and _loss_ for both _training data_ and _validation data_.
It will also print the maximum _validation accuracy_ reached during the training.

![Example output](https://user-images.githubusercontent.com/17264277/43170872-5ff85946-8f75-11e8-86e8-d08a0fa79f15.png)

# Installation

`pip install keras-hist-graph`

# Usage

Requires _Keras_

```py
from keras_hist_graph import plot_history

history = model.fit(x, y, ...)

plot_history(history)
```

# Arguments

_plot_history_ now accepts any of these arguments (in any order)

| argument | default | possible | details |
| -------- | ------- | -------- | ------- |
| fig_size | (10, 6) | (`float`, `float`) | Indicates _width_ and _height_ of the resulting graph |
| min_accuracy | 0.5 | `[0, 1)` | Minimum accuracy to graph (often we don't care if acuracy is below 50%) |
| smooth_factor | 0.75 | `[0, 1]` | Zero to one, inclusive. Smooths out the curves by averaging previous points. Consider makeing smaller if number of epochs is small. |
| start_epoch | 5 | integer >= 0 | Plot the history starting at this epoch. Useful since the first epochs can have very high loss that makes the later loss hard to analyze visually |
| xkcd | True | `True` `False` | Whether to render in the _XKCD_ style. You might need to render twice for all properties to update if you change the boolean after using the method before |

Example:

```py
plot_history(history, fig_size = (11, 8.5), min_accuracy = 0.8, start_epoch = 2, smooth_factor = 0.1)
```

### Notes

[Why use the XKCD style?](https://www.chrisstucchio.com/blog/2014/why_xkcd_style_graphs_are_important.html)

It’s a great way to communicate the imprecision of the underlying data!
