# Log files for storm_from-prism_check_sparse on model [majority.2100](../../models/majority.2100)

Parsed values: `[0.8610000000000001, 0.885, 0.922, 0.804, 0.906]`



### Log file: storm_from-prism_check_sparse_majority.2100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Wallclock time: 14.874 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:26:04 2026
Command line arguments: --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.051s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 0.810s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	192000
Transitions: 	1961600
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 3000 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
Result (for initial states): 0.05429919317
Time for model checking: 13.756s.

Performance statistics:
  * peak memory usage: 219MB
  * CPU time: 14.508s
  * wallclock time: 14.624s
```



### Log file: storm_from-prism_check_sparse_majority.2100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Wallclock time: 15.420 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:14:50 2026
Command line arguments: --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.013s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 0.872s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	192000
Transitions: 	1961600
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 3000 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
Result (for initial states): 0.05429919317
Time for model checking: 14.489s.

Performance statistics:
  * peak memory usage: 218MB
  * CPU time: 15.303s
  * wallclock time: 15.379s
```



### Log file: storm_from-prism_check_sparse_majority.2100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Wallclock time: 15.271 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:25:14 2026
Command line arguments: --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.019s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 0.903s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	192000
Transitions: 	1961600
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 3000 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
Result (for initial states): 0.05429919317
Time for model checking: 14.118s.

Performance statistics:
  * peak memory usage: 218MB
  * CPU time: 14.966s
  * wallclock time: 15.061s
```



### Log file: storm_from-prism_check_sparse_majority.2100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Wallclock time: 14.054 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:24 2026
Command line arguments: --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.005s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 0.799s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	192000
Transitions: 	1961600
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 3000 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
Result (for initial states): 0.05429919317
Time for model checking: 13.204s.

Performance statistics:
  * peak memory usage: 217MB
  * CPU time: 13.960s
  * wallclock time: 14.013s
```



### Log file: storm_from-prism_check_sparse_majority.2100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Wallclock time: 16.335 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:59 2026
Command line arguments: --timemem --buildfull --prism models/majority.2100/model.prism --prismcompat --prop models/majority.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.021s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 0.885s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	192000
Transitions: 	1961600
Reward Models:  none
State Labels: 	3 labels
   * init -> 1 item(s)
   * deadlock -> 0 item(s)
   * target -> 3000 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "change_state": P=? [true U<=2100 "target"] ...
Result (for initial states): 0.05429919317
Time for model checking: 15.381s.

Performance statistics:
  * peak memory usage: 217MB
  * CPU time: 16.196s
  * wallclock time: 16.291s
```

