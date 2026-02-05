# Log files

Tool configuration: storm_from-umb_check_sparse
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [0.051, 0.058, 0.03, 0.044, 0.03]



### Log file: storm_from-umb_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.132 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:57:13 2026
Command line arguments: --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.026s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.022s seconds.
Time for model construction: 0.051s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * target -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.017s.

Performance statistics:
  * peak memory usage: 35MB
  * CPU time: 0.040s
  * wallclock time: 0.087s
```



### Log file: storm_from-umb_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.111 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:30 2026
Command line arguments: --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.043s seconds.
Time for model construction: 0.058s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * target -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.018s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.033s
  * wallclock time: 0.078s
```



### Log file: storm_from-umb_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.989 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 02:49:43 2026
Command line arguments: --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.008s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.020s seconds.
Time for model construction: 0.030s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * target -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.017s.

Performance statistics:
  * peak memory usage: 35MB
  * CPU time: 0.031s
  * wallclock time: 0.055s
```



### Log file: storm_from-umb_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 1.260 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:07 2026
Command line arguments: --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.027s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.014s seconds.
Time for model construction: 0.044s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * target -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.018s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.040s
  * wallclock time: 0.068s
```



### Log file: storm_from-umb_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.102 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:29:13 2026
Command line arguments: --timemem --buildfull --explicit-umb models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.umb --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.008s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.018s seconds.
Time for model construction: 0.030s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	3 labels
   * target -> 2 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.022s.

Performance statistics:
  * peak memory usage: 35MB
  * CPU time: 0.045s
  * wallclock time: 0.055s
```

