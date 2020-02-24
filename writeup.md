# SFND 2D Feature Tracking Writeup

1. The databuffer is implemented using an std::vector with a maximum size of databufferSize. 
We add frames to the databuffer until it grows to a size of databufferSize. Subsequently, 
we track the index of the oldest frame added and replace the oldest frame with the newest frame,
moving the index of the oldest frame cylically from 0 to databuffer-1 and then back to 0.

2. HARRIS, FAST, BRISK, ORB, AKAZE, and SIFT feature detectors are all implemented using the 
appropriate openCV object and can be 
selected by setting the string variable detectorType in MidTermProject_Camera_Student.cpp.

3. Keypoints outside of the ROI which is the region directly in front of the ego vehicle camera
are removed by creating a binary bask for the ROI and using the cv::KeyPointsFilter::runByPixelsMask function.

4. Keypoint descriptors BRIEF, ORB, FREAK, AKAZE and SIFT are all implemented using the appropriate
openCV object and can be seleced by setting the variable descriptorType in MidTermProject_Camera_Student.cpp.

5. FLANN keypoint matching using the default KDTree as an indexer, both nearest neighbor as well as k-nearest neighbor selection
with k=2 are implemented using openCV

6. For K-Nearest-Neighbor matching using FLANN, we implement the descriptor distance ratio test, 
which looks at the ratio of best vs. second-best match to decide whether to keep an associated pair of keypoints.
We use a ratio of 0.8 as threshold.

7. The speed of each detector-descriptor combination is also measured

All statistics are saved in as csv in writeup.csv and also can be viewed as a spreadsheet in writeup.xlsx. Based on the
speed and the number of quality key point matches detected, the best detector-descriptor combination in descending order
are ORB-ORB, SHI-TOMASI-ORB, SHI-TOMASI-BRIEF.