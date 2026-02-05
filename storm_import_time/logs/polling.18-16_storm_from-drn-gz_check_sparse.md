# Log files

Tool configuration: storm_from-drn-gz_check_sparse
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [48.029, 39.806, 192.316, 41.146, 45.458]



### Log file: storm_from-drn-gz_check_sparse_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Wallclock time: 61.522 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:55:41 2026
Command line arguments: --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 48.029s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	3 labels
   * serve_s1 -> 131072 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.5390581563
Time for model checking: 13.428s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 59.664s
  * wallclock time: 61.465s
```



### Log file: storm_from-drn-gz_check_sparse_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Wallclock time: 49.590 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:26:08 2026
Command line arguments: --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 39.806s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	3 labels
   * serve_s1 -> 131072 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.5390581563
Time for model checking: 9.739s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 48.409s
  * wallclock time: 49.550s
```



### Log file: storm_from-drn-gz_check_sparse_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Wallclock time: 224.422 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:05:38 2026
Command line arguments: --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 192.316s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	3 labels
   * serve_s1 -> 131072 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.5390581563
Time for model checking: 31.935s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 220.461s
  * wallclock time: 224.266s
```



### Log file: storm_from-drn-gz_check_sparse_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Wallclock time: 51.142 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 01:11:43 2026
Command line arguments: --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 41.146s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	3 labels
   * serve_s1 -> 131072 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.5390581563
Time for model checking: 9.944s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 49.883s
  * wallclock time: 51.097s
```



### Log file: storm_from-drn-gz_check_sparse_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Wallclock time: 56.190 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:25 2026
Command line arguments: --timemem --buildfull --explicit-drn models/polling.18-16/storm.model.drn.gz --digits 17 --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 45.458s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	3 labels
   * serve_s1 -> 131072 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.5390581563
Time for model checking: 10.682s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 54.870s
  * wallclock time: 56.148s
```

