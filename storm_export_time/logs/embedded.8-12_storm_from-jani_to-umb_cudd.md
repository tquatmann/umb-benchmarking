# Log files for storm_from-jani_to-umb_cudd on model [embedded.8-12](../../models/embedded.8-12)

Parsed values: `[0.002, 0.003, 0.003, 0.003, 0.003]`



### Log file: storm_from-jani_to-umb_cudd_embedded.8-12_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.054 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 07:40:36 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.007s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/embedded.8-12/model.umb'.
Time for model export: 0.002s.


Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.030s
  * wallclock time: 0.021s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/embedded.8-12/model.umb:	Size of output file is 732672 bytes
```



### Log file: storm_from-jani_to-umb_cudd_embedded.8-12_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.075 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:32:55 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.016s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep2.umb'.
Time for model export: 0.003s.


Performance statistics:
  * peak memory usage: 40MB
  * CPU time: 0.026s
  * wallclock time: 0.034s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep2.umb:	Size of output file is 732672 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_embedded.8-12_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.078 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:30:19 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.021s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.005s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep3.umb'.
Time for model export: 0.003s.


Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.031s
  * wallclock time: 0.041s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep3.umb:	Size of output file is 732672 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_embedded.8-12_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.055 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:33:02 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.001s.

Time for model construction: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.005s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep4.umb'.
Time for model export: 0.003s.


Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.030s
  * wallclock time: 0.018s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep4.umb:	Size of output file is 732672 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_embedded.8-12_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.065 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:36:45 2026
Command line arguments: --timemem --buildfull --jani models/embedded.8-12/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.002s.

Time for model construction: 0.008s.

-------------------------------------------------------------- 
Model type: 	CTMC (symbolic)
States: 	8548 (73 nodes)
Transitions: 	36041 (1831 nodes)
Reward Models:  none
Variables: 	rows: 15 meta variables (22 DD variables), columns: 15 meta variables (22 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (23 nodes)
   * fail_actuators
   * l_down
-------------------------------------------------------------- 

Time for model preprocessing: 0.006s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * fail_actuators -> 1064 item(s)
   * deadlock -> 0 item(s)
   * l_down -> 5884 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep5.umb'.
Time for model export: 0.003s.


Performance statistics:
  * peak memory usage: 41MB
  * CPU time: 0.038s
  * wallclock time: 0.021s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/embedded.8-12/model_rep5.umb:	Size of output file is 732672 bytes
Removing output file to save space for repetition #5
```

