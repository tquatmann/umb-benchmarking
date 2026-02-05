# Log files for modest_from-jani_to-umb-xz_default on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[1559696.0, 1619556.0, 1571296.0, 1626112.0, 1627720.0]`



### Log file: modest_from-jani_to-umb-xz_default_wlan.5-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 0.225 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb.xz:	Size of output file is 1559668 bytes
out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties.txt:	Size of output file is 28 bytes
```



### Log file: modest_from-jani_to-umb-xz_default_wlan.5-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 16.040 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 338 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               513772 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.5 s
  Time (merging):     0.3 s

+ UMB export
  Time:        12.9 s
  File size:   1.54 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep2.xz:	Size of output file is 1619528 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep2.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_wlan.5-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 18.301 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 338 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               473745 states/s
  Peak memory:        95.55 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.8 s
  Time (merging):     0.3 s

+ UMB export
  Time:        15.0 s
  File size:   1.50 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep3.xz:	Size of output file is 1571268 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep3.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_wlan.5-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 15.239 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 337 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               545585 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ UMB export
  Time:        12.4 s
  File size:   1.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep4.xz:	Size of output file is 1626084 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep4.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_wlan.5-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 17.301 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 337 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               486558 states/s
  Peak memory:        95.55 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.7 s
  Time (merging):     0.3 s

+ UMB export
  Time:        14.0 s
  File size:   1.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/wlan.5-0/model.umb_rep5.xz:	Size of output file is 1627692 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/wlan.5-0/umbxz.properties_rep5.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #5
```

