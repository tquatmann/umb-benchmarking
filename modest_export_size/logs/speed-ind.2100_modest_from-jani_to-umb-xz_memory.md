# Log files for modest_from-jani_to-umb-xz_memory on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[50865338.0, 50867642.0, 50920878.0, 50912370.0, 50864106.0]`



### Log file: modest_from-jani_to-umb-xz_memory_speed-ind.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.227 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb.xz:	Size of output file is 50865296 bytes
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties.txt:	Size of output file is 42 bytes
```



### Log file: modest_from-jani_to-umb-xz_memory_speed-ind.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 52.004 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive




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

Peak memory usage: 1133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               234223 states/s
  Peak memory:        252.20 MB
  Final size:         11.43 MB
  Time (exploration): 3.2 s
  Time (merging):     0.1 s

+ UMB export
  Time:        48.4 s
  File size:   48.51 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep2.xz:	Size of output file is 50867600 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep2.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_memory_speed-ind.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 51.140 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive




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

Peak memory usage: 1133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               233194 states/s
  Peak memory:        252.20 MB
  Final size:         11.43 MB
  Time (exploration): 3.2 s
  Time (merging):     0.1 s

+ UMB export
  Time:        47.4 s
  File size:   48.56 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep3.xz:	Size of output file is 50920836 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep3.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_memory_speed-ind.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 52.333 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive




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

Peak memory usage: 1133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               255034 states/s
  Peak memory:        252.20 MB
  Final size:         11.43 MB
  Time (exploration): 2.9 s
  Time (merging):     0.1 s

+ UMB export
  Time:        49.0 s
  File size:   48.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep4.xz:	Size of output file is 50912328 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep4.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_memory_speed-ind.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 61.183 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive




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

Peak memory usage: 1138 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               220994 states/s
  Peak memory:        252.20 MB
  Final size:         11.43 MB
  Time (exploration): 3.4 s
  Time (merging):     0.1 s

+ UMB export
  Time:        57.4 s
  File size:   48.51 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/model.umb_rep5.xz:	Size of output file is 50864064 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_memory/speed-ind.2100/umbxz.properties_rep5.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #5
```

