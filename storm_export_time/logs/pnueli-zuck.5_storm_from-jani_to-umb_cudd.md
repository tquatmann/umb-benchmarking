# Log files for storm_from-jani_to-umb_cudd on model [pnueli-zuck.5](../../models/pnueli-zuck.5)

Parsed values: `[0.088, 0.109, 0.116, 0.083, 0.132]`



### Log file: storm_from-jani_to-umb_cudd_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.359 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:44:45 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 0.057s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.539s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model.umb'.
Time for model export: 0.088s.


Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.623s
  * wallclock time: 0.706s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model.umb:	Size of output file is 61800448 bytes
```



### Log file: storm_from-jani_to-umb_cudd_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.917 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:16 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.087s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.615s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep2.umb'.
Time for model export: 0.109s.


Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.715s
  * wallclock time: 0.843s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep2.umb:	Size of output file is 61800448 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.734 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:37:59 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.014s.

Time for model construction: 0.055s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.509s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep3.umb'.
Time for model export: 0.116s.


Performance statistics:
  * peak memory usage: 162MB
  * CPU time: 0.594s
  * wallclock time: 0.700s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep3.umb:	Size of output file is 61800448 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.696 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:52:46 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.018s.

Time for model construction: 0.053s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.491s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep4.umb'.
Time for model export: 0.083s.


Performance statistics:
  * peak memory usage: 162MB
  * CPU time: 0.585s
  * wallclock time: 0.651s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep4.umb:	Size of output file is 61800448 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.866 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:25 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.062s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.564s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep5.umb'.
Time for model export: 0.132s.


Performance statistics:
  * peak memory usage: 162MB
  * CPU time: 0.658s
  * wallclock time: 0.770s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pnueli-zuck.5/model_rep5.umb:	Size of output file is 61800448 bytes
Removing output file to save space for repetition #5
```

