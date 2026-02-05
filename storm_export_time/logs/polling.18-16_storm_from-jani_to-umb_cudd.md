# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [1.813, 2.241, 1.795, 1.826, 1.848]



### Log file: storm_from-jani_to-umb_cudd_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 96.988 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:39:25 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 88.156s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	7077888 (76 nodes)
Transitions: 	69599232 (2783 nodes)
Reward Models:  none
Variables: 	rows: 39 meta variables (43 DD variables), columns: 39 meta variables (43 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (44 nodes)
   * serve_s1
   * serve_s2
-------------------------------------------------------------- 

Time for model preprocessing: 6.945s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/polling.18-16/model.umb'.
Time for model export: 1.813s.


Performance statistics:
  * peak memory usage: 3065MB
  * CPU time: 94.912s
  * wallclock time: 96.947s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/polling.18-16/model.umb:	Size of output file is 1230385152 bytes
```



### Log file: storm_from-jani_to-umb_cudd_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 123.383 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:51:47 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 113.468s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	7077888 (76 nodes)
Transitions: 	69599232 (2783 nodes)
Reward Models:  none
Variables: 	rows: 39 meta variables (43 DD variables), columns: 39 meta variables (43 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (44 nodes)
   * serve_s1
   * serve_s2
-------------------------------------------------------------- 

Time for model preprocessing: 7.571s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep2.umb'.
Time for model export: 2.241s.


Performance statistics:
  * peak memory usage: 3064MB
  * CPU time: 120.612s
  * wallclock time: 123.330s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep2.umb:	Size of output file is 1230385152 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 101.085 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:10:59 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 92.968s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	7077888 (76 nodes)
Transitions: 	69599232 (2783 nodes)
Reward Models:  none
Variables: 	rows: 39 meta variables (43 DD variables), columns: 39 meta variables (43 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (44 nodes)
   * serve_s1
   * serve_s2
-------------------------------------------------------------- 

Time for model preprocessing: 6.231s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep3.umb'.
Time for model export: 1.795s.


Performance statistics:
  * peak memory usage: 3065MB
  * CPU time: 98.877s
  * wallclock time: 101.036s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep3.umb:	Size of output file is 1230385152 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 127.085 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:38:36 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 118.815s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	7077888 (76 nodes)
Transitions: 	69599232 (2783 nodes)
Reward Models:  none
Variables: 	rows: 39 meta variables (43 DD variables), columns: 39 meta variables (43 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (44 nodes)
   * serve_s1
   * serve_s2
-------------------------------------------------------------- 

Time for model preprocessing: 6.352s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep4.umb'.
Time for model export: 1.826s.


Performance statistics:
  * peak memory usage: 3065MB
  * CPU time: 124.648s
  * wallclock time: 127.037s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep4.umb:	Size of output file is 1230385152 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 102.766 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:15:07 2026
Command line arguments: --timemem --buildfull --jani models/polling.18-16/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 94.186s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	7077888 (76 nodes)
Transitions: 	69599232 (2783 nodes)
Reward Models:  none
Variables: 	rows: 39 meta variables (43 DD variables), columns: 39 meta variables (43 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (44 nodes)
   * serve_s1
   * serve_s2
-------------------------------------------------------------- 

Time for model preprocessing: 6.639s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep5.umb'.
Time for model export: 1.848s.


Performance statistics:
  * peak memory usage: 3063MB
  * CPU time: 100.592s
  * wallclock time: 102.714s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/polling.18-16/model_rep5.umb:	Size of output file is 1230385152 bytes
Removing output file to save space for repetition #5
```

