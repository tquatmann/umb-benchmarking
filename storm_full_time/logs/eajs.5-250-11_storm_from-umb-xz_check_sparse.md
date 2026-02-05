# Log files

Tool configuration: storm_from-umb-xz_check_sparse
Benchmark: [eajs.5-250-11](../../models/eajs.5-250-11)
Parsed values: [3.848, 3.156, 3.129, 3.068, 3.599]



### Log file: storm_from-umb-xz_check_sparse_eajs.5-250-11_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Wallclock time: 3.848 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 08:02:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.022s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.840s seconds.
Time for model construction: 1.037s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4256193
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 10.03294069
Time for model checking: 2.732s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 3.510s
  * wallclock time: 3.795s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.5-250-11_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Wallclock time: 3.156 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:25:14 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.053s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.731s seconds.
Time for model construction: 0.916s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4256193
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 10.03294069
Time for model checking: 2.142s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.828s
  * wallclock time: 3.087s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.5-250-11_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Wallclock time: 3.129 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:19 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.095s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.790s seconds.
Time for model construction: 1.014s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4256193
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 10.03294069
Time for model checking: 2.060s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.771s
  * wallclock time: 3.085s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.5-250-11_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Wallclock time: 3.068 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:39 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.002s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.825s seconds.
Time for model construction: 0.968s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4256193
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 10.03294069
Time for model checking: 2.048s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.863s
  * wallclock time: 3.027s
```



### Log file: storm_from-umb-xz_check_sparse_eajs.5-250-11_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Wallclock time: 3.599 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:23 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.xz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.692s seconds.
Time for model construction: 0.831s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	3049471
Transitions: 	6977654
Choices: 	4256193
Reward Models:  utilityLocal
State Labels: 	3 labels
   * emptyBattery -> 13476 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "ExpUtil": R{"utilityLocal"}max=? [F "emptyBattery"] ...
Result (for initial states): 10.03294069
Time for model checking: 1.745s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.392s
  * wallclock time: 2.593s
```

