# Log files

Tool configuration: storm_from-jani_check_cudd
Benchmark: [pnueli-zuck.5](../../models/pnueli-zuck.5)
Parsed values: [0.574, 0.5840000000000001, 0.703, 0.573, 0.603]



### Log file: storm_from-jani_check_cudd_pnueli-zuck.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.857 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:52:33 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.022s.

Time for model construction: 0.061s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.491s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "live": Pmax=? [F "target"] ...
Result (for initial states): 1
Time for model checking: 0.152s.

Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.702s
  * wallclock time: 0.732s
```



### Log file: storm_from-jani_check_cudd_pnueli-zuck.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.794 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:12:23 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.005s.

Time for model construction: 0.058s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.521s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "live": Pmax=? [F "target"] ...
Result (for initial states): 1
Time for model checking: 0.159s.

Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.734s
  * wallclock time: 0.750s
```



### Log file: storm_from-jani_check_cudd_pnueli-zuck.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.957 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:16 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.028s.

Time for model construction: 0.070s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.605s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "live": Pmax=? [F "target"] ...
Result (for initial states): 1
Time for model checking: 0.196s.

Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.878s
  * wallclock time: 0.906s
```



### Log file: storm_from-jani_check_cudd_pnueli-zuck.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.790 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:22:35 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.021s.

Time for model construction: 0.059s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.493s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "live": Pmax=? [F "target"] ...
Result (for initial states): 1
Time for model checking: 0.149s.

Performance statistics:
  * peak memory usage: 163MB
  * CPU time: 0.705s
  * wallclock time: 0.730s
```



### Log file: storm_from-jani_check_cudd_pnueli-zuck.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty  --engine dd-to-sparse --ddlib cudd --cudd:maxmem 8192
Wallclock time: 0.819 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:52:16 2026
Command line arguments: --timemem --buildfull --jani models/pnueli-zuck.5/model.jani --janiproperty --engine dd-to-sparse --ddlib cudd '--cudd:maxmem' 8192
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model input parsing: 0.026s.

Time for model construction: 0.055s.

-------------------------------------------------------------- 
Model type: 	MDP (symbolic)
States: 	397435 (144 nodes)
Transitions: 	2492035 (5259 nodes)
Choices: 	2323315
Reward Models:  none
Variables: 	rows: 10 meta variables (25 DD variables), columns: 10 meta variables (25 DD variables), nondeterminism: 4 meta variables (4 DD variables)
Labels: 	3
   * deadlock -> 0 state(s) (1 nodes)
   * init -> 1 state(s) (26 nodes)
   * target
-------------------------------------------------------------- 

Time for model preprocessing: 0.522s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	397435
Transitions: 	2492035
Choices: 	2323315
Reward Models:  none
State Labels: 	3 labels
   * target -> 10000 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "live": Pmax=? [F "target"] ...
Result (for initial states): 1
Time for model checking: 0.173s.

Performance statistics:
  * peak memory usage: 162MB
  * CPU time: 0.739s
  * wallclock time: 0.781s
```

