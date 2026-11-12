import numpy as np
from bci_eeg.synthetic import make_synthetic_mi

def test_shapes_and_labels():
    X, y = make_synthetic_mi(n_trials=60, n_channels=8, sfreq=160.0, duration=3.0)
    assert X.shape == (60, 8, 480)
    assert y.shape == (60,)
    assert set(np.unique(y)) == {0, 1}
    assert np.sum(y == 0) == np.sum(y == 1)          # balanced

def test_labels_are_shuffled():
    _, y = make_synthetic_mi(n_trials=60)
    assert not np.array_equal(y, np.sort(y))          # not 0,0,0,...,1,1,1

def test_same_seed_same_data_different_seed_different_data():
    X1, y1 = make_synthetic_mi(seed=5)
    X2, y2 = make_synthetic_mi(seed=5)
    X3, _ = make_synthetic_mi(seed=6)
    assert np.array_equal(X1, X2) and np.array_equal(y1, y2)
    assert not np.array_equal(X1, X3)

def test_planted_erd_is_where_the_spec_says():
    """With no mixing, class 0 must have weak 10 Hz power on channel 0, and
    class 1 weak 10 Hz power on channel 1. We read 10 Hz power from the FFT bin
    (bin = frequency * duration, exact because 10 Hz fits whole cycles)."""
    duration = 3.0
    X, y = make_synthetic_mi(n_trials=60, n_channels=4, duration=duration,
                             erd_depth=0.7, mixing=np.eye(4), seed=1)
    bin10 = int(round(10 * duration))
    power = np.abs(np.fft.rfft(X, axis=-1)[:, :, bin10]) ** 2
    assert power[y == 0, 0].mean() < 0.5 * power[y == 1, 0].mean()
    assert power[y == 1, 1].mean() < 0.5 * power[y == 0, 1].mean()
    # channels 2 and 3 carry no planted effect: no strong class difference
    ratio = power[y == 0, 2].mean() / power[y == 1, 2].mean()
    assert 0.5 < ratio < 2.0
