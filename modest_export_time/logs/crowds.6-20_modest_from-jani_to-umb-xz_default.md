# Log files for modest_from-jani_to-umb-xz_default on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[ERR, 64.7, 68.6, 79.2, 74.7]`



### Log file: modest_from-jani_to-umb-xz_default_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 0.236 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb.xz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb.xz:	Size of output file is 11968720 bytes
out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties.txt:	Size of output file is 27 bytes
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 82.886 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 1623 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               674720 states/s
  Peak memory:        746.95 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.8 s
  Time (merging):     2.2 s

+ UMB export
  Time:        64.7 s
  File size:   11.49 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep2.xz:	Size of output file is 12053180 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep2.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 86.673 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 1623 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               680942 states/s
  Peak memory:        746.92 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 15.6 s
  Time (merging):     2.2 s

+ UMB export
  Time:        68.6 s
  File size:   11.56 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep3.xz:	Size of output file is 12122568 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep3.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 100.542 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 1624 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               574789 states/s
  Peak memory:        747.03 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 18.5 s
  Time (merging):     2.5 s

+ UMB export
  Time:        79.2 s
  File size:   11.45 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep4.xz:	Size of output file is 12008924 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep4.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 94.501 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 5, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 10633591 states.

Peak memory usage: 1623 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             10633591
  Choices:            10633591
  Branches:           38261191
  Rate:               619096 states/s
  Peak memory:        746.99 MB
  Final size:         664.95 MB
  Size on disk:       52.94 MB
  Time (exploration): 17.2 s
  Time (merging):     2.3 s

+ UMB export
  Time:        74.7 s
  File size:   11.51 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.6-20/model.umb_rep5.xz:	Size of output file is 12068996 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/crowds.6-20/umbxz.properties_rep5.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
```

