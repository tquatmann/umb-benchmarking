# Log files for modest_from-jani_to-umb-gz_memory on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[ERR, 4.9, 4.4, 4.4, 4.7]`



### Log file: modest_from-jani_to-umb-gz_memory_wlan.6-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.299 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb.gz:	Size of output file is 37822346 bytes
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties.txt:	Size of output file is 28 bytes
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.6-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 13.585 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.

Peak memory usage: 1585 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               619669 states/s
  Peak memory:        593.54 MB
  Final size:         38.80 MB
  Time (exploration): 8.1 s
  Time (merging):     0.2 s

+ UMB export
  Time:        4.9 s
  File size:   36.07 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep2.gz:	Size of output file is 37822518 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep2.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.6-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 11.884 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.

Peak memory usage: 1584 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               716182 states/s
  Peak memory:        593.53 MB
  Final size:         38.80 MB
  Time (exploration): 7.0 s
  Time (merging):     0.2 s

+ UMB export
  Time:        4.4 s
  File size:   36.07 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep3.gz:	Size of output file is 37822564 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep3.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.6-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 11.770 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.

Peak memory usage: 1587 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               728477 states/s
  Peak memory:        593.52 MB
  Final size:         38.80 MB
  Time (exploration): 6.9 s
  Time (merging):     0.2 s

+ UMB export
  Time:        4.4 s
  File size:   36.07 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep4.gz:	Size of output file is 37822565 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep4.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_memory_wlan.6-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 13.222 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.6-0/model.jani --umb out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 5007548 states.

Peak memory usage: 1584 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             5007548
  Choices:            6350470
  Branches:           11475748
  Rate:               624850 states/s
  Peak memory:        593.55 MB
  Final size:         38.80 MB
  Time (exploration): 8.0 s
  Time (merging):     0.2 s

+ UMB export
  Time:        4.7 s
  File size:   36.07 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/model.umb_rep5.gz:	Size of output file is 37822529 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_memory/wlan.6-0/umbgz.properties_rep5.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #5
```

