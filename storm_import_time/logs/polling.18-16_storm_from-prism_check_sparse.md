# Log files

Tool configuration: storm_from-prism_check_sparse
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [72.279, 61.163000000000004, 62.168, 59.966, 62.319]



### Log file: storm_from-prism_check_sparse_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
Wallclock time: 83.123 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:41:38 2026
Command line arguments: --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
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
Time for model construction: 72.259s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.791s.

Performance statistics:
  * peak memory usage: 5744MB
  * CPU time: 81.986s
  * wallclock time: 83.079s
```



### Log file: storm_from-prism_check_sparse_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
Wallclock time: 71.116 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:07:35 2026
Command line arguments: --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
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
Time for model construction: 61.158s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 9.900s.

Performance statistics:
  * peak memory usage: 5742MB
  * CPU time: 69.948s
  * wallclock time: 71.073s
```



### Log file: storm_from-prism_check_sparse_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
Wallclock time: 73.201 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:00:57 2026
Command line arguments: --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
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
Time for model input parsing: 0.006s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 62.162s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.985s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 72.121s
  * wallclock time: 73.162s
```



### Log file: storm_from-prism_check_sparse_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
Wallclock time: 70.492 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:06 2026
Command line arguments: --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 59.958s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 9.989s.

Performance statistics:
  * peak memory usage: 5742MB
  * CPU time: 68.984s
  * wallclock time: 69.965s
```



### Log file: storm_from-prism_check_sparse_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
Wallclock time: 72.310 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:07:38 2026
Command line arguments: --timemem --buildfull --prism models/polling.18-16/model.prism --prismcompat --prop models/polling.18-16/property.props
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

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
WARN  (Program.cpp:1654): The model uses synchronizing Markovian commands. This may lead to unexpected verification results, because of unclear semantics.
Time for model construction: 62.302s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
   * serve_s2 -> 131072 item(s)
   * serve_s1 -> 131072 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 9.922s.

Performance statistics:
  * peak memory usage: 5743MB
  * CPU time: 71.290s
  * wallclock time: 72.263s
```

