# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [egl.10-8](../../models/egl.10-8)
Parsed values: [3204.761, 3346.13, 3481.615, 2922.76, 3365.164]



### Log file: storm_from-jani_check_cudd_egl.10-8_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3226.073 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:43:12 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 3.129s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3201.609s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": Pmin=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 0.5004882812
Time for model checking: 21.101s.

Performance statistics:
  * peak memory usage: 22055MB
  * CPU time: 3209.283s
  * wallclock time: 3226.024s
```



### Log file: storm_from-jani_check_cudd_egl.10-8_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3368.335 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:07:07 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.034s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 4.037s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3342.059s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": Pmin=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 0.5004882812
Time for model checking: 22.042s.

Performance statistics:
  * peak memory usage: 22055MB
  * CPU time: 3350.966s
  * wallclock time: 3368.266s
```



### Log file: storm_from-jani_check_cudd_egl.10-8_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3502.266 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:28:57 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.031s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 3.305s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3478.279s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": Pmin=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 0.5004882812
Time for model checking: 19.629s.

Performance statistics:
  * peak memory usage: 22056MB
  * CPU time: 3486.317s
  * wallclock time: 3501.306s
```



### Log file: storm_from-jani_check_cudd_egl.10-8_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2940.177 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:21 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.013s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 2920.742s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": Pmin=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 0.5004882812
Time for model checking: 17.318s.

Performance statistics:
  * peak memory usage: 22055MB
  * CPU time: 2927.814s
  * wallclock time: 2940.131s
```



### Log file: storm_from-jani_check_cudd_egl.10-8_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3384.408 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:02:32 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.013s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 5.391s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3359.760s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "unfairA": Pmin=? [F ((!"knowA") & "knowB")] ...
Result (for initial states): 0.5004882812
Time for model checking: 19.121s.

Performance statistics:
  * peak memory usage: 22056MB
  * CPU time: 3361.929s
  * wallclock time: 3384.344s
```

