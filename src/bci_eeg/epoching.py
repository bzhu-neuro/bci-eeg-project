from mne import Epochs, events_from_annotations, pick_types

def extract_left_right_epochs(raw, tmin, tmax):
    """
    Extract events from raw annotations and epoch into left/right
    conditions.
    
    Assumes the standard EEGMMIDB annotation scheme where T1=left fist,
    T2=right fist for the imagery runs, and that events_from_annotations
    assigns integer codes 2 and 3 to T1 and T2 respectively (this is
    MNE's typical alphabetical assignment behavior, T0->1, T1->2, T2->3).
    """
    events, event_id = events_from_annotations(raw)
    picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads")
    epochs = Epochs(raw, events=events, event_id=dict(left = 2, right = 3), tmin=tmin, tmax=tmax, picks=picks, baseline=None, preload=True)
    
    return epochs