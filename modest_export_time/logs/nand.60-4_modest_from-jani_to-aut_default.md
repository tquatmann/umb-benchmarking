# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [6.2, 5.8, 5.2, 5.4, 5.3]



### Log file: modest_from-jani_to-aut_default_nand.60-4_rep1.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model.aut AUT  -D --exhaustive
Wallclock time: 33.446 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 18826082 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.60-4/model.aut".

Peak memory usage: 1759 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             18826082
  Choices:            18826082
  Branches:           29772212
  Rate:               787406 states/s
  Peak memory:        795.00 MB
  Final size:         597.92 MB
  Size on disk:       100.44 MB
  Time (exploration): 23.9 s
  Time (merging):     2.4 s

+ Export to AUT
  Time:      6.2 s
  File size: 862.96 MB

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        0.4 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.60-4/model.aut:	Size of output file is 904882999 bytes
```



### Log file: modest_from-jani_to-aut_default_nand.60-4_rep2.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 31.779 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 18826082 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.60-4/model_rep2.aut".

Peak memory usage: 1760 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             18826082
  Choices:            18826082
  Branches:           29772212
  Rate:               824331 states/s
  Peak memory:        794.97 MB
  Final size:         597.92 MB
  Size on disk:       100.44 MB
  Time (exploration): 22.9 s
  Time (merging):     2.2 s

+ Export to AUT
  Time:      5.8 s
  File size: 862.96 MB

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        0.4 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.60-4/model_rep2.aut:	Size of output file is 904882999 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_nand.60-4_rep3.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 29.015 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 18826082 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.60-4/model_rep3.aut".

Peak memory usage: 1758 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             18826082
  Choices:            18826082
  Branches:           29772212
  Rate:               901935 states/s
  Peak memory:        794.91 MB
  Final size:         597.92 MB
  Size on disk:       100.44 MB
  Time (exploration): 20.9 s
  Time (merging):     2.1 s

+ Export to AUT
  Time:      5.2 s
  File size: 862.96 MB

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        0.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.60-4/model_rep3.aut:	Size of output file is 904882999 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_nand.60-4_rep4.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 29.234 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 18826082 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.60-4/model_rep4.aut".

Peak memory usage: 1760 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             18826082
  Choices:            18826082
  Branches:           29772212
  Rate:               884352 states/s
  Peak memory:        794.93 MB
  Final size:         597.92 MB
  Size on disk:       100.44 MB
  Time (exploration): 21.3 s
  Time (merging):     2.0 s

+ Export to AUT
  Time:      5.4 s
  File size: 862.96 MB

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        0.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.60-4/model_rep4.aut:	Size of output file is 904882999 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_nand.60-4_rep5.log

```
Command(s):
../bin/modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 29.137 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/nand.60-4/model.jani --statespace out/modest_from-jani_to-aut_default/nand.60-4/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani:variables[1]: info: Expanding variable "s" into 5 locations in automaton "multiplex".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 18826082 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/nand.60-4/model_rep5.aut".

Peak memory usage: 1759 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             18826082
  Choices:            18826082
  Branches:           29772212
  Rate:               897249 states/s
  Peak memory:        794.93 MB
  Final size:         597.92 MB
  Size on disk:       100.44 MB
  Time (exploration): 21.0 s
  Time (merging):     2.1 s

+ Export to AUT
  Time:      5.3 s
  File size: 862.96 MB

+ Property reliable
  Probability: 0.6867214589192275
  Bounds:      [0.6867214589192275, 0.6867214589192275]
  Time:        0.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/nand.60-4/model_rep5.aut:	Size of output file is 904882999 bytes
Removing output file to save space for repetition #5
```

