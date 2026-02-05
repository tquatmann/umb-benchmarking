# Log files

Tool configuration: modest_from-jani_to-imca_default
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [0.6, 0.6, 0.5, 0.6, 0.5]



### Log file: modest_from-jani_to-imca_default_wlan.5-0_rep1.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model.mrm IMCA  -D --exhaustive
Wallclock time: 5.907 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.5-0/model.mrm".

Peak memory usage: 241 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               477412 states/s
  Peak memory:        95.55 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.7 s
  Time (merging):     0.3 s

+ Export to IMCA
  Time:      0.6 s
  File size: 55.11 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   2.0 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 2.0 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.5-0/model.mrm:	Size of output file is 57788751 bytes
```



### Log file: modest_from-jani_to-imca_default_wlan.5-0_rep2.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 5.179 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.5-0/model_rep2.mrm".

Peak memory usage: 240 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               566092 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 55.11 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.7 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.5-0/model_rep2.mrm:	Size of output file is 57788751 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_wlan.5-0_rep3.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 5.021 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.5-0/model_rep3.mrm".

Peak memory usage: 243 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               580555 states/s
  Peak memory:        95.53 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 55.11 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.7 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.7 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.5-0/model_rep3.mrm:	Size of output file is 57788751 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_wlan.5-0_rep4.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 5.488 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.5-0/model_rep4.mrm".

Peak memory usage: 243 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               538328 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.4 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.6 s
  File size: 55.11 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.9 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.9 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.5-0/model_rep4.mrm:	Size of output file is 57788751 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_wlan.5-0_rep5.log

```
Command(s):
../bin/modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 5.267 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/wlan.5-0/model.jani --statespace out/modest_from-jani_to-imca_default/wlan.5-0/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:variables[3]: info: Expanding variable "s1" into 12 locations in automaton "station1".
model.jani:variables[4]: info: Expanding variable "s2" into 12 locations in automaton "station2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 1295218 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/wlan.5-0/model_rep5.mrm".

Peak memory usage: 242 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             1295218
  Choices:            1646074
  Branches:           2929960
  Rate:               559006 states/s
  Peak memory:        95.54 MB
  Final size:         57.27 MB
  Size on disk:       10.42 MB
  Time (exploration): 2.3 s
  Time (merging):     0.2 s

+ Export to IMCA
  Time:      0.5 s
  File size: 55.11 MB

+ Property sent
  Result: True
  Bounds: [1, 1]
  Time:   1.8 s

  + Precomputations
    Min. prob. 0 states:          0
    Time for min. prob. 0 states: 1.8 s
    Min. prob. 1 states:          1295218
    Time for min. prob. 1 states: 0.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/wlan.5-0/model_rep5.mrm:	Size of output file is 57788751 bytes
Removing output file to save space for repetition #5
```

