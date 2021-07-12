Targets = irisTargets;
TrainData = array2table(irisInputs');
TargetClass = vec2ind(Targets);
TrainData.Class = TargetClass';