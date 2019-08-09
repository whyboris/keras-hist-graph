import matplotlib.pyplot as plt

# Plot model history more easily

# when plotting, smooth out the points by some factor (0.5 = rough, 0.99 = smooth)
# method taken from `Deep Learning with Python` by François Chollet


def smooth_curve(points, factor):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points


def set_plot_history_data(ax, history, which_graph, start_epoch, smooth_factor, xkcd):

    if which_graph == "acc":
        train = smooth_curve(history.history["acc"], smooth_factor)
        valid = smooth_curve(history.history["val_acc"], smooth_factor)

    if which_graph == "loss":
        train = smooth_curve(history.history["loss"], smooth_factor)
        valid = smooth_curve(history.history["val_loss"], smooth_factor)

    if xkcd:
        plt.xkcd()  # make plots look like xkcd
    else:
        plt.rcdefaults()

    epochs = range(1, len(train) + 1)

    trim = start_epoch - 1  # remove first N epochs
    # when graphing loss the first few epochs may skew the (loss) graph

    ax.plot(epochs[trim:], train[trim:], "dodgerblue", linewidth=15, alpha=0.1)
    ax.plot(epochs[trim:], train[trim:], "dodgerblue", label=("Training"))

    ax.plot(epochs[trim:], valid[trim:], "g", linewidth=15, alpha=0.1)
    ax.plot(epochs[trim:], valid[trim:], "g", label=("Validation"))


def get_max_validation_accuracy(history):
    validation = history.history["val_acc"]
    ymax = max(validation)
    return "Max validation accuracy ≈ " + "%.2f" % ymax + "%"


def plot_history(
    history,
    start_epoch=5,
    smooth_factor=0.75,
    xkcd=True,
    fig_size=(10, 6),
    min_accuracy=0.5,
):

    fig, (ax1, ax2) = plt.subplots(
        nrows=2,
        ncols=1,
        figsize=fig_size,
        sharex=True,
        gridspec_kw={"height_ratios": [5, 2]},
    )

    set_plot_history_data(ax1, history, "acc", start_epoch, smooth_factor, xkcd)

    set_plot_history_data(ax2, history, "loss", start_epoch, smooth_factor, xkcd)

    # Accuracy graph
    ax1.set_ylabel("Accuracy")
    ax1.set_ylim(bottom=min_accuracy, top=1)
    ax1.legend(loc="lower right")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.xaxis.set_ticks_position("none")
    ax1.spines["bottom"].set_visible(False)

    # max accuracty text
    plt.text(
        0.97,
        0.97,
        get_max_validation_accuracy(history),
        horizontalalignment="right",
        verticalalignment="top",
        transform=ax1.transAxes,
        fontsize=12,
    )

    # Loss graph
    ax2.set_ylabel("Loss")
    ax2.set_yticks([])
    ax2.plot(legend=False)
    ax2.set_xlabel("Epochs")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
