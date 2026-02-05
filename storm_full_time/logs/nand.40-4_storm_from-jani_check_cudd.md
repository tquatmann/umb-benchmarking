# Log files for storm_from-jani_check_cudd on model [nand.40-4](../../models/nand.40-4)

Parsed values: `[16.722, 4.285, 4.549, 6.145, 4.314]`



### Log file: storm_from-jani_check_cudd_nand.40-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 16.722 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:29:16 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.024s.

Time for model construction: 5.368s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	3999522 (9477 nodes)
Transitions: 	6288542 (52479 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.357s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	3999522
Transitions: 	6288542
Reward Models:  none
State Labels: 	3 labels
   * target -> 4 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6186822208
Time for model checking: 4.812s.

Performance statistics:
  * peak memory usage: 793MB
  * CPU time: 16.178s
  * wallclock time: 16.583s
```



### Log file: storm_from-jani_check_cudd_nand.40-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.285 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:21:34 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 1.197s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	3999522 (9477 nodes)
Transitions: 	6288542 (52479 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.386s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	3999522
Transitions: 	6288542
Reward Models:  none
State Labels: 	3 labels
   * target -> 4 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6186822208
Time for model checking: 1.653s.

Performance statistics:
  * peak memory usage: 793MB
  * CPU time: 4.108s
  * wallclock time: 4.246s
```



### Log file: storm_from-jani_check_cudd_nand.40-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.549 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:07 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 1.326s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	3999522 (9477 nodes)
Transitions: 	6288542 (52479 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.463s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	3999522
Transitions: 	6288542
Reward Models:  none
State Labels: 	3 labels
   * target -> 4 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6186822208
Time for model checking: 1.701s.

Performance statistics:
  * peak memory usage: 793MB
  * CPU time: 4.358s
  * wallclock time: 4.500s
```



### Log file: storm_from-jani_check_cudd_nand.40-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 6.145 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:21:34 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 1.570s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	3999522 (9477 nodes)
Transitions: 	6288542 (52479 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.666s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	3999522
Transitions: 	6288542
Reward Models:  none
State Labels: 	3 labels
   * target -> 4 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6186822208
Time for model checking: 2.836s.

Performance statistics:
  * peak memory usage: 793MB
  * CPU time: 5.788s
  * wallclock time: 6.085s
```



### Log file: storm_from-jani_check_cudd_nand.40-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 4.314 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:24 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 1.253s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	3999522 (9477 nodes)
Transitions: 	6288542 (52479 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 1.402s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	3999522
Transitions: 	6288542
Reward Models:  none
State Labels: 	3 labels
   * target -> 4 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6186822208
Time for model checking: 1.607s.

Performance statistics:
  * peak memory usage: 793MB
  * CPU time: 4.138s
  * wallclock time: 4.272s
```

