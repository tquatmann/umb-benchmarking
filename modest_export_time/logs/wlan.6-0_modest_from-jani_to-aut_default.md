# Log files for modest_from-jani_to-aut_default on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[2.7, 3.0, 2.9, 11.9, 2.6]`



### Log file: modest_from-jani_to-aut_default_wlan.6-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model.aut AUT  -D --exhaustive
Wallclock time: 31.912 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.6-0/model.aut".

Peak memory usage: 593 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               406853 states/s
  Peak memory:        245.58 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 12.3 s
  Time (merging):     0.7 s

+ Export to AUT
  Time:      2.7 s
  File size: 433.07 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   15.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 15.5 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.6-0/model.aut:	Size of output file is 454108899 bytes
```



### Log file: modest_from-jani_to-aut_default_wlan.6-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 36.994 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.6-0/model_rep2.aut".

Peak memory usage: 591 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               361113 states/s
  Peak memory:        245.55 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 13.9 s
  Time (merging):     0.8 s

+ Export to AUT
  Time:      3.0 s
  File size: 433.07 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   18.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 18.8 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.6-0/model_rep2.aut:	Size of output file is 454108899 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_wlan.6-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 33.529 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.6-0/model_rep3.aut".

Peak memory usage: 592 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               372087 states/s
  Peak memory:        245.59 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 13.5 s
  Time (merging):     0.8 s

+ Export to AUT
  Time:      2.9 s
  File size: 433.07 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   15.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 15.9 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.6-0/model_rep3.aut:	Size of output file is 454108899 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_wlan.6-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 50.064 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.6-0/model_rep4.aut".

Peak memory usage: 587 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               345849 states/s
  Peak memory:        245.55 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 14.5 s
  Time (merging):     0.8 s

+ Export to AUT
  Time:      11.9 s
  File size: 433.07 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   22.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 22.4 s
    Min. prob. 1 states:          5007548
    Time for min. prob. 1 states: 0.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.6-0/model_rep4.aut:	Size of output file is 454108899 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_wlan.6-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 30.505 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.6-0/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.6-0/model_rep5.aut".

Peak memory usage: 592 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               419358 states/s
  Peak memory:        245.58 MB
  Final size:         223.56 MB
  Size on disk:       41.24 MB
  Time (exploration): 12.0 s
  Time (merging):     0.7 s

+ Export to AUT
  Time:      2.6 s
  File size: 433.07 MB

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
out/modest_from-jani_to-aut_default/wlan.6-0/model_rep5.aut:	Size of output file is 454108899 bytes
Removing output file to save space for repetition #5
```

