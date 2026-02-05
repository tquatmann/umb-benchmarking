# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [kanban.5](../../models/kanban.5)
Parsed values: [453123072.0, 453123072.0, 453123072.0, 453123072.0, 453123072.0]



### Log file: storm_from-jani_to-umb_cudd_kanban.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.426 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:25:54 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.047s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 8.669s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/kanban.5/model.umb'.
Time for model export: 0.664s.


Performance statistics:
  * peak memory usage: 919MB
  * CPU time: 8.800s
  * wallclock time: 9.392s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/kanban.5/model.umb:	Size of output file is 453123072 bytes
```



### Log file: storm_from-jani_to-umb_cudd_kanban.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.015 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:12:00 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

Time for model construction: 0.056s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 9.304s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/kanban.5/model_rep2.umb'.
Time for model export: 0.606s.


Performance statistics:
  * peak memory usage: 919MB
  * CPU time: 9.466s
  * wallclock time: 9.979s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/kanban.5/model_rep2.umb:	Size of output file is 453123072 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_kanban.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.177 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:36:36 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 0.049s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 8.493s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/kanban.5/model_rep3.umb'.
Time for model export: 0.561s.


Performance statistics:
  * peak memory usage: 918MB
  * CPU time: 8.630s
  * wallclock time: 9.139s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/kanban.5/model_rep3.umb:	Size of output file is 453123072 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_kanban.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.244 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:34 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.062s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 9.458s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/kanban.5/model_rep4.umb'.
Time for model export: 0.670s.


Performance statistics:
  * peak memory usage: 919MB
  * CPU time: 9.589s
  * wallclock time: 10.203s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/kanban.5/model_rep4.umb:	Size of output file is 453123072 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_kanban.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.054 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:30:31 2026
Command line arguments: --timemem --buildfull --jani models/kanban.5/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/kanban.5/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.045s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	2546432 (323 nodes)
Transitions: 	24460016 (6316 nodes)
Reward Models:  throughput
Variables: 	rows: 20 meta variables (52 DD variables), columns: 20 meta variables (52 DD variables)
Labels: 	2
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (53 nodes)
-------------------------------------------------------------- 

Time for model preprocessing: 8.391s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	2546432
Transitions: 	24460016
Reward Models:  throughput
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/kanban.5/model_rep5.umb'.
Time for model export: 0.571s.


Performance statistics:
  * peak memory usage: 919MB
  * CPU time: 8.542s
  * wallclock time: 9.016s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/kanban.5/model_rep5.umb:	Size of output file is 453123072 bytes
Removing output file to save space for repetition #5
```

