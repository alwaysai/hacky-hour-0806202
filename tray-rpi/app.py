import time
import edgeiq
import cv2
import numpy as np
"""
This applictions finds the roi associated with an illuminated LED on a tray shelve.
It then checks to see if the workers hand has picked up the correct electronics
component using a hand detection model and overlapping rectangles algorithm between
roi and hand detection bounding box.
"""

# Turns x, y coordinates into point x, y tuple
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Check to see if two rectangles are overlapping
def Overlap(l1, r1, l2, r2):
    # If one rectangle is on left side of other
    if(l1.x > r2.x or l2.x > r1.x):
        return False

    # If one rectangle is above other
    if(l1.y > r2.y or l2.y > r1.y):
        return False

    return True

def detect_roi(frame, min_x, min_y, max_x, max_y, height=60, color = (255, 0, 0)):
    """
    """
    start_point = (min_x, (min_y-height))
    end_point = (max_x, max_y)
    rectangle = (min_x, (min_y-height), max_x, max_y)
    frame = cv2.rectangle(frame, start_point, end_point, color, thickness=2)
    return frame, rectangle

def main():
    # Load object detection class, model and choose accelerator
    obj_detect = edgeiq.ObjectDetection(
            "alwaysai/hand_detection")
    obj_detect.load(engine=edgeiq.Engine.DNN_OPENVINO)

    # print model, DNN engine and accelerator, and labels associated with
    # the object detection class
    print("Loaded model:\n{}\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Labels:\n{}\n".format(obj_detect.labels))

    # hsv max min boundaries for specific light detection, boundaries numbers
    # represent hue, saturation and value parameters
    boundaries = [([6, 74, 226], [68, 187, 255])]

    # intialize fps fuctions and streamer
    fps = edgeiq.FPS()

    try:
        # intialize and start file video stream and streamer
        with edgeiq.FileVideoStream('Video20.mov', play_realtime=True) as file_stream, \
                edgeiq.Streamer() as streamer:
            print("Strating Video Stream")

            # start fps function
            fps.start()

            # loop tell video is complete
            while file_stream.more():
                # set bounding box color to red
                colors = [(255, 255, 255), (0, 0, 255)]

                grabbed_status = None

                frame = file_stream.read()

                hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                for (lower, upper) in boundaries:
                    # create NumPy arrays from the boundaries
                    lower = np.array(lower, dtype = "uint8")
                    upper = np.array(upper, dtype = "uint8")
                    # find the colors within the specified boundaries and apply
                    # the mask
                    threshold_mask = cv2.inRange(hsv_image, lower, upper)
                    nonzero_pixel_list = (np.transpose(np.nonzero(threshold_mask))).tolist()
                    # check tray boundaries
                    output = [item for item in nonzero_pixel_list if item[1] > 130 and item[1] < 380]
                    output1 = [item for item in output if item[0] > 97]

                    if output1:
                        # use list min and max funtions to find the min and max
                        # coordinates of the lit area
                        max_pixel = max(output1)
                        min_pixel= min(output1)
                        x_check = (max_pixel[1] - min_pixel[1])
                        # adjust roi to account for hand covering LED"
                        if x_check < 40:
                            min_pixel[1] = (max_pixel[1] - 55)

                        # use opencv circle to place min, mean and max coordinates
                        # on the frame
                        cv2.circle(frame, (min_pixel[1], min_pixel[0]), 4, (0, 0, 0), -1)
                        cv2.circle(frame, (max_pixel[1], max_pixel[0]), 4, (0, 0, 0), -1)

                        frame, rectangle1 = detect_roi(frame, min_pixel[1], min_pixel[0],
                            max_pixel[1], max_pixel[0])
                results = obj_detect.detect_objects(frame, confidence_level=.6)

                for prediction in results.predictions:
                    rectangle = prediction.box
                    l2 = Point(rectangle.start_x, rectangle.start_y)
                    r2 = Point(rectangle.end_x, rectangle.end_y)
                    if rectangle1 is not None:
                        l1 = Point(rectangle1[0], rectangle1[1])
                        r1 = Point(rectangle1[2], rectangle1[3])
                        if Overlap(l1, r1, l2, r2):
                            grabbed_status = "component grabbed"
                            # set bounding box color to green
                            colors = [(255, 255, 255), (0, 255, 0)]

                frame = edgeiq.markup_image(
                        frame, results.predictions, colors = colors)

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))

                if not grabbed_status:
                    text.append("No component grabbed")
                else:
                    text.append("{} from tray".format(grabbed_status))

                streamer.send_data(frame, text)

                fps.update()

                if streamer.check_exit():
                    break

    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))

        print("Program Ending")


if __name__ == "__main__":
    main()
