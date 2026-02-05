# Log files for storm_from-jani_check_cudd on model [wlan.6-0](../../models/wlan.6-0)

Parsed values: `[7.234, 7.16, 9.089, 7.445, 7.6]`



### Log file: storm_from-jani_check_cudd_wlan.6-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.234 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:26:34 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.032s.

Time for model construction: 0.214s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.128s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.801s.

Performance statistics:
  * peak memory usage: 593MB
  * CPU time: 7.009s
  * wallclock time: 7.196s
```



### Log file: storm_from-jani_check_cudd_wlan.6-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.160 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:12 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 0.202s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.100s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.793s.

Performance statistics:
  * peak memory usage: 593MB
  * CPU time: 7.000s
  * wallclock time: 7.126s
```



### Log file: storm_from-jani_check_cudd_wlan.6-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.089 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:14:20 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.036s.

Time for model construction: 0.322s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 7.500s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 1.137s.

Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 8.729s
  * wallclock time: 9.041s
```



### Log file: storm_from-jani_check_cudd_wlan.6-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.445 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:08:11 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.033s.

Time for model construction: 0.262s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.194s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.880s.

Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 7.180s
  * wallclock time: 7.394s
```



### Log file: storm_from-jani_check_cudd_wlan.6-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.600 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:13:25 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 0.254s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.406s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "sent": Pmin>=1 [F "target"] ...
Result (for initial states): true

Time for model checking: 0.857s.

Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 7.361s
  * wallclock time: 7.551s
```

