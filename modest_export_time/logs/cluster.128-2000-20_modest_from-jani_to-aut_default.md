# Log files for modest_from-jani_to-aut_default on model [cluster.128-2000-20](../../models/cluster.128-2000-20)

Parsed values: `[0.9, 0.8, TO, 0.8, TO]`



### Log file: modest_from-jani_to-aut_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model.aut AUT  -D --exhaustive
Wallclock time: 6622.511 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.128-2000-20/model.aut".

Peak memory usage: 221 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               223015 states/s
  Peak memory:        80.42 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.7 s
  Time (merging):     0.3 s

+ Export to AUT
  Time:      0.9 s
  File size: 75.66 MB

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6618.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6618.5 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.128-2000-20/model.aut:	Size of output file is 79333426 bytes
```



### Log file: modest_from-jani_to-aut_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 6937.021 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep2.aut".

Peak memory usage: 226 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               243877 states/s
  Peak memory:        80.42 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.5 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 75.66 MB

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6933.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6933.3 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep2.aut:	Size of output file is 79333426 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 7200.010 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep3.aut".

############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep3.aut:	Size of output file is 79333426 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 6417.217 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep4.aut".

Peak memory usage: 224 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               242491 states/s
  Peak memory:        80.42 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.5 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.8 s
  File size: 75.66 MB

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6412.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6412.8 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996


############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep4.aut:	Size of output file is 79333426 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 7200.011 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep5.aut".

############################## Output files ##############################
out/modest_from-jani_to-aut_default/cluster.128-2000-20/model_rep5.aut:	Size of output file is 79333426 bytes
Removing output file to save space for repetition #5
```

