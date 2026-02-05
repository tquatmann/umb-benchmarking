# Log files for storm_from-jani_to-umb_cudd on model [herman.15](../../models/herman.15)

Parsed values: `[230131712.0, 230131712.0, 230131712.0, 230131712.0, 230131712.0]`



### Log file: storm_from-jani_to-umb_cudd_herman.15_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.493 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:24:20 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.060s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.949s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/herman.15/model.umb'.
Time for model export: 0.295s.


Performance statistics:
  * peak memory usage: 478MB
  * CPU time: 1.008s
  * wallclock time: 1.356s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/herman.15/model.umb:	Size of output file is 230131712 bytes
```



### Log file: storm_from-jani_to-umb_cudd_herman.15_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.327 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:59:52 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.975s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/herman.15/model_rep2.umb'.
Time for model export: 0.295s.


Performance statistics:
  * peak memory usage: 479MB
  * CPU time: 1.029s
  * wallclock time: 1.284s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/herman.15/model_rep2.umb:	Size of output file is 230131712 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_herman.15_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.225 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:33:32 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.026s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.870s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/herman.15/model_rep3.umb'.
Time for model export: 0.263s.


Performance statistics:
  * peak memory usage: 479MB
  * CPU time: 0.917s
  * wallclock time: 1.187s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/herman.15/model_rep3.umb:	Size of output file is 230131712 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_herman.15_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.269 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:37:36 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.005s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.903s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/herman.15/model_rep4.umb'.
Time for model export: 0.311s.


Performance statistics:
  * peak memory usage: 479MB
  * CPU time: 0.952s
  * wallclock time: 1.227s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/herman.15/model_rep4.umb:	Size of output file is 230131712 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_herman.15_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 1.186 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:24:23 2026
Command line arguments: --timemem --buildfull --jani models/herman.15/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/herman.15/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.005s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	32768 (16 nodes)
Transitions: 	14348908 (840 nodes)
Reward Models:  steps
Variables: 	rows: 30 meta variables (30 DD variables), columns: 30 meta variables (30 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 32768 state(s) (16 nodes)
   * stable
-------------------------------------------------------------- 

Time for model preprocessing: 0.872s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	32768
Transitions: 	14348908
Reward Models:  steps
State Labels: 	3 labels
   * stable -> 30 item(s)
   * deadlock -> 0 item(s)
   * init -> 32768 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/herman.15/model_rep5.umb'.
Time for model export: 0.267s.


Performance statistics:
  * peak memory usage: 479MB
  * CPU time: 0.924s
  * wallclock time: 1.150s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/herman.15/model_rep5.umb:	Size of output file is 230131712 bytes
Removing output file to save space for repetition #5
```

