# Lab Notebook

Dated research log. Keep entries honest and specific — what you tried, what
failed, what you changed, and why.

##

Day 1: 2026-11-03

**Goal today:** To start the second project: EEG!

**What I did:** Started part 1 of this project. Mostly
preprocessing and simple data loading.

**Result / observation:** N/A

**Problem or surprise (if any):** N/A

**Next step:** Plot the data in the time-frequency domain
and start part 2.

##

Day 1: 2026-11-05

**Goal today:** Finish stage 1 by doing the plotting
exercise.

**What I did:** Used all of the previous source code
(data_loading, constants, etc), and plotted out the
time-frequency plot.

**Result / observation:** I see more signal in C3 for
the left side and more signal for C4 in the right side.
Though, you can clearly still see the signals on both
sides.

**Problem or surprise (if any):** Had to add this "eog" 
term in the extract_left_right code. Also had to swap
baseline from erds analysis to epoching.

**Next step:** Stage phase 2.

##

Day 2: 2026-11-11

**Goal today:** To Start Stage 2. Create a function that
makes up data like the EEG database.

**What I did:** Using a random seed, I created a function
that synthesized data and ran tests to check if it works.

**Result / observation:** N/A

**Problem or surprise (if any):** N/A

**Next step:** Start making a filter.