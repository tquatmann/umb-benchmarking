# Log files

Tool configuration: storm_from-jani_to-umb_cudd
Benchmark: [egl.10-8](../../models/egl.10-8)
Parsed values: [12.877, 16.339, 11.078, 10.381, 11.572]



### Log file: storm_from-jani_to-umb_cudd_egl.10-8_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3092.693 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:38:21 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.502s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3077.187s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-8/model.umb'.
Time for model export: 12.877s.


Performance statistics:
  * peak memory usage: 15240MB
  * CPU time: 3070.226s
  * wallclock time: 3092.642s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-8/model.umb:	Size of output file is 7800892416 bytes
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-8_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2966.826 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:02:54 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.040s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.028s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 2948.166s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep2.umb'.
Time for model export: 16.339s.


Performance statistics:
  * peak memory usage: 15241MB
  * CPU time: 2943.570s
  * wallclock time: 2966.753s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep2.umb:	Size of output file is 7800892416 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-8_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3070.055 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:24:55 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.084s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3056.782s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep3.umb'.
Time for model export: 11.078s.


Performance statistics:
  * peak memory usage: 15240MB
  * CPU time: 3051.559s
  * wallclock time: 3069.997s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep3.umb:	Size of output file is 7800892416 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-8_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 2954.384 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:29:30 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.020s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.405s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 2941.493s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep4.umb'.
Time for model export: 10.381s.


Performance statistics:
  * peak memory usage: 15239MB
  * CPU time: 2933.776s
  * wallclock time: 2954.345s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep4.umb:	Size of output file is 7800892416 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-8_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 3219.222 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:55:49 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-8/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.006s.

WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 17))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 19))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 11))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 13))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 15))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 1) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 2) & (n = 18))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 10))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 12))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 14))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 16))' is unsatisfiable.
WARN  (DdJaniModelBuilder.cpp:1507): The guard '((phase = 3) & (n = 18))' is unsatisfiable.
Time for model construction: 2.130s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	317718526 (101577 nodes)
Transitions: 	318767101 (226124 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (334 DD variables), columns: 87 meta variables (334 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (335 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 3205.226s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	317718526
Transitions: 	318767101
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 162386943 item(s)
   * knowA -> 166571519 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep5.umb'.
Time for model export: 11.572s.


Performance statistics:
  * peak memory usage: 15240MB
  * CPU time: 3196.799s
  * wallclock time: 3219.169s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-8/model_rep5.umb:	Size of output file is 7800892416 bytes
Removing output file to save space for repetition #5
```

