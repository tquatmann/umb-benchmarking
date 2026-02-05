# Log files for modest_from-jani_check_memory on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[4.974, 5.143, 5.183, 5.234, 5.35]`



### Log file: modest_from-jani_check_memory_eajs.5-250-11_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive
Wallclock time: 4.974 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive




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

Peak memory usage: 1194 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               802704 states/s
  Peak memory:        505.82 MB
  Final size:         23.63 MB
  Time (exploration): 3.8 s
  Time (merging):     0.1 s

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.6 s

```



### Log file: modest_from-jani_check_memory_eajs.5-250-11_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive
Wallclock time: 5.143 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive




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

Peak memory usage: 1196 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               772409 states/s
  Peak memory:        505.82 MB
  Final size:         23.63 MB
  Time (exploration): 4.0 s
  Time (merging):     0.1 s

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.6 s

```



### Log file: modest_from-jani_check_memory_eajs.5-250-11_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive
Wallclock time: 5.183 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive




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

Peak memory usage: 1196 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               773977 states/s
  Peak memory:        505.82 MB
  Final size:         23.63 MB
  Time (exploration): 4.0 s
  Time (merging):     0.1 s

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

```



### Log file: modest_from-jani_check_memory_eajs.5-250-11_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive
Wallclock time: 5.234 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive




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

Peak memory usage: 1243 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               756317 states/s
  Peak memory:        388.38 MB
  Final size:         23.63 MB
  Time (exploration): 4.0 s
  Time (merging):     0.1 s

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.6 s

```



### Log file: modest_from-jani_check_memory_eajs.5-250-11_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive
Wallclock time: 5.350 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani -S Memory -D --exhaustive




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

Peak memory usage: 1196 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               751842 states/s
  Peak memory:        505.83 MB
  Final size:         23.63 MB
  Time (exploration): 4.1 s
  Time (merging):     0.1 s

+ Property ExpUtil
  Value:  10.032940688434891
  Bounds: [10.032940688434891, infinity)
  Time:   0.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          3049471
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 4.466131883374015E-08
    Iterations:  22
    Time:        0.6 s

```

