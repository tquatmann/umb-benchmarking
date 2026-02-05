# Log files

Tool configuration: modest_from-jani_to-umb_memory
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [, 0.4, 19.8, 0.5, 0.4]



### Log file: modest_from-jani_to-umb_memory_eajs.6-300-13_rep2.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep2.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep2.txt -S Memory -D --exhaustive
Wallclock time: 11.296 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep2.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep2.txt -S Memory -D --exhaustive




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

Peak memory usage: 2940 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               759705 states/s
  Peak memory:        1289.55 MB
  Final size:         61.23 MB
  Time (exploration): 10.4 s
  Time (merging):     0.3 s

+ UMB export
  Time:        0.4 s
  File size:   604.37 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep2.umb:	Size of output file is 633731584 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep2.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb_memory_eajs.6-300-13_rep3.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep3.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep3.txt -S Memory -D --exhaustive
Wallclock time: 32.911 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep3.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep3.txt -S Memory -D --exhaustive




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

Peak memory usage: 2941 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               636720 states/s
  Peak memory:        1289.59 MB
  Final size:         61.23 MB
  Time (exploration): 12.4 s
  Time (merging):     0.4 s

+ UMB export
  Time:        19.8 s
  File size:   604.37 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep3.umb:	Size of output file is 633731584 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep3.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb_memory_eajs.6-300-13_rep4.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep4.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep4.txt -S Memory -D --exhaustive
Wallclock time: 11.585 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep4.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep4.txt -S Memory -D --exhaustive




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

Peak memory usage: 2941 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               754266 states/s
  Peak memory:        1289.54 MB
  Final size:         61.23 MB
  Time (exploration): 10.5 s
  Time (merging):     0.3 s

+ UMB export
  Time:        0.5 s
  File size:   604.37 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep4.umb:	Size of output file is 633731584 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep4.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb_memory_eajs.6-300-13_rep5.log

```
Command(s):
../bin/modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep5.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep5.txt -S Memory -D --exhaustive
Wallclock time: 13.119 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/eajs.6-300-13/model.jani --umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep5.umb out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep5.txt -S Memory -D --exhaustive




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

Peak memory usage: 2940 MB
Analysis results for model.jani

+ State space exploration
  State size:         32 bytes
  States:             7901694
  Choices:            11897412
  Branches:           19722777
  Rate:               654005 states/s
  Peak memory:        1289.58 MB
  Final size:         61.23 MB
  Time (exploration): 12.1 s
  Time (merging):     0.4 s

+ UMB export
  Time:        0.4 s
  File size:   604.37 MB
  Compression: None


############################## Output files ##############################
out/modest_from-jani_to-umb_memory/eajs.6-300-13/model_rep5.umb:	Size of output file is 633731584 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb_memory/eajs.6-300-13/umb.properties_rep5.txt:	Size of output file is 31 bytes
Removing output file to save space for repetition #5
```

