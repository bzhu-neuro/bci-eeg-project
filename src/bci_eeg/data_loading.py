from mne.datasets import eegbci
from mne.io import read_raw_edf, concatenate_raws
from mne.channels import make_standard_montage
    
def load_subject_raw(subject, runs):
    """
    Download (if needed) and load raw EEG for one subject's motor-imagery
    runs, with channel names standardized and a 10-05 montage attached.
    """
    raw_fnames = eegbci.load_data(subject, runs)
    raws = [read_raw_edf(f, preload=True) for f in raw_fnames]
    raw = concatenate_raws(raws)
    eegbci.standardize(raw)
    montage = make_standard_montage('standard_1005')
    raw.set_montage(montage, match_case=False, match_alias=True)
    
    return raw
