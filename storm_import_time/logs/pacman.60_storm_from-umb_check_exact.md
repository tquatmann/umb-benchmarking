# Log files

Tool configuration: storm_from-umb_check_exact
Benchmark: [pacman.60](../../models/pacman.60)
Parsed values: [23.702, 23.068, 23.26, 23.368, 28.209]



### Log file: storm_from-umb_check_exact_pacman.60_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Wallclock time: 66.876 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:43:12 2026
Command line arguments: --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.007s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.823s seconds.
Time for model construction: 23.702s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * Crash -> 1819987 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 86110546416859324224933809991178655824964067/156250000000000000000000000000000000000000000 (approx. 0.5511074971)
Time for model checking: 41.468s.

Performance statistics:
  * peak memory usage: 19377MB
  * CPU time: 61.047s
  * wallclock time: 65.913s
```



### Log file: storm_from-umb_check_exact_pacman.60_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Wallclock time: 63.142 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:28:12 2026
Command line arguments: --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.827s seconds.
Time for model construction: 23.068s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * Crash -> 1819987 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 86110546416859324224933809991178655824964067/156250000000000000000000000000000000000000000 (approx. 0.5511074971)
Time for model checking: 38.456s.

Performance statistics:
  * peak memory usage: 19377MB
  * CPU time: 57.543s
  * wallclock time: 62.209s
```



### Log file: storm_from-umb_check_exact_pacman.60_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Wallclock time: 66.051 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:24 2026
Command line arguments: --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.033s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.962s seconds.
Time for model construction: 23.260s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * Crash -> 1819987 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 86110546416859324224933809991178655824964067/156250000000000000000000000000000000000000000 (approx. 0.5511074971)
Time for model checking: 41.138s.

Performance statistics:
  * peak memory usage: 19377MB
  * CPU time: 60.221s
  * wallclock time: 65.140s
```



### Log file: storm_from-umb_check_exact_pacman.60_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Wallclock time: 65.802 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:21:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.007s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.824s seconds.
Time for model construction: 23.368s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * Crash -> 1819987 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 86110546416859324224933809991178655824964067/156250000000000000000000000000000000000000000 (approx. 0.5511074971)
Time for model checking: 40.764s.

Performance statistics:
  * peak memory usage: 19376MB
  * CPU time: 60.070s
  * wallclock time: 64.875s
```



### Log file: storm_from-umb_check_exact_pacman.60_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Wallclock time: 83.945 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:56:24 2026
Command line arguments: --timemem --buildfull --explicit-umb models/pacman.60/storm.model.exact.umb --prop models/pacman.60/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 1.060s seconds.
Time for model construction: 28.209s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	38786521
Transitions: 	53648196
Choices: 	48926255
Reward Models:  none
State Labels: 	3 labels
   * deadlock -> 0 item(s)
   * Crash -> 1819987 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "crash": Pmin=? [F "Crash"] ...
Result (for initial states): 86110546416859324224933809991178655824964067/156250000000000000000000000000000000000000000 (approx. 0.5511074971)
Time for model checking: 53.568s.

Performance statistics:
  * peak memory usage: 19376MB
  * CPU time: 76.272s
  * wallclock time: 82.721s
```

