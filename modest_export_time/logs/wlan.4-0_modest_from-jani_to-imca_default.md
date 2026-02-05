# Log files for modest_from-jani_to-imca_default on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[0.2, 0.2, 0.2, 0.2, 0.2]`



### Log file: modest_from-jani_to-imca_default_wlan.4-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model.mrm IMCA  -D --exhaustive
Wallclock time: 1.601 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.4-0/model.mrm".

Peak memory usage: 145 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               433417 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.2 s
  File size: 13.87 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.4-0/model.mrm:	Size of output file is 14543943 bytes
```



### Log file: modest_from-jani_to-imca_default_wlan.4-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 1.683 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.4-0/model_rep2.mrm".

Peak memory usage: 146 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               413669 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.2 s
  File size: 13.87 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.4-0/model_rep2.mrm:	Size of output file is 14543943 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_wlan.4-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 1.433 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.4-0/model_rep3.mrm".

Peak memory usage: 146 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               491453 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.7 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.2 s
  File size: 13.87 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.4-0/model_rep3.mrm:	Size of output file is 14543943 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_wlan.4-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 1.501 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.4-0/model_rep4.mrm".

Peak memory usage: 146 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               466216 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.2 s
  File size: 13.87 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.4-0/model_rep4.mrm:	Size of output file is 14543943 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_wlan.4-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 1.439 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.4-0/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.4-0/model_rep5.mrm".

Peak memory usage: 146 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               491453 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.7 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.2 s
  File size: 13.87 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.4-0/model_rep5.mrm:	Size of output file is 14543943 bytes
Removing output file to save space for repetition #5
```

