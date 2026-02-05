# Log files

Tool configuration: storm_from-prism_check_sparse
Benchmark: [embedded.8-12](../../models/embedded.8-12)
Parsed values: [0.109, 1.442, 0.105, 0.124, 0.132]



### Log file: storm_from-prism_check_sparse_embedded.8-12_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
Wallclock time: 0.109 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:00:04 2026
Command line arguments: --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
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
Time for model input parsing: 0.005s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.043s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * init -> 1 item(s)
   * l_down -> 5884 item(s)
   * deadlock -> 0 item(s)
   * fail_actuators -> 1064 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": P=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036557
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 63MB
  * CPU time: 0.069s
  * wallclock time: 0.057s
```



### Log file: storm_from-prism_check_sparse_embedded.8-12_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
Wallclock time: 1.442 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:08 2026
Command line arguments: --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
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
Time for model input parsing: 0.024s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.039s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * init -> 1 item(s)
   * l_down -> 5884 item(s)
   * deadlock -> 0 item(s)
   * fail_actuators -> 1064 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": P=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036557
Time for model checking: 0.003s.

Performance statistics:
  * peak memory usage: 62MB
  * CPU time: 0.058s
  * wallclock time: 0.071s
```



### Log file: storm_from-prism_check_sparse_embedded.8-12_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
Wallclock time: 0.105 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:55 2026
Command line arguments: --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
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
Time for model construction: 0.057s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * init -> 1 item(s)
   * l_down -> 5884 item(s)
   * deadlock -> 0 item(s)
   * fail_actuators -> 1064 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": P=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036557
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 61MB
  * CPU time: 0.053s
  * wallclock time: 0.068s
```



### Log file: storm_from-prism_check_sparse_embedded.8-12_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
Wallclock time: 0.124 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:56:54 2026
Command line arguments: --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 0.038s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * init -> 1 item(s)
   * l_down -> 5884 item(s)
   * deadlock -> 0 item(s)
   * fail_actuators -> 1064 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": P=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036557
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 63MB
  * CPU time: 0.054s
  * wallclock time: 0.088s
```



### Log file: storm_from-prism_check_sparse_embedded.8-12_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
Wallclock time: 0.132 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:08:42 2026
Command line arguments: --timemem --buildfull --prism models/embedded.8-12/model.prism --prismcompat --prop models/embedded.8-12/property.props
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
Time for model construction: 0.039s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	8548
Transitions: 	36041
Reward Models:  none
State Labels: 	4 labels
   * init -> 1 item(s)
   * l_down -> 5884 item(s)
   * deadlock -> 0 item(s)
   * fail_actuators -> 1064 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "actuators": P=? [(!"l_down") U "fail_actuators"] ...
Result (for initial states): 0.1053036557
Time for model checking: 0.002s.

Performance statistics:
  * peak memory usage: 62MB
  * CPU time: 0.074s
  * wallclock time: 0.050s
```

