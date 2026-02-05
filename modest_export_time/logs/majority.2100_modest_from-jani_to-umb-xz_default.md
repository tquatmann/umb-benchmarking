# Log files for modest_from-jani_to-umb-xz_default on model [majority.2100](../../models/majority.2100)

Parsed values: `[ERR, 11.4, 7.9, 7.9, 10.9]`



### Log file: modest_from-jani_to-umb-xz_default_majority.2100_rep1.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 0.217 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[1]: info: Expanding variable "D" into 6 locations in automaton "D_def".
model.jani:variables[2]: info: Expanding variable "Y" into 5 locations in automaton "Y_def".
model.jani:variables[3]: info: Expanding variable "Z" into 5 locations in automaton "Z_def".
model.jani:variables[4]: info: Expanding variable "CC" into 16 locations in automaton "CC_def".
model.jani:variables[5]: info: Expanding variable "XX" into 5 locations in automaton "XX_def".
model.jani:variables[6]: info: Expanding variable "EE" into 16 locations in automaton "EE_def".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb.xz:	Size of output file is 7360952 bytes
out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties.txt:	Size of output file is 42 bytes
```



### Log file: modest_from-jani_to-umb-xz_default_majority.2100_rep2.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 13.930 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 243 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               96725 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 2.0 s
  Time (merging):     0.2 s

+ UMB export
  Time:        11.4 s
  File size:   7.02 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep2.xz:	Size of output file is 7363376 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep2.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_majority.2100_rep3.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 9.979 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 245 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               118665 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.6 s
  Time (merging):     0.2 s

+ UMB export
  Time:        7.9 s
  File size:   7.02 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep3.xz:	Size of output file is 7361516 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep3.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_majority.2100_rep4.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 9.934 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 244 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               116859 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.7 s
  Time (merging):     0.2 s

+ UMB export
  Time:        7.9 s
  File size:   7.02 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep4.xz:	Size of output file is 7359056 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep4.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_majority.2100_rep5.log

```
Command(s):
../bin/modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 13.368 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/majority.2100/model.jani --umb out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




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

Peak memory usage: 242 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             192000
  Choices:            192000
  Branches:           1961600
  Rate:               100261 states/s
  Peak memory:        71.25 MB
  Final size:         31.40 MB
  Size on disk:       14.92 MB
  Time (exploration): 1.9 s
  Time (merging):     0.2 s

+ UMB export
  Time:        10.9 s
  File size:   7.02 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/majority.2100/model.umb_rep5.xz:	Size of output file is 7362248 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/majority.2100/umbxz.properties_rep5.txt:	Size of output file is 42 bytes
Removing output file to save space for repetition #5
```

