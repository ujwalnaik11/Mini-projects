clc;
clear;
imds = imageDatastore('database','IncludeSubfolders',true,'LabelSource','foldernames');
[trainimds, testimds] = splitEachLabel(imds , 0.7);

cellSize =[8,8];
%numImages =numel(imds.Files);
trainingFeatures=[]
for i= 1:numel(trainimds.Files):
    img = readimage(trainimds, i);
    trainingFeatures(i,:) = extractHOGFeatures(img,'CellSize',cellsize);
end
%trainingFeatures = array2table(trainingFeatures);
%trainingFeatures.class = imds.Labels;
%save trainingFeatures trainingFeatures;
%disp('stop');
%[trainedClassifier, validationAccuracy] = trainClassifier()
trainingLabels = trainimds.Labels;
classifier = fitcecoc(trainingFeatures, trainingLabels);
save classifier classifier;

for i= 1:numel(testimds.Files):
    img = readimage(testimds, i);
    Features = extractHOGFeatures(img,'CellSize',cellsize);
    PredictedClass(i) = predict(Classifier,Feautures);
end
PredictedClass =PredictedClass';
ActualClass = testimds.Labels;
plotconfusion(ActualClass,PredictedClass);

msgbox('Trained Successfully');
