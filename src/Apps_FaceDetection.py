import cv2
from ShowResult import ShowImageResult
# import face_recognition


class FaceDetect:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        # self.init_face_recog()
        # self.face_recognition = face_recognition

    def init_face_recog(self):
        # self.anto_image = face_recognition.load_image_file('train_face/anto/anto_1.png')
        # self.anto_face_encodings = face_recognition.face_encodings(self.anto_image)[0]

        self.obama_image = face_recognition.load_image_file('train_face/adam/adam.png')
        self.obama_face_encodings = face_recognition.face_encodings(self.obama_image)[0]

        self.slender_image = face_recognition.load_image_file('train_face/slender/slender_12.png')
        self.slender_face_encodings = face_recognition.face_encodings(self.slender_image)[0]

        self.known_face_encoding = [self.obama_face_encodings, self.slender_face_encodings]
        self.known_face_name = ["adam", "slender"]

        self.all_face_locations = []
        self.all_face_encodings = []
        self.all_face_names = []

    def faceRecognition(self):
        if self.parent.image is None:
            pass
        else:
            if self.parent.ui.checkPanorama.isChecked():
                result = self.parent.panorama_Image
            elif self.parent.ui.checkAnypoint.isChecked():
                result = self.parent.anypoint_Image
            else:
                result = self.parent.image.copy()
            faceImage = self.detector(result)
            self.show.showOriginalImage(self.parent.image)
            self.show.showResult(faceImage)

    def detector(self, image):
        image_1 = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        all_face_locations = self.face_recognition.face_locations(image_1, number_of_times_to_upsample=1,
                                                                  model='hog')
        all_face_encodings = self.face_recognition.face_encodings(image_1, all_face_locations)
        for current_face_location, current_face_encoding in zip(all_face_locations, all_face_encodings):
            top_pos, right_pos, bottom_pos, left_pos = current_face_location

            top_pos = top_pos * 4
            right_pos = right_pos * 4
            bottom_pos = bottom_pos * 4
            left_pos = left_pos * 4

            # find all the matches and get the list of matches
            all_matches = self.face_recognition.compare_faces(self.known_face_encoding, current_face_encoding)

            # string to hold the label
            name_of_person = 'Unknown face'

            if True in all_matches:
                first_match_index = all_matches.index(True)
                name_of_person = self.known_face_name[first_match_index]

            cv2.rectangle(image, (left_pos, top_pos), (right_pos, bottom_pos), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name_of_person, (left_pos + 5, bottom_pos - 10), font, 0.5, (255, 255, 255), 1)

        return image
