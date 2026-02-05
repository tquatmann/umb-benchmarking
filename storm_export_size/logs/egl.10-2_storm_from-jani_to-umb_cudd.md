# Log files for storm_from-jani_to-umb_cudd on model [egl.10-2](../../models/egl.10-2)

Parsed values: `[1635265536.0, 1635265536.0, 1635265536.0, 1635265536.0, 1635265536.0]`



### Log file: storm_from-jani_to-umb_cudd_egl.10-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 320.086 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Tue Jan 27 23:49:58 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
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
Time for model construction: 0.253s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	66060286 (11963 nodes)
Transitions: 	67108861 (30776 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (172 DD variables), columns: 87 meta variables (172 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (173 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 317.451s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-2/model.umb'.
Time for model export: 2.324s.


Performance statistics:
  * peak memory usage: 3246MB
  * CPU time: 317.356s
  * wallclock time: 320.047s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-2/model.umb:	Size of output file is 1635265536 bytes
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep2.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 321.700 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:10 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep2.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.014s.

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
Time for model construction: 0.299s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	66060286 (11963 nodes)
Transitions: 	67108861 (30776 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (172 DD variables), columns: 87 meta variables (172 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (173 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 318.906s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep2.umb'.
Time for model export: 2.386s.


Performance statistics:
  * peak memory usage: 3245MB
  * CPU time: 318.791s
  * wallclock time: 321.623s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep2.umb:	Size of output file is 1635265536 bytes
Removing output file to save space for repetition #2
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep3.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 331.585 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 08:45:41 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep3.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

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
Time for model construction: 0.263s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	66060286 (11963 nodes)
Transitions: 	67108861 (30776 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (172 DD variables), columns: 87 meta variables (172 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (173 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 328.747s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep3.umb'.
Time for model export: 2.486s.


Performance statistics:
  * peak memory usage: 3246MB
  * CPU time: 328.717s
  * wallclock time: 331.539s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep3.umb:	Size of output file is 1635265536 bytes
Removing output file to save space for repetition #3
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep4.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 361.254 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 07:27:10 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep4.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
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
Time for model construction: 0.305s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	66060286 (11963 nodes)
Transitions: 	67108861 (30776 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (172 DD variables), columns: 87 meta variables (172 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (173 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 358.291s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep4.umb'.
Time for model export: 2.587s.


Performance statistics:
  * peak memory usage: 3246MB
  * CPU time: 358.145s
  * wallclock time: 361.205s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep4.umb:	Size of output file is 1635265536 bytes
Removing output file to save space for repetition #4
```



### Log file: storm_from-jani_to-umb_cudd_egl.10-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep5.umb umb --compression none  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 354.231 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 09:28:17 2026
Command line arguments: --timemem --buildfull --jani models/egl.10-2/model.jani --exportbuild out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep5.umb umb --compression none --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

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
Time for model construction: 0.352s.

-------------------------------------------------------------- 
Model type: 	DTMC (symbolic)
States: 	66060286 (11963 nodes)
Transitions: 	67108861 (30776 nodes)
Reward Models:  none
Variables: 	rows: 87 meta variables (172 DD variables), columns: 87 meta variables (172 DD variables)
Labels: 	4
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (173 nodes)
   * knowA
   * knowB
-------------------------------------------------------------- 

Time for model preprocessing: 351.276s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	66060286
Transitions: 	67108861
Reward Models:  none
State Labels: 	4 labels
   * knowB -> 36680703 item(s)
   * knowA -> 40865279 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Exporting model to 'out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep5.umb'.
Time for model export: 2.526s.


Performance statistics:
  * peak memory usage: 3246MB
  * CPU time: 351.194s
  * wallclock time: 354.174s

############################## Output files ##############################
out/storm_from-jani_to-umb_cudd/egl.10-2/model_rep5.umb:	Size of output file is 1635265536 bytes
Removing output file to save space for repetition #5
```

