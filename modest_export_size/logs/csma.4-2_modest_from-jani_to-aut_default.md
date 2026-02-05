# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [50193879.0, 50193879.0, 50193879.0, 50193879.0, 50193879.0]



### Log file: modest_from-jani_to-aut_default_csma.4-2_rep1.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model.aut AUT  -D --exhaustive
Wallclock time: 3.291 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.4-2/model.aut".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               438918 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.8 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.5 s
  File size: 47.87 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.4-2/model.aut:	Size of output file is 50193879 bytes
```



### Log file: modest_from-jani_to-aut_default_csma.4-2_rep2.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 10.260 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.4-2/model_rep2.aut".

Peak memory usage: 177 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               118189 states/s
  Peak memory:        88.05 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 6.5 s
  Time (merging):     0.4 s

+ Export to AUT
  Time:      1.5 s
  File size: 47.87 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.9 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.4-2/model_rep2.aut:	Size of output file is 50193879 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_csma.4-2_rep3.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 3.302 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.4-2/model_rep3.aut".

Peak memory usage: 177 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               382703 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 2.0 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.5 s
  File size: 47.87 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.3 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.4-2/model_rep3.aut:	Size of output file is 50193879 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_csma.4-2_rep4.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 2.983 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.4-2/model_rep4.aut".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               409437 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.5 s
  File size: 47.87 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.4-2/model_rep4.aut:	Size of output file is 50193879 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_csma.4-2_rep5.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 2.651 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-aut_default/csma.4-2/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.4-2/model_rep5.aut".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               459013 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.7 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.4 s
  File size: 47.87 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.4-2/model_rep5.aut:	Size of output file is 50193879 bytes
Removing output file to save space for repetition #5
```

