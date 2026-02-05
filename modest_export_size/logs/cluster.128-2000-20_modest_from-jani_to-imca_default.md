# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [54870951.0, 54870951.0, 54870951.0, 54870951.0, 54870951.0]



### Log file: modest_from-jani_to-imca_default_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model.mrm IMCA  -D --exhaustive
Wallclock time: 7200.012 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/cluster.128-2000-20/model.mrm".

############################## Output files ##############################
out/modest_from-jani_to-imca_default/cluster.128-2000-20/model.mrm:	Size of output file is 54870951 bytes
```



### Log file: modest_from-jani_to-imca_default_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 6551.309 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep2.mrm".

Peak memory usage: 223 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               238138 states/s
  Peak memory:        80.42 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.5 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.6 s
  File size: 52.33 MB

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6547.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6547.7 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996


############################## Output files ##############################
out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep2.mrm:	Size of output file is 54870951 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 7200.009 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep3.mrm".

############################## Output files ##############################
out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep3.mrm:	Size of output file is 54870951 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 6630.369 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep4.mrm".

Peak memory usage: 224 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               216859 states/s
  Peak memory:        80.43 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.8 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.6 s
  File size: 52.33 MB

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6626.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6626.4 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996


############################## Output files ##############################
out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep4.mrm:	Size of output file is 54870951 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 7200.019 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --statespace out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep5.mrm".

############################## Output files ##############################
out/modest_from-jani_to-imca_default/cluster.128-2000-20/model_rep5.mrm:	Size of output file is 54870951 bytes
Removing output file to save space for repetition #5
```

