# Log files for modest_from-jani_to-umb-gz_default on model [consensus.4-4](../../models/consensus.4-4)

Parsed values: `[ERR, 0.1, 0.1, 0.1, 0.1]`



### Log file: modest_from-jani_to-umb-gz_default_consensus.4-4_rep1.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.165 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb.gz:	Size of output file is 505084 bytes
out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties.txt:	Size of output file is 27 bytes
```



### Log file: modest_from-jani_to-umb-gz_default_consensus.4-4_rep2.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep2.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.609 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep2.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.

Peak memory usage: 97 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               154057 states/s
  Peak memory:        65.44 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.1 s
  File size:   0.48 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep2.gz:	Size of output file is 505099 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep2.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_default_consensus.4-4_rep3.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep3.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.707 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep3.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.

Peak memory usage: 97 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               153509 states/s
  Peak memory:        65.43 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.1 s
  File size:   0.48 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep3.gz:	Size of output file is 505105 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep3.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_default_consensus.4-4_rep4.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep4.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.657 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep4.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.

Peak memory usage: 97 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               148234 states/s
  Peak memory:        65.44 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.3 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.1 s
  File size:   0.48 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep4.gz:	Size of output file is 505117 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep4.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_default_consensus.4-4_rep5.log

```
Command(s):
../bin/modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep5.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.752 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/consensus.4-4/model.jani --umb out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep5.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "pc1" into 4 locations in automaton "process1".
model.jani:variables[5]: info: Expanding variable "pc2" into 4 locations in automaton "process2".
model.jani:variables[7]: info: Expanding variable "pc3" into 4 locations in automaton "process3".
model.jani:variables[9]: info: Expanding variable "pc4" into 4 locations in automaton "process4".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 43136 states.

Peak memory usage: 98 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             43136
  Choices:            115840
  Branches:           144352
  Rate:               94804 states/s
  Peak memory:        65.44 MB
  Final size:         3.09 MB
  Size on disk:       0.44 MB
  Time (exploration): 0.5 s
  Time (merging):     0.0 s

+ UMB export
  Time:        0.1 s
  File size:   0.48 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/consensus.4-4/model.umb_rep5.gz:	Size of output file is 505101 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_default/consensus.4-4/umbgz.properties_rep5.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
```

