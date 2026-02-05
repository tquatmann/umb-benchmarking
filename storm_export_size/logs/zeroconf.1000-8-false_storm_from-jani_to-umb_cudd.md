# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)
Parsed values: [111156224.0, 111156224.0, 111156224.0, 111156224.0, 111156224.0]



### Log file: storm_from-jani_to-umb_cudd_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 14.845 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:38:22 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.029s.

Time for model construction: 11.081s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1870338 (11778 nodes)
Transitions: 	4245554 (100585 nodes)
Choices: 	3443961
Reward Models:  none
Variables: 	rows: 24 meta variables (60 DD variables), columns: 24 meta variables (60 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 3.101s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1870338
Transitions: 	4245554
Choices: 	3443961
Reward Models:  none
State Labels: 	3 labels
   * target -> 16523 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model.umb'.
Time for model export: 0.163s.


Performance statistics:
  * peak memory usage: 466MB
  * CPU time: 14.198s
  * wallclock time: 14.474s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model.umb:	Size of output file is 111156224 bytes
```



### Log file: storm_from-jani_to-umb_cudd_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 12.969 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:14:01 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 9.673s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1870338 (11778 nodes)
Transitions: 	4245554 (100585 nodes)
Choices: 	3443961
Reward Models:  none
Variables: 	rows: 24 meta variables (60 DD variables), columns: 24 meta variables (60 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 3.030s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1870338
Transitions: 	4245554
Choices: 	3443961
Reward Models:  none
State Labels: 	3 labels
   * target -> 16523 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep2.umb'.
Time for model export: 0.140s.


Performance statistics:
  * peak memory usage: 466MB
  * CPU time: 12.726s
  * wallclock time: 12.930s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep2.umb:	Size of output file is 111156224 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 12.619 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:28:59 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 9.292s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1870338 (11778 nodes)
Transitions: 	4245554 (100585 nodes)
Choices: 	3443961
Reward Models:  none
Variables: 	rows: 24 meta variables (60 DD variables), columns: 24 meta variables (60 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 3.035s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1870338
Transitions: 	4245554
Choices: 	3443961
Reward Models:  none
State Labels: 	3 labels
   * target -> 16523 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep3.umb'.
Time for model export: 0.165s.


Performance statistics:
  * peak memory usage: 466MB
  * CPU time: 12.341s
  * wallclock time: 12.582s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep3.umb:	Size of output file is 111156224 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.054 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:22:40 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.029s.

Time for model construction: 13.835s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1870338 (11778 nodes)
Transitions: 	4245554 (100585 nodes)
Choices: 	3443961
Reward Models:  none
Variables: 	rows: 24 meta variables (60 DD variables), columns: 24 meta variables (60 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 3.688s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1870338
Transitions: 	4245554
Choices: 	3443961
Reward Models:  none
State Labels: 	3 labels
   * target -> 16523 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep4.umb'.
Time for model export: 0.158s.


Performance statistics:
  * peak memory usage: 466MB
  * CPU time: 17.393s
  * wallclock time: 17.821s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep4.umb:	Size of output file is 111156224 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 13.066 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:28:59 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 9.731s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1870338 (11778 nodes)
Transitions: 	4245554 (100585 nodes)
Choices: 	3443961
Reward Models:  none
Variables: 	rows: 24 meta variables (60 DD variables), columns: 24 meta variables (60 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 3.046s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1870338
Transitions: 	4245554
Choices: 	3443961
Reward Models:  none
State Labels: 	3 labels
   * target -> 16523 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep5.umb'.
Time for model export: 0.159s.


Performance statistics:
  * peak memory usage: 466MB
  * CPU time: 12.797s
  * wallclock time: 13.024s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/zeroconf.1000-8-false/model_rep5.umb:	Size of output file is 111156224 bytes
Removing output file to save space for repetition #5
```

