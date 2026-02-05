# Log files

Tool configuration: modest_from-jani_check_unsafe-memory
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [3.305, 3.145, 3.39, 3.199, 3.219]



### Log file: modest_from-jani_check_unsafe-memory_crowds.5-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 3.305 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 912 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               1060674 states/s
  Peak memory:        255.19 MB
  Final size:         15.98 MB
  Time (exploration): 2.0 s
  Time (merging):     0.1 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```



### Log file: modest_from-jani_check_unsafe-memory_crowds.5-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 3.145 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 912 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               1108576 states/s
  Peak memory:        255.18 MB
  Final size:         15.98 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```



### Log file: modest_from-jani_check_unsafe-memory_crowds.5-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 3.390 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 914 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               1070032 states/s
  Peak memory:        255.18 MB
  Final size:         15.98 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```



### Log file: modest_from-jani_check_unsafe-memory_crowds.5-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 3.199 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 912 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               1103238 states/s
  Peak memory:        255.18 MB
  Final size:         15.98 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```



### Log file: modest_from-jani_check_unsafe-memory_crowds.5-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive
Wallclock time: 3.219 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --unsafe -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 912 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               1088675 states/s
  Peak memory:        255.18 MB
  Final size:         15.98 MB
  Time (exploration): 1.9 s
  Time (merging):     0.1 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```

