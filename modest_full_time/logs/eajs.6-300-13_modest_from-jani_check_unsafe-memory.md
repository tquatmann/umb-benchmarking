# Log files for modest_from-jani_check_unsafe-memory on model [eajs.6-300-13](../../models/eajs.6-300-13)

Parsed values: `[14.574, 12.906, 17.582, 12.981, 12.776]`



### Log file: modest_from-jani_check_unsafe-memory_eajs.6-300-13_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 14.574 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive




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

Peak memory usage: 2999 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               701874 states/s
  Peak memory:        1292.84 MB
  Final size:         61.23 MB
  Time (exploration): 11.3 s
  Time (merging):     0.4 s

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

```



### Log file: modest_from-jani_check_unsafe-memory_eajs.6-300-13_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 12.906 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive




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

Peak memory usage: 2998 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               799443 states/s
  Peak memory:        1292.81 MB
  Final size:         61.23 MB
  Time (exploration): 9.9 s
  Time (merging):     0.3 s

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.6 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.8 s

```



### Log file: modest_from-jani_check_unsafe-memory_eajs.6-300-13_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 17.582 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive




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

Peak memory usage: 3000 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               593488 states/s
  Peak memory:        1292.91 MB
  Final size:         61.23 MB
  Time (exploration): 13.3 s
  Time (merging):     0.4 s

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   3.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.8 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.1 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        2.7 s

```



### Log file: modest_from-jani_check_unsafe-memory_eajs.6-300-13_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 12.981 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive




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

Peak memory usage: 2999 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               787649 states/s
  Peak memory:        1292.81 MB
  Final size:         61.23 MB
  Time (exploration): 10.0 s
  Time (merging):     0.3 s

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.6 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.8 s

```



### Log file: modest_from-jani_check_unsafe-memory_eajs.6-300-13_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 12.776 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --unsafe -S Memory -D --exhaustive




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

Peak memory usage: 2999 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               796783 states/s
  Peak memory:        1292.80 MB
  Final size:         61.23 MB
  Time (exploration): 9.9 s
  Time (merging):     0.3 s

+ Property ExpUtil
  Value:  12.05111082306636
  Bounds: [12.05111082306636, infinity)
  Time:   2.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.5 s
    Min. prob. 1 states:          7901694
    Time for min. prob. 1 states: 0.0 s

  + Value iteration
    Final error: 8.54690416100535E-07
    Iterations:  24
    Time:        1.7 s

```

