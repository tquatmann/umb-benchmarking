# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [cluster.64-2000-20](../../models/cluster.64-2000-20)
Parsed values: [ERR, ERR, ERR, ERR, ERR]



### Log file: storm_from-prism_check_exact_cluster.64-2000-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
Wallclock time: 1.578 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:00:02 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
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
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 1.507s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 149MB
  * CPU time: 1.502s
  * wallclock time: 1.527s
```



### Log file: storm_from-prism_check_exact_cluster.64-2000-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
Wallclock time: 1.731 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:19:01 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
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
Time for model input parsing: 0.079s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 1.523s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 148MB
  * CPU time: 1.493s
  * wallclock time: 1.622s
```



### Log file: storm_from-prism_check_exact_cluster.64-2000-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
Wallclock time: 1.719 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
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
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 1.497s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 149MB
  * CPU time: 1.500s
  * wallclock time: 1.528s
```



### Log file: storm_from-prism_check_exact_cluster.64-2000-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
Wallclock time: 1.667 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
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
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 1.564s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 148MB
  * CPU time: 1.557s
  * wallclock time: 1.586s
```



### Log file: storm_from-prism_check_exact_cluster.64-2000-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
Wallclock time: 1.730 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:11:46 2026
Command line arguments: --timemem --buildfull --prism models/cluster.64-2000-20/model.prism --prismcompat --prop models/cluster.64-2000-20/property.props --exact
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
Time for model input parsing: 0.021s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 1.637s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 148MB
  * CPU time: 1.641s
  * wallclock time: 1.678s
```

