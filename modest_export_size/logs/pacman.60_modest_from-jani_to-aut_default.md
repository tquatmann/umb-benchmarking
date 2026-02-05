# Log files for modest_from-jani_to-aut_default on model [pacman.60](../../models/pacman.60)

Parsed values: `[2653062451.0, 2653062451.0, 2653062451.0, 2653062451.0, 2653062451.0]`



### Log file: modest_from-jani_to-aut_default_pacman.60_rep1.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model.aut AUT  -D --exhaustive
Wallclock time: 151.249 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.60/model.aut".

Peak memory usage: 3554 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               303946 states/s
  Peak memory:        1660.15 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 127.6 s
  Time (merging):     4.6 s

+ Export to AUT
  Time:      16.4 s
  File size: 2530.16 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        2.0 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.8 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.60/model.aut:	Size of output file is 2653062451 bytes
```



### Log file: modest_from-jani_to-aut_default_pacman.60_rep2.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 125.295 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.60/model_rep2.aut".

Peak memory usage: 3548 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               364874 states/s
  Peak memory:        1675.30 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 106.3 s
  Time (merging):     3.9 s

+ Export to AUT
  Time:      13.2 s
  File size: 2530.16 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.4 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.60/model_rep2.aut:	Size of output file is 2653062451 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_pacman.60_rep3.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 145.705 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.60/model_rep3.aut".

Peak memory usage: 3549 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               315674 states/s
  Peak memory:        1675.34 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 122.9 s
  Time (merging):     4.6 s

+ Export to AUT
  Time:      16.0 s
  File size: 2530.16 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.60/model_rep3.aut:	Size of output file is 2653062451 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_pacman.60_rep4.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 141.188 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.60/model_rep4.aut".

Peak memory usage: 3552 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               322906 states/s
  Peak memory:        1675.33 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 120.1 s
  Time (merging):     4.2 s

+ Export to AUT
  Time:      14.8 s
  File size: 2530.16 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.4 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.60/model_rep4.aut:	Size of output file is 2653062451 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_pacman.60_rep5.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 157.778 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-aut_default/pacman.60/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/pacman.60/model_rep5.aut".

Peak memory usage: 3549 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               286723 states/s
  Peak memory:        1675.34 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 135.3 s
  Time (merging):     4.3 s

+ Export to AUT
  Time:      16.0 s
  File size: 2530.16 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/pacman.60/model_rep5.aut:	Size of output file is 2653062451 bytes
Removing output file to save space for repetition #5
```

