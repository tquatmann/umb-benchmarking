# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [94589127.0, 94589127.0, 94589127.0, 94589127.0, 94589127.0]



### Log file: modest_from-jani_to-aut_default_csma.3-4_rep1.log

```
Command(s):
../bin/modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model.aut AUT  -D --exhaustive
Wallclock time: 4.770 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1460287 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.3-4/model.aut".

Peak memory usage: 249 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1460287
  Choices:            1471059
  Branches:           2396727
  Rate:               528133 states/s
  Peak memory:        141.88 MB
  Final size:         47.79 MB
  Size on disk:       7.94 MB
  Time (exploration): 2.8 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 90.21 MB

+ Property all_before_max
  Probability: 0.9324469288458123
  Bounds:      [0.9324469288458123, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 3.001709289030008E-07
    Iterations:  55
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.3-4/model.aut:	Size of output file is 94589127 bytes
```



### Log file: modest_from-jani_to-aut_default_csma.3-4_rep2.log

```
Command(s):
../bin/modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 5.044 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1460287 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.3-4/model_rep2.aut".

Peak memory usage: 248 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1460287
  Choices:            1471059
  Branches:           2396727
  Rate:               499585 states/s
  Peak memory:        141.88 MB
  Final size:         47.79 MB
  Size on disk:       7.94 MB
  Time (exploration): 2.9 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 90.21 MB

+ Property all_before_max
  Probability: 0.9324469288458123
  Bounds:      [0.9324469288458123, 1]
  Time:        0.7 s

  + Value iteration
    Final error: 3.001709289030008E-07
    Iterations:  55
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.3-4/model_rep2.aut:	Size of output file is 94589127 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_csma.3-4_rep3.log

```
Command(s):
../bin/modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 4.632 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1460287 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.3-4/model_rep3.aut".

Peak memory usage: 249 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1460287
  Choices:            1471059
  Branches:           2396727
  Rate:               540647 states/s
  Peak memory:        141.87 MB
  Final size:         47.79 MB
  Size on disk:       7.94 MB
  Time (exploration): 2.7 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 90.21 MB

+ Property all_before_max
  Probability: 0.9324469288458123
  Bounds:      [0.9324469288458123, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 3.001709289030008E-07
    Iterations:  55
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.3-4/model_rep3.aut:	Size of output file is 94589127 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_csma.3-4_rep4.log

```
Command(s):
../bin/modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 4.997 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1460287 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.3-4/model_rep4.aut".

Peak memory usage: 250 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1460287
  Choices:            1471059
  Branches:           2396727
  Rate:               499927 states/s
  Peak memory:        141.88 MB
  Final size:         47.79 MB
  Size on disk:       7.94 MB
  Time (exploration): 2.9 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 90.21 MB

+ Property all_before_max
  Probability: 0.9324469288458123
  Bounds:      [0.9324469288458123, 1]
  Time:        0.7 s

  + Value iteration
    Final error: 3.001709289030008E-07
    Iterations:  55
    Time:        0.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.3-4/model_rep4.aut:	Size of output file is 94589127 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_csma.3-4_rep5.log

```
Command(s):
../bin/modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 3.970 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/csma.3-4/model.jani --statespace out/modest_from-jani_to-aut_default/csma.3-4/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1460287 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/csma.3-4/model_rep5.aut".

Peak memory usage: 246 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1460287
  Choices:            1471059
  Branches:           2396727
  Rate:               625927 states/s
  Peak memory:        141.87 MB
  Final size:         47.79 MB
  Size on disk:       7.94 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.7 s
  File size: 90.21 MB

+ Property all_before_max
  Probability: 0.9324469288458123
  Bounds:      [0.9324469288458123, 1]
  Time:        0.5 s

  + Value iteration
    Final error: 3.001709289030008E-07
    Iterations:  55
    Time:        0.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/csma.3-4/model_rep5.aut:	Size of output file is 94589127 bytes
Removing output file to save space for repetition #5
```

