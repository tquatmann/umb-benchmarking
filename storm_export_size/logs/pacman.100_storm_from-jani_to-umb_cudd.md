# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [pacman.100](../../models/pacman.100)
Parsed values: [3226472960.0, 3226472960.0, 3226472960.0, 3226472960.0, 3226472960.0]



### Log file: storm_from-jani_to-umb_cudd_pacman.100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 256.313 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:40:28 2026
Command line arguments: --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.021s.

Time for model construction: 194.325s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	79440921 (773429 nodes)
Transitions: 	109963876 (3803440 nodes)
Choices: 	100215175
Reward Models:  none
Variables: 	rows: 15 meta variables (40 DD variables), columns: 15 meta variables (40 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (41 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 53.738s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	79440921
Transitions: 	109963876
Choices: 	100215175
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 3641587 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.100/model.umb'.
Time for model export: 4.248s.


Performance statistics:
  * peak memory usage: 6772MB
  * CPU time: 250.994s
  * wallclock time: 256.267s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.100/model.umb:	Size of output file is 3226472960 bytes
```



### Log file: storm_from-jani_to-umb_cudd_pacman.100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 267.350 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:09 2026
Command line arguments: --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 197.116s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	79440921 (773429 nodes)
Transitions: 	109963876 (3803440 nodes)
Choices: 	100215175
Reward Models:  none
Variables: 	rows: 15 meta variables (40 DD variables), columns: 15 meta variables (40 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (41 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 61.220s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	79440921
Transitions: 	109963876
Choices: 	100215175
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 3641587 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.100/model_rep2.umb'.
Time for model export: 5.066s.


Performance statistics:
  * peak memory usage: 6773MB
  * CPU time: 260.952s
  * wallclock time: 267.265s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.100/model_rep2.umb:	Size of output file is 3226472960 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_pacman.100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 232.207 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:00:53 2026
Command line arguments: --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.019s.

Time for model construction: 170.530s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	79440921 (773429 nodes)
Transitions: 	109963876 (3803440 nodes)
Choices: 	100215175
Reward Models:  none
Variables: 	rows: 15 meta variables (40 DD variables), columns: 15 meta variables (40 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (41 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 53.600s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	79440921
Transitions: 	109963876
Choices: 	100215175
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 3641587 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.100/model_rep3.umb'.
Time for model export: 4.248s.


Performance statistics:
  * peak memory usage: 6773MB
  * CPU time: 226.815s
  * wallclock time: 232.153s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.100/model_rep3.umb:	Size of output file is 3226472960 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_pacman.100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 216.465 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:13:30 2026
Command line arguments: --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.054s.

Time for model construction: 156.165s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	79440921 (773429 nodes)
Transitions: 	109963876 (3803440 nodes)
Choices: 	100215175
Reward Models:  none
Variables: 	rows: 15 meta variables (40 DD variables), columns: 15 meta variables (40 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (41 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 52.394s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	79440921
Transitions: 	109963876
Choices: 	100215175
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 3641587 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.100/model_rep4.umb'.
Time for model export: 4.217s.


Performance statistics:
  * peak memory usage: 6773MB
  * CPU time: 211.411s
  * wallclock time: 216.413s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.100/model_rep4.umb:	Size of output file is 3226472960 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_pacman.100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 297.197 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:30:19 2026
Command line arguments: --timemem --buildfull --jani models/pacman.100/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.100/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.041s.

Time for model construction: 224.202s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	79440921 (773429 nodes)
Transitions: 	109963876 (3803440 nodes)
Choices: 	100215175
Reward Models:  none
Variables: 	rows: 15 meta variables (40 DD variables), columns: 15 meta variables (40 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (41 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 63.363s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	79440921
Transitions: 	109963876
Choices: 	100215175
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 3641587 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.100/model_rep5.umb'.
Time for model export: 5.091s.


Performance statistics:
  * peak memory usage: 6772MB
  * CPU time: 289.165s
  * wallclock time: 297.124s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.100/model_rep5.umb:	Size of output file is 3226472960 bytes
Removing output file to save space for repetition #5
```

