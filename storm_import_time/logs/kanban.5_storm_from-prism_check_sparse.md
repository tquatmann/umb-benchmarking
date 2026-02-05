# Log files for storm_from-prism_check_sparse on model [kanban.5](../../models/kanban.5)

Parsed values: `[14.608, 14.777, 14.729, 19.894, 17.745]`



### Log file: storm_from-prism_check_sparse_kanban.5_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Wallclock time: 23.864 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:32:50 2026
Command line arguments: --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model input parsing: 0.016s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 14.592s.

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

Model checking property "throughput": R{"throughput"}=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 9.198s.

Performance statistics:
  * peak memory usage: 2945MB
  * CPU time: 23.299s
  * wallclock time: 23.814s
```



### Log file: storm_from-prism_check_sparse_kanban.5_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Wallclock time: 24.138 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model input parsing: 0.008s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 14.769s.

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

Model checking property "throughput": R{"throughput"}=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 9.262s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 23.470s
  * wallclock time: 24.048s
```



### Log file: storm_from-prism_check_sparse_kanban.5_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Wallclock time: 23.780 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model input parsing: 0.010s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 14.719s.

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

Model checking property "throughput": R{"throughput"}=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 8.940s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 23.101s
  * wallclock time: 23.677s
```



### Log file: storm_from-prism_check_sparse_kanban.5_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Wallclock time: 37.269 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:59:26 2026
Command line arguments: --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model input parsing: 0.020s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 19.874s.

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

Model checking property "throughput": R{"throughput"}=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 17.303s.

Performance statistics:
  * peak memory usage: 2944MB
  * CPU time: 36.178s
  * wallclock time: 37.210s
```



### Log file: storm_from-prism_check_sparse_kanban.5_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Wallclock time: 28.559 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:18:00 2026
Command line arguments: --timemem --buildfull --prism models/kanban.5/model.prism --prismcompat --prop models/kanban.5/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model input parsing: 0.015s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 17.730s.

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

Model checking property "throughput": R{"throughput"}=? [LRA] ...
Result (for initial states): 0.307124777
Time for model checking: 10.756s.

Performance statistics:
  * peak memory usage: 2945MB
  * CPU time: 27.911s
  * wallclock time: 28.509s
```

