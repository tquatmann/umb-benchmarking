# Log files

Tool configuration: storm_from-drn-xz_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [5.358, 5.568, 6.511, 5.127, 6.464]



### Log file: storm_from-drn-xz_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.358 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:22:26 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.581s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 13 item(s)
   * collision_max_backoff -> 1427 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.648s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.018s
  * wallclock time: 5.264s
```



### Log file: storm_from-drn-xz_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.568 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:54:00 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.717s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 13 item(s)
   * collision_max_backoff -> 1427 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.711s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.159s
  * wallclock time: 5.474s
```



### Log file: storm_from-drn-xz_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 6.511 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:04:03 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.775s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 13 item(s)
   * collision_max_backoff -> 1427 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 3.575s.

Performance statistics:
  * peak memory usage: 978MB
  * CPU time: 5.977s
  * wallclock time: 6.413s
```



### Log file: storm_from-drn-xz_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.127 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:05:05 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.586s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 13 item(s)
   * collision_max_backoff -> 1427 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.424s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 4.814s
  * wallclock time: 5.044s
```



### Log file: storm_from-drn-xz_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 6.464 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:58:25 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.xz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 3.082s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 13 item(s)
   * collision_max_backoff -> 1427 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 3.078s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.905s
  * wallclock time: 6.202s
```

