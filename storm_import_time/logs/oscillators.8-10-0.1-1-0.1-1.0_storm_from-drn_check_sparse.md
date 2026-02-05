# Log files

Tool configuration: storm_from-drn_check_sparse
Benchmark: [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)
Parsed values: [0.055, 0.251, 0.077, 0.093, 0.079]



### Log file: storm_from-drn_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.122 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:20:46 2026
Command line arguments: --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 0.055s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	2 labels
   * target -> 2 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.019s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.090s
  * wallclock time: 0.080s
```



### Log file: storm_from-drn_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.463 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:05:39 2026
Command line arguments: --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 0.251s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	2 labels
   * target -> 2 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.080s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.340s
  * wallclock time: 0.339s
```



### Log file: storm_from-drn_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.142 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:28:43 2026
Command line arguments: --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 0.077s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	2 labels
   * target -> 2 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.019s.

Performance statistics:
  * peak memory usage: 33MB
  * CPU time: 0.086s
  * wallclock time: 0.100s
```



### Log file: storm_from-drn_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.153 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:07:37 2026
Command line arguments: --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 0.093s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	2 labels
   * target -> 2 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.018s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.085s
  * wallclock time: 0.115s
```



### Log file: storm_from-drn_check_sparse_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Wallclock time: 0.142 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:15:20 2026
Command line arguments: --timemem --buildfull --explicit-drn models/oscillators.8-10-0.1-1-0.1-1.0/storm.model.drn --digits 17 --prop models/oscillators.8-10-0.1-1-0.1-1.0/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 0.079s.

-------------------------------------------------------------- 
Model type: 	DTMC (sparse)
States: 	24311
Transitions: 	76623
Reward Models:  time_to_synch
State Labels: 	2 labels
   * target -> 2 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "time_to_synch": R{"time_to_synch"}=? [F "target"] ...
Result (for initial states): 6.007420358
Time for model checking: 0.020s.

Performance statistics:
  * peak memory usage: 34MB
  * CPU time: 0.087s
  * wallclock time: 0.102s
```

