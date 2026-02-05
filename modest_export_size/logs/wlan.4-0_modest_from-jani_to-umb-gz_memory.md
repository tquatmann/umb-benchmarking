# Log files for modest_from-jani_to-umb-gz_memory on model [wlan.4-0](../../models/wlan.4-0)

Parsed values: `[2514378.0, 2514380.0, 2514370.0, 2514393.0, 2514391.0]`



### Log file: modest_from-jani_to-umb-gz_memory_wlan.4-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.264 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb.gz:	Size of output file is 2514350 bytes
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties.txt:	Size of output file is 28 bytes
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.4-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 1.206 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.

Peak memory usage: 225 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               623870 states/s
  Peak memory:        87.08 MB
  Final size:         2.67 MB
  Time (exploration): 0.6 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.3 s
  File size:   2.40 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep2.gz:	Size of output file is 2514352 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep2.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.4-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 1.163 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.

Peak memory usage: 225 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               723270 states/s
  Peak memory:        87.08 MB
  Final size:         2.67 MB
  Time (exploration): 0.5 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.4 s
  File size:   2.40 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep3.gz:	Size of output file is 2514342 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep3.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.4-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 1.321 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.

Peak memory usage: 226 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               616071 states/s
  Peak memory:        87.08 MB
  Final size:         2.67 MB
  Time (exploration): 0.6 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.4 s
  File size:   2.40 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep4.gz:	Size of output file is 2514365 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep4.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.4-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 1.287 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.4-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 345000 states.

Peak memory usage: 225 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             345000
  Choices:            440206
  Branches:           762252
  Rate:               629562 states/s
  Peak memory:        87.08 MB
  Final size:         2.67 MB
  Time (exploration): 0.6 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.4 s
  File size:   2.40 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/model.umb_rep5.gz:	Size of output file is 2514363 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_memory/wlan.4-0/umbgz.properties_rep5.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #5
```

