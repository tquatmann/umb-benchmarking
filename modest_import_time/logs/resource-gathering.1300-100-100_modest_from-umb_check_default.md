# Log files

Tool configuration: modest_from-umb_check_default
Benchmark: [resource-gathering.1300-100-100](../../models/resource-gathering.1300-100-100)
Parsed values: [1.6, TO, 1.2, 1.2, TO]



### Log file: modest_from-umb_check_default_resource-gathering.1300-100-100_rep1.log

```
Command(s):
../bin/modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 27.054 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 133 MB
Analysis results for UMB

+ State space (UMB)
  States:            948693
  Choices:           3050099
  Branches:          3294923
  Time (decompress): 0.1 s
  Time (validate):   0.7 s
  Time (load):       0.8 s

+ Property prgoldgem
  Probability: 0.6630608525241822
  Bounds:      [0.6630608525241822, 0.6630608525241822]
  CDF:         { (0, 0), ..., (1199, 0), (1200, 7.0550791086553654E-10), (1201, 7.0550791086553654E-10), (1202, 7.8389767873948506E-10), (1203, 7.7684259963083002E-09), (1204, 7.8389767873948519E-09), (1205, 1.4908949951946258E-08), (1206, 4.9840301513998593E-08), (1207, 5.1237207177512345E-08), (1208, 1.1805735082117689E-07), (1209, 2.363474408631716E-07), (1210, 2.751839704280749E-07), (1211, 6.0617339875948095E-07), (1212, 9.1586815326840259E-07), (1213, 1.2493339039053002E-06), (1214, 2.3669570082041941E-06), (1215, 3.1356733357303078E-06), (1216, 4.7467593486416863E-06), (1217, 7.6403606716763388E-06), (1218, 9.8624903270049519E-06), (1219, 1.5260746029703193E-05), (1220, 2.1622763536033865E-05), (1221, 2.8592009565092682E-05), (1222, 4.2509727750559321E-05), (1223, 5.5892404142287892E-05), (1224, 7.5758419748182869E-05), (1225, 0.00010553586709131434), (1226, 0.00013481920290011939), (1227, 0.00018285039469700796), (1228, 0.00023986845887096465), (1229, 0.00030522060275988989), (1230, 0.00040432624279823816), (1231, 0.0005094225506899067), (1232, 0.00064784338134533004), (1233, 0.00082879756852540475), (1234, 0.0010227725365989516), (1235, 0.0012888987206105267), (1236, 0.001595536274401188), (1237, 0.001949823931530998), (1238, 0.0024122131578311785), (1239, 0.0029152384066145056), (1240, 0.0035336599281398265), (1241, 0.0042746162474391492), (1242, 0.0050879958342483159), (1243, 0.006096350675987898), (1244, 0.0072239087140312181), (1245, 0.0085089523260178154), (1246, 0.010042747643248803), (1247, 0.01171055342901981), (1248, 0.013658316430921556), (1249, 0.015864607041529168), (1250, 0.018279995858057729), (1251, 0.021082369692672354), (1252, 0.024137626932387021), (1253, 0.02754041232413644), (1254, 0.031373938234056535), (1255, 0.035497046954318691), (1256, 0.040115699057607507), (1257, 0.045150407853085231), (1258, 0.050585089084300358), (1259, 0.056600041751752386), (1260, 0.063016595655027471), (1261, 0.069981999269930317), (1262, 0.077520428464420088), (1263, 0.085504165255664025), (1264, 0.094143606273516353), (1265, 0.10329827628188668), (1266, 0.11299807496842022), (1267, 0.12335990651427053), (1268, 0.13419973433571541), (1269, 0.14567508932360237), (1270, 0.15773032260717509), (1271, 0.17027985640446092), (1272, 0.18347380790962631), (1273, 0.19714266009200504), (1274, 0.2113418833255945), (1275, 0.22609547619485434), (1276, 0.24125280064339497), (1277, 0.2569312426393533), (1278, 0.27302050802459699), (1279, 0.28947784588994485), (1280, 0.30636561391057454), (1281, 0.3235294511529439), (1282, 0.34101824569265776), (1283, 0.35878547159436325), (1284, 0.3767309830137332), (1285, 0.3949110433577776), (1286, 0.41320824549259333), (1287, 0.43160633752849598), (1288, 0.45010040318024302), (1289, 0.46858040214084068), (1290, 0.48707249551704029), (1291, 0.50550731462919174), (1292, 0.52383114693619581), (1293, 0.54205413664537516), (1294, 0.56008850094792673), (1295, 0.57793033629954216), (1296, 0.59554914322272468), (1297, 0.61288461471968758), (1298, 0.62994551645746311), (1299, 0.64667763582308957), (1300, 0.66306085252418223) }
  Time:        25.8 s

  + Step-bounded value iteration
    Iterations: 1300
    Threads:    4
    Time:       25.8 s

```



