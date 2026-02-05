# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [124261245.0, 124261245.0, 124261245.0, 124261245.0, 124261245.0]



### Log file: modest_from-jani_to-imca_default_crowds.5-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model.mrm IMCA  -D --exhaustive
Wallclock time: 6.815 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.5-20/model.mrm".

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               584122 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.5 s
  Time (merging):     0.5 s

+ Export to IMCA
  Time:      1.3 s
  File size: 118.50 MB

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.1 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.1 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.5-20/model.mrm:	Size of output file is 124261245 bytes
```



### Log file: modest_from-jani_to-imca_default_crowds.5-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 6.272 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.5-20/model_rep2.mrm".

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               615875 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.4 s
  Time (merging):     0.5 s

+ Export to IMCA
  Time:      1.1 s
  File size: 118.50 MB

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.5-20/model_rep2.mrm:	Size of output file is 124261245 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_crowds.5-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 7.011 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.5-20/model_rep3.mrm".

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               570861 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.6 s
  Time (merging):     0.5 s

+ Export to IMCA
  Time:      1.3 s
  File size: 118.50 MB

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.2 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.5-20/model_rep3.mrm:	Size of output file is 124261245 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_crowds.5-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 6.232 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.5-20/model_rep4.mrm".

Peak memory usage: 391 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               646380 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.3 s
  Time (merging):     0.4 s

+ Export to IMCA
  Time:      1.1 s
  File size: 118.50 MB

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.0 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.5-20/model_rep4.mrm:	Size of output file is 124261245 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_crowds.5-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 7.472 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.5-20/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.5-20/model_rep5.mrm".

Peak memory usage: 395 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               550441 states/s
  Peak memory:        126.19 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.8 s
  Time (merging):     0.6 s

+ Export to IMCA
  Time:      1.3 s
  File size: 118.50 MB

+ Property positive
  Probability: 0.08606891126753627
  Bounds:      [0.08606891126753627, 1]
  Time:        1.2 s

  + Value iteration
    Final error: 9.368723888609267E-07
    Iterations:  58
    Time:        1.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.5-20/model_rep5.mrm:	Size of output file is 124261245 bytes
Removing output file to save space for repetition #5
```

