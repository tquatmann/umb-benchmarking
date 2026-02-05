# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [eajs.5-250-11](../../models/eajs.5-250-11)
Parsed values: [10.231, 8.68, 8.653, 10.294, 8.565]



### Log file: storm_from-jani_check_cudd_eajs.5-250-11_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.231 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:02:37 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.201s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 9.168s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): inf
Time for model checking: 0.775s.

Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 10.053s
  * wallclock time: 10.177s
```



### Log file: storm_from-jani_check_cudd_eajs.5-250-11_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.680 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:59 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 0.127s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 7.924s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): inf
Time for model checking: 0.544s.

Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 8.538s
  * wallclock time: 8.640s
```



### Log file: storm_from-jani_check_cudd_eajs.5-250-11_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.653 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:54 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.029s.

Time for model construction: 0.124s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 7.811s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): inf
Time for model checking: 0.500s.

Performance statistics:
  * peak memory usage: 449MB
  * CPU time: 8.374s
  * wallclock time: 8.484s
```



### Log file: storm_from-jani_check_cudd_eajs.5-250-11_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.294 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:07:08 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.191s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 9.303s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): inf
Time for model checking: 0.713s.

Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 10.134s
  * wallclock time: 10.239s
```



### Log file: storm_from-jani_check_cudd_eajs.5-250-11_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 8.565 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:01 2026
Command line arguments: --timemem --buildfull --jani models/eajs.5-250-11/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.015s.

Time for model construction: 0.154s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	3049471 (3317 nodes)
Transitions: 	6977654 (27034 nodes)
Choices: 	4256193
Reward Models:  utilityLocal
Variables: 	rows: 21 meta variables (50 DD variables), columns: 21 meta variables (50 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 7.739s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4371481
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): inf
Time for model checking: 0.502s.

Performance statistics:
  * peak memory usage: 450MB
  * CPU time: 8.332s
  * wallclock time: 8.434s
```

