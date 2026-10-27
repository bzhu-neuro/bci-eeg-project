# BCI Project: Testing Synchronization Principles in Real Motor-Imagery EEG

An independent research project decoding motor-imagery EEG, worked as
the companion of [hodgkin-huxley-neuron](https://github.com/bzhu-neuro/hodgkin-huxley-neuron) project to built and validated a
computational model showing how coupling strength and network topology
determine oscillator synchronization. This project tests whether those
same principles show up as measurable, useful phase-synchrony features in
real human EEG during motor imagery.


## Project roadmap

- [ ] **Phase 1 (Fundamentals):** MNE-Python fundamentals, load EEGMMIDB,
      reproduce the classic contralateral mu/beta ERD/ERS pattern.
- [ ] **Phase 2 (Aim 1):** Baseline band-power motor-imagery classifier.
- [ ] **Phase 3 (Aim 2):** Phase-locking value (PLV) synchrony features,
      statistical testing of the desynchronization hypothesis.
- [ ] **Phase 4 (Aim 3):** Compare classification using band-power vs.
      synchrony vs. combined features.
- [ ] **Phase 5 (Aim 4, stretch):** Full connectivity graph + graph-theory
      metrics, echoing the HH project's topology comparison.

## Repository structure

```
bci-eeg-project/
├── src/bci_eeg/
│   ├── constants.py       # Run mappings, frequency bands, channels of interest
│   └── 
├── scripts/
│   └── 
├── tests/
│   └── 
├── notebooks/
├── docs/lab_notebook.md   # Verification status + dated research log
└── results/figures/
```

## Installation

```bash
git clone https://github.com/bzhu-neuro/bci-eeg-project.git
cd bci-eeg-project
python -m venv venv             # prefer to use Miniconda to manage
source venv/bin/activate        # on Windows: venv\Scripts\activate.bat
pip install -r requirements.txt
pip install -e .
```

## Usage

```bash
# Run Phase 1: load subject 1, preprocess, plot ERD/ERS grid

# Run the tests that don't require MNE
pytest tests/ -v
```

## Background

The PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB) provides
64-channel EEG from 109 subjects performing and imagining left/right fist
and both-fists/feet movements. This project uses the imagined left/right
fist runs to study event-related desynchronization (ERD) in the mu
(8–12 Hz) and beta (13–30 Hz) bands over sensorimotor cortex — the
same "network shifting between synchronized and desynchronized states"
phenomenon studied computationally, at a much more abstract level, in the
companion HH project's Stage 3.

## License

MIT — see `LICENSE`.
