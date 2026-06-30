import cv2
import mediapipe as mp
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# MediaPipe
mpHands = mp.solutions.hands

hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)

mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    # ---------------- Emotion ----------------

    try:

        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False,
            silent=True
        )

        if isinstance(result, list):
            emotion = result[0]["dominant_emotion"]
        else:
            emotion = result["dominant_emotion"]

        cv2.putText(
            frame,
            emotion,
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    except Exception:
        pass

    # ---------------- Hands ----------------

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                frame,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            lmList=[]

            h,w,c=frame.shape

            for id,lm in enumerate(handLms.landmark):

                cx=int(lm.x*w)
                cy=int(lm.y*h)

                lmList.append((cx,cy))

            fingers=[]

            if lmList[4][0]>lmList[3][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            for i in range(1,5):

                if lmList[tipIds[i]][1]<lmList[tipIds[i]-2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total=fingers.count(1)

            cv2.putText(
                frame,
                f"Fingers : {total}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,0,0),
                2
            )

    cv2.imshow("AI Camera",frame)

    if cv2.waitKey(1)==ord("q"):
        break

cap.release()

cv2.destroyAllWindows()