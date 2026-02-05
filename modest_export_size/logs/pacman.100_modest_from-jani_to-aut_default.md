# Log files for modest_from-jani_to-aut_default on model [pacman.100](../../models/pacman.100)

Parsed values: `[5633489486.0, 5633489486.0, 5633489486.0, 5633489486.0, 5633489486.0]`



### Log file: modest_from-jani_to-aut_default_pacman.100_rep1.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model.aut AUT  -D --exhaustive
Wallclock time: 281.533 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.100/model.aut".

Peak memory usage: 7034 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               339126 states/s
  Peak memory:        2883.40 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 234.3 s
  Time (merging):     8.5 s

+ Export to AUT
  Time:      34.3 s
  File size: 5372.51 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        3.8 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        3.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.100/model.aut:	Size of output file is 5633489486 bytes
```



### Log file: modest_from-jani_to-aut_default_pacman.100_rep2.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 340.017 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.100/model_rep2.aut".

Peak memory usage: 7035 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               274386 states/s
  Peak memory:        2947.35 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 289.6 s
  Time (merging):     10.7 s

+ Export to AUT
  Time:      35.0 s
  File size: 5372.51 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        4.0 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        3.8 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.100/model_rep2.aut:	Size of output file is 5633489486 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_pacman.100_rep3.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 310.291 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.100/model_rep3.aut".

Peak memory usage: 7030 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               311177 states/s
  Peak memory:        3116.86 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 255.3 s
  Time (merging):     9.2 s

+ Export to AUT
  Time:      41.8 s
  File size: 5372.51 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        3.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        3.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.100/model_rep3.aut:	Size of output file is 5633489486 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_pacman.100_rep4.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 284.585 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.100/model_rep4.aut".

Peak memory usage: 7031 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               329152 states/s
  Peak memory:        3183.29 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 241.4 s
  Time (merging):     8.9 s

+ Export to AUT
  Time:      30.1 s
  File size: 5372.51 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        3.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        3.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.100/model_rep4.aut:	Size of output file is 5633489486 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_pacman.100_rep5.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 267.390 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.100/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.100/model_rep5.aut".

Peak memory usage: 7028 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               349909 states/s
  Peak memory:        3180.33 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 227.1 s
  Time (merging):     8.0 s

+ Export to AUT
  Time:      29.1 s
  File size: 5372.51 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        2.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.100/model_rep5.aut:	Size of output file is 5633489486 bytes
Removing output file to save space for repetition #5
```

