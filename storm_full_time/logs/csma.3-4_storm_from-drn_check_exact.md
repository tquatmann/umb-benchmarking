# Log files

Tool configuration: storm_from-drn_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [5.756, 5.307, 5.189, 6.97, 6.409]



### Log file: storm_from-drn_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.756 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:56:12 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.852s.

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
Time for model checking: 2.771s.

Performance statistics:
  * peak memory usage: 978MB
  * CPU time: 5.313s
  * wallclock time: 5.659s
```



### Log file: storm_from-drn_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.307 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:58:27 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.433s.

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
Time for model checking: 2.730s.

Performance statistics:
  * peak memory usage: 979MB
  * CPU time: 4.861s
  * wallclock time: 5.199s
```



### Log file: storm_from-drn_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 5.189 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:13:24 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.493s.

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
Time for model checking: 2.562s.

Performance statistics:
  * peak memory usage: 978MB
  * CPU time: 4.730s
  * wallclock time: 5.103s
```



### Log file: storm_from-drn_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 6.970 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:02:01 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 3.134s.

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
Time for model checking: 3.630s.

Performance statistics:
  * peak memory usage: 977MB
  * CPU time: 6.250s
  * wallclock time: 6.810s
```



### Log file: storm_from-drn_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Wallclock time: 6.409 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:05 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.3-4/storm.model.exact.drn --digits 17 --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 2.407s.

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
Time for model checking: 2.441s.

Performance statistics:
  * peak memory usage: 978MB
  * CPU time: 4.559s
  * wallclock time: 4.884s
```

