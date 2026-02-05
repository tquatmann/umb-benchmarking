# Log files for storm_from-jani_check_cudd on model [wlan.5-0](../../models/wlan.5-0)

Parsed values: `[2.138, 1.7480000000000002, 2.0869999999999997, 2.089, 1.9449999999999998]`



### Log file: storm_from-jani_check_cudd_wlan.5-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.420 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:28:09 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.007s.

Time for model construction: 0.161s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.970s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.226s.

Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 2.338s
  * wallclock time: 2.375s
```



### Log file: storm_from-jani_check_cudd_wlan.5-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.653 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:47 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 0.125s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.614s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.189s.

Performance statistics:
  * peak memory usage: 198MB
  * CPU time: 1.909s
  * wallclock time: 1.947s
```



### Log file: storm_from-jani_check_cudd_wlan.5-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.386 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.019s.

Time for model construction: 0.154s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.914s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.197s.

Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 2.240s
  * wallclock time: 2.294s
```



### Log file: storm_from-jani_check_cudd_wlan.5-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.388 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:25 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 0.154s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.926s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.198s.

Performance statistics:
  * peak memory usage: 198MB
  * CPU time: 2.259s
  * wallclock time: 2.298s
```



### Log file: storm_from-jani_check_cudd_wlan.5-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.220 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:01:00 2026
Command line arguments: --timemem --buildfull --jani models/wlan.5-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.007s.

Time for model construction: 0.163s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	1295218 (3237 nodes)
Transitions: 	2929960 (19712 nodes)
Choices: 	1646074
Reward Models:  none
Variables: 	rows: 16 meta variables (48 DD variables), columns: 16 meta variables (48 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (49 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.775s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1295218
Transitions: 	2929960
Choices: 	1646074
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.200s.

Performance statistics:
  * peak memory usage: 199MB
  * CPU time: 2.142s
  * wallclock time: 2.156s
```

