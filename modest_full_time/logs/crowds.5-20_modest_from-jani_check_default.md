# Log files for modest_from-jani_check_default on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[5.198, 4.852, 5.94, 5.252, 5.044]`



### Log file: modest_from-jani_check_default_crowds.5-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani  -D --exhaustive
Wallclock time: 5.198 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               609684 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.4 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.1 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.1 s

```



### Log file: modest_from-jani_check_default_crowds.5-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani  -D --exhaustive
Wallclock time: 4.852 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 394 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               664074 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.1 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```



### Log file: modest_from-jani_check_default_crowds.5-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani  -D --exhaustive
Wallclock time: 5.940 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               587116 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.5 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.2 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.2 s

```



### Log file: modest_from-jani_check_default_crowds.5-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani  -D --exhaustive
Wallclock time: 5.252 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               612400 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.4 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.1 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.1 s

```



### Log file: modest_from-jani_check_default_crowds.5-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani  -D --exhaustive
Wallclock time: 5.044 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 391 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               634642 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.3 s
  Time (merging):     0.5 s

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.1 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s

```

