# Log files for modest_from-jani_to-aut_default on model [nand.40-4](../../models/nand.40-4)

Parsed values: `[180830818.0, 180830818.0, 180830818.0, 180830818.0, 180830818.0]`



### Log file: modest_from-jani_to-aut_default_nand.40-4_rep1.log

```
Command(s):
../bin/modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model.aut AUT  -D --exhaustive
Wallclock time: 7.817 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 3999522 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.40-4/model.aut".

Peak memory usage: 427 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             3999522
  Choices:            3999522
  Branches:           6288542
  Rate:               782839 states/s
  Peak memory:        153.75 MB
  Final size:         126.47 MB
  Size on disk:       21.16 MB
  Time (exploration): 5.1 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      1.5 s
  File size: 172.45 MB

+ Property reliable
  Probability: 0.6186822208151973
  Bounds:      [0.6186822208151973, 0.6186822208151973]
  Time:        0.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.40-4/model.aut:	Size of output file is 180830818 bytes
```



### Log file: modest_from-jani_to-aut_default_nand.40-4_rep2.log

```
Command(s):
../bin/modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 6.508 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 3999522 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.40-4/model_rep2.aut".

Peak memory usage: 426 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             3999522
  Choices:            3999522
  Branches:           6288542
  Rate:               909189 states/s
  Peak memory:        134.66 MB
  Final size:         126.47 MB
  Size on disk:       21.16 MB
  Time (exploration): 4.4 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      1.3 s
  File size: 172.45 MB

+ Property reliable
  Probability: 0.6186822208151973
  Bounds:      [0.6186822208151973, 0.6186822208151973]
  Time:        0.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.40-4/model_rep2.aut:	Size of output file is 180830818 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_nand.40-4_rep3.log

```
Command(s):
../bin/modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 27.161 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 3999522 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.40-4/model_rep3.aut".

Peak memory usage: 425 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             3999522
  Choices:            3999522
  Branches:           6288542
  Rate:               210801 states/s
  Peak memory:        175.10 MB
  Final size:         126.47 MB
  Size on disk:       21.16 MB
  Time (exploration): 19.0 s
  Time (merging):     1.9 s

+ Export to AUT
  Time:      5.1 s
  File size: 172.45 MB

+ Property reliable
  Probability: 0.6186822208151973
  Bounds:      [0.6186822208151973, 0.6186822208151973]
  Time:        0.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.40-4/model_rep3.aut:	Size of output file is 180830818 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_nand.40-4_rep4.log

```
Command(s):
../bin/modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 6.492 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 3999522 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.40-4/model_rep4.aut".

Peak memory usage: 428 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             3999522
  Choices:            3999522
  Branches:           6288542
  Rate:               897962 states/s
  Peak memory:        134.67 MB
  Final size:         126.47 MB
  Size on disk:       21.16 MB
  Time (exploration): 4.5 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      1.2 s
  File size: 172.45 MB

+ Property reliable
  Probability: 0.6186822208151973
  Bounds:      [0.6186822208151973, 0.6186822208151973]
  Time:        0.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.40-4/model_rep4.aut:	Size of output file is 180830818 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_nand.40-4_rep5.log

```
Command(s):
../bin/modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 7.372 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.40-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.40-4/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 3999522 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.40-4/model_rep5.aut".

Peak memory usage: 426 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             3999522
  Choices:            3999522
  Branches:           6288542
  Rate:               821088 states/s
  Peak memory:        134.68 MB
  Final size:         126.47 MB
  Size on disk:       21.16 MB
  Time (exploration): 4.9 s
  Time (merging):     0.5 s

+ Export to AUT
  Time:      1.5 s
  File size: 172.45 MB

+ Property reliable
  Probability: 0.6186822208151973
  Bounds:      [0.6186822208151973, 0.6186822208151973]
  Time:        0.1 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.40-4/model_rep5.aut:	Size of output file is 180830818 bytes
Removing output file to save space for repetition #5
```

