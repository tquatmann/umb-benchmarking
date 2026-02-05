# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [wlan.6-0](../../models/wlan.6-0)
Parsed values: [0.374, 0.506, 0.356, 0.414, 0.339]



### Log file: storm_from-jani_to-umb_cudd_wlan.6-0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.269 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:25:54 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 0.214s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.605s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.6-0/model.umb'.
Time for model export: 0.374s.


Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 6.867s
  * wallclock time: 7.224s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.6-0/model.umb:	Size of output file is 276365824 bytes
```



### Log file: storm_from-jani_to-umb_cudd_wlan.6-0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.987 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:25 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.009s.

Time for model construction: 0.228s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 7.138s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep2.umb'.
Time for model export: 0.506s.


Performance statistics:
  * peak memory usage: 593MB
  * CPU time: 7.394s
  * wallclock time: 7.906s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep2.umb:	Size of output file is 276365824 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_wlan.6-0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 7.163 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:26:58 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.035s.

Time for model construction: 0.198s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.495s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep3.umb'.
Time for model export: 0.356s.


Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 6.742s
  * wallclock time: 7.106s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep3.umb:	Size of output file is 276365824 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_wlan.6-0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 6.796 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:25:21 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.008s.

Time for model construction: 0.192s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.106s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep4.umb'.
Time for model export: 0.414s.


Performance statistics:
  * peak memory usage: 593MB
  * CPU time: 6.313s
  * wallclock time: 6.740s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep4.umb:	Size of output file is 276365824 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_wlan.6-0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 6.707 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:58:53 2026
Command line arguments: --timemem --buildfull --jani models/wlan.6-0/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 0.189s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	5007548 (3680 nodes)
Transitions: 	11475748 (22292 nodes)
Choices: 	6350470
Reward Models:  none
Variables: 	rows: 16 meta variables (50 DD variables), columns: 16 meta variables (50 DD variables), nondeterminism: 7 meta variables (7 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (51 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 6.090s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	5007548
Transitions: 	11475748
Choices: 	6350470
Reward Models:  none
State Labels: 	3 labels
   * target -> 1 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep5.umb'.
Time for model export: 0.339s.


Performance statistics:
  * peak memory usage: 594MB
  * CPU time: 6.318s
  * wallclock time: 6.666s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/wlan.6-0/model_rep5.umb:	Size of output file is 276365824 bytes
Removing output file to save space for repetition #5
```

