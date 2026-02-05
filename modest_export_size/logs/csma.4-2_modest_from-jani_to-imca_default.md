# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [25205318.0, 25205318.0, 25205318.0, 25205318.0, 25205318.0]



### Log file: modest_from-jani_to-imca_default_csma.4-2_rep1.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model.mrm IMCA  -D --exhaustive
Wallclock time: 3.230 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/csma.4-2/model.mrm".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               442230 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.7 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.3 s
  File size: 24.04 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/csma.4-2/model.mrm:	Size of output file is 25205318 bytes
```



### Log file: modest_from-jani_to-imca_default_csma.4-2_rep2.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 2.721 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/csma.4-2/model_rep2.mrm".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               419121 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.8 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.3 s
  File size: 24.04 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/csma.4-2/model_rep2.mrm:	Size of output file is 25205318 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_csma.4-2_rep3.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 2.618 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/csma.4-2/model_rep3.mrm".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               451399 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.7 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.3 s
  File size: 24.04 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/csma.4-2/model_rep3.mrm:	Size of output file is 25205318 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_csma.4-2_rep4.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 2.419 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/csma.4-2/model_rep4.mrm".

Peak memory usage: 176 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               481645 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.6 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.3 s
  File size: 24.04 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/csma.4-2/model_rep4.mrm:	Size of output file is 25205318 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_csma.4-2_rep5.log

```
Command(s):
../bin/modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 2.860 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.4-2/model.jani --statespace out/modest_from-jani_to-imca_default/csma.4-2/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 761962 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/csma.4-2/model_rep5.mrm".

Peak memory usage: 178 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             761962
  Choices:            825504
  Branches:           1327068
  Rate:               407031 states/s
  Peak memory:        84.62 MB
  Final size:         26.55 MB
  Size on disk:       4.37 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Export to IMCA
  Time:      0.3 s
  File size: 24.04 MB

+ Property all_before_max
  Probability: 0.7764601488725227
  Bounds:      [0.7764601488725227, 1]
  Time:        0.2 s

  + Value iteration
    Final error: 5.657466320453835E-07
    Iterations:  38
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/csma.4-2/model_rep5.mrm:	Size of output file is 25205318 bytes
Removing output file to save space for repetition #5
```

