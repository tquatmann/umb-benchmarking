# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [eajs.6-300-13](../../models/eajs.6-300-13)
Parsed values: [574860288.0, 574860288.0, 574860288.0, 574860288.0, 574860288.0]



### Log file: storm_from-jani_to-umb_cudd_eajs.6-300-13_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 33.084 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 07:43:41 2026
Command line arguments: --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.435s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	7901694 (4897 nodes)
Transitions: 	19722777 (43029 nodes)
Choices: 	11897412
Reward Models:  utilityLocal
Variables: 	rows: 24 meta variables (58 DD variables), columns: 24 meta variables (58 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (59 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 31.651s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	12068996
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model.umb'.
Time for model export: 0.890s.


Performance statistics:
  * peak memory usage: 1169MB
  * CPU time: 32.050s
  * wallclock time: 33.039s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model.umb:	Size of output file is 574860288 bytes
```



### Log file: storm_from-jani_to-umb_cudd_eajs.6-300-13_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 27.046 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:27:59 2026
Command line arguments: --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.025s.

Time for model construction: 0.277s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	7901694 (4897 nodes)
Transitions: 	19722777 (43029 nodes)
Choices: 	11897412
Reward Models:  utilityLocal
Variables: 	rows: 24 meta variables (58 DD variables), columns: 24 meta variables (58 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (59 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 25.946s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	12068996
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep2.umb'.
Time for model export: 0.709s.


Performance statistics:
  * peak memory usage: 1169MB
  * CPU time: 26.184s
  * wallclock time: 27.007s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep2.umb:	Size of output file is 574860288 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_eajs.6-300-13_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 27.292 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:55:49 2026
Command line arguments: --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.019s.

Time for model construction: 0.376s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	7901694 (4897 nodes)
Transitions: 	19722777 (43029 nodes)
Choices: 	11897412
Reward Models:  utilityLocal
Variables: 	rows: 24 meta variables (58 DD variables), columns: 24 meta variables (58 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (59 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 25.876s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	12068996
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep3.umb'.
Time for model export: 0.738s.


Performance statistics:
  * peak memory usage: 1169MB
  * CPU time: 26.088s
  * wallclock time: 27.093s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep3.umb:	Size of output file is 574860288 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_eajs.6-300-13_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 28.364 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:21:39 2026
Command line arguments: --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 0.375s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	7901694 (4897 nodes)
Transitions: 	19722777 (43029 nodes)
Choices: 	11897412
Reward Models:  utilityLocal
Variables: 	rows: 24 meta variables (58 DD variables), columns: 24 meta variables (58 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (59 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 26.978s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	12068996
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep4.umb'.
Time for model export: 0.807s.


Performance statistics:
  * peak memory usage: 1169MB
  * CPU time: 27.308s
  * wallclock time: 28.245s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep4.umb:	Size of output file is 574860288 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_eajs.6-300-13_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 27.669 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:26:24 2026
Command line arguments: --timemem --buildfull --jani models/eajs.6-300-13/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.097s.

Time for model construction: 0.349s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	7901694 (4897 nodes)
Transitions: 	19722777 (43029 nodes)
Choices: 	11897412
Reward Models:  utilityLocal
Variables: 	rows: 24 meta variables (58 DD variables), columns: 24 meta variables (58 DD variables), nondeterminism: 5 meta variables (5 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (59 nodes)
   * emptyBattery
-------------------------------------------------------------- 

Time for model preprocessing: 26.247s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	7901694
Transitions: 	19722777
Choices: 	12068996
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 28620 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep5.umb'.
Time for model export: 0.756s.


Performance statistics:
  * peak memory usage: 1169MB
  * CPU time: 26.571s
  * wallclock time: 27.504s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/eajs.6-300-13/model_rep5.umb:	Size of output file is 574860288 bytes
Removing output file to save space for repetition #5
```

