# Log files

Tool configuration: storm_from-umb-xz_check_sparse
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [1.185, 1.208, 1.245, 3.84, 1.252]



### Log file: storm_from-umb-xz_check_sparse_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Wallclock time: 1.185 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:33:19 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.019s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.256s seconds.
Time for model construction: 0.313s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.819s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 1.068s
  * wallclock time: 1.144s
```



### Log file: storm_from-umb-xz_check_sparse_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Wallclock time: 1.208 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.007s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.295s seconds.
Time for model construction: 0.344s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.820s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 1.105s
  * wallclock time: 1.168s
```



### Log file: storm_from-umb-xz_check_sparse_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Wallclock time: 1.245 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:54:30 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.280s seconds.
Time for model construction: 0.344s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.863s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 1.115s
  * wallclock time: 1.209s
```



### Log file: storm_from-umb-xz_check_sparse_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Wallclock time: 3.840 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:05:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 1.112s seconds.
Time for model construction: 1.282s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 2.431s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 3.601s
  * wallclock time: 3.721s
```



### Log file: storm_from-umb-xz_check_sparse_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Wallclock time: 1.252 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:58:26 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.xz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.023s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.248s seconds.
Time for model construction: 0.309s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.781s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 1.022s
  * wallclock time: 1.094s
```

