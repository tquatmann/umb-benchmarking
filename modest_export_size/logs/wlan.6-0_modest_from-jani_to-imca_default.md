# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [wlan.6-0](../../models/wlan.6-0)
Parsed values: [237968248.0, 237968248.0, 237968248.0, 237968248.0, 237968248.0]



### Log file: modest_from-jani_to-imca_default_wlan.6-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model.mrm IMCA  -D --exhaustive
Wallclock time: 29.701 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.6-0/model.mrm".

Peak memory usage: 590 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               428032 states/s
  Peak memory:        245.58 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 11.7 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      1.9 s
  File size: 226.94 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   14.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 14.9 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.6-0/model.mrm:	Size of output file is 237968248 bytes
```



### Log file: modest_from-jani_to-imca_default_wlan.6-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 31.130 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.6-0/model_rep2.mrm".

Peak memory usage: 590 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               417435 states/s
  Peak memory:        245.58 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 12.0 s
  Time (merging):     0.8 s

+ Export to IMCA
  Time:      2.0 s
  File size: 226.94 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   16.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 15.9 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.6-0/model_rep2.mrm:	Size of output file is 237968248 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_wlan.6-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 31.700 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.6-0/model_rep3.mrm".

Peak memory usage: 592 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               415564 states/s
  Peak memory:        245.59 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 12.1 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      1.9 s
  File size: 226.94 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   16.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 16.7 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.6-0/model_rep3.mrm:	Size of output file is 237968248 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_wlan.6-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 28.946 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.6-0/model_rep4.mrm".

Peak memory usage: 594 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               443303 states/s
  Peak memory:        245.57 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 11.3 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      1.9 s
  File size: 226.94 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   14.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 14.7 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.6-0/model_rep4.mrm:	Size of output file is 237968248 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_wlan.6-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 31.069 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.6-0/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.6-0/model_rep5.mrm".

Peak memory usage: 592 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               428875 states/s
  Peak memory:        245.57 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 11.7 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      1.9 s
  File size: 226.94 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   16.1 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 16.0 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.6-0/model_rep5.mrm:	Size of output file is 237968248 bytes
Removing output file to save space for repetition #5
```

