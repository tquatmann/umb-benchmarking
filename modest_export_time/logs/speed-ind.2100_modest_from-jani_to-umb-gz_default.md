# Log files for modest_from-jani_to-umb-gz_default on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[ERR, 3.9, 3.0, 2.5, 3.0]`



### Log file: modest_from-jani_to-umb-gz_default_speed-ind.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.340 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "S1" into 6 locations in automaton "S1_def".
model.jani:variables[2]: info: Expanding variable "S2" into 11 locations in automaton "S2_def".
model.jani:variables[3]: info: Expanding variable "S3" into 11 locations in automaton "S3_def".
model.jani:variables[4]: info: Expanding variable "S4" into 4 locations in automaton "S4_def".
model.jani:variables[5]: info: Expanding variable "Y" into 4 locations in automaton "Y_def".
model.jani:variables[6]: info: Expanding variable "Z" into 4 locations in automaton "Z_def".
model.jani:automata[6].variables[0]: info: Expanding variable "CC" into 4 locations in automaton "CC_def".
model.jani:variables[7]: info: Expanding variable "XX" into 4 locations in automaton "XX_def".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb.gz:	Size of output file is 72262596 bytes
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties.txt:	Size of output file is 42 bytes
```



### Log file: modest_from-jani_to-umb-gz_default_speed-ind.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep2.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 14.353 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep2.txt --umb-compress GZIP -D --exhaustive




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

Peak memory usage: 298 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               79775 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.3 s
  Time (merging):     0.7 s

+ UMB export
  Time:        3.9 s
  File size:   68.91 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep2.gz:	Size of output file is 72262519 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep2.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_default_speed-ind.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep3.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 13.194 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep3.txt --umb-compress GZIP -D --exhaustive




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

Peak memory usage: 299 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               81071 states/s
  Peak memory:        82.80 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 9.2 s
  Time (merging):     0.7 s

+ UMB export
  Time:        3.0 s
  File size:   68.91 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep3.gz:	Size of output file is 72262528 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep3.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_default_speed-ind.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep4.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 11.153 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep4.txt --umb-compress GZIP -D --exhaustive




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

Peak memory usage: 301 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               96112 states/s
  Peak memory:        82.77 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 7.8 s
  Time (merging):     0.6 s

+ UMB export
  Time:        2.5 s
  File size:   68.91 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep4.gz:	Size of output file is 72262579 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep4.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_default_speed-ind.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep5.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 12.896 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/speed-ind.2100/model.jani --umb out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep5.txt --umb-compress GZIP -D --exhaustive




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

Peak memory usage: 300 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             743424
  Choices:            743424
  Branches:           9518080
  Rate:               83540 states/s
  Peak memory:        82.79 MB
  Final size:         150.91 MB
  Size on disk:       83.46 MB
  Time (exploration): 8.9 s
  Time (merging):     0.6 s

+ UMB export
  Time:        3.0 s
  File size:   68.91 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/model.umb_rep5.gz:	Size of output file is 72262526 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_default/speed-ind.2100/umbgz.properties_rep5.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #5
```

