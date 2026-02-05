# Log files for modest_from-jani_to-aut_default on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[1017724123.0, 1017724123.0, 1017724123.0, 1017724123.0, 1017724123.0]`



### Log file: modest_from-jani_to-aut_default_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model.aut AUT  -D --exhaustive
Wallclock time: 30.289 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/crowds.6-20/model.aut".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               685066 states/s
  Peak memory:        746.93 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.5 s
  Time (merging):     2.2 s

+ Export to AUT
  Time:      6.2 s
  File size: 970.58 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.0 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/crowds.6-20/model.aut:	Size of output file is 1017724123 bytes
```



### Log file: modest_from-jani_to-aut_default_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 31.786 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/crowds.6-20/model_rep2.aut".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               651289 states/s
  Peak memory:        746.96 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 16.3 s
  Time (merging):     2.3 s

+ Export to AUT
  Time:      6.5 s
  File size: 970.58 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.1 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/crowds.6-20/model_rep2.aut:	Size of output file is 1017724123 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 30.312 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/crowds.6-20/model_rep3.aut".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               679984 states/s
  Peak memory:        746.93 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.7 s
  Time (merging):     2.1 s

+ Export to AUT
  Time:      6.2 s
  File size: 970.58 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.1 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/crowds.6-20/model_rep3.aut:	Size of output file is 1017724123 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 36.474 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/crowds.6-20/model_rep4.aut".

Peak memory usage: 1614 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               559104 states/s
  Peak memory:        747.07 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 19.0 s
  Time (merging):     2.5 s

+ Export to AUT
  Time:      7.3 s
  File size: 970.58 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        7.3 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        7.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/crowds.6-20/model_rep4.aut:	Size of output file is 1017724123 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 35.435 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-aut_default/crowds.6-20/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/crowds.6-20/model_rep5.aut".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               580563 states/s
  Peak memory:        747.04 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 18.3 s
  Time (merging):     2.6 s

+ Export to AUT
  Time:      7.4 s
  File size: 970.58 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.8 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/crowds.6-20/model_rep5.aut:	Size of output file is 1017724123 bytes
Removing output file to save space for repetition #5
```

