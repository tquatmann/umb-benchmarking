# Log files for storm_from-umb-gz_check_sparse on model [eajs.5-250-11](../../models/eajs.5-250-11)

Parsed values: `[0.495, 0.526, 0.59, 0.578, 0.784]`



### Log file: storm_from-umb-gz_check_sparse_eajs.5-250-11_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Wallclock time: 2.433 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 07:59:31 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.028s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.345s seconds.
Time for model construction: 0.495s.

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
Time for model checking: 1.865s.

Performance statistics:
  * peak memory usage: 804MB
  * CPU time: 2.161s
  * wallclock time: 2.390s
```



### Log file: storm_from-umb-gz_check_sparse_eajs.5-250-11_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Wallclock time: 2.425 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:01 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.388s seconds.
Time for model construction: 0.526s.

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
Time for model checking: 1.773s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.085s
  * wallclock time: 2.311s
```



### Log file: storm_from-umb-gz_check_sparse_eajs.5-250-11_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Wallclock time: 2.617 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:14:55 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.436s seconds.
Time for model construction: 0.590s.

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
Time for model checking: 1.952s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.316s
  * wallclock time: 2.573s
```



### Log file: storm_from-umb-gz_check_sparse_eajs.5-250-11_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Wallclock time: 2.976 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:14:49 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.006s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.425s seconds.
Time for model construction: 0.578s.

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
Time for model checking: 2.314s.

Performance statistics:
  * peak memory usage: 805MB
  * CPU time: 2.642s
  * wallclock time: 2.925s
```



### Log file: storm_from-umb-gz_check_sparse_eajs.5-250-11_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Wallclock time: 4.770 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:06:05 2026
Command line arguments: --timemem --buildfull --explicit-umb models/eajs.5-250-11/storm.model.umb.gz --prop models/eajs.5-250-11/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.015s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.489s seconds.
Time for model construction: 0.784s.

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
Time for model checking: 3.893s.

Performance statistics:
  * peak memory usage: 803MB
  * CPU time: 3.933s
  * wallclock time: 4.718s
```

