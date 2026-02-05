# Log files for modest_from-jani_check_memory on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[17.971, 21.384, 15.864, 18.704, 18.015]`



### Log file: modest_from-jani_check_memory_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive
Wallclock time: 17.971 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4447 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               978341 states/s
  Peak memory:        1963.24 MB
  Final size:         82.40 MB
  Time (exploration): 10.9 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.4 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.4 s

```



### Log file: modest_from-jani_check_memory_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive
Wallclock time: 21.384 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4446 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               843802 states/s
  Peak memory:        1963.29 MB
  Final size:         82.40 MB
  Time (exploration): 12.6 s
  Time (merging):     0.6 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        7.9 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        7.9 s

```



### Log file: modest_from-jani_check_memory_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive
Wallclock time: 15.864 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4445 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               1119561 states/s
  Peak memory:        1963.20 MB
  Final size:         82.40 MB
  Time (exploration): 9.5 s
  Time (merging):     0.4 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        5.7 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        5.7 s

```



### Log file: modest_from-jani_check_memory_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive
Wallclock time: 18.704 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4446 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               940610 states/s
  Peak memory:        1963.25 MB
  Final size:         82.40 MB
  Time (exploration): 11.3 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.6 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.6 s

```



### Log file: modest_from-jani_check_memory_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive
Wallclock time: 18.015 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4446 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               974397 states/s
  Peak memory:        1963.25 MB
  Final size:         82.40 MB
  Time (exploration): 10.9 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.4 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.3 s

```

