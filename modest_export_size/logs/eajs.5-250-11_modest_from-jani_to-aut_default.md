# Log files for modest_from-jani_to-aut_default on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[351545778.0, 351545778.0, 351545778.0, 351545778.0, 351545778.0]`



### Log file: modest_from-jani_to-aut_default_eajs.5-250-11_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model.aut AUT  -D --exhaustive
Wallclock time: 11.347 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: info: Need 24 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_4, Process_3.location = Process_3_loc_3_0, Process_5.location = Process_5_loc_5_2, Process_4.location = Process_4_loc_4_0, battery_load = 220, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 4, t_3 = 0, loc_3 = 0, loc_5 = 2, t_5 = 4, t_4 = 0, loc_4 = 0, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 3049471 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.5-250-11/model.aut".

Peak memory usage: 489 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               451172 states/s
  Peak memory:        193.20 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.8 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      2.5 s
  File size: 335.26 MB

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   1.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.5-250-11/model.aut:	Size of output file is 351545778 bytes
```



### Log file: modest_from-jani_to-aut_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 39.101 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: info: Need 24 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_4, Process_3.location = Process_3_loc_3_0, Process_5.location = Process_5_loc_5_2, Process_4.location = Process_4_loc_4_0, battery_load = 220, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 4, t_3 = 0, loc_3 = 0, loc_5 = 2, t_5 = 4, t_4 = 0, loc_4 = 0, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 3049471 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep2.aut".

Peak memory usage: 493 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               129390 states/s
  Peak memory:        198.70 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 23.6 s
  Time (merging):     2.1 s

+ Export to AUT
  Time:      8.9 s
  File size: 335.26 MB

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   3.6 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.8 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.1 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        2.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep2.aut:	Size of output file is 351545778 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 10.983 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: info: Need 24 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_4, Process_3.location = Process_3_loc_3_0, Process_5.location = Process_5_loc_5_2, Process_4.location = Process_4_loc_4_0, battery_load = 220, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 4, t_3 = 0, loc_3 = 0, loc_5 = 2, t_5 = 4, t_4 = 0, loc_4 = 0, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 3049471 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep3.aut".

Peak memory usage: 490 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               460854 states/s
  Peak memory:        193.23 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.6 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      2.4 s
  File size: 335.26 MB

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep3.aut:	Size of output file is 351545778 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 9.649 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: info: Need 24 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_4, Process_3.location = Process_3_loc_3_0, Process_5.location = Process_5_loc_5_2, Process_4.location = Process_4_loc_4_0, battery_load = 220, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 4, t_3 = 0, loc_3 = 0, loc_5 = 2, t_5 = 4, t_4 = 0, loc_4 = 0, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 3049471 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep4.aut".

Peak memory usage: 489 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               528963 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 5.8 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      2.1 s
  File size: 335.26 MB

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep4.aut:	Size of output file is 351545778 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 10.001 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --statespace out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: info: Need 24 bytes per state.
model.jani: warning: The probabilities for a transition labelled "tick" with 4 branches in state (Battery.location = l, Process_1.location = Process_1_loc_1_2, Process_2.location = Process_2_loc_2_0, Resources.location = Resources_user_1_4, Process_3.location = Process_3_loc_3_0, Process_5.location = Process_5_loc_5_2, Process_4.location = Process_4_loc_4_0, battery_load = 220, loc_1 = 2, t_1 = 0, t_2 = 0, loc_2 = 0, boost_1 = 0, user_1 = 4, t_3 = 0, loc_3 = 0, loc_5 = 2, t_5 = 4, t_4 = 0, loc_4 = 0, failure_1 = False) do not sum up to the expected value of 1 (actual sum: 0.99999999999999989). Results will likely be affected by floating-point errors.
model.jani: info: Explored 3049471 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep5.aut".

Peak memory usage: 489 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               503545 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.1 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      2.2 s
  File size: 335.26 MB

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/eajs.5-250-11/model_rep5.aut:	Size of output file is 351545778 bytes
Removing output file to save space for repetition #5
```

