# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [45.16, 51.495, 43.832, 44.476, 56.311]



### Log file: storm_from-jani_check_cudd_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 45.160 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:01:05 2026
Command line arguments: --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.277s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	597012 (130 nodes)
Transitions: 	2908192 (29440 nodes)
Reward Models:  none
Variables: 	rows: 17 meta variables (31 DD variables), columns: 17 meta variables (31 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (32 nodes)
   * minimum
-------------------------------------------------------------- 

Time for model preprocessing: 0.981s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * minimum -> 141117 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": Pmin=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 43.856s.

Performance statistics:
  * peak memory usage: 181MB
  * CPU time: 44.931s
  * wallclock time: 45.123s
```



### Log file: storm_from-jani_check_cudd_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 51.495 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:05:03 2026
Command line arguments: --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 0.252s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	597012 (130 nodes)
Transitions: 	2908192 (29440 nodes)
Reward Models:  none
Variables: 	rows: 17 meta variables (31 DD variables), columns: 17 meta variables (31 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (32 nodes)
   * minimum
-------------------------------------------------------------- 

Time for model preprocessing: 1.046s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * minimum -> 141117 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": Pmin=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 50.121s.

Performance statistics:
  * peak memory usage: 182MB
  * CPU time: 51.224s
  * wallclock time: 51.449s
```



### Log file: storm_from-jani_check_cudd_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 43.832 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:19 2026
Command line arguments: --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 0.227s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	597012 (130 nodes)
Transitions: 	2908192 (29440 nodes)
Reward Models:  none
Variables: 	rows: 17 meta variables (31 DD variables), columns: 17 meta variables (31 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (32 nodes)
   * minimum
-------------------------------------------------------------- 

Time for model preprocessing: 0.960s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * minimum -> 141117 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": Pmin=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 42.578s.

Performance statistics:
  * peak memory usage: 182MB
  * CPU time: 43.669s
  * wallclock time: 43.797s
```



### Log file: storm_from-jani_check_cudd_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 44.476 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:08:38 2026
Command line arguments: --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 0.280s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	597012 (130 nodes)
Transitions: 	2908192 (29440 nodes)
Reward Models:  none
Variables: 	rows: 17 meta variables (31 DD variables), columns: 17 meta variables (31 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (32 nodes)
   * minimum
-------------------------------------------------------------- 

Time for model preprocessing: 0.968s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * minimum -> 141117 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": Pmin=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 43.164s.

Performance statistics:
  * peak memory usage: 182MB
  * CPU time: 44.229s
  * wallclock time: 44.436s
```



### Log file: storm_from-jani_check_cudd_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 56.311 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:10 2026
Command line arguments: --timemem --buildfull --jani models/cluster.128-2000-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 0.294s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	597012 (130 nodes)
Transitions: 	2908192 (29440 nodes)
Reward Models:  none
Variables: 	rows: 17 meta variables (31 DD variables), columns: 17 meta variables (31 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (32 nodes)
   * minimum
-------------------------------------------------------------- 

Time for model preprocessing: 1.128s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * minimum -> 141117 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": Pmin=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 51.494s.

Performance statistics:
  * peak memory usage: 181MB
  * CPU time: 52.660s
  * wallclock time: 52.930s
```

