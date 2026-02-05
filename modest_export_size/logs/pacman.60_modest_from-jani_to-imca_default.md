# Log files for modest_from-jani_to-imca_default on model [pacman.60](../../models/pacman.60)

Parsed values: `[1344160052.0, 1344160052.0, 1344160052.0, 1344160052.0, 1344160052.0]`



### Log file: modest_from-jani_to-imca_default_pacman.60_rep1.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model.mrm IMCA  -D --exhaustive
Wallclock time: 154.962 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.60/model.mrm".

Peak memory usage: 3549 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               287035 states/s
  Peak memory:        1675.33 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 135.2 s
  Time (merging):     4.5 s

+ Export to IMCA
  Time:      12.2 s
  File size: 1281.89 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.9 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.60/model.mrm:	Size of output file is 1344160052 bytes
```



### Log file: modest_from-jani_to-imca_default_pacman.60_rep2.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 138.315 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.60/model_rep2.mrm".

Peak memory usage: 3550 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               322310 states/s
  Peak memory:        1644.16 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 120.4 s
  Time (merging):     4.4 s

+ Export to IMCA
  Time:      11.4 s
  File size: 1281.89 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.5 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.60/model_rep2.mrm:	Size of output file is 1344160052 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_pacman.60_rep3.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 147.316 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.60/model_rep3.mrm".

Peak memory usage: 3551 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               302700 states/s
  Peak memory:        1675.34 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 128.2 s
  Time (merging):     4.3 s

+ Export to IMCA
  Time:      12.3 s
  File size: 1281.89 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.9 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.60/model_rep3.mrm:	Size of output file is 1344160052 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_pacman.60_rep4.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 137.595 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.60/model_rep4.mrm".

Peak memory usage: 3549 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               322431 states/s
  Peak memory:        1675.34 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 120.3 s
  Time (merging):     4.1 s

+ Export to IMCA
  Time:      10.9 s
  File size: 1281.89 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.60/model_rep4.mrm:	Size of output file is 1344160052 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_pacman.60_rep5.log

```
Command(s):
../bin/modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 126.805 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pacman.60/model.jani --statespace out/modest_from-jani_to-imca_default/pacman.60/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "pMove" into 3 locations in automaton "arbiter".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 38786521 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pacman.60/model_rep5.mrm".

Peak memory usage: 3550 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             38786521
  Choices:            48926255
  Branches:           53648196
  Rate:               351089 states/s
  Peak memory:        1644.12 MB
  Final size:         1191.88 MB
  Size on disk:       194.60 MB
  Time (exploration): 110.5 s
  Time (merging):     3.9 s

+ Export to IMCA
  Time:      10.2 s
  File size: 1281.89 MB

+ Property crash
  Probability: 0.5511074970678997
  Bounds:      [0.5511074970678997, 0.5511074970678997]
  Time:        1.5 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pacman.60/model_rep5.mrm:	Size of output file is 1344160052 bytes
Removing output file to save space for repetition #5
```

