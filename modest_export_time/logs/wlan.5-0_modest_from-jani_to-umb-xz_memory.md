# Log files for modest_from-jani_to-umb-xz_memory on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[ERR, 11.3, 11.3, 14.6, 13.4]`



### Log file: modest_from-jani_to-umb-xz_memory_wlan.5-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.193 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb.xz:	Size of output file is 1627828 bytes
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties.txt:	Size of output file is 28 bytes
```



### Log file: modest_from-jani_to-umb-xz_memory_wlan.5-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 12.920 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 583 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               1014266 states/s
  Peak memory:        180.80 MB
  Final size:         10.04 MB
  Time (exploration): 1.3 s
  Time (merging):     0.0 s

+ UMB export
  Time:        11.3 s
  File size:   1.41 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep2.xz:	Size of output file is 1477920 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep2.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_memory_wlan.5-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 12.924 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 580 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               989471 states/s
  Peak memory:        180.80 MB
  Final size:         10.04 MB
  Time (exploration): 1.3 s
  Time (merging):     0.0 s

+ UMB export
  Time:        11.3 s
  File size:   1.54 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep3.xz:	Size of output file is 1616468 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep3.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_memory_wlan.5-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 16.488 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 581 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               836164 states/s
  Peak memory:        180.81 MB
  Final size:         10.04 MB
  Time (exploration): 1.6 s
  Time (merging):     0.0 s

+ UMB export
  Time:        14.6 s
  File size:   1.58 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep4.xz:	Size of output file is 1655164 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep4.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_memory_wlan.5-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 15.191 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 580 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               884712 states/s
  Peak memory:        180.80 MB
  Final size:         10.04 MB
  Time (exploration): 1.5 s
  Time (merging):     0.0 s

+ UMB export
  Time:        13.4 s
  File size:   1.47 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/model.umb_rep5.xz:	Size of output file is 1536952 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_memory/wlan.5-0/umbxz.properties_rep5.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #5
```

