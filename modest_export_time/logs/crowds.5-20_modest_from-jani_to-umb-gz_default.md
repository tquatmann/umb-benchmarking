# Log files for modest_from-jani_to-umb-gz_default on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[ERR, 1.0, 1.0, 1.1, 1.1]`



### Log file: modest_from-jani_to-umb-gz_default_crowds.5-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 0.380 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: error: UMB file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb.gz" already exists.

############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb.gz:	Size of output file is 8359914 bytes
out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties.txt:	Size of output file is 27 bytes
```



### Log file: modest_from-jani_to-umb-gz_default_crowds.5-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep2.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 4.787 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep2.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep2.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 380 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               664931 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.1 s
  Time (merging):     0.5 s

+ UMB export
  Time:        1.0 s
  File size:   7.97 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep2.gz:	Size of output file is 8359929 bytes
Removing output file to save space for repetition #2
out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep2.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-umb-gz_default_crowds.5-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep3.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 4.888 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep3.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep3.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 378 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               644763 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.2 s
  Time (merging):     0.5 s

+ UMB export
  Time:        1.0 s
  File size:   7.97 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep3.gz:	Size of output file is 8359953 bytes
Removing output file to save space for repetition #3
out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep3.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-umb-gz_default_crowds.5-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep4.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 5.617 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep4.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep4.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 379 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               569442 states/s
  Peak memory:        126.26 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.6 s
  Time (merging):     0.5 s

+ UMB export
  Time:        1.1 s
  File size:   7.97 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep4.gz:	Size of output file is 8359867 bytes
Removing output file to save space for repetition #4
out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep4.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-umb-gz_default_crowds.5-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep5.txt --umb-compress GZIP  -D --exhaustive
Wallclock time: 5.615 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.5-20/model.jani --umb out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep5.gz out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep5.txt --umb-compress GZIP -D --exhaustive




model.jani:model: info: model is a DTMC model.
model.jani: info: Need 40 bytes per state.
model.jani: warning: The probabilities for a transition labelled "τ" with 20 branches in state (crowds.location = l, observe0 = 0, crowds.runCount = 4, crowds.lastSeen = 0, crowds.observe1 = 0, crowds.observe2 = 0, crowds.observe3 = 0, crowds.observe4 = 0, crowds.observe5 = 0, crowds.observe6 = 0, crowds.observe7 = 0, crowds.observe8 = 0, crowds.observe9 = 0, crowds.observe10 = 0, crowds.observe11 = 0, crowds.observe12 = 0, crowds.observe13 = 0, crowds.observe14 = 0, crowds.observe15 = 0, crowds.observe16 = 0, crowds.observe17 = 0, crowds.observe18 = 0, crowds.observe19 = 0, crowds.launch = False, crowds.new = False, crowds.start = False, crowds.run = False, crowds.good = True, crowds.bad = False, crowds.recordLast = True, crowds.badObserve = False, crowds.deliver = False, crowds.done = False) do not sum up to the expected value of 1 (actual sum: 1.0000000000000002). Results will likely be affected by floating-point errors.
model.jani: info: Explored 2061951 states.

Peak memory usage: 377 MB
Analysis results for model.jani

+ State space exploration
  State size:         40 bytes
  States:             2061951
  Choices:            2061951
  Branches:           7374951
  Rate:               568344 states/s
  Peak memory:        126.27 MB
  Final size:         128.26 MB
  Size on disk:       10.19 MB
  Time (exploration): 3.6 s
  Time (merging):     0.5 s

+ UMB export
  Time:        1.1 s
  File size:   7.97 MB
  Compression: GZip (Optimal)


############################## Output files ##############################
out/modest_from-jani_to-umb-gz_default/crowds.5-20/model.umb_rep5.gz:	Size of output file is 8359895 bytes
Removing output file to save space for repetition #5
out/modest_from-jani_to-umb-gz_default/crowds.5-20/umbgz.properties_rep5.txt:	Size of output file is 27 bytes
Removing output file to save space for repetition #5
```

