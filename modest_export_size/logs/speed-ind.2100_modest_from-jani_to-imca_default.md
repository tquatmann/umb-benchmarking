# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [speed-ind.2100](../../models/speed-ind.2100)
Parsed values: [245236119.0, 245236119.0, 245236119.0, 245236119.0, 245236119.0]



### Log file: modest_from-jani_to-imca_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model.mrm IMCA  -D --exhaustive
Wallclock time: 2176.189 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/speed-ind.2100/model.mrm".

Peak memory usage: 323 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               80544 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.3 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      2.4 s
  File size: 233.88 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        2163.5 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             2163.5 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-imca_default/speed-ind.2100/model.mrm:	Size of output file is 245236119 bytes
```



### Log file: modest_from-jani_to-imca_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 1752.724 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep2.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep2.mrm".

Peak memory usage: 322 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               96199 states/s
  Peak memory:        82.77 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.8 s
  Time (merging):     0.6 s

+ Export to IMCA
  Time:      2.1 s
  File size: 233.88 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1742.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1742.0 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep2.mrm:	Size of output file is 245236119 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 1932.868 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep3.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep3.mrm".

Peak memory usage: 323 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               96825 states/s
  Peak memory:        82.77 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.7 s
  Time (merging):     0.6 s

+ Export to IMCA
  Time:      1.9 s
  File size: 233.88 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1922.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1922.3 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep3.mrm:	Size of output file is 245236119 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 2029.207 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep4.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep4.mrm".

Peak memory usage: 323 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               95617 states/s
  Peak memory:        82.78 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.8 s
  Time (merging):     0.6 s

+ Export to IMCA
  Time:      2.1 s
  File size: 233.88 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        2018.4 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             2018.4 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep4.mrm:	Size of output file is 245236119 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 1990.323 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --statespace out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep5.mrm IMCA -D --exhaustive




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
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep5.mrm".

Peak memory usage: 324 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               84538 states/s
  Peak memory:        82.79 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 8.8 s
  Time (merging):     0.7 s

+ Export to IMCA
  Time:      2.3 s
  File size: 233.88 MB

+ Property change_state
  Probability: 0.042319497978288025
  Bounds:      [0.042294497978287986, 0.04234449797828806]
  Time:        1978.3 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 0.0 s

  + Unif+
    Time:             1978.3 s
    Max. exit rate:   2.74304977527707
    Iterations:       1
    Final unif. rate: 2.74304977527707


############################## Output files ##############################
out/modest_from-jani_to-imca_default/speed-ind.2100/model_rep5.mrm:	Size of output file is 245236119 bytes
Removing output file to save space for repetition #5
```

