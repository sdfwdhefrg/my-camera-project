import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('错误无法打开摄像头')
    exit()
print("按下 'q' 键退出程序...")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1) & 0xFF == ord('q')
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('screenshot.jpg',frame)
        print('截图已保存')
cap.release()
cv2.destroyAllWindows()





