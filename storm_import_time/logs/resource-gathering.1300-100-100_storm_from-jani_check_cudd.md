# Log files for storm_from-jani_check_cudd on model [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)

Parsed values: `[1.233, 1.165, 1.241, 1.164, 1.451]`



### Log file: storm_from-jani_check_cudd_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 21.328 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:27:06 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 0.214s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 0.993s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true Usteps<=1300 "success"] ...
Result (for initial states): 0.6630608525
Time for model checking: 20.052s.

Performance statistics:
  * peak memory usage: 382MB
  * CPU time: 21.156s
  * wallclock time: 21.290s
```



### Log file: storm_from-jani_check_cudd_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 19.934 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:03 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.187s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 0.973s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true Usteps<=1300 "success"] ...
Result (for initial states): 0.6630608525
Time for model checking: 18.634s.

Performance statistics:
  * peak memory usage: 383MB
  * CPU time: 19.704s
  * wallclock time: 19.804s
```



### Log file: storm_from-jani_check_cudd_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 21.378 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:18:00 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 0.209s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.004s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true Usteps<=1300 "success"] ...
Result (for initial states): 0.6630608525
Time for model checking: 20.082s.

Performance statistics:
  * peak memory usage: 382MB
  * CPU time: 21.215s
  * wallclock time: 21.328s
```



### Log file: storm_from-jani_check_cudd_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 19.551 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:09:43 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.188s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 0.973s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true Usteps<=1300 "success"] ...
Result (for initial states): 0.6630608525
Time for model checking: 18.345s.

Performance statistics:
  * peak memory usage: 383MB
  * CPU time: 19.394s
  * wallclock time: 19.515s
```



### Log file: storm_from-jani_check_cudd_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 31.085 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:20:33 2026
Command line arguments: --timemem --buildfull --jani models/resource-gathering.1300-100-100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.029s.

Time for model construction: 0.329s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	958894 (53 nodes)
Transitions: 	3325526 (701 nodes)
Choices: 	3080702
Reward Models:  none
Variables: 	rows: 10 meta variables (26 DD variables), columns: 10 meta variables (26 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (27 nodes)
   * success
-------------------------------------------------------------- 

Time for model preprocessing: 1.093s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true Usteps<=1300 "success"] ...
Result (for initial states): 0.6630608525
Time for model checking: 29.575s.

Performance statistics:
  * peak memory usage: 383MB
  * CPU time: 30.823s
  * wallclock time: 31.031s
```

