# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [5.779999999999999, 5.6419999999999995, 6.471, 5.73, 5.729]



### Log file: storm_from-prism_check_exact_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Wallclock time: 7.576 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:57:13 2026
Command line arguments: --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 5.757s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.688s.

Performance statistics:
  * peak memory usage: 653MB
  * CPU time: 7.304s
  * wallclock time: 7.500s
```



### Log file: storm_from-prism_check_exact_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Wallclock time: 7.336 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:31 2026
Command line arguments: --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 5.637s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.598s.

Performance statistics:
  * peak memory usage: 652MB
  * CPU time: 7.119s
  * wallclock time: 7.264s
```



### Log file: storm_from-prism_check_exact_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Wallclock time: 8.385 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:26:40 2026
Command line arguments: --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 6.466s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.806s.

Performance statistics:
  * peak memory usage: 652MB
  * CPU time: 8.148s
  * wallclock time: 8.301s
```



### Log file: storm_from-prism_check_exact_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Wallclock time: 7.815 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:55:31 2026
Command line arguments: --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 5.721s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.954s.

Performance statistics:
  * peak memory usage: 651MB
  * CPU time: 7.464s
  * wallclock time: 7.743s
```



### Log file: storm_from-prism_check_exact_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Wallclock time: 7.493 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:11:45 2026
Command line arguments: --timemem --buildfull --prism models/csma.4-2/model.prism --prismcompat --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.015s.

Time for model construction: 5.714s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.668s.

Performance statistics:
  * peak memory usage: 653MB
  * CPU time: 7.278s
  * wallclock time: 7.431s
```

