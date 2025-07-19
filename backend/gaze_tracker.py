def is_looking_away(landmarks_list):
    if not landmarks_list:
        return True
    landmarks = landmarks_list[0]
    try:
        left_eye = landmarks['left_eye']
        right_eye = landmarks['right_eye']
        nose = landmarks['nose_bridge'][-1]
        eye_center_x = (left_eye[0][0] + right_eye[-1][0]) / 2
        if abs(eye_center_x - nose[0]) > 40:
            return True
    except:
        return True
    return False
