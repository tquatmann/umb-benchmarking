# Log files for storm_from-jani_check_cudd on model [zeroconf.1000-8-false](../../models/zeroconf.1000-8-false)

Parsed values: `[18.875, 18.047, 18.028, 28.637, 28.15]`



### Log file: storm_from-jani_check_cudd_zeroconf.1000-8-false_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.875 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:41:07 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 10.532s.

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

Time for model preprocessing: 3.479s.

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

Model checking property "correct_max": Pmax=? [F "target"] ...
Result (for initial states): 4.801413635e-08
Time for model checking: 4.719s.

Performance statistics:
  * peak memory usage: 509MB
  * CPU time: 18.634s
  * wallclock time: 18.827s
```



### Log file: storm_from-jani_check_cudd_zeroconf.1000-8-false_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.047 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:04 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 9.138s.

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

Time for model preprocessing: 3.016s.

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

Model checking property "correct_max": Pmax=? [F "target"] ...
Result (for initial states): 4.801413635e-08
Time for model checking: 4.126s.

Performance statistics:
  * peak memory usage: 508MB
  * CPU time: 16.217s
  * wallclock time: 16.371s
```



### Log file: storm_from-jani_check_cudd_zeroconf.1000-8-false_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.028 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 10.577s.

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

Time for model preprocessing: 3.034s.

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

Model checking property "correct_max": Pmax=? [F "target"] ...
Result (for initial states): 4.801413635e-08
Time for model checking: 4.150s.

Performance statistics:
  * peak memory usage: 496MB
  * CPU time: 17.718s
  * wallclock time: 17.852s
```



### Log file: storm_from-jani_check_cudd_zeroconf.1000-8-false_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 28.637 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:35 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 16.470s.

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

Time for model preprocessing: 3.721s.

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

Model checking property "correct_max": Pmax=? [F "target"] ...
Result (for initial states): 4.801413635e-08
Time for model checking: 8.250s.

Performance statistics:
  * peak memory usage: 500MB
  * CPU time: 28.252s
  * wallclock time: 28.581s
```



### Log file: storm_from-jani_check_cudd_zeroconf.1000-8-false_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 28.150 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:12:14 2026
Command line arguments: --timemem --buildfull --jani models/zeroconf.1000-8-false/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 17.276s.

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

Time for model preprocessing: 3.282s.

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

Model checking property "correct_max": Pmax=? [F "target"] ...
Result (for initial states): 4.801413635e-08
Time for model checking: 7.378s.

Performance statistics:
  * peak memory usage: 500MB
  * CPU time: 27.833s
  * wallclock time: 28.089s
```

