# Log files

Tool configuration: storm_from-drn_check_exact
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [1.539, 1.714, 1.488, 1.477, 1.66]



### Log file: storm_from-drn_check_exact_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.270 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:52:02 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.539s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 9 item(s)
   * collision_max_backoff -> 3444 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.630s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 2.952s
  * wallclock time: 3.198s
```



### Log file: storm_from-drn_check_exact_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.751 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:57:23 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.714s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 9 item(s)
   * collision_max_backoff -> 3444 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.927s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 3.423s
  * wallclock time: 3.666s
```



### Log file: storm_from-drn_check_exact_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 5.533 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:04 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.488s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 9 item(s)
   * collision_max_backoff -> 3444 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.596s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 2.897s
  * wallclock time: 3.105s
```



### Log file: storm_from-drn_check_exact_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.161 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:55:20 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.477s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 9 item(s)
   * collision_max_backoff -> 3444 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.599s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 2.881s
  * wallclock time: 3.098s
```



### Log file: storm_from-drn_check_exact_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.637 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:52:16 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.660s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	3 labels
   * all_delivered -> 9 item(s)
   * collision_max_backoff -> 3444 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.870s.

Performance statistics:
  * peak memory usage: 639MB
  * CPU time: 3.294s
  * wallclock time: 3.559s
```

