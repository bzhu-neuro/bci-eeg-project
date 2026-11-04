def filter_raw(raw, low_hz, high_hz):
    """
    Bandpass filter in place and return the same Raw object (MNE's
    .filter() modifies in place and also returns self, matching this
    function's return value for convenient chaining).
    """
    return raw.copy().filter(l_freq=low_hz, h_freq=high_hz)

