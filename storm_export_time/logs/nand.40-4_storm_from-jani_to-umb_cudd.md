# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [nand.40-4](../../models/nand.40-4)
Parsed values: [0.193, 0.704, 0.173, 0.198, 0.205]



### Log file: storm_from-jani_to-umb_cudd_nand.40-4_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.848 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:31:27 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 1.218s.

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

Time for model preprocessing: 1.393s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/nand.40-4/model.umb'.
Time for model export: 0.193s.


Performance statistics:
  * peak memory usage: 345MB
  * CPU time: 2.630s
  * wallclock time: 2.814s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/nand.40-4/model.umb:	Size of output file is 134124032 bytes
```



### Log file: storm_from-jani_to-umb_cudd_nand.40-4_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 12.740 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:06 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

Time for model construction: 5.485s.

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

Time for model preprocessing: 6.386s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep2.umb'.
Time for model export: 0.704s.


Performance statistics:
  * peak memory usage: 344MB
  * CPU time: 11.963s
  * wallclock time: 12.607s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep2.umb:	Size of output file is 134124032 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_nand.40-4_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2.838 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:24:12 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 1.232s.

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

Time for model preprocessing: 1.388s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep3.umb'.
Time for model export: 0.173s.


Performance statistics:
  * peak memory usage: 344MB
  * CPU time: 2.635s
  * wallclock time: 2.801s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep3.umb:	Size of output file is 134124032 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_nand.40-4_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.380 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:10:59 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 1.475s.

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

Time for model preprocessing: 1.653s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep4.umb'.
Time for model export: 0.198s.


Performance statistics:
  * peak memory usage: 345MB
  * CPU time: 3.146s
  * wallclock time: 3.336s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep4.umb:	Size of output file is 134124032 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_nand.40-4_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3.546 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:55 2026
Command line arguments: --timemem --buildfull --jani models/nand.40-4/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 1.561s.

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

Time for model preprocessing: 1.698s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep5.umb'.
Time for model export: 0.205s.


Performance statistics:
  * peak memory usage: 344MB
  * CPU time: 3.290s
  * wallclock time: 3.476s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/nand.40-4/model_rep5.umb:	Size of output file is 134124032 bytes
Removing output file to save space for repetition #5
```

