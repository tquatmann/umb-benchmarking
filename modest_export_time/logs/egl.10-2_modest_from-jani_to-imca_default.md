# Log files for modest_from-jani_to-imca_default on model [egl.10-2](../../models/egl.10-2)

Parsed values: `[14.3, 11.9, 15.8, 13.9, 13.8]`



### Log file: modest_from-jani_to-imca_default_egl.10-2_rep1.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model.mrm IMCA  -D --exhaustive
Wallclock time: 138.176 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/egl.10-2/model.mrm".

Peak memory usage: 9552 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               567168 states/s
  Peak memory:        6942.43 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 116.5 s
  Time (merging):     5.6 s

+ Export to IMCA
  Time:      14.3 s
  File size: 1643.06 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.3 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.1 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/egl.10-2/model.mrm:	Size of output file is 1722870698 bytes
```



### Log file: modest_from-jani_to-imca_default_egl.10-2_rep2.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 116.298 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/egl.10-2/model_rep2.mrm".

Peak memory usage: 9554 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               672931 states/s
  Peak memory:        6941.88 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 98.2 s
  Time (merging):     4.7 s

+ Export to IMCA
  Time:      11.9 s
  File size: 1643.06 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.2 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        0.9 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/egl.10-2/model_rep2.mrm:	Size of output file is 1722870698 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_egl.10-2_rep3.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 150.966 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/egl.10-2/model_rep3.mrm".

Peak memory usage: 9555 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               520771 states/s
  Peak memory:        6942.69 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 126.9 s
  Time (merging):     6.2 s

+ Export to IMCA
  Time:      15.8 s
  File size: 1643.06 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.6 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.3 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/egl.10-2/model_rep3.mrm:	Size of output file is 1722870698 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_egl.10-2_rep4.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 133.599 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/egl.10-2/model_rep4.mrm".

Peak memory usage: 9554 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               585630 states/s
  Peak memory:        6942.28 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 112.8 s
  Time (merging):     5.0 s

+ Export to IMCA
  Time:      13.9 s
  File size: 1643.06 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.5 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.2 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/egl.10-2/model_rep4.mrm:	Size of output file is 1722870698 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_egl.10-2_rep5.log

```
Command(s):
../bin/modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 133.476 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/egl.10-2/model.jani --statespace out/modest_from-jani_to-imca_default/egl.10-2/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 88 bytes per state.
model.jani: info: Explored 66060286 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/egl.10-2/model_rep5.mrm".

Peak memory usage: 9555 MB
Analysis results for model.jani

+ State space exploration
  State size:         88 bytes
  States:             66060286
  Choices:            66060286
  Branches:           67108861
  Rate:               588437 states/s
  Peak memory:        6942.28 MB
  Final size:         1528.00 MB
  Size on disk:       255.83 MB
  Time (exploration): 112.3 s
  Time (merging):     5.1 s

+ Export to IMCA
  Time:      13.8 s
  File size: 1643.06 MB

+ Property unfairA
  Probability: 0.50048828125
  Bounds:      [0.50048828125, 0.50048828125]
  Time:        1.8 s

  + Value iteration
    Final error: 0
    Iterations:  2
    Time:        1.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/egl.10-2/model_rep5.mrm:	Size of output file is 1722870698 bytes
Removing output file to save space for repetition #5
```

