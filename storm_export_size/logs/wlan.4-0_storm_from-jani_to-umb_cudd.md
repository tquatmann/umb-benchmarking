# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [18619904.0, 18619904.0, 18619904.0, 18619904.0, 18619904.0]



### Log file: storm_from-jani_to-umb_cudd_wlan.4-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.647 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:46:17 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.097s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.477s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.4-0/model.umb'.
Time for model export: 0.025s.


Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.592s
  * wallclock time: 0.611s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.4-0/model.umb:	Size of output file is 18619904 bytes
```



### Log file: storm_from-jani_to-umb_cudd_wlan.4-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.621 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:48:44 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.093s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.451s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep2.umb'.
Time for model export: 0.024s.


Performance statistics:
  * peak memory usage: 97MB
  * CPU time: 0.572s
  * wallclock time: 0.579s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep2.umb:	Size of output file is 18619904 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_wlan.4-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.752 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:08 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.130s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.538s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep3.umb'.
Time for model export: 0.027s.


Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.686s
  * wallclock time: 0.706s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep3.umb:	Size of output file is 18619904 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_wlan.4-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.631 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:41:07 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.097s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.461s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep4.umb'.
Time for model export: 0.024s.


Performance statistics:
  * peak memory usage: 97MB
  * CPU time: 0.572s
  * wallclock time: 0.593s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep4.umb:	Size of output file is 18619904 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_wlan.4-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.709 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:40:37 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.035s.

Time for model construction: 0.102s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.499s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep5.umb'.
Time for model export: 0.025s.


Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.618s
  * wallclock time: 0.669s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.4-0/model_rep5.umb:	Size of output file is 18619904 bytes
Removing output file to save space for repetition #5
```

