# Log files for modest_from-jani_to-umb-xz_memory on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[ERR, 66.9, 71.4, 78.6, 71.6]`



### Log file: modest_from-jani_to-umb-xz_memory_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 0.319 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb.xz:	Size of output file is 12080272 bytes
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties.txt:	Size of output file is 27 bytes
```



### Log file: modest_from-jani_to-umb-xz_memory_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 78.165 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep2.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4458 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               1018738 states/s
  Peak memory:        1963.21 MB
  Final size:         82.40 MB
  Time (exploration): 10.5 s
  Time (merging):     0.6 s

+ UMB export
  Time:        66.9 s
  File size:   11.49 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep2.xz:	Size of output file is 12047260 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep2.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_memory_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 81.606 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep3.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4460 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               1112184 states/s
  Peak memory:        1963.20 MB
  Final size:         82.40 MB
  Time (exploration): 9.6 s
  Time (merging):     0.4 s

+ UMB export
  Time:        71.4 s
  File size:   11.56 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep3.xz:	Size of output file is 12125532 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep3.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_memory_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 90.864 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep4.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4459 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               926513 states/s
  Peak memory:        1963.26 MB
  Final size:         82.40 MB
  Time (exploration): 11.5 s
  Time (merging):     0.5 s

+ UMB export
  Time:        78.6 s
  File size:   11.55 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep4.xz:	Size of output file is 12115984 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep4.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_memory_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive
Wallclock time: 83.218 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep5.txt --umb-compress XZ -S Memory -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 4460 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               977712 states/s
  Peak memory:        1963.24 MB
  Final size:         82.40 MB
  Time (exploration): 10.9 s
  Time (merging):     0.5 s

+ UMB export
  Time:        71.6 s
  File size:   11.21 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/model.umb_rep5.xz:	Size of output file is 11757268 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_memory/crowds.6-20/umbxz.properties_rep5.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
```

