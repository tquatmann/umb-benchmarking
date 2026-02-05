# Log files

Tool configuration: modest_from-umb_check_default
Benchmark: [firewire.false-36-800](../../models/firewire.false-36-800)
Parsed values: [1.0, TO, TO, TO, TO]



### Log file: modest_from-umb_check_default_firewire.false-36-800_rep1.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7.550 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 62 MB
Analysis results for UMB

+ State space (UMB)
  States:            212268
  Choices:           478756
  Branches:          481792
  Time (decompress): 0.1 s
  Time (validate):   0.4 s
  Time (load):       0.5 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        7.0 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        6.9 s

```



### Log file: modest_from-umb_check_default_firewire.false-36-800_rep2.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.161 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt -D --exhaustive



```



### Log file: modest_from-umb_check_default_firewire.false-36-800_rep3.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.018 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt -D --exhaustive




##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateRewardBoundedModified(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
```



### Log file: modest_from-umb_check_default_firewire.false-36-800_rep4.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.005 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt -D --exhaustive




##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
```



### Log file: modest_from-umb_check_default_firewire.false-36-800_rep5.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.014 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/modest.model.umb models/firewire.false-36-800/modest.umb.properties.txt -D --exhaustive



```

