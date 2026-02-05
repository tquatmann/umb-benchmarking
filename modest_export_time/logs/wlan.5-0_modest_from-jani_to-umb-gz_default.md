# Log files for modest_from-jani_to-umb-gz_default on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[ERR, 1.1, 1.4, 1.4, 1.2]`



### Log file: modest_from-jani_to-umb-gz_default_wlan.5-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.492 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb.gz:	Size of output file is 9653495 bytes
out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties.txt:	Size of output file is 28 bytes
```



### Log file: modest_from-jani_to-umb-gz_default_wlan.5-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep2.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 3.911 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep2.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 241 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               583169 states/s
  Peak memory:        95.53 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.2 s
  Time (merging):     0.2 s

+ UMB export
  Time:        1.1 s
  File size:   9.21 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep2.gz:	Size of output file is 9653491 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep2.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_default_wlan.5-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep3.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 5.135 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep3.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 244 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               461589 states/s
  Peak memory:        95.56 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.8 s
  Time (merging):     0.3 s

+ UMB export
  Time:        1.4 s
  File size:   9.21 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep3.gz:	Size of output file is 9653511 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep3.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_default_wlan.5-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep4.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 4.679 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep4.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 241 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               484556 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.7 s
  Time (merging):     0.3 s

+ UMB export
  Time:        1.4 s
  File size:   9.21 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep4.gz:	Size of output file is 9653530 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep4.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_default_wlan.5-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep5.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 4.049 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --umb out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep5.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.

Peak memory usage: 242 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               585013 states/s
  Peak memory:        95.53 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.2 s
  Time (merging):     0.2 s

+ UMB export
  Time:        1.2 s
  File size:   9.21 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/wlan.5-0/model.umb_rep5.gz:	Size of output file is 9653479 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_default/wlan.5-0/umbgz.properties_rep5.txt:	Size of output file is 28 bytes
Removing output file to save space for repetition #5
```

