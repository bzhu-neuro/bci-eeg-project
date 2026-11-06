from bci_eeg.constants import ERDS_FREQ_MIN, ERDS_FREQ_MAX, ERDS_FREQ_STEP, BASELINE_WINDOW
import numpy as np

def compute_erds_power(epochs, channel_name, baselines = BASELINE_WINDOW):
    """
    Compute a baseline-corrected (percent change) time-frequency power map
    for a single channel, across the mu/beta range.
    """
    freqs = np.arange(ERDS_FREQ_MIN, ERDS_FREQ_MAX, ERDS_FREQ_STEP)
    n_cycles = freqs / 2.0
    epochs_picked = epochs.copy().pick(channel_name)
    power = epochs_picked.compute_tfr(
        method="multitaper", 
        freqs=freqs, 
        n_cycles=n_cycles, 
        return_itc=False,
        average=True,
        decim=2,
        use_fft = True
    )
    power.apply_baseline(baseline=baselines, mode='percent')
    return power
