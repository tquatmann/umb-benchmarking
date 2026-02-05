# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.1, 0.1, 0.1, 0.1, 0.1]



### Log file: modest_from-jani_to-aut_default_embedded.8-12_rep1.log

```
Command(s):
../bin/modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model.aut AUT  -D --exhaustive
Wallclock time: 4.198 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 8548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/embedded.8-12/model.aut".

Peak memory usage: 67 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             8548
  Choices:            8548
  Branches:           36041
  Rate:               77009 states/s
  Peak memory:        41.30 MB
  Final size:         0.62 MB
  Size on disk:       0.14 MB
  Time (exploration): 0.1 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 1.30 MB

+ Property actuators
  Probability: 0.10350970285712112
  Bounds:      [0.10350970285712112, 1]
  Time:        3.8 s

  + Value iteration
    Final error: 9.999901531850148E-07
    Iterations:  94800
    Time:        3.8 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/embedded.8-12/model.aut:	Size of output file is 1359052 bytes
```



### Log file: modest_from-jani_to-aut_default_embedded.8-12_rep2.log

```
Command(s):
../bin/modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 4.544 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 8548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/embedded.8-12/model_rep2.aut".

Peak memory usage: 67 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             8548
  Choices:            8548
  Branches:           36041
  Rate:               71233 states/s
  Peak memory:        41.30 MB
  Final size:         0.62 MB
  Size on disk:       0.14 MB
  Time (exploration): 0.1 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 1.30 MB

+ Property actuators
  Probability: 0.10350970285712112
  Bounds:      [0.10350970285712112, 1]
  Time:        4.1 s

  + Value iteration
    Final error: 9.999901531850148E-07
    Iterations:  94800
    Time:        4.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/embedded.8-12/model_rep2.aut:	Size of output file is 1359052 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_embedded.8-12_rep3.log

```
Command(s):
../bin/modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 4.766 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 8548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/embedded.8-12/model_rep3.aut".

Peak memory usage: 69 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             8548
  Choices:            8548
  Branches:           36041
  Rate:               67307 states/s
  Peak memory:        41.30 MB
  Final size:         0.62 MB
  Size on disk:       0.14 MB
  Time (exploration): 0.1 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 1.30 MB

+ Property actuators
  Probability: 0.10350970285712112
  Bounds:      [0.10350970285712112, 1]
  Time:        4.3 s

  + Value iteration
    Final error: 9.999901531850148E-07
    Iterations:  94800
    Time:        4.3 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/embedded.8-12/model_rep3.aut:	Size of output file is 1359052 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_embedded.8-12_rep4.log

```
Command(s):
../bin/modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 4.859 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 8548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/embedded.8-12/model_rep4.aut".

Peak memory usage: 67 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             8548
  Choices:            8548
  Branches:           36041
  Rate:               65754 states/s
  Peak memory:        41.33 MB
  Final size:         0.62 MB
  Size on disk:       0.14 MB
  Time (exploration): 0.2 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 1.30 MB

+ Property actuators
  Probability: 0.10350970285712112
  Bounds:      [0.10350970285712112, 1]
  Time:        4.4 s

  + Value iteration
    Final error: 9.999901531850148E-07
    Iterations:  94800
    Time:        4.4 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/embedded.8-12/model_rep4.aut:	Size of output file is 1359052 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_embedded.8-12_rep5.log

```
Command(s):
../bin/modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 4.612 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/embedded.8-12/model.jani --statespace out/modest_from-jani_to-aut_default/embedded.8-12/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 8548 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/embedded.8-12/model_rep5.aut".

Peak memory usage: 65 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             8548
  Choices:            8548
  Branches:           36041
  Rate:               70645 states/s
  Peak memory:        41.30 MB
  Final size:         0.62 MB
  Size on disk:       0.14 MB
  Time (exploration): 0.1 s
  Time (merging):     0.0 s

+ Export to AUT
  Time:      0.1 s
  File size: 1.30 MB

+ Property actuators
  Probability: 0.10350970285712112
  Bounds:      [0.10350970285712112, 1]
  Time:        4.2 s

  + Value iteration
    Final error: 9.999901531850148E-07
    Iterations:  94800
    Time:        4.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/embedded.8-12/model_rep5.aut:	Size of output file is 1359052 bytes
Removing output file to save space for repetition #5
```

