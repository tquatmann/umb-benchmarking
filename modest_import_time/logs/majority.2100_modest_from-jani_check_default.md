# Log files for modest_from-jani_check_default on model [majority.2100](../../models/majority.2100)

Parsed values: `[2.0, 1.8, 1.8, 1.8, 1.9]`



### Log file: modest_from-jani_check_default_majority.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani  -D --exhaustive
Wallclock time: 509.044 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani -D --exhaustive




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

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               105148 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.8 s
  Time (merging):     0.2 s

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        506.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             506.7 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222

```



### Log file: modest_from-jani_check_default_majority.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani  -D --exhaustive
Wallclock time: 656.703 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani -D --exhaustive




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

Peak memory usage: 155 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               120301 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.6 s
  Time (merging):     0.2 s

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        654.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             654.5 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222

```



### Log file: modest_from-jani_check_default_majority.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani  -D --exhaustive
Wallclock time: 433.278 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani -D --exhaustive




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

Peak memory usage: 152 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               125163 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.6 s
  Time (merging):     0.2 s

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        431.2 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             431.2 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222

```



### Log file: modest_from-jani_check_default_majority.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani  -D --exhaustive
Wallclock time: 444.987 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani -D --exhaustive




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

Peak memory usage: 156 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               120983 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.6 s
  Time (merging):     0.2 s

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        442.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             442.9 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222

```



### Log file: modest_from-jani_check_default_majority.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani  -D --exhaustive
Wallclock time: 479.721 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani -D --exhaustive




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

Peak memory usage: 154 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               117647 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.7 s
  Time (merging):     0.2 s

+ Property change_state
  Probability: 0.054324193162944165
  Bounds:      [0.05429919316294412, 0.05434919316294422]
  Time:        477.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             477.5 s
    Max. exit rate:   3.222771171745222
    Iterations:       1
    Final unif. rate: 3.222771171745222

```

