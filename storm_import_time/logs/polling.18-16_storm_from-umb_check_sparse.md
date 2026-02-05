# Log files for storm_from-umb_check_sparse on model [polling.18-16](../../models/polling.18-16)

Parsed values: `[1.547, 1.532, 1.593, 1.569, 1.446]`



### Log file: storm_from-umb_check_sparse_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Wallclock time: 13.305 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:40:36 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.565s seconds.
Time for model construction: 1.547s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 11.716s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 11.833s
  * wallclock time: 13.269s
```



### Log file: storm_from-umb_check_sparse_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Wallclock time: 11.905 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:22:16 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.022s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.613s seconds.
Time for model construction: 1.532s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.331s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 10.598s
  * wallclock time: 11.869s
```



### Log file: storm_from-umb_check_sparse_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Wallclock time: 12.354 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:14:18 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.643s seconds.
Time for model construction: 1.593s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.698s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 10.898s
  * wallclock time: 12.298s
```



### Log file: storm_from-umb_check_sparse_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Wallclock time: 12.249 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:08:43 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.582s seconds.
Time for model construction: 1.569s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.606s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 10.778s
  * wallclock time: 12.182s
```



### Log file: storm_from-umb_check_sparse_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Wallclock time: 11.562 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:07:15 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.015s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.549s seconds.
Time for model construction: 1.446s.

-------------------------------------------------------------- 
Model type: 	CTMC (sparse)
States: 	7077888
Transitions: 	69599232
Reward Models:  none
State Labels: 	4 labels
   * serve_s1 -> 131072 item(s)
   * deadlock -> 0 item(s)
   * serve_s2 -> 131072 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "s1_before_s2": P=? [(!"serve_s2") U "serve_s1"] ...
Result (for initial states): 0.539005252
Time for model checking: 10.056s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 10.382s
  * wallclock time: 11.520s
```

