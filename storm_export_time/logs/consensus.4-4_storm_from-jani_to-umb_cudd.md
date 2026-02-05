# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [consensus.4-4](../../models/consensus.4-4)
Parsed values: [0.006, 0.009, 0.009, 0.009, 0.006]



### Log file: storm_from-jani_to-umb_cudd_consensus.4-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.120 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:48:23 2026
Command line arguments: --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.024s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	43136 (111 nodes)
Transitions: 	144352 (2372 nodes)
Choices: 	115840
Reward Models:  none
Variables: 	rows: 13 meta variables (22 DD variables), columns: 13 meta variables (22 DD variables), nondeterminism: 3 meta variables (3 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 0.045s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * agree -> 9170 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.4-4/model.umb'.
Time for model export: 0.006s.


Performance statistics:
  * peak memory usage: 48MB
  * CPU time: 0.085s
  * wallclock time: 0.083s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.4-4/model.umb:	Size of output file is 3617280 bytes
```



### Log file: storm_from-jani_to-umb_cudd_consensus.4-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.132 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:32:22 2026
Command line arguments: --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.026s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	43136 (111 nodes)
Transitions: 	144352 (2372 nodes)
Choices: 	115840
Reward Models:  none
Variables: 	rows: 13 meta variables (22 DD variables), columns: 13 meta variables (22 DD variables), nondeterminism: 3 meta variables (3 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 0.048s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * agree -> 9170 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep2.umb'.
Time for model export: 0.009s.


Performance statistics:
  * peak memory usage: 48MB
  * CPU time: 0.104s
  * wallclock time: 0.089s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep2.umb:	Size of output file is 3617280 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_consensus.4-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.137 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:21:10 2026
Command line arguments: --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.025s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	43136 (111 nodes)
Transitions: 	144352 (2372 nodes)
Choices: 	115840
Reward Models:  none
Variables: 	rows: 13 meta variables (22 DD variables), columns: 13 meta variables (22 DD variables), nondeterminism: 3 meta variables (3 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 0.044s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * agree -> 9170 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep3.umb'.
Time for model export: 0.009s.


Performance statistics:
  * peak memory usage: 48MB
  * CPU time: 0.098s
  * wallclock time: 0.088s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep3.umb:	Size of output file is 3617280 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_consensus.4-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.158 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:26:59 2026
Command line arguments: --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 0.026s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	43136 (111 nodes)
Transitions: 	144352 (2372 nodes)
Choices: 	115840
Reward Models:  none
Variables: 	rows: 13 meta variables (22 DD variables), columns: 13 meta variables (22 DD variables), nondeterminism: 3 meta variables (3 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 0.047s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * agree -> 9170 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep4.umb'.
Time for model export: 0.009s.


Performance statistics:
  * peak memory usage: 48MB
  * CPU time: 0.093s
  * wallclock time: 0.114s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep4.umb:	Size of output file is 3617280 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_consensus.4-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.152 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:46:41 2026
Command line arguments: --timemem --buildfull --jani models/consensus.4-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 0.020s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	43136 (111 nodes)
Transitions: 	144352 (2372 nodes)
Choices: 	115840
Reward Models:  none
Variables: 	rows: 13 meta variables (22 DD variables), columns: 13 meta variables (22 DD variables), nondeterminism: 3 meta variables (3 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 0.038s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	43136
Transitions: 	144352
Choices: 	115840
Reward Models:  none
State Labels: 	4 labels
   * finished -> 64 item(s)
   * agree -> 9170 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep5.umb'.
Time for model export: 0.006s.


Performance statistics:
  * peak memory usage: 47MB
  * CPU time: 0.078s
  * wallclock time: 0.095s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.4-4/model_rep5.umb:	Size of output file is 3617280 bytes
Removing output file to save space for repetition #5
```

