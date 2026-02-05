# Log files for storm_from-prism_check_sparse on model [fms.8](../../models/fms.8)

Parsed values: `[44.577, 49.73, 45.322, 41.684, 41.756]`



### Log file: storm_from-prism_check_sparse_fms.8_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
Wallclock time: 44.577 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:44:46 2026
Command line arguments: --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
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
Time for model input parsing: 0.014s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 32.722s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}=? [LRA] ...
Result (for initial states): 116.6583013
Time for model checking: 11.780s.

Performance statistics:
  * peak memory usage: 4882MB
  * CPU time: 43.346s
  * wallclock time: 44.532s
```



### Log file: storm_from-prism_check_sparse_fms.8_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
Wallclock time: 49.730 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:18 2026
Command line arguments: --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
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
Time for model input parsing: 0.017s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 36.554s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}=? [LRA] ...
Result (for initial states): 116.6583013
Time for model checking: 12.993s.

Performance statistics:
  * peak memory usage: 4882MB
  * CPU time: 48.346s
  * wallclock time: 49.591s
```



### Log file: storm_from-prism_check_sparse_fms.8_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
Wallclock time: 45.322 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:30 2026
Command line arguments: --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
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
Time for model input parsing: 0.004s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 33.732s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}=? [LRA] ...
Result (for initial states): 116.6583013
Time for model checking: 11.529s.

Performance statistics:
  * peak memory usage: 4883MB
  * CPU time: 44.160s
  * wallclock time: 45.281s
```



### Log file: storm_from-prism_check_sparse_fms.8_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
Wallclock time: 41.684 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:12:45 2026
Command line arguments: --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
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
Time for model input parsing: 0.018s.

WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 31.322s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}=? [LRA] ...
Result (for initial states): 116.6583013
Time for model checking: 10.285s.

Performance statistics:
  * peak memory usage: 4883MB
  * CPU time: 40.625s
  * wallclock time: 41.647s
```



### Log file: storm_from-prism_check_sparse_fms.8_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
Wallclock time: 41.756 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:03 2026
Command line arguments: --timemem --buildfull --prism models/fms.8/model.prism --prismcompat --prop models/fms.8/property.props
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
Time for model construction: 31.316s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	4459455
Transitions: 	38533968
Reward Models:  productivity
State Labels: 	2 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "productivity": R{"productivity"}=? [LRA] ...
Result (for initial states): 116.6583013
Time for model checking: 10.284s.

Performance statistics:
  * peak memory usage: 4882MB
  * CPU time: 40.631s
  * wallclock time: 41.622s
```

