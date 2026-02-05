# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [csma.4-2](../../models/csma.4-2)
Parsed values: [3.367, 2.899, 5.145, 4.723, 4.549]



### Log file: storm_from-jani_check_cudd_csma.4-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.367 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:43:44 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 1.716s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.898s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.523s.

Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 3.247s
  * wallclock time: 3.318s
```



### Log file: storm_from-jani_check_cudd_csma.4-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.899 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:19 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.014s.

Time for model construction: 1.176s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.000s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.493s.

Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.784s
  * wallclock time: 2.834s
```



### Log file: storm_from-jani_check_cudd_csma.4-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 5.145 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:05 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 1.153s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.988s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.480s.

Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 2.720s
  * wallclock time: 2.775s
```



### Log file: storm_from-jani_check_cudd_csma.4-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.723 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 1.689s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 0.898s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.538s.

Performance statistics:
  * peak memory usage: 247MB
  * CPU time: 3.230s
  * wallclock time: 3.285s
```



### Log file: storm_from-jani_check_cudd_csma.4-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.549 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:53:00 2026
Command line arguments: --timemem --buildfull --jani models/csma.4-2/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.017s.

Time for model construction: 2.388s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	761962 (17838 nodes)
Transitions: 	1327068 (122419 nodes)
Choices: 	825504
Reward Models:  none
Variables: 	rows: 24 meta variables (59 DD variables), columns: 24 meta variables (59 DD variables), nondeterminism: 16 meta variables (16 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (60 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.138s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	761962
Transitions: 	1327068
Choices: 	825504
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 3444 item(s)
   * all_delivered -> 9 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.7764601493
Time for model checking: 0.755s.

Performance statistics:
  * peak memory usage: 246MB
  * CPU time: 4.390s
  * wallclock time: 4.489s
```

