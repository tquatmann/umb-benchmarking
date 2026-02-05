# Log files for modest_from-umb_check_default on model [crowds.6-20](../../models/crowds.6-20)

Parsed values: `[1.6, TO, 4.2, TO, TO]`



### Log file: modest_from-umb_check_default_crowds.6-20_rep1.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 36.198 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 864 MB
Analysis results for UMB

+ State space (UMB)
  States:            10633591
  Choices:           10633591
  Branches:          38261191
  Time (decompress): 0.1 s
  Time (validate):   0.7 s
  Time (load):       0.8 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        35.3 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        35.2 s

```



### Log file: modest_from-umb_check_default_crowds.6-20_rep2.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.018 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt -D --exhaustive




##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.ValueIteration.PerformUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, System.Nullable`1<UInt64>, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken, Boolean, Int64 ByRef, Double ByRef, Boolean ByRef)
   at Modest.ModelChecking.ValueIteration.PerformPartitionUnboundedValueIteration(Modest.ModelChecking.PropertyAnalysisTask, Partition, Int64, UnboundedValueIterationPartitionData, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration+<>c__DisplayClass7_0.<IterateUnbounded>g__FixpointStep|1(Int32, Int32, Modest.Modularity.OperationState)
   at Modest.StateSpace.Helpers.IteratePartitions(Modest.StateSpace.StateSpace, System.Action`2<Int32,Modest.Modularity.OperationState>, System.Func`4<Int32,Int32,Modest.Modularity.OperationState,Boolean>, System.Action`2<Int32,Modest.Modularity.OperationState>, Modest.Modularity.OperationState)
   at Modest.ModelChecking.ValueIteration.IterateUnbounded(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.LocationErrorHandler, Modest.Modularity.OperationState)
```



### Log file: modest_from-umb_check_default_crowds.6-20_rep3.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 10.091 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 863 MB
Analysis results for UMB

+ State space (UMB)
  States:            10633591
  Choices:           10633591
  Branches:          38261191
  Time (decompress): 0.1 s
  Time (validate):   2.0 s
  Time (load):       2.1 s

+ Property positive
  Probability: 0.1204761609299478
  Bounds:      [0.1204761609299478, 1]
  Time:        6.5 s

  + Value iteration
    Final error: 8.778542281008603E-07
    Iterations:  63
    Time:        6.5 s

```



### Log file: modest_from-umb_check_default_crowds.6-20_rep4.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.033 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt -D --exhaustive



```



### Log file: modest_from-umb_check_default_crowds.6-20_rep5.log

```
Command(s):
../bin/modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.036 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/crowds.6-20/modest.model.umb models/crowds.6-20/modest.umb.properties.txt -D --exhaustive



```

