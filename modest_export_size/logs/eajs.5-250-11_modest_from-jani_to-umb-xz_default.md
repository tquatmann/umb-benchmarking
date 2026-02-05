# Log files

Tool configuration: modest_from-jani_to-umb-xz_default
Benchmark: [eajs.5-250-11](../../models/eajs.5-250-11)
Parsed values: [, 6134867.0, 6089019.0, 6090899.0, 6130135.0]



### Log file: modest_from-jani_to-umb-xz_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 35.697 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 561 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               520832 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 5.9 s
  Time (merging):     0.5 s

+ UMB export
  Time:        29.0 s
  File size:   5.85 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep2.xz:	Size of output file is 6134836 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep2.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 40.414 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 562 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               473888 states/s
  Peak memory:        193.23 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.5 s
  Time (merging):     0.6 s

+ UMB export
  Time:        32.5 s
  File size:   5.81 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep3.xz:	Size of output file is 6088988 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep3.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 33.751 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 561 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               541262 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 5.6 s
  Time (merging):     0.5 s

+ UMB export
  Time:        27.3 s
  File size:   5.81 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep4.xz:	Size of output file is 6090868 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep4.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 44.158 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 562 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               449377 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.8 s
  Time (merging):     0.6 s

+ UMB export
  Time:        36.5 s
  File size:   5.85 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/model.umb_rep5.xz:	Size of output file is 6130104 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/eajs.5-250-11/umbxz.properties_rep5.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #5
```

