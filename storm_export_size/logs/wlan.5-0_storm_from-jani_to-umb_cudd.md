# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [wlan.5-0](../../models/wlan.5-0)
Parsed values: [70907392.0, 70907392.0, 70907392.0, 70907392.0, 70907392.0]



### Log file: storm_from-jani_to-umb_cudd_wlan.5-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.045 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:38:22 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 0.140s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.752s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.5-0/model.umb'.
Time for model export: 0.095s.


Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 1.913s
  * wallclock time: 2.001s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.5-0/model.umb:	Size of output file is 70907392 bytes
```



### Log file: storm_from-jani_to-umb_cudd_wlan.5-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.969 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:40:38 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.129s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.672s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep2.umb'.
Time for model export: 0.119s.


Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 1.828s
  * wallclock time: 1.932s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep2.umb:	Size of output file is 70907392 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_wlan.5-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.936 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:16:02 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.144s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.648s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep3.umb'.
Time for model export: 0.092s.


Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 1.819s
  * wallclock time: 1.895s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep3.umb:	Size of output file is 70907392 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_wlan.5-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.234 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:17:35 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.007s.

Time for model construction: 0.185s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.845s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep4.umb'.
Time for model export: 0.135s.


Performance statistics:
  * peak memory usage: 198MB
  * CPU time: 2.052s
  * wallclock time: 2.184s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep4.umb:	Size of output file is 70907392 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_wlan.5-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.942 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:25:43 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.148s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.644s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep5.umb'.
Time for model export: 0.094s.


Performance statistics:
  * peak memory usage: 198MB
  * CPU time: 1.816s
  * wallclock time: 1.901s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.5-0/model_rep5.umb:	Size of output file is 70907392 bytes
Removing output file to save space for repetition #5
```

