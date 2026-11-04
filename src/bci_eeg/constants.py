"""
Constants for the EEGMMIDB motor-imagery pipeline.
"""


# EEGMMIDB run numbers for "imagine opening/closing left or right fist"
# (3 repeated runs of the same task per subject).
RUNS_LEFT_RIGHT_IMAGERY = [4, 8, 12]


# Frequency range covering mu (8-12 Hz) and beta (13-30 Hz) bands, the
# two bands classically involved in motor ERD/ERS.
ERDS_FREQ_MIN = 6
ERDS_FREQ_MAX = 30
ERDS_FREQ_STEP = 1


MU_BAND = (8,12)
BETA_BAND = (13,30)


# Motor cortex channels for the classic contralateral ERD comparison.
CHANNELS_OF_INTEREST = ["C3", "C4"]


# Epoch window (seconds) relative to event onset: includes pre-stimulus
# baseline through the imagery period.
EPOCH_TMIN = -1.0
EPOCH_TMAX = 4.0
BASELINE_WINDOW = (-1.0, 0.0)


# Bandpass filter range applied during preprocessing.
FILTER_LOW_HZ = 1.0
FILTER_HIGH_HZ = 40.0
