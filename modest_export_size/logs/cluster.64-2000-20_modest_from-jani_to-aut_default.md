# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [19135495.0, 19135495.0, 19135495.0, 19135495.0, 19135495.0]



### Log file: modest_from-jani_to-aut_default_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model.aut AUT  -D --exhaustive
Wallclock time: 1533.207 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 151060 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.64-2000-20/model.aut".

Peak memory usage: 141 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             151060
  Choices:            151060
  Branches:           733216
  Rate:               169730 states/s
  Peak memory:        66.17 MB
  Final size:         12.34 MB
  Size on disk:       3.59 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 18.25 MB

+ Property qos1
  Probability: 0.0010695396728838996
  Bounds:      [0.0010445396728838941, 0.0010945396728839051]
  Time:        1531.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1531.8 s
    Max. exit rate:   50.252
    Iterations:       1
    Final unif. rate: 50.252


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.64-2000-20/model.aut:	Size of output file is 19135495 bytes
```



### Log file: modest_from-jani_to-aut_default_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 1359.465 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 151060 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep2.aut".

Peak memory usage: 143 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             151060
  Choices:            151060
  Branches:           733216
  Rate:               163485 states/s
  Peak memory:        66.17 MB
  Final size:         12.34 MB
  Size on disk:       3.59 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 18.25 MB

+ Property qos1
  Probability: 0.0010695396728838996
  Bounds:      [0.0010445396728838941, 0.0010945396728839051]
  Time:        1358.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1358.0 s
    Max. exit rate:   50.252
    Iterations:       1
    Final unif. rate: 50.252


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep2.aut:	Size of output file is 19135495 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 1245.019 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 151060 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep3.aut".

Peak memory usage: 141 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             151060
  Choices:            151060
  Branches:           733216
  Rate:               164913 states/s
  Peak memory:        66.17 MB
  Final size:         12.34 MB
  Size on disk:       3.59 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 18.25 MB

+ Property qos1
  Probability: 0.0010695396728838996
  Bounds:      [0.0010445396728838941, 0.0010945396728839051]
  Time:        1243.6 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1243.6 s
    Max. exit rate:   50.252
    Iterations:       1
    Final unif. rate: 50.252


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep3.aut:	Size of output file is 19135495 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 1360.858 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 151060 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep4.aut".

Peak memory usage: 143 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             151060
  Choices:            151060
  Branches:           733216
  Rate:               174032 states/s
  Peak memory:        66.17 MB
  Final size:         12.34 MB
  Size on disk:       3.59 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 18.25 MB

+ Property qos1
  Probability: 0.0010695396728838996
  Bounds:      [0.0010445396728838941, 0.0010945396728839051]
  Time:        1359.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1359.4 s
    Max. exit rate:   50.252
    Iterations:       1
    Final unif. rate: 50.252


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep4.aut:	Size of output file is 19135495 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 1363.091 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.64-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 151060 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep5.aut".

Peak memory usage: 142 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             151060
  Choices:            151060
  Branches:           733216
  Rate:               184896 states/s
  Peak memory:        66.17 MB
  Final size:         12.34 MB
  Size on disk:       3.59 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 18.25 MB

+ Property qos1
  Probability: 0.0010695396728838996
  Bounds:      [0.0010445396728838941, 0.0010945396728839051]
  Time:        1361.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1361.8 s
    Max. exit rate:   50.252
    Iterations:       1
    Final unif. rate: 50.252


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.64-2000-20/model_rep5.aut:	Size of output file is 19135495 bytes
Removing output file to save space for repetition #5
```

