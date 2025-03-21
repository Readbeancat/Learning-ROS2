import face_recognition
import cv2
from ament_index_python.packages import get_package_share_directory
import os

def main():
    # 获取包的共享目录
    pkg_share_path = get_package_share_directory('demo_python_service')
    # 去掉多余的 demo_python_service 层级
    base_path = os.path.dirname(pkg_share_path)
    img_path = os.path.join(base_path, 'demo_python_serviceresource', 'img1.png')
    print(f"尝试读取的图像路径: {img_path}")

    # 读取图像
    image = cv2.imread(img_path)

    # 检查图像是否成功读取
    if image is None:
        print(f"无法读取图像文件: {img_path}。请检查文件路径是否正确，或者文件是否损坏。")
        return

    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1, model='hog')

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 4)

    cv2.imshow('Face Detecte Result', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()