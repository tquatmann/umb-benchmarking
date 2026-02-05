# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [181207347.0, 181207347.0, 181207347.0, 181207347.0, 181207347.0]



### Log file: modest_from-jani_to-aut_default_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model.aut AUT  -D --exhaustive
Wallclock time: 5.751 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model.aut".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               547932 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.4 s
  Time (merging):     0.3 s

+ Export to AUT
  Time:      1.1 s
  File size: 172.81 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model.aut:	Size of output file is 181207347 bytes
```



### Log file: modest_from-jani_to-aut_default_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 7.969 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep2.aut".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               389254 states/s
  Peak memory:        126.69 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 4.8 s
  Time (merging):     0.4 s

+ Export to AUT
  Time:      1.4 s
  File size: 172.81 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        1.1 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        1.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep2.aut:	Size of output file is 181207347 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 5.734 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep3.aut".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               549225 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.4 s
  Time (merging):     0.3 s

+ Export to AUT
  Time:      1.1 s
  File size: 172.81 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep3.aut:	Size of output file is 181207347 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 6.920 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep4.aut".

Peak memory usage: 311 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               441776 states/s
  Peak memory:        126.67 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 4.2 s
  Time (merging):     0.4 s

+ Export to AUT
  Time:      1.3 s
  File size: 172.81 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.8 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep4.aut:	Size of output file is 181207347 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 5.848 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --statespace out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep5.aut".

Peak memory usage: 309 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               532581 states/s
  Peak memory:        126.66 MB
  Final size:         90.72 MB
  Size on disk:       14.35 MB
  Time (exploration): 3.5 s
  Time (merging):     0.3 s

+ Export to AUT
  Time:      1.1 s
  File size: 172.81 MB

+ Property correct_max
  Probability: 4.801413635072429E-08
  Bounds:      [4.801413635072429E-08, 1]
  Time:        0.7 s

  + Value iteration
    Final error: 1.682816104324629E-07
    Iterations:  26
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/zeroconf.1000-8-false/model_rep5.aut:	Size of output file is 181207347 bytes
Removing output file to save space for repetition #5
```

