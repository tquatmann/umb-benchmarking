# Log files for modest_from-jani_to-aut_default on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[261425462.0, 261425462.0, 261425462.0, 261425462.0, 261425462.0]`



### Log file: modest_from-jani_to-aut_default_consensus.6-2_rep1.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model.aut AUT  -D --exhaustive
Wallclock time: 28.930 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani:variables[11]: info: Expanding variable "pc5" into 4 locations in automaton "process5".
model.jani:variables[13]: info: Expanding variable "pc6" into 4 locations in automaton "process6".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1258240 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.6-2/model.aut".

Peak memory usage: 318 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1258240
  Choices:            5008128
  Branches:           6236736
  Rate:               189808 states/s
  Peak memory:        121.18 MB
  Final size:         133.37 MB
  Size on disk:       19.72 MB
  Time (exploration): 6.6 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      2.3 s
  File size: 249.31 MB

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        19.2 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        19.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.6-2/model.aut:	Size of output file is 261425462 bytes
```



### Log file: modest_from-jani_to-aut_default_consensus.6-2_rep2.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 24.545 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani:variables[11]: info: Expanding variable "pc5" into 4 locations in automaton "process5".
model.jani:variables[13]: info: Expanding variable "pc6" into 4 locations in automaton "process6".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1258240 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.6-2/model_rep2.aut".

Peak memory usage: 318 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1258240
  Choices:            5008128
  Branches:           6236736
  Rate:               221834 states/s
  Peak memory:        121.17 MB
  Final size:         133.37 MB
  Size on disk:       19.72 MB
  Time (exploration): 5.7 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      1.6 s
  File size: 249.31 MB

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        16.6 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        16.6 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.6-2/model_rep2.aut:	Size of output file is 261425462 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_consensus.6-2_rep3.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 23.949 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani:variables[11]: info: Expanding variable "pc5" into 4 locations in automaton "process5".
model.jani:variables[13]: info: Expanding variable "pc6" into 4 locations in automaton "process6".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1258240 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.6-2/model_rep3.aut".

Peak memory usage: 317 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1258240
  Choices:            5008128
  Branches:           6236736
  Rate:               224846 states/s
  Peak memory:        121.16 MB
  Final size:         133.37 MB
  Size on disk:       19.72 MB
  Time (exploration): 5.6 s
  Time (merging):     0.4 s

+ Export to AUT
  Time:      1.6 s
  File size: 249.31 MB

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        16.1 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        16.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.6-2/model_rep3.aut:	Size of output file is 261425462 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_consensus.6-2_rep4.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 23.390 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani:variables[11]: info: Expanding variable "pc5" into 4 locations in automaton "process5".
model.jani:variables[13]: info: Expanding variable "pc6" into 4 locations in automaton "process6".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1258240 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.6-2/model_rep4.aut".

Peak memory usage: 317 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1258240
  Choices:            5008128
  Branches:           6236736
  Rate:               229271 states/s
  Peak memory:        121.16 MB
  Final size:         133.37 MB
  Size on disk:       19.72 MB
  Time (exploration): 5.5 s
  Time (merging):     0.4 s

+ Export to AUT
  Time:      1.5 s
  File size: 249.31 MB

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        15.7 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        15.7 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.6-2/model_rep4.aut:	Size of output file is 261425462 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_consensus.6-2_rep5.log

```
Command(s):
../bin/modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 28.689 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.6-2/model.jani --statespace out/modest_from-jani_to-aut_default/consensus.6-2/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani:variables[11]: info: Expanding variable "pc5" into 4 locations in automaton "process5".
model.jani:variables[13]: info: Expanding variable "pc6" into 4 locations in automaton "process6".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1258240 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/consensus.6-2/model_rep5.aut".

Peak memory usage: 317 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1258240
  Choices:            5008128
  Branches:           6236736
  Rate:               189408 states/s
  Peak memory:        121.18 MB
  Final size:         133.37 MB
  Size on disk:       19.72 MB
  Time (exploration): 6.7 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      1.9 s
  File size: 249.31 MB

+ Property disagree
  Probability: 0.36362422496221386
  Bounds:      [0.36362422496221386, 1]
  Time:        19.4 s

  + Value iteration
    Final error: 9.857326206509403E-07
    Iterations:  736
    Time:        19.4 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/consensus.6-2/model_rep5.aut:	Size of output file is 261425462 bytes
Removing output file to save space for repetition #5
```