### Log file: modest_from-umb_check_default_resource-gathering.1300-100-100_rep2.log

```
Command(s):
../bin/modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.034 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt -D --exhaustive




##############################Output to stderr##############################
Fatal error. System.AccessViolationException: Attempted to read or write protected memory. This is often an indication that other memory is corrupt.
   at Modest.ModelChecking.StepBoundedValueIteration+<>c__DisplayClass8_0.<IterateParallel>g__Iterate|1(System.Object)
   at Modest.ModelChecking.StepBoundedValueIteration.IterateParallel(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, UInt64, System.Collections.Generic.List`1<Modest.Pair`2<UInt64,Double>>, Int32, Boolean, ULongRef, DoubleRef, Modest.Modularity.LocationErrorHandler, System.Threading.CancellationToken)
   at Modest.ModelChecking.StepBoundedValueIteration.Solve(Modest.ModelChecking.PropertyAnalysisTask, Modest.StateSpace.StateSpace, Modest.Modularity.AnalysisDataSet, System.String, Modest.Modularity.OperationState, Modest.Modularity.LocationErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperty(Modest.StateSpace.StateSpace, Modest.ModelChecking.ReachabilityPropertyInfo, System.String, System.String, Modest.StateSpace.StateSet`1<UmbState>, System.IDisposable ByRef, System.Func`3<Boolean,Boolean,Boolean>, System.String, Modest.Modularity.AnalysisDataSet, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].CheckProperties(Modest.StateSpace.StateSpace, Modest.StateSpace.StateSet`1<UmbState>, Boolean[], System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.MAModelChecker`1[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]].ModelCheck(System.String, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheckGeneric[[Modest.StateSpace.UnifiedBinaryFormat+UmbState, Modest.StateSpace, Version=3.1.0.0, Culture=neutral, PublicKeyToken=null]](Modest.Exploration.Network`1<UmbState>, Modest.StateSpace.UmbModel, System.Object, System.String, System.Object, System.Object, Modest.Modularity.ILocation, Modest.Modularity.OperationState, Modest.Modularity.ComponentErrorHandler)
   at invoke Modest.Exploration.Network`1__Modest.StateSpace.UnifiedBinaryFormat\+UmbState\, Modest.StateSpace\, Version=3.1.0.0\, Culture=neutral\, PublicKeyToken=null__ : Modest.StateSpace.UmbModel : System.Object : System.String : System.Object : System.Object : Modest.Modularity.ILocation : Modest.Modularity.OperationState : Modest.Modularity.ComponentErrorHandler : Modest.Modularity.AnalysisDataSet.GeneratedClass.DoInvoke(System.Object, System.Object[], System.Reflection.MethodInfo)
   at Modest.DirectInvoker.InvokeDirect(System.Reflection.MethodInfo, System.Object, System.Object[])
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(Modest.Modularity.IModel, CompilationParameters<AnalysisParams>, System.Object, Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams, Modest.Modularity.IModel[], Int32, Boolean, Boolean, Boolean, Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.AnalysisEngine`1[[System.__Canon, System.Private.CoreLib, Version=9.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Analyze(System.__Canon, Modest.Modularity.IModel, Int32, Boolean, Modest.Modularity.IExperiment[], Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.ModelChecking.AnalysisEngine`1[[System.__Canon, System.Private.CoreLib, Version=9.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Analyze(Modest.Modularity.IParameterObject, Modest.Modularity.IModel[], Modest.Modularity.IExperiment[][], Modest.Modularity.OperationState, Modest.Modularity.IErrorHandler)
   at Modest.Executable.ModelChecker.Run(Modest.Modularity.IParameterObject, System.Diagnostics.Stopwatch, Modest.Modularity.Tools.IOutputHandler, System.Threading.CancellationToken)
   at Modest.Executable.Program.Main(System.String[])
```



### Log file: modest_from-umb_check_default_resource-gathering.1300-100-100_rep3.log

```
Command(s):
../bin/modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 1625.584 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 163 MB
Analysis results for UMB

+ State space (UMB)
  States:            948693
  Choices:           3050099
  Branches:          3294923
  Time (decompress): 0.1 s
  Time (validate):   0.5 s
  Time (load):       0.6 s

+ Property prgoldgem
  Probability: 0.6630608525241822
  Bounds:      [0.6630608525241822, 0.6630608525241822]
  CDF:         { (0, 0), ..., (1199, 0), (1200, 7.0550791086553654E-10), (1201, 7.0550791086553654E-10), (1202, 7.8389767873948506E-10), (1203, 7.7684259963083002E-09), (1204, 7.8389767873948519E-09), (1205, 1.4908949951946258E-08), (1206, 4.9840301513998593E-08), (1207, 5.1237207177512345E-08), (1208, 1.1805735082117689E-07), (1209, 2.363474408631716E-07), (1210, 2.751839704280749E-07), (1211, 6.0617339875948095E-07), (1212, 9.1586815326840259E-07), (1213, 1.2493339039053002E-06), (1214, 2.3669570082041941E-06), (1215, 3.1356733357303078E-06), (1216, 4.7467593486416863E-06), (1217, 7.6403606716763388E-06), (1218, 9.8624903270049519E-06), (1219, 1.5260746029703193E-05), (1220, 2.1622763536033865E-05), (1221, 2.8592009565092682E-05), (1222, 4.2509727750559321E-05), (1223, 5.5892404142287892E-05), (1224, 7.5758419748182869E-05), (1225, 0.00010553586709131434), (1226, 0.00013481920290011939), (1227, 0.00018285039469700796), (1228, 0.00023986845887096465), (1229, 0.00030522060275988989), (1230, 0.00040432624279823816), (1231, 0.0005094225506899067), (1232, 0.00064784338134533004), (1233, 0.00082879756852540475), (1234, 0.0010227725365989516), (1235, 0.0012888987206105267), (1236, 0.001595536274401188), (1237, 0.001949823931530998), (1238, 0.0024122131578311785), (1239, 0.0029152384066145056), (1240, 0.0035336599281398265), (1241, 0.0042746162474391492), (1242, 0.0050879958342483159), (1243, 0.006096350675987898), (1244, 0.0072239087140312181), (1245, 0.0085089523260178154), (1246, 0.010042747643248803), (1247, 0.01171055342901981), (1248, 0.013658316430921556), (1249, 0.015864607041529168), (1250, 0.018279995858057729), (1251, 0.021082369692672354), (1252, 0.024137626932387021), (1253, 0.02754041232413644), (1254, 0.031373938234056535), (1255, 0.035497046954318691), (1256, 0.040115699057607507), (1257, 0.045150407853085231), (1258, 0.050585089084300358), (1259, 0.056600041751752386), (1260, 0.063016595655027471), (1261, 0.069981999269930317), (1262, 0.077520428464420088), (1263, 0.085504165255664025), (1264, 0.094143606273516353), (1265, 0.10329827628188668), (1266, 0.11299807496842022), (1267, 0.12335990651427053), (1268, 0.13419973433571541), (1269, 0.14567508932360237), (1270, 0.15773032260717509), (1271, 0.17027985640446092), (1272, 0.18347380790962631), (1273, 0.19714266009200504), (1274, 0.2113418833255945), (1275, 0.22609547619485434), (1276, 0.24125280064339497), (1277, 0.2569312426393533), (1278, 0.27302050802459699), (1279, 0.28947784588994485), (1280, 0.30636561391057454), (1281, 0.3235294511529439), (1282, 0.34101824569265776), (1283, 0.35878547159436325), (1284, 0.3767309830137332), (1285, 0.3949110433577776), (1286, 0.41320824549259333), (1287, 0.43160633752849598), (1288, 0.45010040318024302), (1289, 0.46858040214084068), (1290, 0.48707249551704029), (1291, 0.50550731462919174), (1292, 0.52383114693619581), (1293, 0.54205413664537516), (1294, 0.56008850094792673), (1295, 0.57793033629954216), (1296, 0.59554914322272468), (1297, 0.61288461471968758), (1298, 0.62994551645746311), (1299, 0.64667763582308957), (1300, 0.66306085252418223) }
  Time:        1624.8 s

  + Step-bounded value iteration
    Iterations: 1300
    Threads:    4
    Time:       1624.8 s

```



### Log file: modest_from-umb_check_default_resource-gathering.1300-100-100_rep4.log

```
Command(s):
../bin/modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7.725 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt -D --exhaustive




Peak memory usage: 134 MB
Analysis results for UMB

+ State space (UMB)
  States:            948693
  Choices:           3050099
  Branches:          3294923
  Time (decompress): 0.1 s
  Time (validate):   0.5 s
  Time (load):       0.6 s

+ Property prgoldgem
  Probability: 0.6630608525241822
  Bounds:      [0.6630608525241822, 0.6630608525241822]
  CDF:         { (0, 0), ..., (1199, 0), (1200, 7.0550791086553654E-10), (1201, 7.0550791086553654E-10), (1202, 7.8389767873948506E-10), (1203, 7.7684259963083002E-09), (1204, 7.8389767873948519E-09), (1205, 1.4908949951946258E-08), (1206, 4.9840301513998593E-08), (1207, 5.1237207177512345E-08), (1208, 1.1805735082117689E-07), (1209, 2.363474408631716E-07), (1210, 2.751839704280749E-07), (1211, 6.0617339875948095E-07), (1212, 9.1586815326840259E-07), (1213, 1.2493339039053002E-06), (1214, 2.3669570082041941E-06), (1215, 3.1356733357303078E-06), (1216, 4.7467593486416863E-06), (1217, 7.6403606716763388E-06), (1218, 9.8624903270049519E-06), (1219, 1.5260746029703193E-05), (1220, 2.1622763536033865E-05), (1221, 2.8592009565092682E-05), (1222, 4.2509727750559321E-05), (1223, 5.5892404142287892E-05), (1224, 7.5758419748182869E-05), (1225, 0.00010553586709131434), (1226, 0.00013481920290011939), (1227, 0.00018285039469700796), (1228, 0.00023986845887096465), (1229, 0.00030522060275988989), (1230, 0.00040432624279823816), (1231, 0.0005094225506899067), (1232, 0.00064784338134533004), (1233, 0.00082879756852540475), (1234, 0.0010227725365989516), (1235, 0.0012888987206105267), (1236, 0.001595536274401188), (1237, 0.001949823931530998), (1238, 0.0024122131578311785), (1239, 0.0029152384066145056), (1240, 0.0035336599281398265), (1241, 0.0042746162474391492), (1242, 0.0050879958342483159), (1243, 0.006096350675987898), (1244, 0.0072239087140312181), (1245, 0.0085089523260178154), (1246, 0.010042747643248803), (1247, 0.01171055342901981), (1248, 0.013658316430921556), (1249, 0.015864607041529168), (1250, 0.018279995858057729), (1251, 0.021082369692672354), (1252, 0.024137626932387021), (1253, 0.02754041232413644), (1254, 0.031373938234056535), (1255, 0.035497046954318691), (1256, 0.040115699057607507), (1257, 0.045150407853085231), (1258, 0.050585089084300358), (1259, 0.056600041751752386), (1260, 0.063016595655027471), (1261, 0.069981999269930317), (1262, 0.077520428464420088), (1263, 0.085504165255664025), (1264, 0.094143606273516353), (1265, 0.10329827628188668), (1266, 0.11299807496842022), (1267, 0.12335990651427053), (1268, 0.13419973433571541), (1269, 0.14567508932360237), (1270, 0.15773032260717509), (1271, 0.17027985640446092), (1272, 0.18347380790962631), (1273, 0.19714266009200504), (1274, 0.2113418833255945), (1275, 0.22609547619485434), (1276, 0.24125280064339497), (1277, 0.2569312426393533), (1278, 0.27302050802459699), (1279, 0.28947784588994485), (1280, 0.30636561391057454), (1281, 0.3235294511529439), (1282, 0.34101824569265776), (1283, 0.35878547159436325), (1284, 0.3767309830137332), (1285, 0.3949110433577776), (1286, 0.41320824549259333), (1287, 0.43160633752849598), (1288, 0.45010040318024302), (1289, 0.46858040214084068), (1290, 0.48707249551704029), (1291, 0.50550731462919174), (1292, 0.52383114693619581), (1293, 0.54205413664537516), (1294, 0.56008850094792673), (1295, 0.57793033629954216), (1296, 0.59554914322272468), (1297, 0.61288461471968758), (1298, 0.62994551645746311), (1299, 0.64667763582308957), (1300, 0.66306085252418223) }
  Time:        7.0 s

  + Step-bounded value iteration
    Iterations: 1300
    Threads:    4
    Time:       7.0 s

```



### Log file: modest_from-umb_check_default_resource-gathering.1300-100-100_rep5.log

```
Command(s):
../bin/modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt  -D --exhaustive
Wallclock time: 7200.025 seconds
Return code: None (timeout)
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/resource-gathering.1300-100-100/modest.model.umb models/resource-gathering.1300-100-100/modest.umb.properties.txt -D --exhaustive



```

