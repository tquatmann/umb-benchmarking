# Log files for modest_from-jani_to-aut_default on model [oscillators.8-10-0.1-1-0.1-1.0](../../models/oscillators.8-10-0.1-1-0.1-1.0)

Parsed values: `[ERR, ERR, ERR, ERR, ERR]`



### Log file: modest_from-jani_to-aut_default_oscillators.8-10-0.1-1-0.1-1.0_rep1.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model.aut AUT  -D --exhaustive
Wallclock time: 44.303 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_oscillators.8-10-0.1-1-0.1-1.0_rep2.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 43.416 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep2.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_oscillators.8-10-0.1-1-0.1-1.0_rep3.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 42.092 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep3.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_oscillators.8-10-0.1-1-0.1-1.0_rep4.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 41.438 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep4.aut:	File does not exist.
```



### Log file: modest_from-jani_to-aut_default_oscillators.8-10-0.1-1-0.1-1.0_rep5.log

```
Command(s):
../bin/modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 44.776 seconds
Return code: -6
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/oscillators.8-10-0.1-1-0.1-1.0/model.jani --statespace out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is a DTMC model.

##############################Output to stderr##############################
Unhandled exception. System.Runtime.InteropServices.COMException (0x80131198): No logical space left to create more user strings. (0x80131198)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at System.Reflection.Emit.RuntimeModuleBuilder.<GetStringConstant>g____PInvoke|26_0(QCallModule __module_native, UInt16* __str_native, Int32 __length_native)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_3.<CreateJump>b__4(Int32 assignmentIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_2.<CreateJump>b__3(Int32 targetIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_1.<CreateJump>b__2(Int32 edgeIndex)
   at Modest.Exploration.Compiled.CompilerHelper.CreateJumpTable(ILGenerator ilgen, Int32 labelCount, Action`1 generateCase, String description)
   at Modest.Exploration.Compiled.CompiledAutomaton.<>c__DisplayClass24_0.<CreateJump>b__1(Int32 locationIndex)
   at Modest.Exploration.Compiled.CompiledAutomaton.CreateJump(TypeBuilder tb)
   at Modest.Exploration.Compiled.CompiledAutomaton.Compile(Dictionary`2 edgeLabelMapping)
   at Modest.Exploration.Compiled.NetworkCompiler.CompileNetwork(NetworkCompilationState compilationState, Expression[] expressions, Expression[] timeConstraints)
   at Modest.Exploration.NetworkCompilerHelper.Compile(AutomataNetwork automataNetwork, ExplorationConfiguration config, Expression[] expressions, Expression[] timeConstraints, Dictionary`2 clockBounds, HashSet`1 extraSymbolicVariables, StateProjection[] projections, OperationState operationState, String extraStatusString)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.ModelCheck(IModel model, CompilationParameters compilationParams, Object parametersObj, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.ModelCheckingAnalysisEngine.Analyze(AnalysisParams analysisParameters, IModel[] models, Int32 index, Boolean isLast, Boolean useDtmcSemantics, Boolean isContinuousTimeMarkovModel, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(AP analysisParameters, IModel model, Int32 index, Boolean isLast, IExperiment[] modelParameters, OperationState operationState, IErrorHandler errors)
   at Modest.ModelChecking.AnalysisEngine`1.Analyze(IParameterObject analysisParameters, IModel[] models, IExperiment[][] experiments, OperationState operationState, IErrorHandler errors)
   at Modest.Executable.ModelChecker.Run(IParameterObject parameterObj, Stopwatch time, IOutputHandler outputHandler, CancellationToken cancellationToken)
   at Modest.Executable.Program.Main(String[] args)

############################## Output files ##############################
out/modest_from-jani_to-aut_default/oscillators.8-10-0.1-1-0.1-1.0/model_rep5.aut:	File does not exist.
```

