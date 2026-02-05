# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [117.629, 129.223, 119.222, 118.254, 383.498]



### Log file: storm_from-jani_check_cudd_fms.8_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 117.629 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:27:38 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.032s.

Time for model construction: 50.357s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	4459455 (30357 nodes)
Transitions: 	38533968 (2542723 nodes)
Reward Models:  productivity
Variables: 	rows: 24 meta variables (70 DD variables), columns: 24 meta variables (70 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (71 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 49.638s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}min=? [LRA] ...
Result (for initial states): 116.6245863
Time for model checking: 17.152s.

Performance statistics:
  * peak memory usage: 4877MB
  * CPU time: 116.294s
  * wallclock time: 117.551s
```



### Log file: storm_from-jani_check_cudd_fms.8_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 129.223 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:22:09 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 56.035s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	4459455 (30357 nodes)
Transitions: 	38533968 (2542723 nodes)
Reward Models:  productivity
Variables: 	rows: 24 meta variables (70 DD variables), columns: 24 meta variables (70 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (71 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 52.360s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}min=? [LRA] ...
Result (for initial states): 116.6245863
Time for model checking: 20.309s.

Performance statistics:
  * peak memory usage: 4877MB
  * CPU time: 127.588s
  * wallclock time: 129.080s
```



### Log file: storm_from-jani_check_cudd_fms.8_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 119.222 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:36:52 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.019s.

Time for model construction: 49.894s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	4459455 (30357 nodes)
Transitions: 	38533968 (2542723 nodes)
Reward Models:  productivity
Variables: 	rows: 24 meta variables (70 DD variables), columns: 24 meta variables (70 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (71 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 51.447s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}min=? [LRA] ...
Result (for initial states): 116.6245863
Time for model checking: 17.289s.

Performance statistics:
  * peak memory usage: 4901MB
  * CPU time: 117.676s
  * wallclock time: 119.060s
```



### Log file: storm_from-jani_check_cudd_fms.8_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 118.254 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:01 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

Time for model construction: 49.308s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	4459455 (30357 nodes)
Transitions: 	38533968 (2542723 nodes)
Reward Models:  productivity
Variables: 	rows: 24 meta variables (70 DD variables), columns: 24 meta variables (70 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (71 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 51.379s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}min=? [LRA] ...
Result (for initial states): 116.6245863
Time for model checking: 17.100s.

Performance statistics:
  * peak memory usage: 4877MB
  * CPU time: 116.680s
  * wallclock time: 118.134s
```



### Log file: storm_from-jani_check_cudd_fms.8_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 383.498 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:23:12 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 133.885s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	4459455 (30357 nodes)
Transitions: 	38533968 (2542723 nodes)
Reward Models:  productivity
Variables: 	rows: 24 meta variables (70 DD variables), columns: 24 meta variables (70 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (71 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 200.543s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}min=? [LRA] ...
Result (for initial states): 116.6245863
Time for model checking: 47.965s.

Performance statistics:
  * peak memory usage: 4903MB
  * CPU time: 378.074s
  * wallclock time: 383.265s
```

