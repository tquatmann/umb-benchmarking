# Log files for storm_from-prism_check_sparse on model [speed-ind.2100](../../models/speed-ind.2100)

Parsed values: `[4.3069999999999995, 4.813, 4.2250000000000005, 3.75, 4.385]`



### Log file: storm_from-prism_check_sparse_speed-ind.2100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Wallclock time: 81.012 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:48:24 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.012s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 4.295s.

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
Result (for initial states): 0.04229449798
Time for model checking: 76.642s.

Performance statistics:
  * peak memory usage: 770MB
  * CPU time: 80.569s
  * wallclock time: 80.965s
```



### Log file: storm_from-prism_check_sparse_speed-ind.2100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Wallclock time: 108.276 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:04:02 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.013s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 4.800s.

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
Result (for initial states): 0.04229449798
Time for model checking: 103.401s.

Performance statistics:
  * peak memory usage: 770MB
  * CPU time: 107.615s
  * wallclock time: 108.221s
```



### Log file: storm_from-prism_check_sparse_speed-ind.2100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Wallclock time: 86.119 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:27:11 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.014s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 4.211s.

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
Result (for initial states): 0.04229449798
Time for model checking: 81.822s.

Performance statistics:
  * peak memory usage: 770MB
  * CPU time: 85.680s
  * wallclock time: 86.078s
```



### Log file: storm_from-prism_check_sparse_speed-ind.2100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Wallclock time: 81.448 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:11:45 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.020s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 3.730s.

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
Result (for initial states): 0.04229449798
Time for model checking: 77.652s.

Performance statistics:
  * peak memory usage: 769MB
  * CPU time: 81.099s
  * wallclock time: 81.408s
```



### Log file: storm_from-prism_check_sparse_speed-ind.2100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Wallclock time: 79.651 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:06 2026
Command line arguments: --timemem --buildfull --prism models/speed-ind.2100/model.prism --prismcompat --prop models/speed-ind.2100/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

WARN  (Program.cpp:238): The input model is a CTMC, but uses probabilistic commands like they are used in PRISM. Consider rewriting the commands to use Markovian commands instead.
Time for model input parsing: 0.011s.

WARN  (FormulaParserGrammar.cpp:346): Identifier `T' coincides with a reserved keyword or operator. Property expressions using the variable or constant 'T' might not be parsed correctly.
Time for model construction: 4.374s.

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
Result (for initial states): 0.04229449798
Time for model checking: 75.218s.

Performance statistics:
  * peak memory usage: 769MB
  * CPU time: 79.279s
  * wallclock time: 79.608s
```

