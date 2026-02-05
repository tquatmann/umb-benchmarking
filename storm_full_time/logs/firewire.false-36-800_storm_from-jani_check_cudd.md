# Log files for storm_from-jani_check_cudd on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[10.835, 10.962, 12.171, 12.194, 10.749]`



### Log file: storm_from-jani_check_cudd_firewire.false-36-800_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.835 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:32:19 2026
Command line arguments: --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.027s.

Time for model construction: 0.531s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	212268 (16296 nodes)
Transitions: 	481792 (77836 nodes)
Choices: 	478756
Reward Models:  time
Variables: 	rows: 14 meta variables (60 DD variables), columns: 14 meta variables (60 DD variables), nondeterminism: 14 meta variables (14 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * done
-------------------------------------------------------------- 

Time for model preprocessing: 0.883s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * done -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 0.939453125
Time for model checking: 9.336s.

Performance statistics:
  * peak memory usage: 203MB
  * CPU time: 10.716s
  * wallclock time: 10.793s
```



### Log file: storm_from-jani_check_cudd_firewire.false-36-800_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.962 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.004s.

Time for model construction: 0.600s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	212268 (16296 nodes)
Transitions: 	481792 (77836 nodes)
Choices: 	478756
Reward Models:  time
Variables: 	rows: 14 meta variables (60 DD variables), columns: 14 meta variables (60 DD variables), nondeterminism: 14 meta variables (14 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * done
-------------------------------------------------------------- 

Time for model preprocessing: 0.816s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * done -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 0.939453125
Time for model checking: 9.416s.

Performance statistics:
  * peak memory usage: 202MB
  * CPU time: 10.797s
  * wallclock time: 10.854s
```



### Log file: storm_from-jani_check_cudd_firewire.false-36-800_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 12.171 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:03:31 2026
Command line arguments: --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.044s.

Time for model construction: 0.599s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	212268 (16296 nodes)
Transitions: 	481792 (77836 nodes)
Choices: 	478756
Reward Models:  time
Variables: 	rows: 14 meta variables (60 DD variables), columns: 14 meta variables (60 DD variables), nondeterminism: 14 meta variables (14 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * done
-------------------------------------------------------------- 

Time for model preprocessing: 0.915s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * done -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 0.939453125
Time for model checking: 10.395s.

Performance statistics:
  * peak memory usage: 203MB
  * CPU time: 11.852s
  * wallclock time: 11.969s
```



### Log file: storm_from-jani_check_cudd_firewire.false-36-800_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 12.194 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:49:24 2026
Command line arguments: --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 0.627s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	212268 (16296 nodes)
Transitions: 	481792 (77836 nodes)
Choices: 	478756
Reward Models:  time
Variables: 	rows: 14 meta variables (60 DD variables), columns: 14 meta variables (60 DD variables), nondeterminism: 14 meta variables (14 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * done
-------------------------------------------------------------- 

Time for model preprocessing: 0.905s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * done -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 0.939453125
Time for model checking: 10.558s.

Performance statistics:
  * peak memory usage: 201MB
  * CPU time: 11.865s
  * wallclock time: 12.130s
```



### Log file: storm_from-jani_check_cudd_firewire.false-36-800_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 10.749 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:58 2026
Command line arguments: --timemem --buildfull --jani models/firewire.false-36-800/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.011s.

Time for model construction: 0.539s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	212268 (16296 nodes)
Transitions: 	481792 (77836 nodes)
Choices: 	478756
Reward Models:  time
Variables: 	rows: 14 meta variables (60 DD variables), columns: 14 meta variables (60 DD variables), nondeterminism: 14 meta variables (14 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (61 nodes)
   * done
-------------------------------------------------------------- 

Time for model preprocessing: 0.798s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	212268
Transitions: 	481792
Choices: 	478756
Reward Models:  time
State Labels: 	3 labels
   * done -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "deadline": Pmin=? [true Urew{"time"}<=800 "done"] ...
Result (for initial states): 0.939453125
Time for model checking: 9.348s.

Performance statistics:
  * peak memory usage: 202MB
  * CPU time: 10.634s
  * wallclock time: 10.710s
```

