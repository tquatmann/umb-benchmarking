# Log files

Tool configuration: storm_from-prism_check_sparse
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [46.551, 43.137, 43.412, 43.166, 42.968]



### Log file: storm_from-prism_check_sparse_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
Wallclock time: 46.551 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:01:35 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 2.109s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 141117 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 44.375s.

Performance statistics:
  * peak memory usage: 201MB
  * CPU time: 46.276s
  * wallclock time: 46.492s
```



### Log file: storm_from-prism_check_sparse_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
Wallclock time: 43.137 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
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
Time for model input parsing: 0.003s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 2.139s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 141117 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 40.920s.

Performance statistics:
  * peak memory usage: 200MB
  * CPU time: 42.964s
  * wallclock time: 43.068s
```



### Log file: storm_from-prism_check_sparse_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
Wallclock time: 43.412 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 2.127s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 141117 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 41.229s.

Performance statistics:
  * peak memory usage: 201MB
  * CPU time: 43.241s
  * wallclock time: 43.375s
```



### Log file: storm_from-prism_check_sparse_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
Wallclock time: 43.166 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:13:17 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
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
Time for model input parsing: 0.012s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 2.103s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 141117 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 40.998s.

Performance statistics:
  * peak memory usage: 201MB
  * CPU time: 42.927s
  * wallclock time: 43.132s
```



### Log file: storm_from-prism_check_sparse_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
Wallclock time: 42.968 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:59:27 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 2.096s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	597012
Transitions: 	2908192
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 141117 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001072402534
Time for model checking: 40.806s.

Performance statistics:
  * peak memory usage: 200MB
  * CPU time: 42.785s
  * wallclock time: 42.934s
```

