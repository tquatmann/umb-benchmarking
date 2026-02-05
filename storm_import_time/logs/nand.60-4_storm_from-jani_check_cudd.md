# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [nand.60-4](../../models/nand.60-4)
Parsed values: [10.437, 10.009, 9.484, 9.433, 9.503]



### Log file: storm_from-jani_check_cudd_nand.60-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 19.087 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:53:36 2026
Command line arguments: --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 3.621s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	18826082 (16543 nodes)
Transitions: 	29772212 (102395 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.800s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	18826082
Transitions: 	29772212
Reward Models:  none
State Labels: 	3 labels
   * target -> 6 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6867214589
Time for model checking: 8.577s.

Performance statistics:
  * peak memory usage: 3635MB
  * CPU time: 18.312s
  * wallclock time: 19.029s
```



### Log file: storm_from-jani_check_cudd_nand.60-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.463 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:08 2026
Command line arguments: --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 3.508s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	18826082 (16543 nodes)
Transitions: 	29772212 (102395 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.499s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	18826082
Transitions: 	29772212
Reward Models:  none
State Labels: 	3 labels
   * target -> 6 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6867214589
Time for model checking: 8.348s.

Performance statistics:
  * peak memory usage: 3635MB
  * CPU time: 17.697s
  * wallclock time: 18.373s
```



### Log file: storm_from-jani_check_cudd_nand.60-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 17.826 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:02 2026
Command line arguments: --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.013s.

Time for model construction: 3.350s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	18826082 (16543 nodes)
Transitions: 	29772212 (102395 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.121s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	18826082
Transitions: 	29772212
Reward Models:  none
State Labels: 	3 labels
   * target -> 6 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6867214589
Time for model checking: 8.285s.

Performance statistics:
  * peak memory usage: 3635MB
  * CPU time: 17.144s
  * wallclock time: 17.781s
```



### Log file: storm_from-jani_check_cudd_nand.60-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 17.739 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:55:32 2026
Command line arguments: --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 3.310s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	18826082 (16543 nodes)
Transitions: 	29772212 (102395 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.121s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	18826082
Transitions: 	29772212
Reward Models:  none
State Labels: 	3 labels
   * target -> 6 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6867214589
Time for model checking: 8.235s.

Performance statistics:
  * peak memory usage: 3635MB
  * CPU time: 17.017s
  * wallclock time: 17.681s
```



### Log file: storm_from-jani_check_cudd_nand.60-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 18.113 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:35 2026
Command line arguments: --timemem --buildfull --jani models/nand.60-4/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 3.367s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	18826082 (16543 nodes)
Transitions: 	29772212 (102395 nodes)
Reward Models:  none
Variables: 	rows: 9 meta variables (34 DD variables), columns: 9 meta variables (34 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (35 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.127s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	18826082
Transitions: 	29772212
Reward Models:  none
State Labels: 	3 labels
   * target -> 6 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "reliable": Pmin=? [F "target"] ...
Result (for initial states): 0.6867214589
Time for model checking: 8.541s.

Performance statistics:
  * peak memory usage: 3635MB
  * CPU time: 17.342s
  * wallclock time: 18.057s
```

