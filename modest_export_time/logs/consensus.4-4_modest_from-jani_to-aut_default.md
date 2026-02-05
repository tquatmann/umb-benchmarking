# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [0.1, 0.1, 0.1, 0.1, 0.1]



### Log file: modest_from-jani_to-aut_default_consensus.4-4_rep1.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model.aut AUT  -D --exhaustive
Wallclock time: 1.281 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.4-4/model.aut".

Peak memory usage: 105 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               121510 states/s
  Peak memory:        65.43 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.4 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 5.05 MB

+ Property disagree
  Probability: 0.15605633046939615
  Bounds:      [0.15605633046939615, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 9.981462390211186E-07
    Iterations:  1246
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.4-4/model.aut:	Size of output file is 5298561 bytes
```



### Log file: modest_from-jani_to-aut_default_consensus.4-4_rep2.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 1.368 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.4-4/model_rep2.aut".

Peak memory usage: 104 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               128000 states/s
  Peak memory:        65.43 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.4 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 5.05 MB

+ Property disagree
  Probability: 0.15605633046939615
  Bounds:      [0.15605633046939615, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 9.981462390211186E-07
    Iterations:  1246
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.4-4/model_rep2.aut:	Size of output file is 5298561 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_consensus.4-4_rep3.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 1.172 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.4-4/model_rep3.aut".

Peak memory usage: 105 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               154057 states/s
  Peak memory:        65.44 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 5.05 MB

+ Property disagree
  Probability: 0.15605633046939615
  Bounds:      [0.15605633046939615, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 9.981462390211186E-07
    Iterations:  1246
    Time:        0.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.4-4/model_rep3.aut:	Size of output file is 5298561 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_consensus.4-4_rep4.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 1.202 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.4-4/model_rep4.aut".

Peak memory usage: 104 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               145239 states/s
  Peak memory:        65.43 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 5.05 MB

+ Property disagree
  Probability: 0.15605633046939615
  Bounds:      [0.15605633046939615, 1]
  Time:        0.6 s

  + Value iteration
    Final error: 9.981462390211186E-07
    Iterations:  1246
    Time:        0.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.4-4/model_rep4.aut:	Size of output file is 5298561 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_consensus.4-4_rep5.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 1.137 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.4-4/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.4-4/model_rep5.aut".

Peak memory usage: 107 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               155165 states/s
  Peak memory:        65.44 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 5.05 MB

+ Property disagree
  Probability: 0.15605633046939615
  Bounds:      [0.15605633046939615, 1]
  Time:        0.5 s

  + Value iteration
    Final error: 9.981462390211186E-07
    Iterations:  1246
    Time:        0.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.4-4/model_rep5.aut:	Size of output file is 5298561 bytes
Removing output file to save space for repetition #5
```

