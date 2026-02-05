# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [herman.15](../../models/herman.15)
Parsed values: [0.9770000000000001, 1.4129999999999998, 0.994, 0.9, 0.909]



### Log file: storm_from-jani_check_cudd_herman.15_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.298 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:19:44 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 0.023s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.932s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "steps": R{"steps"}min=? [F "stable"] ...
Result (for initial states): 33.33333555
Time for model checking: 1.159s.

Performance statistics:
  * peak memory usage: 736MB
  * CPU time: 2.015s
  * wallclock time: 2.143s
```



### Log file: storm_from-jani_check_cudd_herman.15_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.115 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:56 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.050s.

Time for model construction: 0.078s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 1.285s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "steps": R{"steps"}min=? [F "stable"] ...
Result (for initial states): 33.33333555
Time for model checking: 1.614s.

Performance statistics:
  * peak memory usage: 735MB
  * CPU time: 2.690s
  * wallclock time: 3.051s
```



### Log file: storm_from-jani_check_cudd_herman.15_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.181 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.021s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.967s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "steps": R{"steps"}min=? [F "stable"] ...
Result (for initial states): 33.33333555
Time for model checking: 1.113s.

Performance statistics:
  * peak memory usage: 736MB
  * CPU time: 1.857s
  * wallclock time: 2.113s
```



### Log file: storm_from-jani_check_cudd_herman.15_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.990 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:54:17 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 0.005s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.871s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "steps": R{"steps"}min=? [F "stable"] ...
Result (for initial states): 33.33333555
Time for model checking: 1.047s.

Performance statistics:
  * peak memory usage: 736MB
  * CPU time: 1.830s
  * wallclock time: 1.954s
```



### Log file: storm_from-jani_check_cudd_herman.15_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.076 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:03 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.898s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "steps": R{"steps"}min=? [F "stable"] ...
Result (for initial states): 33.33333555
Time for model checking: 1.058s.

Performance statistics:
  * peak memory usage: 734MB
  * CPU time: 1.867s
  * wallclock time: 1.973s
```

