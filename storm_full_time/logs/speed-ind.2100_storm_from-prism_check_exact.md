# Log files for storm_from-prism_check_exact on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: storm_from-prism_check_exact_speed-ind.2100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Wallclock time: 29.487 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:45:17 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.018s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
Time for model construction: 29.084s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 24576 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 1725MB
  * CPU time: 28.763s
  * wallclock time: 29.275s
```



### Log file: storm_from-prism_check_exact_speed-ind.2100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Wallclock time: 29.110 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:24:16 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.022s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
Time for model construction: 28.706s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 24576 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 1726MB
  * CPU time: 28.348s
  * wallclock time: 28.896s
```



### Log file: storm_from-prism_check_exact_speed-ind.2100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Wallclock time: 30.018 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:49:42 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.046s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
Time for model construction: 29.480s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 24576 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 1725MB
  * CPU time: 29.172s
  * wallclock time: 29.695s
```



### Log file: storm_from-prism_check_exact_speed-ind.2100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Wallclock time: 28.998 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:12:16 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.014s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
Time for model construction: 28.578s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 24576 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 1726MB
  * CPU time: 28.272s
  * wallclock time: 28.766s
```



### Log file: storm_from-prism_check_exact_speed-ind.2100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Wallclock time: 30.349 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:00:29 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.016s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (storm-cli.cpp:27): The model checking query does not seem to be supported for the selected engine. Storm will try to solve the query, but you will most likely get an error for at least one of the provided properties.
Time for model construction: 29.895s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	743424
Transitions: 	9518080
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 24576 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
ERROR (model-handling.h:1082): Property is unsupported by selected engine/settings.


Performance statistics:
  * peak memory usage: 1726MB
  * CPU time: 29.502s
  * wallclock time: 30.089s
```

