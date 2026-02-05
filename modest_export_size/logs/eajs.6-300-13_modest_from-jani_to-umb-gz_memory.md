# Log files

Tool configuration: modest_from-jani_to-umb-gz_memory
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [, 55733157.0, 55733131.0, 55733143.0, 55733155.0]



### Log file: modest_from-jani_to-umb-gz_memory_eajs.6-300-13_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 17.644 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




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

Peak memory usage: 2942 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               746006 states/s
  Peak memory:        1289.55 MB
  Final size:         61.23 MB
  Time (exploration): 10.6 s
  Time (merging):     0.3 s

+ UMB export
  Time:        6.5 s
  File size:   53.15 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep2.gz:	Size of output file is 55733126 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep2.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_memory_eajs.6-300-13_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 19.226 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




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

Peak memory usage: 2942 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               674148 states/s
  Peak memory:        1289.58 MB
  Final size:         61.23 MB
  Time (exploration): 11.7 s
  Time (merging):     0.4 s

+ UMB export
  Time:        6.9 s
  File size:   53.15 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep3.gz:	Size of output file is 55733100 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep3.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_memory_eajs.6-300-13_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 20.144 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




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

Peak memory usage: 2943 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               677095 states/s
  Peak memory:        1289.58 MB
  Final size:         61.23 MB
  Time (exploration): 11.7 s
  Time (merging):     0.3 s

+ UMB export
  Time:        7.8 s
  File size:   53.15 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep4.gz:	Size of output file is 55733112 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep4.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_memory_eajs.6-300-13_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 17.610 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




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

Peak memory usage: 2819 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               758466 states/s
  Peak memory:        1289.54 MB
  Final size:         61.23 MB
  Time (exploration): 10.4 s
  Time (merging):     0.4 s

+ UMB export
  Time:        6.5 s
  File size:   53.15 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/model.umb_rep5.gz:	Size of output file is 55733124 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_memory/eajs.6-300-13/umbgz.properties_rep5.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #5
```

