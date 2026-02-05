# Log files for modest_from-jani_to-imca_default on model [eajs.6-300-13](../../models/eajs.6-300-13)

Parsed values: `[5.0, 4.5, 5.2, 5.3, 4.3]`



### Log file: modest_from-jani_to-imca_default_eajs.6-300-13_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model.mrm IMCA  -D --exhaustive
Wallclock time: 27.655 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 7 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[13]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani:variables[14]: info: Expanding variable "loc_6" into 3 locations in automaton "Process_6".
model.jani:variables[17]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani: info: Need 32 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_5, Process_3.location = Process_3_loc_3_0, Process_4.location = Process_4_loc_4_0, Process_6.location = Process_6_loc_6_2, Process_5.location = Process_5_loc_5_0, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 5, t_3 = 0, loc_3 = 0, t_4 = 0, loc_4 = 0, loc_6 = 2, t_6 = 4, t_5 = 0, loc_5 = 0, battery_load = 270, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 7901694 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/eajs.6-300-13/model.mrm".

Peak memory usage: 1178 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               443641 states/s
  Peak memory:        449.35 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 17.8 s
  Time (merging):     1.6 s

+ Export to IMCA
  Time:      5.0 s
  File size: 608.77 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.6 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/eajs.6-300-13/model.mrm:	Size of output file is 638339544 bytes
```



### Log file: modest_from-jani_to-imca_default_eajs.6-300-13_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 24.169 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 7 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[13]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani:variables[14]: info: Expanding variable "loc_6" into 3 locations in automaton "Process_6".
model.jani:variables[17]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani: info: Need 32 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_5, Process_3.location = Process_3_loc_3_0, Process_4.location = Process_4_loc_4_0, Process_6.location = Process_6_loc_6_2, Process_5.location = Process_5_loc_5_0, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 5, t_3 = 0, loc_3 = 0, t_4 = 0, loc_4 = 0, loc_6 = 2, t_6 = 4, t_5 = 0, loc_5 = 0, battery_load = 270, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 7901694 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep2.mrm".

Peak memory usage: 1175 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               517127 states/s
  Peak memory:        449.27 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 15.3 s
  Time (merging):     1.3 s

+ Export to IMCA
  Time:      4.5 s
  File size: 608.77 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.6 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.6 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.9 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep2.mrm:	Size of output file is 638339544 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_eajs.6-300-13_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 27.870 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 7 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[13]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani:variables[14]: info: Expanding variable "loc_6" into 3 locations in automaton "Process_6".
model.jani:variables[17]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani: info: Need 32 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_5, Process_3.location = Process_3_loc_3_0, Process_4.location = Process_4_loc_4_0, Process_6.location = Process_6_loc_6_2, Process_5.location = Process_5_loc_5_0, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 5, t_3 = 0, loc_3 = 0, t_4 = 0, loc_4 = 0, loc_6 = 2, t_6 = 4, t_5 = 0, loc_5 = 0, battery_load = 270, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 7901694 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep3.mrm".

Peak memory usage: 1177 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               443816 states/s
  Peak memory:        449.33 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 17.8 s
  Time (merging):     1.5 s

+ Export to IMCA
  Time:      5.2 s
  File size: 608.77 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.6 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.1 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep3.mrm:	Size of output file is 638339544 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_eajs.6-300-13_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 29.096 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 7 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[13]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani:variables[14]: info: Expanding variable "loc_6" into 3 locations in automaton "Process_6".
model.jani:variables[17]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani: info: Need 32 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_5, Process_3.location = Process_3_loc_3_0, Process_4.location = Process_4_loc_4_0, Process_6.location = Process_6_loc_6_2, Process_5.location = Process_5_loc_5_0, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 5, t_3 = 0, loc_3 = 0, t_4 = 0, loc_4 = 0, loc_6 = 2, t_6 = 4, t_5 = 0, loc_5 = 0, battery_load = 270, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 7901694 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep4.mrm".

Peak memory usage: 1177 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               422347 states/s
  Peak memory:        449.35 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 18.7 s
  Time (merging):     1.6 s

+ Export to IMCA
  Time:      5.3 s
  File size: 608.77 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   3.1 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.8 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.3 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep4.mrm:	Size of output file is 638339544 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_eajs.6-300-13_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 23.826 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 7 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[13]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani:variables[14]: info: Expanding variable "loc_6" into 3 locations in automaton "Process_6".
model.jani:variables[17]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani: info: Need 32 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_5, Process_3.location = Process_3_loc_3_0, Process_4.location = Process_4_loc_4_0, Process_6.location = Process_6_loc_6_2, Process_5.location = Process_5_loc_5_0, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 5, t_3 = 0, loc_3 = 0, t_4 = 0, loc_4 = 0, loc_6 = 2, t_6 = 4, t_5 = 0, loc_5 = 0, battery_load = 270, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 7901694 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep5.mrm".

Peak memory usage: 1178 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               523846 states/s
  Peak memory:        449.28 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 15.1 s
  Time (merging):     1.3 s

+ Export to IMCA
  Time:      4.3 s
  File size: 608.77 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.5 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.1 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/eajs.6-300-13/model_rep5.mrm:	Size of output file is 638339544 bytes
Removing output file to save space for repetition #5
```

