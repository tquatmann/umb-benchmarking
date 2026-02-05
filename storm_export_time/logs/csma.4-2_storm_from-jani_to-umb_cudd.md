# Log files for storm_from-jani_to-umb_cudd on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[0.073, 0.045, 0.072, 0.04, 0.078]`



### Log file: storm_from-jani_to-umb_cudd_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.258 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:25:54 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 1.120s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.885s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.4-2/model.umb'.
Time for model export: 0.073s.


Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.128s
  * wallclock time: 2.218s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.4-2/model.umb:	Size of output file is 34328576 bytes
```



### Log file: storm_from-jani_to-umb_cudd_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.675 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:37:05 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 1.446s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.975s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep2.umb'.
Time for model export: 0.045s.


Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.552s
  * wallclock time: 2.625s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep2.umb:	Size of output file is 34328576 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.850 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:59:23 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 1.612s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.925s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep3.umb'.
Time for model export: 0.072s.


Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.683s
  * wallclock time: 2.798s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep3.umb:	Size of output file is 34328576 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.107 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:36:45 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 1.059s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.832s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep4.umb'.
Time for model export: 0.040s.


Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.003s
  * wallclock time: 2.067s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep4.umb:	Size of output file is 34328576 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.151 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:16:03 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.032s.

Time for model construction: 1.752s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.921s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep5.umb'.
Time for model export: 0.078s.


Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.721s
  * wallclock time: 3.013s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/csma.4-2/model_rep5.umb:	Size of output file is 34328576 bytes
Removing output file to save space for repetition #5
```

