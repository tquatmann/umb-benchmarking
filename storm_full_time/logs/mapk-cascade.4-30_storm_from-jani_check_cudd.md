# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [mapk-cascade.4-30](../../models/mapk-cascade.4-30)
Parsed values: [26.378, 22.463, 28.556, 27.712, 26.654]



### Log file: storm_from-jani_check_cudd_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 26.378 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:45:17 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 4.162s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 20.954s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "activated_time": R{"time"}min=? [F "target"] ...
Result (for initial states): inf
Time for model checking: 1.169s.

Performance statistics:
  * peak memory usage: 1128MB
  * CPU time: 26.028s
  * wallclock time: 26.331s
```



### Log file: storm_from-jani_check_cudd_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 22.463 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:09:09 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.030s.

Time for model construction: 3.310s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 17.716s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "activated_time": R{"time"}min=? [F "target"] ...
Result (for initial states): inf
Time for model checking: 1.163s.

Performance statistics:
  * peak memory usage: 1129MB
  * CPU time: 21.977s
  * wallclock time: 22.238s
```



### Log file: storm_from-jani_check_cudd_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 28.556 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:26:09 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 5.382s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 21.458s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "activated_time": R{"time"}min=? [F "target"] ...
Result (for initial states): inf
Time for model checking: 1.591s.

Performance statistics:
  * peak memory usage: 1128MB
  * CPU time: 28.065s
  * wallclock time: 28.482s
```



### Log file: storm_from-jani_check_cudd_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 27.712 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:01 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 4.381s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 21.911s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "activated_time": R{"time"}min=? [F "target"] ...
Result (for initial states): inf
Time for model checking: 1.321s.

Performance statistics:
  * peak memory usage: 1128MB
  * CPU time: 27.276s
  * wallclock time: 27.659s
```



### Log file: storm_from-jani_check_cudd_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 26.654 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:04 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 3.825s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 21.582s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "activated_time": R{"time"}min=? [F "target"] ...
Result (for initial states): inf
Time for model checking: 1.125s.

Performance statistics:
  * peak memory usage: 1128MB
  * CPU time: 26.264s
  * wallclock time: 26.559s
```

