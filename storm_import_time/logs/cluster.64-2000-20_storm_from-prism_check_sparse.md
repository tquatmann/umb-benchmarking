# Log files

Tool configuration: storm_from-prism_check_sparse
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [0.638, 0.633, 0.551, 0.5630000000000001, 0.663]



### Log file: storm_from-prism_check_sparse_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
Wallclock time: 13.041 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:01:36 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
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
Time for model construction: 0.634s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	151060
Transitions: 	733216
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 36133 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001044539673
Time for model checking: 12.348s.

Performance statistics:
  * peak memory usage: 87MB
  * CPU time: 12.952s
  * wallclock time: 12.991s
```



### Log file: storm_from-prism_check_sparse_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
Wallclock time: 13.229 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:15:51 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
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
Time for model construction: 0.629s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	151060
Transitions: 	733216
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 36133 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001044539673
Time for model checking: 12.539s.

Performance statistics:
  * peak memory usage: 86MB
  * CPU time: 13.110s
  * wallclock time: 13.178s
```



### Log file: storm_from-prism_check_sparse_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
Wallclock time: 11.056 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:15:51 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
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
Time for model input parsing: 0.013s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.538s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	151060
Transitions: 	733216
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 36133 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001044539673
Time for model checking: 10.448s.

Performance statistics:
  * peak memory usage: 87MB
  * CPU time: 10.959s
  * wallclock time: 11.017s
```



### Log file: storm_from-prism_check_sparse_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
Wallclock time: 11.715 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:06:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
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
Time for model input parsing: 0.011s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.552s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	151060
Transitions: 	733216
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 36133 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001044539673
Time for model checking: 10.419s.

Performance statistics:
  * peak memory usage: 85MB
  * CPU time: 10.952s
  * wallclock time: 10.997s
```



### Log file: storm_from-prism_check_sparse_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
Wallclock time: 12.891 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:03:00 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props
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
Time for model input parsing: 0.019s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.644s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	151060
Transitions: 	733216
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * minimum -> 36133 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "qos1": P=? [true U<=2000 (!"minimum")] ...
Result (for initial states): 0.001044539673
Time for model checking: 12.162s.

Performance statistics:
  * peak memory usage: 87MB
  * CPU time: 12.486s
  * wallclock time: 12.844s
```

