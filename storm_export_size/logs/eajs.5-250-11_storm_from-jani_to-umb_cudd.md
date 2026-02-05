# Log files for storm_from-jani_to-umb_cudd on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[207139328.0, 207139328.0, 207139328.0, 207139328.0, 207139328.0]`



### Log file: storm_from-jani_to-umb_cudd_eajs.5-250-11_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.278 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 07:42:08 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.151s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 7.745s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model.umb'.
Time for model export: 0.323s.


Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 7.934s
  * wallclock time: 8.242s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model.umb:	Size of output file is 207139328 bytes
```



### Log file: storm_from-jani_to-umb_cudd_eajs.5-250-11_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.943 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:56:50 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.241s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 8.189s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep2.umb'.
Time for model export: 0.425s.


Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 8.475s
  * wallclock time: 8.891s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep2.umb:	Size of output file is 207139328 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_eajs.5-250-11_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.126 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:37:50 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.131s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 7.675s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep3.umb'.
Time for model export: 0.260s.


Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 7.853s
  * wallclock time: 8.089s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep3.umb:	Size of output file is 207139328 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_eajs.5-250-11_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.091 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:11 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.192s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 8.979s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep4.umb'.
Time for model export: 0.355s.


Performance statistics:
  * peak memory usage: 449MB
  * CPU time: 9.220s
  * wallclock time: 9.555s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep4.umb:	Size of output file is 207139328 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_eajs.5-250-11_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.722 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:26:01 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.220s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 9.113s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep5.umb'.
Time for model export: 0.312s.


Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 9.361s
  * wallclock time: 9.677s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.5-250-11/model_rep5.umb:	Size of output file is 207139328 bytes
Removing output file to save space for repetition #5
```

