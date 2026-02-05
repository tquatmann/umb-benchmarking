# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [0.08, 0.096, 0.125, 0.116, 0.085]



### Log file: storm_from-jani_to-umb_cudd_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.013 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:32:30 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 0.566s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.239s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.3-4/model.umb'.
Time for model export: 0.080s.


Performance statistics:
  * peak memory usage: 233MB
  * CPU time: 1.880s
  * wallclock time: 1.970s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.3-4/model.umb:	Size of output file is 62541824 bytes
```



### Log file: storm_from-jani_to-umb_cudd_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.884 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:33 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.534s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.143s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep2.umb'.
Time for model export: 0.096s.


Performance statistics:
  * peak memory usage: 233MB
  * CPU time: 1.755s
  * wallclock time: 1.847s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep2.umb:	Size of output file is 62541824 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.706 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:16 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 0.972s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.364s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep3.umb'.
Time for model export: 0.125s.


Performance statistics:
  * peak memory usage: 233MB
  * CPU time: 2.418s
  * wallclock time: 2.586s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep3.umb:	Size of output file is 62541824 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.708 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:26:07 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 1.052s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.406s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep4.umb'.
Time for model export: 0.116s.


Performance statistics:
  * peak memory usage: 233MB
  * CPU time: 2.538s
  * wallclock time: 2.667s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep4.umb:	Size of output file is 62541824 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.193 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:38:02 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.630s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.351s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep5.umb'.
Time for model export: 0.085s.


Performance statistics:
  * peak memory usage: 233MB
  * CPU time: 2.043s
  * wallclock time: 2.150s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.3-4/model_rep5.umb:	Size of output file is 62541824 bytes
Removing output file to save space for repetition #5
```

