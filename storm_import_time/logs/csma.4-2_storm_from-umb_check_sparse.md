# Log files

Tool configuration: storm_from-umb_check_sparse
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [0.129, 0.107, 0.105, 0.118, 0.118]



### Log file: storm_from-umb_check_sparse_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Wallclock time: 0.586 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:42:42 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.019s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.087s seconds.
Time for model construction: 0.129s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.401s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.423s
  * wallclock time: 0.550s
```



### Log file: storm_from-umb_check_sparse_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Wallclock time: 0.611 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:13:55 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.065s seconds.
Time for model construction: 0.107s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.453s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.483s
  * wallclock time: 0.563s
```



### Log file: storm_from-umb_check_sparse_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Wallclock time: 0.589 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:02:32 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.008s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.073s seconds.
Time for model construction: 0.105s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.432s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.442s
  * wallclock time: 0.552s
```



### Log file: storm_from-umb_check_sparse_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Wallclock time: 0.584 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:34:43 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.019s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.077s seconds.
Time for model construction: 0.118s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.397s.

Performance statistics:
  * peak memory usage: 169MB
  * CPU time: 0.412s
  * wallclock time: 0.541s
```



### Log file: storm_from-umb_check_sparse_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Wallclock time: 0.608 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:30 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.078s seconds.
Time for model construction: 0.118s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.444s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.464s
  * wallclock time: 0.566s
```

