# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [fms.8](../../models/fms.8)
Parsed values: [0.871, 1.025, 0.921, 0.936, 1.038]



### Log file: storm_from-jani_to-umb_cudd_fms.8_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 103.786 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:32:30 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 55.613s.

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

Time for model preprocessing: 46.903s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/fms.8/model.umb'.
Time for model export: 0.871s.


Performance statistics:
  * peak memory usage: 1897MB
  * CPU time: 102.269s
  * wallclock time: 103.734s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/fms.8/model.umb:	Size of output file is 724697088 bytes
```



### Log file: storm_from-jani_to-umb_cudd_fms.8_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 115.895 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:24:13 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 63.852s.

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

Time for model preprocessing: 50.552s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/fms.8/model_rep2.umb'.
Time for model export: 1.025s.


Performance statistics:
  * peak memory usage: 1904MB
  * CPU time: 114.304s
  * wallclock time: 115.824s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/fms.8/model_rep2.umb:	Size of output file is 724697088 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_fms.8_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 95.004 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:32:32 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 47.497s.

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

Time for model preprocessing: 46.181s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/fms.8/model_rep3.umb'.
Time for model export: 0.921s.


Performance statistics:
  * peak memory usage: 1897MB
  * CPU time: 93.785s
  * wallclock time: 94.941s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/fms.8/model_rep3.umb:	Size of output file is 724697088 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_fms.8_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 96.962 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:52:46 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.019s.

Time for model construction: 50.709s.

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

Time for model preprocessing: 44.927s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/fms.8/model_rep4.umb'.
Time for model export: 0.936s.


Performance statistics:
  * peak memory usage: 1897MB
  * CPU time: 95.784s
  * wallclock time: 96.911s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/fms.8/model_rep4.umb:	Size of output file is 724697088 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_fms.8_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 131.776 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:30:31 2026
Command line arguments: --timemem --buildfull --jani models/fms.8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/fms.8/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 75.576s.

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

Time for model preprocessing: 54.602s.

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

Exporting model to 'out/storm_from-jani_to-umb_cudd/fms.8/model_rep5.umb'.
Time for model export: 1.038s.


Performance statistics:
  * peak memory usage: 1896MB
  * CPU time: 130.072s
  * wallclock time: 131.701s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/fms.8/model_rep5.umb:	Size of output file is 724697088 bytes
Removing output file to save space for repetition #5
```

