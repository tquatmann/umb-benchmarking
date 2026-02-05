# Log files

Tool configuration: modest_from-jani_to-umb-xz_default
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [, 2208735.0, 2200211.0, 2216887.0, 2215167.0]



### Log file: modest_from-jani_to-umb-xz_default_crowds.5-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep2.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 16.599 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep2.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep2.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 472 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               640159 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.2 s
  Time (merging):     0.5 s

+ UMB export
  Time:        12.7 s
  File size:   2.11 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep2.xz:	Size of output file is 2208708 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep2.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.5-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep3.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 18.784 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep3.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep3.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 471 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               536129 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.9 s
  Time (merging):     0.6 s

+ UMB export
  Time:        14.1 s
  File size:   2.10 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep3.xz:	Size of output file is 2200184 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep3.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.5-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep4.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 22.676 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep4.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep4.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 473 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               469586 states/s
  Peak memory:        126.25 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 4.4 s
  Time (merging):     0.6 s

+ UMB export
  Time:        17.3 s
  File size:   2.11 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep4.xz:	Size of output file is 2216860 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep4.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-xz_default_crowds.5-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep5.txt --umb-compress XZ  -D --exhaustive
Wallclock time: 20.326 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep5.xz out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep5.txt --umb-compress XZ -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 473 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               520301 states/s
  Peak memory:        126.27 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 4.0 s
  Time (merging):     0.5 s

+ UMB export
  Time:        15.6 s
  File size:   2.11 MB
  Compression: XZ (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-xz_default/crowds.5-20/model.umb_rep5.xz:	Size of output file is 2215140 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-xz_default/crowds.5-20/umbxz.properties_rep5.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
```

