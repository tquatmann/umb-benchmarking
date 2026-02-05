# Log files

Tool configuration: storm_from-prism_check_exact
Benchmark: [cluster.128-2000-20](../../models/cluster.128-2000-20)
Parsed values: [6.026, 5.9559999999999995, 6.742, 6.568, 6.0840000000000005]



### Log file: storm_from-prism_check_exact_cluster.128-2000-20_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
Wallclock time: 6.189 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:03:07 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
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
Time for model construction: 6.023s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 473MB
  * CPU time: 5.983s
  * wallclock time: 6.085s
```



### Log file: storm_from-prism_check_exact_cluster.128-2000-20_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
Wallclock time: 6.138 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
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
Time for model construction: 5.935s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 473MB
  * CPU time: 5.897s
  * wallclock time: 6.012s
```



### Log file: storm_from-prism_check_exact_cluster.128-2000-20_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
Wallclock time: 6.914 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:22:06 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
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
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 6.738s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 473MB
  * CPU time: 6.701s
  * wallclock time: 6.805s
```



### Log file: storm_from-prism_check_exact_cluster.128-2000-20_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
Wallclock time: 6.822 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:50:14 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
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
Time for model input parsing: 0.116s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 6.452s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 473MB
  * CPU time: 6.362s
  * wallclock time: 6.655s
```



### Log file: storm_from-prism_check_exact_cluster.128-2000-20_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
Wallclock time: 6.252 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:58:56 2026
Command line arguments: --timemem --buildfull --prism models/cluster.128-2000-20/model.prism --prismcompat --prop models/cluster.128-2000-20/property.props --exact
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
Time for model input parsing: 0.009s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 6.075s.

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
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 473MB
  * CPU time: 6.027s
  * wallclock time: 6.156s
```

