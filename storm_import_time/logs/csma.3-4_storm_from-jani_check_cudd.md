# Log files for storm_from-jani_check_cudd on model [csma.3-4](../../models/csma.3-4)

Parsed values: `[2.02, 1.82, 2.6310000000000002, 1.884, 1.693]`



### Log file: storm_from-jani_check_cudd_csma.3-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.963 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:50:59 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 0.642s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.351s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.821s.

Performance statistics:
  * peak memory usage: 241MB
  * CPU time: 2.860s
  * wallclock time: 2.923s
```



### Log file: storm_from-jani_check_cudd_csma.3-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.728 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:29 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.636s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.181s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.789s.

Performance statistics:
  * peak memory usage: 241MB
  * CPU time: 2.643s
  * wallclock time: 2.690s
```



### Log file: storm_from-jani_check_cudd_csma.3-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.810 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:32 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 1.214s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.413s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 1.018s.

Performance statistics:
  * peak memory usage: 241MB
  * CPU time: 3.698s
  * wallclock time: 3.757s
```



### Log file: storm_from-jani_check_cudd_csma.3-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.818 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:57 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.614s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.266s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.816s.

Performance statistics:
  * peak memory usage: 240MB
  * CPU time: 2.736s
  * wallclock time: 2.778s
```



### Log file: storm_from-jani_check_cudd_csma.3-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.540 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:17 2026
Command line arguments: --timemem --buildfull --jani models/csma.3-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.542s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1460287 (24552 nodes)
Transitions: 	2396727 (113363 nodes)
Choices: 	1471059
Reward Models:  none
Variables: 	rows: 19 meta variables (55 DD variables), columns: 19 meta variables (55 DD variables), nondeterminism: 13 meta variables (13 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (56 nodes)
   * all_delivered
   * collision_max_backoff
-------------------------------------------------------------- 

Time for model preprocessing: 1.148s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1460287
Transitions: 	2396727
Choices: 	1471059
Reward Models:  none
State Labels: 	4 labels
   * collision_max_backoff -> 1427 item(s)
   * all_delivered -> 13 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "all_before_max": Pmax=? [(!"collision_max_backoff") U "all_delivered"] ...
Result (for initial states): 0.9324469288
Time for model checking: 0.736s.

Performance statistics:
  * peak memory usage: 241MB
  * CPU time: 2.466s
  * wallclock time: 2.500s
```

