# Log files for storm_from-jani_to-umb_cudd on model [mapk-cascade.4-30](../../models/mapk-cascade.4-30)

Parsed values: `[0.514, 0.48, 0.427, 0.511, 0.426]`



### Log file: storm_from-jani_to-umb_cudd_mapk-cascade.4-30_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 23.677 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:23:17 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 4.145s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 18.946s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model.umb'.
Time for model export: 0.514s.


Performance statistics:
  * peak memory usage: 922MB
  * CPU time: 23.064s
  * wallclock time: 23.630s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model.umb:	Size of output file is 353330176 bytes
```



### Log file: storm_from-jani_to-umb_cudd_mapk-cascade.4-30_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 22.961 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:48:44 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 3.138s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 19.277s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep2.umb'.
Time for model export: 0.480s.


Performance statistics:
  * peak memory usage: 922MB
  * CPU time: 22.408s
  * wallclock time: 22.920s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep2.umb:	Size of output file is 353330176 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_mapk-cascade.4-30_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 21.674 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:26:01 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.011s.

Time for model construction: 3.084s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 18.092s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep3.umb'.
Time for model export: 0.427s.


Performance statistics:
  * peak memory usage: 922MB
  * CPU time: 21.150s
  * wallclock time: 21.636s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep3.umb:	Size of output file is 353330176 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_mapk-cascade.4-30_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 23.651 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:30:50 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 3.235s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 19.845s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep4.umb'.
Time for model export: 0.511s.


Performance statistics:
  * peak memory usage: 922MB
  * CPU time: 23.056s
  * wallclock time: 23.615s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep4.umb:	Size of output file is 353330176 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_mapk-cascade.4-30_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 21.397 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:12:59 2026
Command line arguments: --timemem --buildfull --jani models/mapk-cascade.4-30/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 3.197s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2042426 (4323 nodes)
Transitions: 	18970804 (97697 nodes)
Reward Models:  time
Variables: 	rows: 29 meta variables (65 DD variables), columns: 29 meta variables (65 DD variables)
Labels: 	3
   * deadlock -> 350940 state(s) (3056 nodes)
   * init -> 1 state(s) (66 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 17.718s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2042426
Transitions: 	18970804
Reward Models:  time
State Labels: 	3 labels
   * target -> 338423 item(s)
   * deadlock -> 350940 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep5.umb'.
Time for model export: 0.426s.


Performance statistics:
  * peak memory usage: 922MB
  * CPU time: 20.923s
  * wallclock time: 21.361s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/mapk-cascade.4-30/model_rep5.umb:	Size of output file is 353330176 bytes
Removing output file to save space for repetition #5
```

