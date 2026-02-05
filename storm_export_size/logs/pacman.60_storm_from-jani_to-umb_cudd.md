# Log files for storm_from-jani_to-umb_cudd on model [pacman.60](../../models/pacman.60)

Parsed values: `[1574630912.0, 1574630912.0, 1574630912.0, 1574630912.0, 1574630912.0]`



### Log file: storm_from-jani_to-umb_cudd_pacman.60_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 141.721 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:36:11 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 97.589s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	38786521 (736888 nodes)
Transitions: 	53648196 (3546225 nodes)
Choices: 	48926255
Reward Models:  none
Variables: 	rows: 15 meta variables (39 DD variables), columns: 15 meta variables (39 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (40 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 37.792s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 1819987 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.60/model.umb'.
Time for model export: 2.562s.


Performance statistics:
  * peak memory usage: 3587MB
  * CPU time: 138.776s
  * wallclock time: 141.679s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.60/model.umb:	Size of output file is 1574630912 bytes
```



### Log file: storm_from-jani_to-umb_cudd_pacman.60_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 206.462 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:35:35 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.052s.

Time for model construction: 155.666s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	38786521 (736888 nodes)
Transitions: 	53648196 (3546225 nodes)
Choices: 	48926255
Reward Models:  none
Variables: 	rows: 15 meta variables (39 DD variables), columns: 15 meta variables (39 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (40 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 42.620s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 1819987 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.60/model_rep2.umb'.
Time for model export: 2.886s.


Performance statistics:
  * peak memory usage: 3586MB
  * CPU time: 202.014s
  * wallclock time: 206.403s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.60/model_rep2.umb:	Size of output file is 1574630912 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_pacman.60_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 138.140 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:39 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 97.249s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	38786521 (736888 nodes)
Transitions: 	53648196 (3546225 nodes)
Choices: 	48926255
Reward Models:  none
Variables: 	rows: 15 meta variables (39 DD variables), columns: 15 meta variables (39 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (40 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 34.767s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 1819987 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.60/model_rep3.umb'.
Time for model export: 2.359s.


Performance statistics:
  * peak memory usage: 3587MB
  * CPU time: 135.165s
  * wallclock time: 138.086s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.60/model_rep3.umb:	Size of output file is 1574630912 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_pacman.60_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 127.413 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:27:14 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.020s.

Time for model construction: 90.532s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	38786521 (736888 nodes)
Transitions: 	53648196 (3546225 nodes)
Choices: 	48926255
Reward Models:  none
Variables: 	rows: 15 meta variables (39 DD variables), columns: 15 meta variables (39 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (40 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 31.049s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 1819987 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.60/model_rep4.umb'.
Time for model export: 2.275s.


Performance statistics:
  * peak memory usage: 3587MB
  * CPU time: 124.412s
  * wallclock time: 127.341s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.60/model_rep4.umb:	Size of output file is 1574630912 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_pacman.60_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 210.235 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:41:38 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/pacman.60/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 160.562s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	38786521 (736888 nodes)
Transitions: 	53648196 (3546225 nodes)
Choices: 	48926255
Reward Models:  none
Variables: 	rows: 15 meta variables (39 DD variables), columns: 15 meta variables (39 DD variables), nondeterminism: 9 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (40 nodes)
   * Crash
-------------------------------------------------------------- 

Time for model preprocessing: 41.756s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * Crash -> 1819987 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/pacman.60/model_rep5.umb'.
Time for model export: 2.811s.


Performance statistics:
  * peak memory usage: 3587MB
  * CPU time: 206.116s
  * wallclock time: 210.180s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/pacman.60/model_rep5.umb:	Size of output file is 1574630912 bytes
Removing output file to save space for repetition #5
```

