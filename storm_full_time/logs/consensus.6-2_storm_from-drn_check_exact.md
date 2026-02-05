# Log files for storm_from-drn_check_exact on model [consensus.6-2](../../models/consensus.6-2)

Parsed values: `[7065.431, 6805.544, TO, 7189.59, 6717.122]`



### Log file: storm_from-drn_check_exact_consensus.6-2_rep1.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Wallclock time: 7065.431 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 02:45:17 2026
Command line arguments: --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 12.273s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	3 labels
   * finished -> 384 item(s)
   * init -> 1 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 7052.782s.

Performance statistics:
  * peak memory usage: 3314MB
  * CPU time: 7046.015s
  * wallclock time: 7065.183s
```



### Log file: storm_from-drn_check_exact_consensus.6-2_rep2.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Wallclock time: 6805.544 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 20:38:18 2026
Command line arguments: --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 11.742s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	3 labels
   * finished -> 384 item(s)
   * init -> 1 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6793.269s.

Performance statistics:
  * peak memory usage: 3316MB
  * CPU time: 6783.761s
  * wallclock time: 6805.139s
```



### Log file: storm_from-drn_check_exact_consensus.6-2_rep3.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Wallclock time: 7203.024 seconds
Return code: None (timeout)
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 00:49:54 2026
Command line arguments: --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 12.133s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	3 labels
   * finished -> 384 item(s)
   * init -> 1 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...

##############################Output to stderr##############################
ERROR: The program received signal 15 and will be aborted in 3s.
Received signal 14
```



### Log file: storm_from-drn_check_exact_consensus.6-2_rep4.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Wallclock time: 7189.590 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Thu Jan 29 03:04:03 2026
Command line arguments: --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 11.835s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	3 labels
   * finished -> 384 item(s)
   * init -> 1 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 7177.516s.

Performance statistics:
  * peak memory usage: 3316MB
  * CPU time: 7164.131s
  * wallclock time: 7189.446s
```



### Log file: storm_from-drn_check_exact_consensus.6-2_rep5.log

```
Command(s):
../bin/storm --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Wallclock time: 6717.122 seconds
Return code: 0
##############################
Storm 1.11.1 (dev)

Date: Wed Jan 28 22:08:06 2026
Command line arguments: --timemem --buildfull --explicit-drn models/consensus.6-2/storm.model.exact.drn --digits 17 --prop models/consensus.6-2/property.props --exact
Current working directory: /rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final

Time for model construction: 11.805s.

-------------------------------------------------------------- 
Model type: 	MDP (sparse)
States: 	1258240
Transitions: 	6236736
Choices: 	5008128
Reward Models:  none
State Labels: 	3 labels
   * finished -> 384 item(s)
   * init -> 1 item(s)
   * agree -> 114258 item(s)
Choice Labels: 	none
-------------------------------------------------------------- 

Model checking property "disagree": Pmax=? [F ("finished" & (!"agree"))] ...
Result (for initial states): 37101798760906709/102027593703751680 (approx. 0.3636447496)
Time for model checking: 6705.086s.

Performance statistics:
  * peak memory usage: 3316MB
  * CPU time: 6705.148s
  * wallclock time: 6716.971s
```

