# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [crowds.6-20](../../models/crowds.6-20)
Parsed values: [65.567, 65.968, 82.798, 64.432, 64.748]



### Log file: storm_from-jani_check_cudd_crowds.6-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 65.567 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:51:31 2026
Command line arguments: --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
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
Time for model construction: 0.174s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	10633591 (4792 nodes)
Transitions: 	38261191 (26509 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 230230 state(s) (464 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 43.087s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	10633591
Transitions: 	38261191
Reward Models:  none
State Labels: 	3 labels
   * target -> 352935 item(s)
   * deadlock -> 230230 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.1204764668
Time for model checking: 22.235s.

Performance statistics:
  * peak memory usage: 1799MB
  * CPU time: 65.089s
  * wallclock time: 65.513s
```



### Log file: storm_from-jani_check_cudd_crowds.6-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 65.968 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:21:44 2026
Command line arguments: --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.013s.

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
Time for model construction: 0.191s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	10633591 (4792 nodes)
Transitions: 	38261191 (26509 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 230230 state(s) (464 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 43.557s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	10633591
Transitions: 	38261191
Reward Models:  none
State Labels: 	3 labels
   * target -> 352935 item(s)
   * deadlock -> 230230 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.1204764668
Time for model checking: 22.139s.

Performance statistics:
  * peak memory usage: 1799MB
  * CPU time: 65.460s
  * wallclock time: 65.917s
```



### Log file: storm_from-jani_check_cudd_crowds.6-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 82.798 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:21 2026
Command line arguments: --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

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
Time for model construction: 0.167s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	10633591 (4792 nodes)
Transitions: 	38261191 (26509 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 230230 state(s) (464 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 46.812s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	10633591
Transitions: 	38261191
Reward Models:  none
State Labels: 	3 labels
   * target -> 352935 item(s)
   * deadlock -> 230230 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.1204764668
Time for model checking: 35.698s.

Performance statistics:
  * peak memory usage: 1799MB
  * CPU time: 81.917s
  * wallclock time: 82.746s
```



### Log file: storm_from-jani_check_cudd_crowds.6-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 64.432 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
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
Time for model construction: 0.176s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	10633591 (4792 nodes)
Transitions: 	38261191 (26509 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 230230 state(s) (464 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 42.148s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	10633591
Transitions: 	38261191
Reward Models:  none
State Labels: 	3 labels
   * target -> 352935 item(s)
   * deadlock -> 230230 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.1204764668
Time for model checking: 22.019s.

Performance statistics:
  * peak memory usage: 1799MB
  * CPU time: 63.958s
  * wallclock time: 64.363s
```



### Log file: storm_from-jani_check_cudd_crowds.6-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 64.748 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:29 2026
Command line arguments: --timemem --buildfull --jani models/crowds.6-20/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.018s.

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
Time for model construction: 0.192s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	10633591 (4792 nodes)
Transitions: 	38261191 (26509 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 230230 state(s) (464 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 42.400s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	10633591
Transitions: 	38261191
Reward Models:  none
State Labels: 	3 labels
   * target -> 352935 item(s)
   * deadlock -> 230230 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "positive": Pmin=? [F "target"] ...
Result (for initial states): 0.1204764668
Time for model checking: 22.057s.

Performance statistics:
  * peak memory usage: 1799MB
  * CPU time: 64.253s
  * wallclock time: 64.683s
```

