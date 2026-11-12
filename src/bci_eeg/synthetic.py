
"""
Synthetic motor-imagery-like EEG generator.


Model: n_channels noise sources; sources 0 and 1 also carry a 10 Hz (mu)
and 20 Hz (beta) oscillation. In class 0 ("left imagery") source 0's
oscillation is suppressed (an ERD); in class 1 source 1's is suppressed.
Sources are then mixed into channels by a random matrix, mimicking volume
conduction. CSP should be able to "unmix" this.
"""

import numpy as np


def make_synthetic_mi(n_trials=60, n_channels=8, sfreq=160.0, duration=3.0,
                      erd_depth=0.6, amplitude=1.0, mixing_strength=0.3,
                      seed=0, mixing=None):
    n_times = int(sfreq * duration)
    times = np.arange(n_times)/sfreq

    rng = np.random.default_rng(seed)
    y = rng.permutation(np.tile([0,1],n_trials//2 + 1)[:n_trials])
    noise = rng.standard_normal((n_trials, n_channels, n_times))

    for trial in range(n_trials):
        for index in (0,1):
            for freq in (10,20):
                if y[trial] == index:
                    amp = amplitude * (1 - erd_depth)
                else:
                    amp = amplitude
                noise[trial,index,:] += amp * np.sin(2 * np.pi * freq * times + rng.uniform(0, 2 * np.pi))
    if mixing is None:
        mixing = np.eye(n_channels) + mixing_strength * rng.standard_normal((n_channels, n_channels))
    
    X = np.einsum("cs,est->ect", mixing, noise)
    return X,y