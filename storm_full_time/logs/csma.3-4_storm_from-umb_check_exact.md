# Log files

Tool configuration: storm_from-umb_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [3.734, 4.052, 3.903, 4.33, 4.494]



### Log file: storm_from-umb_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Wallclock time: 3.734 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:54:38 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.077s seconds.
Time for model construction: 1.110s.

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
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.486s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.323s
  * wallclock time: 3.643s
```



### Log file: storm_from-umb_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Wallclock time: 4.052 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:55 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.025s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.137s seconds.
Time for model construction: 1.257s.

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
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.659s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.577s
  * wallclock time: 3.955s
```



### Log file: storm_from-umb_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Wallclock time: 3.903 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:19 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.011s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.057s seconds.
Time for model construction: 1.058s.

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
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.702s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.545s
  * wallclock time: 3.797s
```



### Log file: storm_from-umb_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Wallclock time: 4.330 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:57:53 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.019s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.103s seconds.
Time for model construction: 1.249s.

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
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.936s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.885s
  * wallclock time: 4.229s
```



### Log file: storm_from-umb_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Wallclock time: 4.494 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.086s seconds.
Time for model construction: 1.317s.

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
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 3.039s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 4.049s
  * wallclock time: 4.397s
```

