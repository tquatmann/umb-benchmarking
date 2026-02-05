# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [haddad-monmege.100-0.7](../../models/haddad-monmege.100-0.7)
Parsed values: [0.078, 0.03, 0.019000000000000003, 0.022000000000000002, 0.059]



### Log file: storm_from-jani_check_cudd_haddad-monmege.100-0.7_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.118 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:55:09 2026
Command line arguments: --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.064s.

Time for model construction: 0.014s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	201 (10 nodes)
Transitions: 	400 (133 nodes)
Reward Models:  none
Variables: 	rows: 2 meta variables (9 DD variables), columns: 2 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (10 nodes)
   * Target
-------------------------------------------------------------- 

Time for model preprocessing: 0.000s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	201
Transitions: 	400
Reward Models:  none
State Labels: 	3 labels
   * Target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "target": Pmin=? [F "Target"] ...
Result (for initial states): 0.5
Time for model checking: 0.000s.

Performance statistics:
  * peak memory usage: 39MB
  * CPU time: 0.026s
  * wallclock time: 0.082s
```



### Log file: storm_from-jani_check_cudd_haddad-monmege.100-0.7_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.258 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:18 2026
Command line arguments: --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.017s.

Time for model construction: 0.013s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	201 (10 nodes)
Transitions: 	400 (133 nodes)
Reward Models:  none
Variables: 	rows: 2 meta variables (9 DD variables), columns: 2 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (10 nodes)
   * Target
-------------------------------------------------------------- 

Time for model preprocessing: 0.000s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	201
Transitions: 	400
Reward Models:  none
State Labels: 	3 labels
   * Target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "target": Pmin=? [F "Target"] ...
Result (for initial states): 0.5
Time for model checking: 0.000s.

Performance statistics:
  * peak memory usage: 38MB
  * CPU time: 0.035s
  * wallclock time: 0.036s
```



### Log file: storm_from-jani_check_cudd_haddad-monmege.100-0.7_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.069 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:07:48 2026
Command line arguments: --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.016s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	201 (10 nodes)
Transitions: 	400 (133 nodes)
Reward Models:  none
Variables: 	rows: 2 meta variables (9 DD variables), columns: 2 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (10 nodes)
   * Target
-------------------------------------------------------------- 

Time for model preprocessing: 0.001s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	201
Transitions: 	400
Reward Models:  none
State Labels: 	3 labels
   * Target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "target": Pmin=? [F "Target"] ...
Result (for initial states): 0.5
Time for model checking: 0.000s.

Performance statistics:
  * peak memory usage: 39MB
  * CPU time: 0.042s
  * wallclock time: 0.023s
```



### Log file: storm_from-jani_check_cudd_haddad-monmege.100-0.7_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.125 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:28:57 2026
Command line arguments: --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.016s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	201 (10 nodes)
Transitions: 	400 (133 nodes)
Reward Models:  none
Variables: 	rows: 2 meta variables (9 DD variables), columns: 2 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (10 nodes)
   * Target
-------------------------------------------------------------- 

Time for model preprocessing: 0.001s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	201
Transitions: 	400
Reward Models:  none
State Labels: 	3 labels
   * Target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "target": Pmin=? [F "Target"] ...
Result (for initial states): 0.5
Time for model checking: 0.001s.

Performance statistics:
  * peak memory usage: 39MB
  * CPU time: 0.026s
  * wallclock time: 0.026s
```



### Log file: storm_from-jani_check_cudd_haddad-monmege.100-0.7_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.111 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:06:05 2026
Command line arguments: --timemem --buildfull --jani models/haddad-monmege.100-0.7/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.014s.

Time for model construction: 0.045s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	201 (10 nodes)
Transitions: 	400 (133 nodes)
Reward Models:  none
Variables: 	rows: 2 meta variables (9 DD variables), columns: 2 meta variables (9 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (10 nodes)
   * Target
-------------------------------------------------------------- 

Time for model preprocessing: 0.000s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	201
Transitions: 	400
Reward Models:  none
State Labels: 	3 labels
   * Target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "target": Pmin=? [F "Target"] ...
Result (for initial states): 0.5
Time for model checking: 0.000s.

Performance statistics:
  * peak memory usage: 39MB
  * CPU time: 0.041s
  * wallclock time: 0.064s
```

