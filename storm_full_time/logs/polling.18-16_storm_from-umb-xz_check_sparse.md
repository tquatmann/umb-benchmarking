# Log files

Tool configuration: storm_from-umb-xz_check_sparse
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [18.088, 16.323, 16.012, 17.123, 16.938]



### Log file: storm_from-umb-xz_check_sparse_polling.18-16_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Wallclock time: 18.088 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:30:13 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.011s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 5.358s seconds.
Time for model construction: 6.280s.

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
Time for model checking: 11.737s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 17.058s
  * wallclock time: 18.046s
```



### Log file: storm_from-umb-xz_check_sparse_polling.18-16_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Wallclock time: 16.323 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:02 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.019s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 5.348s seconds.
Time for model construction: 6.249s.

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
Time for model checking: 10.014s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 15.376s
  * wallclock time: 16.286s
```



### Log file: storm_from-umb-xz_check_sparse_polling.18-16_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Wallclock time: 16.012 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:16:58 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.031s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 5.341s seconds.
Time for model construction: 6.234s.

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
Time for model checking: 9.692s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 15.052s
  * wallclock time: 15.975s
```



### Log file: storm_from-umb-xz_check_sparse_polling.18-16_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Wallclock time: 17.123 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 21:23:58 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.021s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 5.731s seconds.
Time for model construction: 6.676s.

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
Time for model checking: 10.396s.

Performance statistics:
  * peak memory usage: 5731MB
  * CPU time: 15.764s
  * wallclock time: 17.078s
```



### Log file: storm_from-umb-xz_check_sparse_polling.18-16_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Wallclock time: 16.938 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:20:33 2026
Command line arguments: --timemem --buildfull --explicit-umb models/polling.18-16/storm.model.umb.xz --prop models/polling.18-16/property.props
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.012s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 5.711s seconds.
Time for model construction: 6.638s.

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
Time for model checking: 10.235s.

Performance statistics:
  * peak memory usage: 5732MB
  * CPU time: 15.882s
  * wallclock time: 16.893s
```

