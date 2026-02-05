# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [speed-ind.2100](../../models/speed-ind.2100)
Parsed values: [307.57399999999996, 247.54399999999998, 274.697, 273.93199999999996, 265.443]



### Log file: storm_from-jani_check_cudd_speed-ind.2100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 408.268 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:31:48 2026
Command line arguments: --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 302.787s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	743424 (165 nodes)
Transitions: 	9518080 (46954 nodes)
Reward Models:  none
Variables: 	rows: 16 meta variables (66 DD variables), columns: 16 meta variables (66 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (67 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 4.779s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * target -> 24576 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": Pmin=? [true U<=2100 "target"] ...
Result (for initial states): 0.04229449798
Time for model checking: 100.604s.

Performance statistics:
  * peak memory usage: 1523MB
  * CPU time: 406.356s
  * wallclock time: 408.216s
```



### Log file: storm_from-jani_check_cudd_speed-ind.2100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 322.268 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:11 2026
Command line arguments: --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 242.945s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	743424 (165 nodes)
Transitions: 	9518080 (46954 nodes)
Reward Models:  none
Variables: 	rows: 16 meta variables (66 DD variables), columns: 16 meta variables (66 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (67 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 4.590s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * target -> 24576 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": Pmin=? [true U<=2100 "target"] ...
Result (for initial states): 0.04229449798
Time for model checking: 74.644s.

Performance statistics:
  * peak memory usage: 1523MB
  * CPU time: 321.017s
  * wallclock time: 322.218s
```



### Log file: storm_from-jani_check_cudd_speed-ind.2100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 351.191 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:22:01 2026
Command line arguments: --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 269.171s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	743424 (165 nodes)
Transitions: 	9518080 (46954 nodes)
Reward Models:  none
Variables: 	rows: 16 meta variables (66 DD variables), columns: 16 meta variables (66 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (67 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 5.517s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * target -> 24576 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": Pmin=? [true U<=2100 "target"] ...
Result (for initial states): 0.04229449798
Time for model checking: 76.398s.

Performance statistics:
  * peak memory usage: 1523MB
  * CPU time: 349.739s
  * wallclock time: 351.139s
```



### Log file: storm_from-jani_check_cudd_speed-ind.2100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 360.733 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:11 2026
Command line arguments: --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 269.239s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	743424 (165 nodes)
Transitions: 	9518080 (46954 nodes)
Reward Models:  none
Variables: 	rows: 16 meta variables (66 DD variables), columns: 16 meta variables (66 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (67 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 4.685s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * target -> 24576 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": Pmin=? [true U<=2100 "target"] ...
Result (for initial states): 0.04229449798
Time for model checking: 86.704s.

Performance statistics:
  * peak memory usage: 1524MB
  * CPU time: 359.007s
  * wallclock time: 360.678s
```



### Log file: storm_from-jani_check_cudd_speed-ind.2100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 346.881 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:23:05 2026
Command line arguments: --timemem --buildfull --jani models/speed-ind.2100/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.053s.

Time for model construction: 260.772s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	743424 (165 nodes)
Transitions: 	9518080 (46954 nodes)
Reward Models:  none
Variables: 	rows: 16 meta variables (66 DD variables), columns: 16 meta variables (66 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (67 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 4.618s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * target -> 24576 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": Pmin=? [true U<=2100 "target"] ...
Result (for initial states): 0.04229449798
Time for model checking: 81.359s.

Performance statistics:
  * peak memory usage: 1524MB
  * CPU time: 345.015s
  * wallclock time: 346.836s
```

