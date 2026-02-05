# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.056, 0.113, 0.07, 0.084, 0.067]



### Log file: storm_from-jani_check_cudd_embedded.8-12_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.056 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:02:07 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": Pmin=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036082
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.031s
  * wallclock time: 0.018s
```



### Log file: storm_from-jani_check_cudd_embedded.8-12_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.113 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:26:10 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.032s.

Time for model construction: 0.008s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": Pmin=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036082
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.057s
  * wallclock time: 0.053s
```



### Log file: storm_from-jani_check_cudd_embedded.8-12_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.070 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:11 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.009s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": Pmin=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036082
Time for model checking: 0.003s.

Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.034s
  * wallclock time: 0.027s
```



### Log file: storm_from-jani_check_cudd_embedded.8-12_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.084 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:11:52 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 0.007s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": Pmin=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036082
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.036s
  * wallclock time: 0.046s
```



### Log file: storm_from-jani_check_cudd_embedded.8-12_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.067 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:30 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.013s.

Time for model construction: 0.007s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.005s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": Pmin=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036082
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.029s
  * wallclock time: 0.031s
```

