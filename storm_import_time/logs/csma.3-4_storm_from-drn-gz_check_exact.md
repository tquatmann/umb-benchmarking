# Log files

Tool configuration: storm_from-drn-gz_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [2.639, 2.504, 2.939, 2.454, 2.664]



### Log file: storm_from-drn-gz_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.273 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:19:13 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.639s.

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
Time for model checking: 2.500s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 4.895s
  * wallclock time: 5.193s
```



### Log file: storm_from-drn-gz_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.419 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:12:45 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.504s.

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
Time for model checking: 2.773s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.001s
  * wallclock time: 5.331s
```



### Log file: storm_from-drn-gz_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.689 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:22:07 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.939s.

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
Time for model checking: 2.556s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.234s
  * wallclock time: 5.532s
```



### Log file: storm_from-drn-gz_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.000 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:57:25 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.454s.

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
Time for model checking: 2.435s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 4.663s
  * wallclock time: 4.922s
```



### Log file: storm_from-drn-gz_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.503 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:03 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn.gz --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.664s.

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
Time for model checking: 2.656s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 5.049s
  * wallclock time: 5.356s
```

