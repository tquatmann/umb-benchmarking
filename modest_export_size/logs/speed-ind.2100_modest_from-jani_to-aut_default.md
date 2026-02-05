# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [speed-ind.2100](../../models/speed-ind.2100)
Parsed values: [341778537.0, 341778537.0, 341778537.0, 341778537.0, 341778537.0]



### Log file: modest_from-jani_to-aut_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model.aut AUT  -D --exhaustive
Wallclock time: 2143.868 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (S1_def.location = S1_def_S1_200, S2_def.location = S2_def_S2_10, S3_def.location = S3_def_S3_120, S4_def.location = S4_def_S4_0, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_120, XX_def.location = XX_def_XX_0, S1 = 200, S2 = 10, S3 = 120, S4 = 0, Y = 0, Z = 0, XX = 0) do not sum up to the expected value of 0.006901220380210752 (actual sum: 0.0069012203802107531). Results will likely be affected by floating-point errors.
model.jani: info: Explored 743424 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/speed-ind.2100/model.aut".

Peak memory usage: 322 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               80188 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.3 s
  Time (merging):     0.7 s

+ Export to AUT
  Time:      2.7 s
  File size: 325.95 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        2130.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             2130.8 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-aut_default/speed-ind.2100/model.aut:	Size of output file is 341778537 bytes
```



### Log file: modest_from-jani_to-aut_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 1783.771 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (S1_def.location = S1_def_S1_200, S2_def.location = S2_def_S2_10, S3_def.location = S3_def_S3_120, S4_def.location = S4_def_S4_0, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_120, XX_def.location = XX_def_XX_0, S1 = 200, S2 = 10, S3 = 120, S4 = 0, Y = 0, Z = 0, XX = 0) do not sum up to the expected value of 0.006901220380210752 (actual sum: 0.0069012203802107531). Results will likely be affected by floating-point errors.
model.jani: info: Explored 743424 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep2.aut".

Peak memory usage: 323 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               94728 states/s
  Peak memory:        82.78 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.9 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      2.3 s
  File size: 325.95 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1772.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1772.7 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep2.aut:	Size of output file is 341778537 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 2213.466 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (S1_def.location = S1_def_S1_200, S2_def.location = S2_def_S2_10, S3_def.location = S3_def_S3_120, S4_def.location = S4_def_S4_0, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_120, XX_def.location = XX_def_XX_0, S1 = 200, S2 = 10, S3 = 120, S4 = 0, Y = 0, Z = 0, XX = 0) do not sum up to the expected value of 0.006901220380210752 (actual sum: 0.0069012203802107531). Results will likely be affected by floating-point errors.
model.jani: info: Explored 743424 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep3.aut".

Peak memory usage: 321 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               78661 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.5 s
  Time (merging):     0.7 s

+ Export to AUT
  Time:      2.7 s
  File size: 325.95 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        2200.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             2200.3 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep3.aut:	Size of output file is 341778537 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 1816.371 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (S1_def.location = S1_def_S1_200, S2_def.location = S2_def_S2_10, S3_def.location = S3_def_S3_120, S4_def.location = S4_def_S4_0, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_120, XX_def.location = XX_def_XX_0, S1 = 200, S2 = 10, S3 = 120, S4 = 0, Y = 0, Z = 0, XX = 0) do not sum up to the expected value of 0.006901220380210752 (actual sum: 0.0069012203802107531). Results will likely be affected by floating-point errors.
model.jani: info: Explored 743424 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep4.aut".

Peak memory usage: 322 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               93254 states/s
  Peak memory:        82.77 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 8.0 s
  Time (merging):     0.6 s

+ Export to AUT
  Time:      2.4 s
  File size: 325.95 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1805.1 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1805.1 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep4.aut:	Size of output file is 341778537 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 1987.443 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: info: Need 16 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 2 branches in state (S1_def.location = S1_def_S1_200, S2_def.location = S2_def_S2_10, S3_def.location = S3_def_S3_120, S4_def.location = S4_def_S4_0, Y_def.location = Y_def_Y_0, Z_def.location = Z_def_Z_0, CC_def.location = CC_def_CC_120, XX_def.location = XX_def_XX_0, S1 = 200, S2 = 10, S3 = 120, S4 = 0, Y = 0, Z = 0, XX = 0) do not sum up to the expected value of 0.006901220380210752 (actual sum: 0.0069012203802107531). Results will likely be affected by floating-point errors.
model.jani: info: Explored 743424 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep5.aut".

Peak memory usage: 322 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               82990 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.0 s
  Time (merging):     0.7 s

+ Export to AUT
  Time:      2.6 s
  File size: 325.95 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1974.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1974.9 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-aut_default/speed-ind.2100/model_rep5.aut:	Size of output file is 341778537 bytes
Removing output file to save space for repetition #5
```

