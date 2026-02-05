# Log files

Tool configuration: modest_from-jani_to-aut_default
Benchmark: [egl.10-2](../../models/egl.10-2)
Parsed values: [1854666238.0, 1854666238.0, 1854666238.0, 1854666238.0, 1854666238.0]



### Log file: modest_from-jani_to-aut_default_egl.10-2_rep1.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model.aut AUT  -D --exhaustive
Wallclock time: 133.695 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/egl.10-2/model.aut".

Peak memory usage: 9554 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               585963 states/s
  Peak memory:        6942.33 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 112.8 s
  Time (merging):     5.3 s

+ Export to AUT
  Time:      13.5 s
  File size: 1768.75 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/egl.10-2/model.aut:	Size of output file is 1854666238 bytes
```



### Log file: modest_from-jani_to-aut_default_egl.10-2_rep2.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 133.258 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/egl.10-2/model_rep2.aut".

Peak memory usage: 9552 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               584392 states/s
  Peak memory:        6942.30 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 113.1 s
  Time (merging):     5.3 s

+ Export to AUT
  Time:      13.0 s
  File size: 1768.75 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/egl.10-2/model_rep2.aut:	Size of output file is 1854666238 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_egl.10-2_rep3.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 146.264 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/egl.10-2/model_rep3.aut".

Peak memory usage: 9554 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               531326 states/s
  Peak memory:        6942.63 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 124.4 s
  Time (merging):     5.7 s

+ Export to AUT
  Time:      14.4 s
  File size: 1768.75 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.1 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/egl.10-2/model_rep3.aut:	Size of output file is 1854666238 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_egl.10-2_rep4.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 133.678 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/egl.10-2/model_rep4.aut".

Peak memory usage: 9554 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               583077 states/s
  Peak memory:        6942.29 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 113.3 s
  Time (merging):     5.5 s

+ Export to AUT
  Time:      13.0 s
  File size: 1768.75 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.4 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/egl.10-2/model_rep4.aut:	Size of output file is 1854666238 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_egl.10-2_rep5.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 125.319 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-aut_default/egl.10-2/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/egl.10-2/model_rep5.aut".

Peak memory usage: 9553 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               616522 states/s
  Peak memory:        6942.16 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 107.2 s
  Time (merging):     5.0 s

+ Export to AUT
  Time:      11.5 s
  File size: 1768.75 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.2 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/egl.10-2/model_rep5.aut:	Size of output file is 1854666238 bytes
Removing output file to save space for repetition #5
```

