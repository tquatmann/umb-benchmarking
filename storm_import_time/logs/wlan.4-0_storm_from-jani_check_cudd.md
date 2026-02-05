# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [wlan.4-0](../../models/wlan.4-0)
Parsed values: [0.662, 0.562, 0.655, 0.7739999999999999, 0.558]



### Log file: storm_from-jani_check_cudd_wlan.4-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.798 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:25:33 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.029s.

Time for model construction: 0.125s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.508s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.052s.

Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.695s
  * wallclock time: 0.723s
```



### Log file: storm_from-jani_check_cudd_wlan.4-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.661 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.096s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.461s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.041s.

Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.610s
  * wallclock time: 0.611s
```



### Log file: storm_from-jani_check_cudd_wlan.4-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.753 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:10:40 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.109s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.541s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.044s.

Performance statistics:
  * peak memory usage: 97MB
  * CPU time: 0.695s
  * wallclock time: 0.707s
```



### Log file: storm_from-jani_check_cudd_wlan.4-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.909 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:13:19 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 0.174s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.574s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.065s.

Performance statistics:
  * peak memory usage: 97MB
  * CPU time: 0.831s
  * wallclock time: 0.849s
```



### Log file: storm_from-jani_check_cudd_wlan.4-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.226 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:46 2026
Command line arguments: --timemem --buildfull --jani models/wlan.4-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 0.092s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	345000 (2819 nodes)
Transitions: 	762252 (15964 nodes)
Choices: 	440206
Reward Models:  none
Variables: 	rows: 16 meta variables (46 DD variables), columns: 16 meta variables (46 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (47 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.450s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	345000
Transitions: 	762252
Choices: 	440206
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.039s.

Performance statistics:
  * peak memory usage: 98MB
  * CPU time: 0.584s
  * wallclock time: 0.606s
```

