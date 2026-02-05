# Log files for modest_from-jani_to-umb-xz_memory on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[ERR, 24.3, 30.7, 22.3, 23.6]`



### Log file: modest_from-jani_to-umb-xz_memory_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.190 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb.xz:	Size of output file is 7108500 bytes
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties.txt:	Size of output file is 30 bytes
```



### Log file: modest_from-jani_to-umb-xz_memory_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 26.579 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 828 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               911433 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.1 s
  Time (merging):     0.1 s

+ UMB export
  Time:        24.3 s
  File size:   6.78 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep2.xz:	Size of output file is 7104740 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep2.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_memory_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 33.558 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 828 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               727155 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.6 s
  Time (merging):     0.1 s

+ UMB export
  Time:        30.7 s
  File size:   6.78 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep3.xz:	Size of output file is 7108920 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep3.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_memory_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 24.647 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 828 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               930554 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.0 s
  Time (merging):     0.1 s

+ UMB export
  Time:        22.3 s
  File size:   6.77 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep4.xz:	Size of output file is 7103468 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep4.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_memory_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 25.814 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 828 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               953414 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.0 s
  Time (merging):     0.1 s

+ UMB export
  Time:        23.6 s
  File size:   6.78 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/model.umb_rep5.xz:	Size of output file is 7105948 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_memory/zeroconf.1000-8-false/umbxz.properties_rep5.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #5
```

