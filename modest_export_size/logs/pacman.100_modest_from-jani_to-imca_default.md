# Log files for modest_from-jani_to-imca_default on model [pacman.100](../../models/pacman.100)

Parsed values: `[2784367052.0, 2784367052.0, 2784367052.0, 2784367052.0, 2784367052.0]`



### Log file: modest_from-jani_to-imca_default_pacman.100_rep1.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model.mrm IMCA  -D --exhaustive
Wallclock time: 252.339 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.100/model.mrm".

Peak memory usage: 7027 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               364786 states/s
  Peak memory:        3180.31 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 217.8 s
  Time (merging):     8.1 s

+ Export to IMCA
  Time:      22.5 s
  File size: 2655.38 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        2.9 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.100/model.mrm:	Size of output file is 2784367052 bytes
```



### Log file: modest_from-jani_to-imca_default_pacman.100_rep2.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 247.290 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.100/model_rep2.mrm".

Peak memory usage: 7027 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               367316 states/s
  Peak memory:        3180.29 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 216.4 s
  Time (merging):     7.7 s

+ Export to IMCA
  Time:      20.0 s
  File size: 2655.38 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        2.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.100/model_rep2.mrm:	Size of output file is 2784367052 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_pacman.100_rep3.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 245.290 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.100/model_rep3.mrm".

Peak memory usage: 7027 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               371466 states/s
  Peak memory:        3180.22 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 213.9 s
  Time (merging):     7.6 s

+ Export to IMCA
  Time:      20.8 s
  File size: 2655.38 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        2.5 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.100/model_rep3.mrm:	Size of output file is 2784367052 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_pacman.100_rep4.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 249.874 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.100/model_rep4.mrm".

Peak memory usage: 7029 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               364368 states/s
  Peak memory:        3180.29 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 218.0 s
  Time (merging):     7.5 s

+ Export to IMCA
  Time:      20.6 s
  File size: 2655.38 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        3.2 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.9 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.100/model_rep4.mrm:	Size of output file is 2784367052 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_pacman.100_rep5.log

```
Command(s):
../bin/modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 285.536 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.100/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.100/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 79440921 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.100/model_rep5.mrm".

Peak memory usage: 7029 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             79440921
  Choices:            100215175
  Branches:           109963876
  Rate:               313732 states/s
  Peak memory:        3142.28 MB
  Final size:         2442.50 MB
  Size on disk:       398.95 MB
  Time (exploration): 253.2 s
  Time (merging):     7.8 s

+ Export to IMCA
  Time:      21.1 s
  File size: 2655.38 MB

+ Property crash
  Probability: 0.5511176224662503
  Bounds:      [0.5511176224662503, 0.5511176224662503]
  Time:        2.7 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        2.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.100/model_rep5.mrm:	Size of output file is 2784367052 bytes
Removing output file to save space for repetition #5
```

