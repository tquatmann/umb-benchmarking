# Log files for modest_from-jani_to-umb-xz_default on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[ERR, 43.1, 55.4, 47.3, 61.0]`



### Log file: modest_from-jani_to-umb-xz_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 0.209 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb.xz:	Size of output file is 50867564 bytes
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties.txt:	Size of output file is 42 bytes
```



### Log file: modest_from-jani_to-umb-xz_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 51.825 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 394 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               95311 states/s
  Peak memory:        82.77 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.8 s
  Time (merging):     0.6 s

+ UMB export
  Time:        43.1 s
  File size:   48.56 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep2.xz:	Size of output file is 50922980 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep2.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 66.090 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               77472 states/s
  Peak memory:        82.81 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.6 s
  Time (merging):     0.7 s

+ UMB export
  Time:        55.4 s
  File size:   48.56 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep3.xz:	Size of output file is 50918140 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep3.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 57.279 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 392 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               83757 states/s
  Peak memory:        82.79 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 8.9 s
  Time (merging):     0.7 s

+ UMB export
  Time:        47.3 s
  File size:   48.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep4.xz:	Size of output file is 50903516 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep4.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 71.201 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 393 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               80457 states/s
  Peak memory:        82.81 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.3 s
  Time (merging):     0.7 s

+ UMB export
  Time:        61.0 s
  File size:   48.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/model.umb_rep5.xz:	Size of output file is 50907224 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/speed-ind.2100/umbxz.properties_rep5.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #5
```

