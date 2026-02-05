# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [crowds.5-20](../../models/crowds.5-20)
Parsed values: [9.100999999999999, 10.084, 8.945, 9.933, 9.15]



### Log file: storm_from-jani_check_cudd_crowds.5-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.190 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:26:04 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.144s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 8.934s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.08606908468
Time for model checking: 1.044s.

Performance statistics:
  * peak memory usage: 372MB
  * CPU time: 10.068s
  * wallclock time: 10.152s
```



### Log file: storm_from-jani_check_cudd_crowds.5-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 11.386 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:19 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.186s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 9.876s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.08606908468
Time for model checking: 1.251s.

Performance statistics:
  * peak memory usage: 371MB
  * CPU time: 11.205s
  * wallclock time: 11.343s
```



### Log file: storm_from-jani_check_cudd_crowds.5-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 11.361 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.130s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 8.812s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.08606908468
Time for model checking: 0.974s.

Performance statistics:
  * peak memory usage: 371MB
  * CPU time: 9.837s
  * wallclock time: 9.926s
```



### Log file: storm_from-jani_check_cudd_crowds.5-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 11.152 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:08:07 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.030s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.179s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 9.724s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.08606908468
Time for model checking: 1.150s.

Performance statistics:
  * peak memory usage: 372MB
  * CPU time: 10.981s
  * wallclock time: 11.090s
```



### Log file: storm_from-jani_check_cudd_crowds.5-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.237 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:52:28 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.127s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 8.996s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.08606908468
Time for model checking: 1.001s.

Performance statistics:
  * peak memory usage: 371MB
  * CPU time: 10.093s
  * wallclock time: 10.159s
```

