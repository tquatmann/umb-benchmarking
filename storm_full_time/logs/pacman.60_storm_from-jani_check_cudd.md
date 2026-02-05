# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [pacman.60](../../models/pacman.60)
Parsed values: [185.836, 193.156, 167.912, 186.415, 186.095]



### Log file: storm_from-jani_check_cudd_pacman.60_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 185.836 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:18:11 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.096s.

Time for model construction: 132.312s.

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

Time for model preprocessing: 36.143s.

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

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 0.5511074971
Time for model checking: 13.108s.

Performance statistics:
  * peak memory usage: 4375MB
  * CPU time: 183.199s
  * wallclock time: 185.386s
```



### Log file: storm_from-jani_check_cudd_pacman.60_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 193.156 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:20 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 133.024s.

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

Time for model preprocessing: 40.621s.

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

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 0.5511074971
Time for model checking: 14.434s.

Performance statistics:
  * peak memory usage: 4337MB
  * CPU time: 190.439s
  * wallclock time: 192.990s
```



### Log file: storm_from-jani_check_cudd_pacman.60_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 167.912 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:55:19 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 117.748s.

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

Time for model preprocessing: 34.224s.

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

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 0.5511074971
Time for model checking: 11.683s.

Performance statistics:
  * peak memory usage: 4336MB
  * CPU time: 165.891s
  * wallclock time: 167.809s
```



### Log file: storm_from-jani_check_cudd_pacman.60_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 186.415 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:33 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.063s.

Time for model construction: 131.878s.

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

Time for model preprocessing: 37.884s.

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

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 0.5511074971
Time for model checking: 12.382s.

Performance statistics:
  * peak memory usage: 4374MB
  * CPU time: 184.114s
  * wallclock time: 186.336s
```



### Log file: storm_from-jani_check_cudd_pacman.60_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 186.095 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:21 2026
Command line arguments: --timemem --buildfull --jani models/pacman.60/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 133.835s.

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

Time for model preprocessing: 35.039s.

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

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 0.5511074971
Time for model checking: 13.152s.

Performance statistics:
  * peak memory usage: 4336MB
  * CPU time: 184.088s
  * wallclock time: 186.030s
```

