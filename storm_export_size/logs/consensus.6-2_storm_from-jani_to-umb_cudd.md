# Log files for storm_from-jani_to-umb_cudd on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[150562304.0, 150562304.0, 150562304.0, 150562304.0, 150562304.0]`



### Log file: storm_from-jani_to-umb_cudd_consensus.6-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.159 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:29:05 2026
Command line arguments: --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.174s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1258240 (224 nodes)
Transitions: 	6236736 (7148 nodes)
Choices: 	5008128
Reward Models:  none
Variables: 	rows: 19 meta variables (30 DD variables), columns: 19 meta variables (30 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (31 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 1.495s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.6-2/model.umb'.
Time for model export: 0.201s.


Performance statistics:
  * peak memory usage: 333MB
  * CPU time: 1.598s
  * wallclock time: 1.879s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.6-2/model.umb:	Size of output file is 150562304 bytes
```



### Log file: storm_from-jani_to-umb_cudd_consensus.6-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.893 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:10:58 2026
Command line arguments: --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 0.040s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1258240 (224 nodes)
Transitions: 	6236736 (7148 nodes)
Choices: 	5008128
Reward Models:  none
Variables: 	rows: 19 meta variables (30 DD variables), columns: 19 meta variables (30 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (31 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 1.490s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep2.umb'.
Time for model export: 0.202s.


Performance statistics:
  * peak memory usage: 332MB
  * CPU time: 1.579s
  * wallclock time: 1.760s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep2.umb:	Size of output file is 150562304 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_consensus.6-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.131 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:38:35 2026
Command line arguments: --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.053s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1258240 (224 nodes)
Transitions: 	6236736 (7148 nodes)
Choices: 	5008128
Reward Models:  none
Variables: 	rows: 19 meta variables (30 DD variables), columns: 19 meta variables (30 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (31 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 1.787s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep3.umb'.
Time for model export: 0.238s.


Performance statistics:
  * peak memory usage: 332MB
  * CPU time: 1.913s
  * wallclock time: 2.087s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep3.umb:	Size of output file is 150562304 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_consensus.6-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.345 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:37:15 2026
Command line arguments: --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.060s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1258240 (224 nodes)
Transitions: 	6236736 (7148 nodes)
Choices: 	5008128
Reward Models:  none
Variables: 	rows: 19 meta variables (30 DD variables), columns: 19 meta variables (30 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (31 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 1.918s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep4.umb'.
Time for model export: 0.294s.


Performance statistics:
  * peak memory usage: 333MB
  * CPU time: 2.048s
  * wallclock time: 2.281s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep4.umb:	Size of output file is 150562304 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_consensus.6-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.834 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:28:29 2026
Command line arguments: --timemem --buildfull --jani models/consensus.6-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 0.042s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1258240 (224 nodes)
Transitions: 	6236736 (7148 nodes)
Choices: 	5008128
Reward Models:  none
Variables: 	rows: 19 meta variables (30 DD variables), columns: 19 meta variables (30 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (31 nodes)
   * agree
   * finished
-------------------------------------------------------------- 

Time for model preprocessing: 1.492s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	4 labels
   * finished -> 384 item(s)
   * agree -> 114258 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep5.umb'.
Time for model export: 0.229s.


Performance statistics:
  * peak memory usage: 332MB
  * CPU time: 1.594s
  * wallclock time: 1.794s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/consensus.6-2/model_rep5.umb:	Size of output file is 150562304 bytes
Removing output file to save space for repetition #5
```

