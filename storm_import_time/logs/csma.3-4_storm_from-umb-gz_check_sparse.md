# Log files for storm_from-umb-gz_check_sparse on model [csma.3-4](../../models/csma.3-4)

Parsed values: `[0.192, 0.18, 0.218, 0.229, 0.199]`



### Log file: storm_from-umb-gz_check_sparse_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Wallclock time: 1.058 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:46:51 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.139s seconds.
Time for model construction: 0.192s.

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
Time for model checking: 0.816s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 0.947s
  * wallclock time: 1.017s
```



### Log file: storm_from-umb-gz_check_sparse_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Wallclock time: 1.026 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:23:36 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.006s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.136s seconds.
Time for model construction: 0.180s.

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
Time for model checking: 0.809s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 0.923s
  * wallclock time: 0.991s
```



### Log file: storm_from-umb-gz_check_sparse_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Wallclock time: 1.087 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:51:28 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.153s seconds.
Time for model construction: 0.218s.

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
Time for model checking: 0.810s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 0.945s
  * wallclock time: 1.041s
```



### Log file: storm_from-umb-gz_check_sparse_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Wallclock time: 1.417 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:10:45 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.022s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.152s seconds.
Time for model construction: 0.229s.

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
Time for model checking: 1.126s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 1.261s
  * wallclock time: 1.360s
```



### Log file: storm_from-umb-gz_check_sparse_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Wallclock time: 1.004 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:15 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.umb.gz --prop models/csma.3-4/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.141s seconds.
Time for model construction: 0.199s.

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
Time for model checking: 0.738s.

Performance statistics:
  * peak memory usage: 239MB
  * CPU time: 0.864s
  * wallclock time: 0.962s
```

