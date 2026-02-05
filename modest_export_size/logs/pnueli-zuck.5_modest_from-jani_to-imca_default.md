# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [52388895.0, 52388895.0, 52388895.0, 52388895.0, 52388895.0]



### Log file: modest_from-jani_to-imca_default_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model.mrm IMCA  -D --exhaustive
Wallclock time: 3.956 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "p0" into 16 locations in automaton "process0".
model.jani:variables[2]: info: Expanding variable "p1" into 16 locations in automaton "process1".
model.jani:variables[3]: info: Expanding variable "p2" into 16 locations in automaton "process2".
model.jani:variables[4]: info: Expanding variable "p3" into 16 locations in automaton "process3".
model.jani:variables[5]: info: Expanding variable "p4" into 16 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 397435 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pnueli-zuck.5/model.mrm".

Peak memory usage: 180 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             397435
  Choices:            2323315
  Branches:           2492035
  Rate:               167271 states/s
  Peak memory:        74.47 MB
  Final size:         55.75 MB
  Size on disk:       7.76 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 49.96 MB

+ Property live
  Probability: 1
  Bounds:      [1, 1]
  Time:        0.4 s

  + Value iteration
    Final error: 5.774204007950579E-07
    Iterations:  37
    Time:        0.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pnueli-zuck.5/model.mrm:	Size of output file is 52388895 bytes
```



### Log file: modest_from-jani_to-imca_default_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 3.896 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "p0" into 16 locations in automaton "process0".
model.jani:variables[2]: info: Expanding variable "p1" into 16 locations in automaton "process1".
model.jani:variables[3]: info: Expanding variable "p2" into 16 locations in automaton "process2".
model.jani:variables[4]: info: Expanding variable "p3" into 16 locations in automaton "process3".
model.jani:variables[5]: info: Expanding variable "p4" into 16 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 397435 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep2.mrm".

Peak memory usage: 182 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             397435
  Choices:            2323315
  Branches:           2492035
  Rate:               176716 states/s
  Peak memory:        74.46 MB
  Final size:         55.75 MB
  Size on disk:       7.76 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 49.96 MB

+ Property live
  Probability: 1
  Bounds:      [1, 1]
  Time:        0.4 s

  + Value iteration
    Final error: 5.774204007950579E-07
    Iterations:  37
    Time:        0.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep2.mrm:	Size of output file is 52388895 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 3.901 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "p0" into 16 locations in automaton "process0".
model.jani:variables[2]: info: Expanding variable "p1" into 16 locations in automaton "process1".
model.jani:variables[3]: info: Expanding variable "p2" into 16 locations in automaton "process2".
model.jani:variables[4]: info: Expanding variable "p3" into 16 locations in automaton "process3".
model.jani:variables[5]: info: Expanding variable "p4" into 16 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 397435 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep3.mrm".

Peak memory usage: 183 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             397435
  Choices:            2323315
  Branches:           2492035
  Rate:               166500 states/s
  Peak memory:        74.46 MB
  Final size:         55.75 MB
  Size on disk:       7.76 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 49.96 MB

+ Property live
  Probability: 1
  Bounds:      [1, 1]
  Time:        0.4 s

  + Value iteration
    Final error: 5.774204007950579E-07
    Iterations:  37
    Time:        0.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep3.mrm:	Size of output file is 52388895 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 3.734 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "p0" into 16 locations in automaton "process0".
model.jani:variables[2]: info: Expanding variable "p1" into 16 locations in automaton "process1".
model.jani:variables[3]: info: Expanding variable "p2" into 16 locations in automaton "process2".
model.jani:variables[4]: info: Expanding variable "p3" into 16 locations in automaton "process3".
model.jani:variables[5]: info: Expanding variable "p4" into 16 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 397435 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep4.mrm".

Peak memory usage: 182 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             397435
  Choices:            2323315
  Branches:           2492035
  Rate:               174850 states/s
  Peak memory:        74.47 MB
  Final size:         55.75 MB
  Size on disk:       7.76 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 49.96 MB

+ Property live
  Probability: 1
  Bounds:      [1, 1]
  Time:        0.4 s

  + Value iteration
    Final error: 5.774204007950579E-07
    Iterations:  37
    Time:        0.4 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep4.mrm:	Size of output file is 52388895 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 3.543 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/pnueli-zuck.5/model.jani --statespace out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[1]: info: Expanding variable "p0" into 16 locations in automaton "process0".
model.jani:variables[2]: info: Expanding variable "p1" into 16 locations in automaton "process1".
model.jani:variables[3]: info: Expanding variable "p2" into 16 locations in automaton "process2".
model.jani:variables[4]: info: Expanding variable "p3" into 16 locations in automaton "process3".
model.jani:variables[5]: info: Expanding variable "p4" into 16 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 397435 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep5.mrm".

Peak memory usage: 179 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             397435
  Choices:            2323315
  Branches:           2492035
  Rate:               192930 states/s
  Peak memory:        74.46 MB
  Final size:         55.75 MB
  Size on disk:       7.76 MB
  Time (exploration): 2.1 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 49.96 MB

+ Property live
  Probability: 1
  Bounds:      [1, 1]
  Time:        0.3 s

  + Value iteration
    Final error: 5.774204007950579E-07
    Iterations:  37
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/pnueli-zuck.5/model_rep5.mrm:	Size of output file is 52388895 bytes
Removing output file to save space for repetition #5
```

