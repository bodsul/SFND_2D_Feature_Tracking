import csv

#Detector, Descriptor, Average number of Keypoints per frame, Average number of Matched Keypoints per consecutive frames, 
#Average Detector speed per frame, Average Descriptor speed per frame

infile = "../build/out.txt"
first_line = True
outfile = "../writeup.csv"
n_frames = 10

with open(infile, 'r') as f, open(outfile, 'w') as out_f:
    for line in f.readlines():
        line = line.rstrip('\n')
        if 'detector:' in line and 'descriptor:' in line:
            if first_line:
                header = "Detector, Descriptor, Average number of Keypoints in ROI per frame, Average number of Matched Keypoints in ROI per consecutive frames, " \
                        "Average Detector speed per frame (ms), Average Descriptor speed per frame(ms)\n"
                out_f.write(header)
                first_line = False
            else:
                avg_detection_time /= n_frames
                avg_description_time /= n_frames
                avg_num_key_points_roi /= n_frames
                avg_matched_keypoints /= n_frames-1
                out_line = ', '.join([detector, descriptor, str(avg_num_key_points_roi), str(avg_matched_keypoints), str(avg_detection_time), str(avg_description_time)])
                out_f.write(out_line + '\n')
            words = line.split(' ')
            detector = words[1]
            descriptor = words[3]
            avg_num_keypoints = 0
            avg_detection_time = 0
            avg_description_time = 0
            avg_num_key_points_roi = 0
            avg_matched_keypoints = 0

        elif 'detection with n=' in line:
            start = line.find('n=')
            start = start+2
            end = line.find(" keypoints")
            end = end
            avg_num_keypoints += int(line[start:end])
            start = line.find(' in ')
            start = start + 4
            end = line.find(' ms')
            avg_detection_time += float(line[start:end])
        elif 'descriptor extraction' in line:
            start = line.find(' in ')
            start +=4
            end = line.find( 'ms')
            avg_description_time += float(line[start:end])
        elif 'ROI' in line:
            start = line.find('ROI: ')
            start = start + 5
            avg_num_key_points_roi += int(line[start: ])
        elif 'matched keypoints:' in line:
            start = line.find('keypoints:')
            start = start + len('keypoints:')
            avg_matched_keypoints += int(line[start: ])