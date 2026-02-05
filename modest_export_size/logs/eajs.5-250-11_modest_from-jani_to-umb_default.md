# Log files for modest_from-jani_to-umb_default on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[226687007.0, 226687007.0, 226687007.0, 226687007.0, 226687007.0]`



### Log file: modest_from-jani_to-umb_default_eajs.5-250-11_rep1.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties.txt  -D --exhaustive
Wallclock time: 0.269 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties.txt -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "loc_1" into 3 locations in automaton "Process_1".
model.jani:variables[7]: info: Expanding variable "loc_2" into 3 locations in automaton "Process_2".
model.jani:variables[9]: info: Expanding variable "user_1" into 6 locations in automaton "Resources".
model.jani:variables[11]: info: Expanding variable "loc_3" into 3 locations in automaton "Process_3".
model.jani:variables[12]: info: Expanding variable "loc_5" into 3 locations in automaton "Process_5".
model.jani:variables[15]: info: Expanding variable "loc_4" into 3 locations in automaton "Process_4".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb_default/eajs.5-250-11/model.umb" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb_default/eajs.5-250-11/model.umb:	Size of output file is 226686976 bytes
out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties.txt:	Size of output file is 31 bytes
```



### Log file: modest_from-jani_to-umb_default_eajs.5-250-11_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep2.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep2.txt  -D --exhaustive
Wallclock time: 6.534 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep2.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep2.txt -D --exhaustive




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

Peak memory usage: 468 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               553745 states/s
  Peak memory:        193.19 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 5.5 s
  Time (merging):     0.5 s

+ UMB export
  Time:        0.2 s
  File size:   216.19 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep2.umb:	Size of output file is 226686976 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep2.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb_default_eajs.5-250-11_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep3.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep3.txt  -D --exhaustive
Wallclock time: 7.397 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep3.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep3.txt -D --exhaustive




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

Peak memory usage: 467 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               496980 states/s
  Peak memory:        193.21 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.2 s
  Time (merging):     0.6 s

+ UMB export
  Time:        0.3 s
  File size:   216.19 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep3.umb:	Size of output file is 226686976 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep3.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb_default_eajs.5-250-11_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep4.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep4.txt  -D --exhaustive
Wallclock time: 7.617 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep4.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep4.txt -D --exhaustive




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

Peak memory usage: 466 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               490190 states/s
  Peak memory:        193.19 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 6.2 s
  Time (merging):     0.6 s

+ UMB export
  Time:        0.3 s
  File size:   216.19 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep4.umb:	Size of output file is 226686976 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep4.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb_default_eajs.5-250-11_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep5.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep5.txt  -D --exhaustive
Wallclock time: 6.503 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.5-250-11/model.jani --umb out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep5.umb out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep5.txt -D --exhaustive




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

Peak memory usage: 467 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             3049471
  Choices:            4256193
  Branches:           6977654
  Rate:               551242 states/s
  Peak memory:        193.20 MB
  Final size:         192.18 MB
  Size on disk:       17.66 MB
  Time (exploration): 5.5 s
  Time (merging):     0.5 s

+ UMB export
  Time:        0.2 s
  File size:   216.19 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_default/eajs.5-250-11/model_rep5.umb:	Size of output file is 226686976 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb_default/eajs.5-250-11/umb.properties_rep5.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #5
```

