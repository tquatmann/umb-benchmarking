# Log files

Tool configuration: storm_from-drn-xz_check_exact
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [3.529, 3.458, 4.357, 3.629, 3.416]



### Log file: storm_from-drn-xz_check_exact_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.529 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:21:50 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.633s.

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
Time for model checking: 1.790s.

Performance statistics:
  * peak memory usage: 637MB
  * CPU time: 3.242s
  * wallclock time: 3.458s
```



### Log file: storm_from-drn-xz_check_exact_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.458 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:17:59 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
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
Time for model checking: 1.612s.

Performance statistics:
  * peak memory usage: 637MB
  * CPU time: 3.198s
  * wallclock time: 3.390s
```



### Log file: storm_from-drn-xz_check_exact_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 4.357 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:57:24 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.911s.

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
Time for model checking: 2.033s.

Performance statistics:
  * peak memory usage: 638MB
  * CPU time: 3.770s
  * wallclock time: 3.989s
```



### Log file: storm_from-drn-xz_check_exact_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.629 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:22 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.757s.

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
Time for model checking: 1.784s.

Performance statistics:
  * peak memory usage: 637MB
  * CPU time: 3.369s
  * wallclock time: 3.563s
```



### Log file: storm_from-drn-xz_check_exact_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Wallclock time: 3.416 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:03:30 2026
Command line arguments: --timemem --buildfull --explicit-drn models/csma.4-2/storm.model.exact.drn.xz --digits 17 --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 1.640s.

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
Time for model checking: 1.674s.

Performance statistics:
  * peak memory usage: 638MB
  * CPU time: 3.151s
  * wallclock time: 3.353s
```

