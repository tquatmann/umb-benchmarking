# Log files for storm_from-umb-gz_check_sparse on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[0.181, 0.151, 0.146, 0.162, 0.146]`



### Log file: storm_from-umb-gz_check_sparse_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Wallclock time: 0.666 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:41:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.037s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.120s seconds.
Time for model construction: 0.181s.

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
Time for model checking: 0.433s.

Performance statistics:
  * peak memory usage: 169MB
  * CPU time: 0.503s
  * wallclock time: 0.629s
```



### Log file: storm_from-umb-gz_check_sparse_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Wallclock time: 0.716 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:50:56 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.025s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.100s seconds.
Time for model construction: 0.151s.

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
Time for model checking: 0.507s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.585s
  * wallclock time: 0.663s
```



### Log file: storm_from-umb-gz_check_sparse_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Wallclock time: 0.647 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:06:06 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.023s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.099s seconds.
Time for model construction: 0.146s.

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
Time for model checking: 0.433s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.527s
  * wallclock time: 0.602s
```



### Log file: storm_from-umb-gz_check_sparse_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Wallclock time: 1.061 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:49:24 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.022s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.103s seconds.
Time for model construction: 0.162s.

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
Time for model checking: 0.833s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.890s
  * wallclock time: 1.014s
```



### Log file: storm_from-umb-gz_check_sparse_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Wallclock time: 0.668 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.gz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.025s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.095s seconds.
Time for model construction: 0.146s.

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
  * peak memory usage: 169MB
  * CPU time: 0.532s
  * wallclock time: 0.606s
```

