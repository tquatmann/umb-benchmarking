# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [0.6, 0.6, 0.7, 0.7, 0.6]



### Log file: modest_from-jani_to-aut_default_majority.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model.aut AUT  -D --exhaustive
Wallclock time: 437.295 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (D_def.location = D_def_D_200, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_130, XX_def.location = XX_def_XX_0, EE_def.location = EE_def_EE_0, D = 200, Y = 0, Z = 0, CC = 130, XX = 0, EE = 0) do not sum up to the expected value of 0.47382274357191556 (actual sum: 0.47382274357191551). Results will likely be affected by floating-point errors.
model.jani: info: Explored 192000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/majority.2100/model.aut".

Peak memory usage: 152 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               121442 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.6 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.6 s
  File size: 65.41 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        434.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             434.7 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-aut_default/majority.2100/model.aut:	Size of output file is 68585864 bytes
```



### Log file: modest_from-jani_to-aut_default_majority.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 447.294 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (D_def.location = D_def_D_200, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_130, XX_def.location = XX_def_XX_0, EE_def.location = EE_def_EE_0, D = 200, Y = 0, Z = 0, CC = 130, XX = 0, EE = 0) do not sum up to the expected value of 0.47382274357191556 (actual sum: 0.47382274357191551). Results will likely be affected by floating-point errors.
model.jani: info: Explored 192000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/majority.2100/model_rep2.aut".

Peak memory usage: 153 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               110281 states/s
  Peak memory:        71.26 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.6 s
  File size: 65.41 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        444.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             444.2 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-aut_default/majority.2100/model_rep2.aut:	Size of output file is 68585864 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_majority.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 485.418 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (D_def.location = D_def_D_200, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_130, XX_def.location = XX_def_XX_0, EE_def.location = EE_def_EE_0, D = 200, Y = 0, Z = 0, CC = 130, XX = 0, EE = 0) do not sum up to the expected value of 0.47382274357191556 (actual sum: 0.47382274357191551). Results will likely be affected by floating-point errors.
model.jani: info: Explored 192000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/majority.2100/model_rep3.aut".

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               103560 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.7 s
  File size: 65.41 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        482.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             482.4 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-aut_default/majority.2100/model_rep3.aut:	Size of output file is 68585864 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_majority.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 530.962 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (D_def.location = D_def_D_200, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_130, XX_def.location = XX_def_XX_0, EE_def.location = EE_def_EE_0, D = 200, Y = 0, Z = 0, CC = 130, XX = 0, EE = 0) do not sum up to the expected value of 0.47382274357191556 (actual sum: 0.47382274357191551). Results will likely be affected by floating-point errors.
model.jani: info: Explored 192000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/majority.2100/model_rep4.aut".

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               100629 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.7 s
  File size: 65.41 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        527.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             527.8 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-aut_default/majority.2100/model_rep4.aut:	Size of output file is 68585864 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_majority.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 438.232 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-aut_default/majority.2100/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (D_def.location = D_def_D_200, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_130, XX_def.location = XX_def_XX_0, EE_def.location = EE_def_EE_0, D = 200, Y = 0, Z = 0, CC = 130, XX = 0, EE = 0) do not sum up to the expected value of 0.47382274357191556 (actual sum: 0.47382274357191551). Results will likely be affected by floating-point errors.
model.jani: info: Explored 192000 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/majority.2100/model_rep5.aut".

Peak memory usage: 157 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               116931 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.7 s
  Time (merging):     0.2 s

+ Export to AUT
  Time:      0.6 s
  File size: 65.41 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        435.6 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             435.6 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-aut_default/majority.2100/model_rep5.aut:	Size of output file is 68585864 bytes
Removing output file to save space for repetition #5
```

