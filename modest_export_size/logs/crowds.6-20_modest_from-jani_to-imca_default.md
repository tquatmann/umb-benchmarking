# Log files for modest_from-jani_to-imca_default on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[678480608.0, 678480608.0, 678480608.0, 678480608.0, 678480608.0]`



### Log file: modest_from-jani_to-imca_default_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model.mrm IMCA  -D --exhaustive
Wallclock time: 33.036 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.6-20/model.mrm".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               613630 states/s
  Peak memory:        746.99 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 17.3 s
  Time (merging):     2.4 s

+ Export to IMCA
  Time:      5.9 s
  File size: 647.05 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.7 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.6-20/model.mrm:	Size of output file is 678480608 bytes
```



### Log file: modest_from-jani_to-imca_default_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 32.391 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.6-20/model_rep2.mrm".

Peak memory usage: 1615 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               618232 states/s
  Peak memory:        746.99 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 17.2 s
  Time (merging):     2.4 s

+ Export to IMCA
  Time:      6.0 s
  File size: 647.05 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.5 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.5 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.6-20/model_rep2.mrm:	Size of output file is 678480608 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 39.584 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.6-20/model_rep3.mrm".

Peak memory usage: 1611 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               555598 states/s
  Peak memory:        747.06 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 19.2 s
  Time (merging):     2.5 s

+ Export to IMCA
  Time:      6.9 s
  File size: 647.05 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        10.6 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        10.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.6-20/model_rep3.mrm:	Size of output file is 678480608 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 29.021 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.6-20/model_rep4.mrm".

Peak memory usage: 1612 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               690897 states/s
  Peak memory:        746.92 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.4 s
  Time (merging):     2.1 s

+ Export to IMCA
  Time:      5.2 s
  File size: 647.05 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.0 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.6-20/model_rep4.mrm:	Size of output file is 678480608 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 29.461 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --statespace out/modest_from-jani_to-imca_default/crowds.6-20/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/crowds.6-20/model_rep5.mrm".

Peak memory usage: 1610 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               688125 states/s
  Peak memory:        746.92 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.5 s
  Time (merging):     2.2 s

+ Export to IMCA
  Time:      5.6 s
  File size: 647.05 MB

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.0 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/crowds.6-20/model_rep5.mrm:	Size of output file is 678480608 bytes
Removing output file to save space for repetition #5
```

