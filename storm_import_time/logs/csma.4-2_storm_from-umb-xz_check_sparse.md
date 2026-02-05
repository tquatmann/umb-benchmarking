# Log files for storm_from-umb-xz_check_sparse on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[0.233, 0.23, 0.221, 0.23, 0.217]`



### Log file: storm_from-umb-xz_check_sparse_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Wallclock time: 0.864 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:42:42 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.025s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.181s seconds.
Time for model construction: 0.233s.

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
Time for model checking: 0.563s.

Performance statistics:
  * peak memory usage: 169MB
  * CPU time: 0.739s
  * wallclock time: 0.800s
```



### Log file: storm_from-umb-xz_check_sparse_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Wallclock time: 0.730 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.023s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.182s seconds.
Time for model construction: 0.230s.

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
  * CPU time: 0.612s
  * wallclock time: 0.682s
```



### Log file: storm_from-umb-xz_check_sparse_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Wallclock time: 0.761 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:06:38 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.016s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.181s seconds.
Time for model construction: 0.221s.

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
Time for model checking: 0.493s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.656s
  * wallclock time: 0.717s
```



### Log file: storm_from-umb-xz_check_sparse_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Wallclock time: 0.727 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.027s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.181s seconds.
Time for model construction: 0.230s.

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
Time for model checking: 0.441s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.609s
  * wallclock time: 0.686s
```



### Log file: storm_from-umb-xz_check_sparse_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Wallclock time: 0.788 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:24 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.umb.xz --prop models/csma.4-2/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.016s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.179s seconds.
Time for model construction: 0.217s.

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
Time for model checking: 0.410s.

Performance statistics:
  * peak memory usage: 170MB
  * CPU time: 0.568s
  * wallclock time: 0.641s
```

