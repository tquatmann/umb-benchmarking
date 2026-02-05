# Log files for modest_from-jani_to-umb-gz_memory on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[17083223.0, 17083145.0, 17083153.0, 17083165.0, 17083221.0]`



### Log file: modest_from-jani_to-umb-gz_memory_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 0.184 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb.gz:	Size of output file is 17083193 bytes
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties.txt:	Size of output file is 30 bytes
```



### Log file: modest_from-jani_to-umb-gz_memory_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 5.004 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep2.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 735 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               763200 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.5 s
  Time (merging):     0.1 s

+ UMB export
  Time:        2.2 s
  File size:   16.29 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep2.gz:	Size of output file is 17083115 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep2.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_memory_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 4.125 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep3.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 735 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               951952 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.0 s
  Time (merging):     0.1 s

+ UMB export
  Time:        1.8 s
  File size:   16.29 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep3.gz:	Size of output file is 17083123 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep3.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_memory_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 4.588 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep4.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 735 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               801967 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.3 s
  Time (merging):     0.1 s

+ UMB export
  Time:        1.9 s
  File size:   16.29 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep4.gz:	Size of output file is 17083135 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep4.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_memory_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive
Wallclock time: 4.053 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/zeroconf.1000-8-false/model.jani --umb out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep5.txt --umb-compress GZIP -S Memory -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "l" into 5 locations in automaton "host0".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 1862970 states.

Peak memory usage: 735 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             1862970
  Choices:            3431320
  Branches:           4229631
  Rate:               919531 states/s
  Peak memory:        225.53 MB
  Final size:         14.44 MB
  Time (exploration): 2.0 s
  Time (merging):     0.1 s

+ UMB export
  Time:        1.7 s
  File size:   16.29 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/model.umb_rep5.gz:	Size of output file is 17083191 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_memory/zeroconf.1000-8-false/umbgz.properties_rep5.txt:	Size of output file is 30 bytes
Removing output file to save space for repetition #5
```

