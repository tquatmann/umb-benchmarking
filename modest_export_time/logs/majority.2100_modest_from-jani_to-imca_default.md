# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [majority.2100](../../models/majority.2100)
Parsed values: [0.5, 0.5, 0.5, 0.5, 0.5]



### Log file: modest_from-jani_to-imca_default_majority.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model.mrm IMCA  -D --exhaustive
Wallclock time: 528.187 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/majority.2100/model.mrm".

Peak memory usage: 154 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               103281 states/s
  Peak memory:        71.24 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 47.48 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        525.1 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             525.1 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-imca_default/majority.2100/model.mrm:	Size of output file is 49784283 bytes
```



### Log file: modest_from-jani_to-imca_default_majority.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 483.061 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep2.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/majority.2100/model_rep2.mrm".

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               106667 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.8 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 47.48 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        480.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             480.2 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-imca_default/majority.2100/model_rep2.mrm:	Size of output file is 49784283 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_majority.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 478.574 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep3.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/majority.2100/model_rep3.mrm".

Peak memory usage: 154 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               113811 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.7 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 47.48 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        475.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             475.8 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-imca_default/majority.2100/model_rep3.mrm:	Size of output file is 49784283 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_majority.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 528.921 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep4.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/majority.2100/model_rep4.mrm".

Peak memory usage: 153 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               104405 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 47.48 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        526.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             526.0 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-imca_default/majority.2100/model_rep4.mrm:	Size of output file is 49784283 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_majority.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 493.313 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --statespace out/modest_from-jani_to-imca_default/majority.2100/model_rep5.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/majority.2100/model_rep5.mrm".

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               114558 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.7 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 47.48 MB

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        490.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             490.7 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222


############################## Output files ##############################
out/modest_from-jani_to-imca_default/majority.2100/model_rep5.mrm:	Size of output file is 49784283 bytes
Removing output file to save space for repetition #5
```

