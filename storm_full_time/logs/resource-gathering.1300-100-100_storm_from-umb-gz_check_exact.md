# Log files

Tool configuration: storm_from-umb-gz_check_exact
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [1015.461, 1011.842, 1161.846, 926.579, 928.49]



### Log file: storm_from-umb-gz_check_exact_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 1015.461 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:16:37 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.020s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.218s seconds.
Time for model construction: 1.765s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 1013.495s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 1010.915s
  * wallclock time: 1015.319s
```



### Log file: storm_from-umb-gz_check_exact_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 1011.842 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:05 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.022s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.203s seconds.
Time for model construction: 1.685s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 1007.418s.

Performance statistics:
  * peak memory usage: 2017MB
  * CPU time: 1004.258s
  * wallclock time: 1009.154s
```



### Log file: storm_from-umb-gz_check_exact_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 1161.846 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:29:22 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.018s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.192s seconds.
Time for model construction: 1.867s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 1159.697s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 1156.714s
  * wallclock time: 1161.635s
```



### Log file: storm_from-umb-gz_check_exact_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 926.579 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:26 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.014s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.162s seconds.
Time for model construction: 1.551s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 924.865s.

Performance statistics:
  * peak memory usage: 2018MB
  * CPU time: 923.328s
  * wallclock time: 926.462s
```



### Log file: storm_from-umb-gz_check_exact_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Wallclock time: 928.490 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:37:18 2026
Command line arguments: --timemem --buildfull --explicit-umb models/resource-gathering.1300-100-100/storm.model.exact.umb.gz --prop models/resource-gathering.1300-100-100/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

First pass: Index file loaded in 0.013s seconds.
Index file is #1 file in the archive.
Second pass: bin files loaded in 0.190s seconds.
Time for model construction: 1.587s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	958894
Transitions: 	3325526
Choices: 	3080702
Reward Models:  none
State Labels: 	3 labels
   * success -> 94 item(s)
   * deadlock -> 0 item(s)
   * init -> 1 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "prgoldgem": Pmax=? [true U<=1300 "success"] ...
Result (for initial states): 663060852524178402183203507211353729666956663727350680069210275332115007280621137868004961937357709723179891739352387145366201684190399713388720604667954409751611188058893055489955897549953315586276348761790028621965783364895926897299241911/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 (approx. 0.6630608525)
Time for model checking: 926.747s.

Performance statistics:
  * peak memory usage: 2017MB
  * CPU time: 925.220s
  * wallclock time: 928.381s
```

