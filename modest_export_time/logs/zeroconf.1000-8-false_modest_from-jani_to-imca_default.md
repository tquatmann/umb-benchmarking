# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [0.8, 0.9, 0.8, 0.8, 1.0]



### Log file: modest_from-jani_to-imca_default_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model.mrm IMCA  -D --exhaustive
Wallclock time: 5.686 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model.mrm".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               515059 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.6 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.8 s
  File size: 86.69 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model.mrm:	Size of output file is 90903738 bytes
```



### Log file: modest_from-jani_to-imca_default_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 6.765 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep2.mrm".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               438449 states/s
  Peak memory:        126.67 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 4.3 s
  Time (merging):     0.4 s

+ Export to IMCA
  Time:      0.9 s
  File size: 86.69 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.9 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.9 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep2.mrm:	Size of output file is 90903738 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 5.374 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep3.mrm".

Peak memory usage: 311 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               555116 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.4 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.8 s
  File size: 86.69 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep3.mrm:	Size of output file is 90903738 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 5.867 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep4.mrm".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               498520 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.8 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.8 s
  File size: 86.69 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.7 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep4.mrm:	Size of output file is 90903738 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 6.353 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep5.mrm".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               469262 states/s
  Peak memory:        126.67 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 4.0 s
  Time (merging):     0.4 s

+ Export to IMCA
  Time:      1.0 s
  File size: 86.69 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.7 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/zeroconf.1000-8-false/model_rep5.mrm:	Size of output file is 90903738 bytes
Removing output file to save space for repetition #5
```

