# Log files for storm_from-jani_to-umb_cudd on model [crowds.5-20](../../models/crowds.5-20)

Parsed values: `[0.166, 0.258, 0.279, 0.204, 0.19]`



### Log file: storm_from-jani_to-umb_cudd_crowds.5-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.070 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:23:16 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.127s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 8.726s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/crowds.5-20/model.umb'.
Time for model export: 0.166s.


Performance statistics:
  * peak memory usage: 318MB
  * CPU time: 8.880s
  * wallclock time: 9.029s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/crowds.5-20/model.umb:	Size of output file is 135279104 bytes
```



### Log file: storm_from-jani_to-umb_cudd_crowds.5-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.970 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:32:02 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.192s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 10.462s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep2.umb'.
Time for model export: 0.258s.


Performance statistics:
  * peak memory usage: 318MB
  * CPU time: 10.662s
  * wallclock time: 10.923s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep2.umb:	Size of output file is 135279104 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_crowds.5-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 11.358 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:49:46 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.023s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.182s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 10.704s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep3.umb'.
Time for model export: 0.279s.


Performance statistics:
  * peak memory usage: 318MB
  * CPU time: 10.897s
  * wallclock time: 11.196s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep3.umb:	Size of output file is 135279104 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_crowds.5-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 9.227 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:42:08 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.003s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.139s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 8.808s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep4.umb'.
Time for model export: 0.204s.


Performance statistics:
  * peak memory usage: 318MB
  * CPU time: 8.974s
  * wallclock time: 9.161s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep4.umb:	Size of output file is 135279104 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_crowds.5-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.803 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:37:36 2026
Command line arguments: --timemem --buildfull --jani models/crowds.5-20/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard 'false' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
WARN  (DdJaniModelBuilder.cpp:1725): Guard of an edge in a DTMC overlaps with previous guards.
Time for model construction: 0.230s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	2061951 (4026 nodes)
Transitions: 	7374951 (21557 nodes)
Reward Models:  none
Variables: 	rows: 33 meta variables (79 DD variables), columns: 33 meta variables (79 DD variables)
Labels: 	3
   * deadlock -> 53130 state(s) (400 nodes)
   * init -> 1 state(s) (80 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 10.299s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	2061951
Transitions: 	7374951
Reward Models:  none
State Labels: 	3 labels
   * target -> 45628 item(s)
   * deadlock -> 53130 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep5.umb'.
Time for model export: 0.190s.


Performance statistics:
  * peak memory usage: 318MB
  * CPU time: 10.530s
  * wallclock time: 10.731s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/crowds.5-20/model_rep5.umb:	Size of output file is 135279104 bytes
Removing output file to save space for repetition #5
```

