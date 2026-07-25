import cv2
import os
import imageio_ffmpeg
import subprocess

# Folder where videos will be saved
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\7th experiment"

os.makedirs(save_folder, exist_ok=True)

# Temporary frame folder
frame_folder = os.path.join(save_folder, "frames")

os.makedirs(frame_folder, exist_ok=True)


# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()


count = 0

print("Recording... Press q to stop")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)

    # Save frames
    cv2.imwrite(
        os.path.join(frame_folder, f"frame_{count:05d}.jpg"),
        frame
    )

    count += 1


    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


print("Frames captured:", count)


# -------- CREATE NORMAL VIDEO --------

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()


normal = os.path.join(save_folder, "normal_video.mp4")

subprocess.run([
    ffmpeg,
    "-framerate", "30",
    "-i",
    os.path.join(frame_folder, "frame_%05d.jpg"),
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    normal
])


# -------- CREATE SLOW VIDEO --------

slow = os.path.join(save_folder, "slow_motion_video.mp4")

subprocess.run([
    ffmpeg,
    "-framerate", "10",
    "-i",
    os.path.join(frame_folder, "frame_%05d.jpg"),
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    slow
])


# -------- CREATE FAST VIDEO --------

fast = os.path.join(save_folder, "fast_motion_video.mp4")

subprocess.run([
    ffmpeg,
    "-framerate", "60",
    "-i",
    os.path.join(frame_folder, "frame_%05d.jpg"),
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    fast
])


print("DONE!")
print("Videos saved in 7th experiment folder")