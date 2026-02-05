# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [csma.3-4](../../models/csma.3-4)
Parsed values: [12.331, 15.092, 13.109, 12.256, 13.73]



### Log file: storm_from-prism_check_exact_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Wallclock time: 12.331 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:43:44 2026
Command line arguments: --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.102s.

Time for model construction: 9.535s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.418s.

Performance statistics:
  * peak memory usage: 990MB
  * CPU time: 11.762s
  * wallclock time: 12.130s
```



### Log file: storm_from-prism_check_exact_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Wallclock time: 15.092 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:28:57 2026
Command line arguments: --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 11.590s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 3.226s.

Performance statistics:
  * peak memory usage: 990MB
  * CPU time: 14.514s
  * wallclock time: 14.909s
```



### Log file: storm_from-prism_check_exact_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Wallclock time: 13.109 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 10.444s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.512s.

Performance statistics:
  * peak memory usage: 990MB
  * CPU time: 12.746s
  * wallclock time: 13.000s
```



### Log file: storm_from-prism_check_exact_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Wallclock time: 12.256 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:06:05 2026
Command line arguments: --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.017s.

Time for model construction: 9.626s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.490s.

Performance statistics:
  * peak memory usage: 990MB
  * CPU time: 11.897s
  * wallclock time: 12.171s
```



### Log file: storm_from-prism_check_exact_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Wallclock time: 13.730 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:25 2026
Command line arguments: --timemem --buildfull --prism models/csma.3-4/model.prism --prismcompat --prop models/csma.3-4/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.007s.

Time for model construction: 10.918s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 2599282671417859453572130598089066646673439/2787593149816327892691964784081045188247552 (approx. 0.9324469288)
Time for model checking: 2.635s.

Performance statistics:
  * peak memory usage: 990MB
  * CPU time: 13.342s
  * wallclock time: 13.602s
```

