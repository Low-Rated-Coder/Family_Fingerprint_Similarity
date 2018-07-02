% Clearing the workspace ...
clc

% Loading the images ...
srcFiles = dir('path_to_image');  % the folder in which your images exists ...
for i = 1 : length(srcFiles)
    filename = strcat('path_to_folder',srcFiles(i).name);
    I = imread(filename);
    imshow(I)
    set(gcf,'position',[1 1 600 600]); % parameters for window to be displayed ....
    
    %Binarize the image ...
    J = I(:,:,1)>160; % iterate over every x and every y in first plane ...
    imshow(J)
    set(gcf,'position',[1 1 600 600]);

    %Thinning the image ...
    K = bwmorph(~J,'thin','inf'); % Applying thinning operation till image doesn't changes ...
    imshow(~K)
    set(gcf,'position',[1 1 600 600]);
    
    groundtruthsp.core=[183   148;   184   182];
    groundtruthsp.delta=[116   251;   286   278];
    
    % Detect singular points of image using walking algorithm ....
    detectedsp = walking(~K);

    % mark singular points on the image
    imshow(~K); 
    hold on;
    
    % groundtruth
    plot(groundtruthsp.core(:,1), groundtruthsp.core(:,2), 'or', 'markersize',10,'linewidth',2);
    plot(groundtruthsp.delta(:,1), groundtruthsp.delta(:,2), '^r', 'markersize',10, 'linewidth' ,2);

    %detected
    if size(detectedsp.core) > 0
        plot(detectedsp.core(:,1), detectedsp.core(:,2), 'go', 'markersize',12,'linewidth',2);
    end
    if size(detectedsp.delta) > 0
        plot(detectedsp.delta(:,1), detectedsp.delta(:,2), 'g^', 'markersize',12, 'linewidth' ,2);
    end
    
    [a,b] = size(detectedsp.core);
    [c,d] = size(detectedsp.delta);
    count = [a,c];
    %if exist('Mother.csv','file')
    %    dlmwrite('Mother.csv',count,'delimiter',',','-append');
    %else     
    %    csvwrite('Mother.csv',count);
    %end
end