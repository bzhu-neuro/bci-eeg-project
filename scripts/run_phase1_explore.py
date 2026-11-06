from bci_eeg.constants import RUNS_LEFT_RIGHT_IMAGERY, FILTER_LOW_HZ, FILTER_HIGH_HZ, EPOCH_TMIN, EPOCH_TMAX, CHANNELS_OF_INTEREST
from bci_eeg.data_loading import load_subject_raw
from bci_eeg.preprocessing import filter_raw
from bci_eeg.epoching import extract_left_right_epochs
from bci_eeg.plotting import plot_erds_grid

raw = load_subject_raw(1, RUNS_LEFT_RIGHT_IMAGERY)
filtered_raw = filter_raw(raw, FILTER_LOW_HZ, FILTER_HIGH_HZ)
epochs = extract_left_right_epochs(filtered_raw, EPOCH_TMIN, EPOCH_TMAX)
plot_erds_grid(epochs, CHANNELS_OF_INTEREST, "results/figures/phase1_left_right_C3_C4_channels.png", conditions=("left", "right"))
