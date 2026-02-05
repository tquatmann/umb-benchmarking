# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [0.3, 0.3, 0.3, 0.3, 0.3]



### Log file: modest_from-jani_to-aut_default_wlan.4-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model.aut AUT  -D --exhaustive
Wallclock time: 1.873 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.4-0/model.aut".

Peak memory usage: 145 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               379956 states/s
  Peak memory:        70.65 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.3 s
  File size: 26.44 MB

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
out/modest_from-jani_to-aut_default/wlan.4-0/model.aut:	Size of output file is 27725494 bytes
```



### Log file: modest_from-jani_to-aut_default_wlan.4-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 1.874 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.4-0/model_rep2.aut".

Peak memory usage: 148 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               377462 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.3 s
  File size: 26.44 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.2 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.4-0/model_rep2.aut:	Size of output file is 27725494 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_wlan.4-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 1.574 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.4-0/model_rep3.aut".

Peak memory usage: 146 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               448635 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.3 s
  File size: 26.44 MB

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
out/modest_from-jani_to-aut_default/wlan.4-0/model_rep3.aut:	Size of output file is 27725494 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_wlan.4-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 1.937 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.4-0/model_rep4.aut".

Peak memory usage: 149 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               371367 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 1.0 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.3 s
  File size: 26.44 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   0.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.3 s
    Min. prob. 1 states:          345000
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.4-0/model_rep4.aut:	Size of output file is 27725494 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_wlan.4-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 1.868 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.4-0/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.4-0/model_rep5.aut".

Peak memory usage: 145 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               381215 states/s
  Peak memory:        70.67 MB
  Final size:         14.99 MB
  Size on disk:       2.65 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.3 s
  File size: 26.44 MB

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
out/modest_from-jani_to-aut_default/wlan.4-0/model_rep5.aut:	Size of output file is 27725494 bytes
Removing output file to save space for repetition #5
```

