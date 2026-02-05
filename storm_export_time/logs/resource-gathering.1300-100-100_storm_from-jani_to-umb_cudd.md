# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [0.138, 0.23, 0.114, 0.117, 0.143]



### Log file: storm_from-jani_to-umb_cudd_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.425 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:23:48 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.198s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.044s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model.umb'.
Time for model export: 0.138s.


Performance statistics:
  * peak memory usage: 227MB
  * CPU time: 1.266s
  * wallclock time: 1.386s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model.umb:	Size of output file is 85897216 bytes
```



### Log file: storm_from-jani_to-umb_cudd_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.772 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:37:12 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.276s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.215s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep2.umb'.
Time for model export: 0.230s.


Performance statistics:
  * peak memory usage: 226MB
  * CPU time: 1.520s
  * wallclock time: 1.730s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep2.umb:	Size of output file is 85897216 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.358 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:37:50 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.216s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 0.986s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep3.umb'.
Time for model export: 0.114s.


Performance statistics:
  * peak memory usage: 227MB
  * CPU time: 1.225s
  * wallclock time: 1.323s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep3.umb:	Size of output file is 85897216 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.413 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:59:23 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.236s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.008s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep4.umb'.
Time for model export: 0.117s.


Performance statistics:
  * peak memory usage: 227MB
  * CPU time: 1.269s
  * wallclock time: 1.365s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep4.umb:	Size of output file is 85897216 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.435 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:07 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.220s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.028s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep5.umb'.
Time for model export: 0.143s.


Performance statistics:
  * peak memory usage: 226MB
  * CPU time: 1.277s
  * wallclock time: 1.396s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/resource-gathering.1300-100-100/model_rep5.umb:	Size of output file is 85897216 bytes
Removing output file to save space for repetition #5
```

