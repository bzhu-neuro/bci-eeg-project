import matplotlib.pyplot as plt
from bci_eeg.erds_analysis import compute_erds_power

def plot_erds_grid(epochs, channels, save_path, conditions=("left", "right")):
    """
    Produce the classic 2x2 (condition x channel) ERD/ERS grid used to
    visually check for the contralateral pattern. Save the figure to a given path.


    Returns the created matplotlib Figure.
    """
    fig, ax = plt.subplots(nrows=len(conditions), ncols=len(channels), figsize=(5*len(channels), 4*len(conditions)), sharex=True, sharey=True)

    for row, condition in enumerate(conditions):
        condition_epoch = epochs[condition]
        for column, channel in enumerate(channels):
            axis = ax[row, column]
            power = compute_erds_power(condition_epoch, channel, baseline=None)
            power.plot(axes = axis, colorbar=(column == len(channels)-1))
            axis.set_title(condition + " imagery -- " + channel)
            axis.set_xlabel("Time (s)")
            axis.set_ylabel("Frequency (Hz)")

            fig.savefig(save_path, dpi=140)
            