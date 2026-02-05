# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [112536473.0, 112536473.0, 112536473.0, 112536473.0, 112536473.0]



### Log file: modest_from-jani_to-aut_default_wlan.5-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model.aut AUT  -D --exhaustive
Wallclock time: 5.425 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.5-0/model.aut".

Peak memory usage: 240 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               563383 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 107.32 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.7 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.5-0/model.aut:	Size of output file is 112536473 bytes
```



### Log file: modest_from-jani_to-aut_default_wlan.5-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 5.282 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.5-0/model_rep2.aut".

Peak memory usage: 242 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               565844 states/s
  Peak memory:        95.53 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 107.32 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.7 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.5-0/model_rep2.aut:	Size of output file is 112536473 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_wlan.5-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 5.673 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.5-0/model_rep3.aut".

Peak memory usage: 243 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               518710 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.5 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 107.32 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.8 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.5-0/model_rep3.aut:	Size of output file is 112536473 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_wlan.5-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 5.509 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.5-0/model_rep4.aut".

Peak memory usage: 242 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               548356 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 107.32 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.8 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.5-0/model_rep4.aut:	Size of output file is 112536473 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_wlan.5-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 5.445 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-aut_default/wlan.5-0/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/wlan.5-0/model_rep5.aut".

Peak memory usage: 243 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               544209 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 107.32 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.8 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/wlan.5-0/model_rep5.aut:	Size of output file is 112536473 bytes
Removing output file to save space for repetition #5
```

