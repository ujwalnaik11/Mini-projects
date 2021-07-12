faceDetector = vision.CascadeObjectDetector('Nose');
I = imread('2.jpg');
bboxes = step(faceDetector, I)
IFaces = insertObjectAnnotation(I, 'rectangle', bboxes, 'Face');   
figure, imshow(IFaces), title('Detected faces');
disp('stop')

