# Log files

Tool configuration: modest_from-jani_check_memory
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [TO, TO, 6931.828, TO, 6412.634]



### Log file: modest_from-jani_check_memory_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive
Wallclock time: 7200.011 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
```



### Log file: modest_from-jani_check_memory_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive
Wallclock time: 7200.012 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
```



### Log file: modest_from-jani_check_memory_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive
Wallclock time: 6931.828 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.

Peak memory usage: 378 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               453312 states/s
  Peak memory:        155.73 MB
  Final size:         9.18 MB
  Time (exploration): 1.3 s
  Time (merging):     0.0 s

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6930.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6930.2 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996

```



### Log file: modest_from-jani_check_memory_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive
Wallclock time: 7200.022 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
```



### Log file: modest_from-jani_check_memory_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive
Wallclock time: 6412.634 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.

Peak memory usage: 378 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               517341 states/s
  Peak memory:        155.72 MB
  Final size:         9.18 MB
  Time (exploration): 1.2 s
  Time (merging):     0.0 s

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6411.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6411.3 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996

```

