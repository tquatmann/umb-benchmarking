# Log files

Tool configuration: modest_from-jani_check_unsafe
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [6663.272, TO, 6376.512, TO, 6353.489]



### Log file: modest_from-jani_check_unsafe_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive
Wallclock time: 6663.272 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.

Peak memory usage: 223 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               253293 states/s
  Peak memory:        85.02 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6660.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6660.4 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996

```



### Log file: modest_from-jani_check_unsafe_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive
Wallclock time: 7200.015 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
```



### Log file: modest_from-jani_check_unsafe_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive
Wallclock time: 6376.512 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.

Peak memory usage: 219 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               252543 states/s
  Peak memory:        85.02 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6373.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6373.7 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996

```



### Log file: modest_from-jani_check_unsafe_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive
Wallclock time: 7200.019 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.
```



### Log file: modest_from-jani_check_unsafe_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive
Wallclock time: 6353.489 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/cluster.128-2000-20/model.jani --unsafe -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 597012 states.

Peak memory usage: 225 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             597012
  Choices:            597012
  Branches:           2908192
  Rate:               247620 states/s
  Peak memory:        85.01 MB
  Final size:         48.93 MB
  Size on disk:       14.50 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Property qos1
  Probability: 0.0010974025337729253
  Bounds:      [0.0010724025337729205, 0.0011224025337729301]
  Time:        6350.6 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             6350.6 s
    Max. exit rate:   50.507999999999996
    Iterations:       1
    Final unif. rate: 50.507999999999996

```

