# Log files for storm_from-jani_check_cudd on model [kanban.5](../../models/kanban.5)

Parsed values: `[9.357000000000001, 8.887, 8.584000000000001, 9.293, 9.568]`



### Log file: storm_from-jani_check_cudd_kanban.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 17.855 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:44:46 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.052s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 9.303s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.3071249629
Time for model checking: 8.443s.

Performance statistics:
  * peak memory usage: 2920MB
  * CPU time: 17.290s
  * wallclock time: 17.807s
```



### Log file: storm_from-jani_check_cudd_kanban.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.754 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:05:34 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 0.048s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 8.817s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.3071249629
Time for model checking: 9.813s.

Performance statistics:
  * peak memory usage: 2918MB
  * CPU time: 18.002s
  * wallclock time: 18.710s
```



### Log file: storm_from-jani_check_cudd_kanban.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 17.226 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:11 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 0.046s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 8.515s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.3071249629
Time for model checking: 8.588s.

Performance statistics:
  * peak memory usage: 2920MB
  * CPU time: 16.649s
  * wallclock time: 17.180s
```



### Log file: storm_from-jani_check_cudd_kanban.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.018 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:21 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.046s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 9.245s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.3071249629
Time for model checking: 8.678s.

Performance statistics:
  * peak memory usage: 2920MB
  * CPU time: 17.468s
  * wallclock time: 17.980s
```



### Log file: storm_from-jani_check_cudd_kanban.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 19.138 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:28:43 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.055s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 9.510s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "throughput": R{"throughput"}min=? [LRA] ...
Result (for initial states): 0.3071249629
Time for model checking: 9.514s.

Performance statistics:
  * peak memory usage: 2920MB
  * CPU time: 18.530s
  * wallclock time: 19.089s
```

