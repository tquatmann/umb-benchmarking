# Log files

Tool configuration: storm_from-umb-gz_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [1.141, 1.349, 1.147, 1.165, 1.185]



### Log file: storm_from-umb-gz_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Wallclock time: 4.065 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:20:45 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.002s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.144s seconds.
Time for model construction: 1.141s.

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
Time for model checking: 2.779s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.705s
  * wallclock time: 3.959s
```



### Log file: storm_from-umb-gz_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Wallclock time: 4.295 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.007s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.172s seconds.
Time for model construction: 1.349s.

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
Time for model checking: 2.741s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.847s
  * wallclock time: 4.133s
```



### Log file: storm_from-umb-gz_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Wallclock time: 3.971 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:03 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.008s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.138s seconds.
Time for model construction: 1.147s.

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
Time for model checking: 2.694s.

Performance statistics:
  * peak memory usage: 971MB
  * CPU time: 3.618s
  * wallclock time: 3.878s
```



### Log file: storm_from-umb-gz_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Wallclock time: 3.857 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:21:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.010s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.150s seconds.
Time for model construction: 1.165s.

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
Time for model checking: 2.550s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.502s
  * wallclock time: 3.763s
```



### Log file: storm_from-umb-gz_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Wallclock time: 3.990 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:04:02 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.3-4/storm.model.exact.umb.gz --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.006s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.146s seconds.
Time for model construction: 1.185s.

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
Time for model checking: 2.676s.

Performance statistics:
  * peak memory usage: 972MB
  * CPU time: 3.635s
  * wallclock time: 3.899s
```

