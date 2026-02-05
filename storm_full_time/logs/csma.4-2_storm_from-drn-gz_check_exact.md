# Log files for storm_from-drn-gz_check_exact on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[3.548, 12.818, 3.621, 3.902, 4.504]`



### Log file: storm_from-drn-gz_check_exact_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.548 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:45:17 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.708s.

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
Time for model checking: 1.746s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 3.276s
  * wallclock time: 3.477s
```



### Log file: storm_from-drn-gz_check_exact_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 12.818 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:19 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 6.812s.

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
Time for model checking: 5.701s.

Performance statistics:
  * peak memory usage: 639MB
  * CPU time: 12.008s
  * wallclock time: 12.594s
```



### Log file: storm_from-drn-gz_check_exact_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.621 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.728s.

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
Time for model checking: 1.767s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 3.303s
  * wallclock time: 3.519s
```



### Log file: storm_from-drn-gz_check_exact_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.902 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:11:52 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.754s.

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
Time for model checking: 2.032s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 3.578s
  * wallclock time: 3.813s
```



### Log file: storm_from-drn-gz_check_exact_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 4.504 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:08 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.gz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.489s.

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
Time for model checking: 1.600s.

Performance statistics:
  * peak memory usage: 640MB
  * CPU time: 2.946s
  * wallclock time: 3.110s
```

