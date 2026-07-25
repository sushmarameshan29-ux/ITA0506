import cv2

input_video = "captured_video.mp4"

cap = cv2.VideoCapture(input_video)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(width, height, fps)

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()


# -------- SLOW MOTION --------

slow_factor = 3

slow_out = cv2.VideoWriter(
    "slow_motion.mp4",
    cv2.VideoWriter_fourcc(*"avc1"),
    fps,
    (width, height)
)

for frame in frames:
    for i in range(slow_factor):
        slow_out.write(frame)

slow_out.release()


# -------- FAST MOTION --------

fast_factor = 3

fast_out = cv2.VideoWriter(
    "fast_motion.mp4",
    cv2.VideoWriter_fourcc(*"avc1"),
    fps,
    (width, height)
)

for i in range(0, len(frames), fast_factor):
    fast_out.write(frames[i])

fast_out.release()


print("Saved successfully!")