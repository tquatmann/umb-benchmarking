# Log files for storm_from-umb_check_exact on model [csma.4-2](../../models/csma.4-2)

Parsed values: `[2.659, 2.573, 2.559, 2.514, 2.681]`



### Log file: storm_from-umb_check_exact_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Wallclock time: 2.659 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:26:36 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.010s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.094s seconds.
Time for model construction: 0.762s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.787s.

Performance statistics:
  * peak memory usage: 635MB
  * CPU time: 2.360s
  * wallclock time: 2.586s
```



### Log file: storm_from-umb_check_exact_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Wallclock time: 2.573 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:01:00 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.070s seconds.
Time for model construction: 0.702s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.740s.

Performance statistics:
  * peak memory usage: 634MB
  * CPU time: 2.265s
  * wallclock time: 2.501s
```



### Log file: storm_from-umb_check_exact_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Wallclock time: 2.559 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:34 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.004s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.069s seconds.
Time for model construction: 0.640s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.764s.

Performance statistics:
  * peak memory usage: 634MB
  * CPU time: 2.221s
  * wallclock time: 2.429s
```



### Log file: storm_from-umb_check_exact_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Wallclock time: 2.514 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:55:19 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.005s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.077s seconds.
Time for model construction: 0.704s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.707s.

Performance statistics:
  * peak memory usage: 635MB
  * CPU time: 2.203s
  * wallclock time: 2.444s
```



### Log file: storm_from-umb_check_exact_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Wallclock time: 2.681 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:04:03 2026
Command line arguments: --timemem --buildfull --explicit-umb models/csma.4-2/storm.model.exact.umb --prop models/csma.4-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.007s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.095s seconds.
Time for model construction: 0.759s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 283699444885771093844545259966420317194574918841/365375409332725729550921208179070754913983135744 (approx. 0.7764601493)
Time for model checking: 1.821s.

Performance statistics:
  * peak memory usage: 635MB
  * CPU time: 2.373s
  * wallclock time: 2.604s
```

