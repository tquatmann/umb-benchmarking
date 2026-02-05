# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [5.5, 7.0, 5.9, 5.9, 6.1]



### Log file: modest_from-jani_to-aut_default_eajs.6-300-13_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model.aut AUT  -D --exhaustive
Wallclock time: 25.295 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model.aut AUT -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.6-300-13/model.aut".

Peak memory usage: 1178 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               520602 states/s
  Peak memory:        449.26 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 15.2 s
  Time (merging):     1.3 s

+ Export to AUT
  Time:      5.5 s
  File size: 980.44 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.5 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.8 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.6-300-13/model.aut:	Size of output file is 1028067810 bytes
```



### Log file: modest_from-jani_to-aut_default_eajs.6-300-13_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 31.762 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep2.aut AUT -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep2.aut".

Peak memory usage: 1179 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               405839 states/s
  Peak memory:        449.39 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 19.5 s
  Time (merging):     1.7 s

+ Export to AUT
  Time:      7.0 s
  File size: 980.44 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   3.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.7 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep2.aut:	Size of output file is 1028067810 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_eajs.6-300-13_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 26.014 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep3.aut AUT -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep3.aut".

Peak memory usage: 1180 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               496899 states/s
  Peak memory:        449.28 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 15.9 s
  Time (merging):     1.4 s

+ Export to AUT
  Time:      5.9 s
  File size: 980.44 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.5 s

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
out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep3.aut:	Size of output file is 1028067810 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_eajs.6-300-13_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 26.589 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep4.aut AUT -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep4.aut".

Peak memory usage: 1179 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               482989 states/s
  Peak memory:        449.29 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 16.4 s
  Time (merging):     1.4 s

+ Export to AUT
  Time:      5.9 s
  File size: 980.44 MB

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
    Time:        2.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep4.aut:	Size of output file is 1028067810 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_eajs.6-300-13_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 27.648 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep5.aut AUT -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep5.aut".

Peak memory usage: 1178 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               473184 states/s
  Peak memory:        449.31 MB
  Final size:         542.19 MB
  Size on disk:       48.04 MB
  Time (exploration): 16.7 s
  Time (merging):     1.9 s

+ Export to AUT
  Time:      6.1 s
  File size: 980.44 MB

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.7 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.9 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.6-300-13/model_rep5.aut:	Size of output file is 1028067810 bytes
Removing output file to save space for repetition #5
```

