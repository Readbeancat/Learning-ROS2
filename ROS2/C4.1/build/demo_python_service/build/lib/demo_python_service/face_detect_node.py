import rclpy
from rclpy.node import Node
from chapt4_interfaces.srv import FaceDetector 
from ament_index_python.packages import get_package_share_directory
from cv_bridge import CvBridge  
import cv2
import face_recognition
import time
import os

class FaceDetectionNode(Node):
    def __init__(self):
        super().__init__('face_detection_node')
        self.bridge = CvBridge()
        self.service = self.create_service(FaceDetector, '/face_detect', self.detect_face_callback)
        self.upsample_times = 1
        self.model = 'hog'
        self.defaut_image_path = os.path.join(
            get_package_share_directory('demo_python_service'), 
           'resource', 
            'img1.png'
        )
        if not os.path.exists(self.defaut_image_path):
            self.get_logger().error(f"默认图像文件不存在: {self.defaut_image_path}")
        else:
            self.get_logger().info(f"默认图像路径: {self.defaut_image_path}")

    def detect_face_callback(self, request, response):
        self.get_logger().info("服务回调被调用")
        try:
            if request.image.data:
                self.get_logger().info("接收到客户端图像数据")
                cv_image = self.bridge.imgmsg_to_cv2(request.image, 'bgr8')
            else:
                self.get_logger().info("使用默认图像")
                cv_image = cv2.imread(self.defaut_image_path)
                if cv_image is None:
                    self.get_logger().error(f"无法加载默认图像: {self.defaut_image_path}")
                    return response
            start_time = time.time()
            self.get_logger().info('加载完图像，开始检测')
            face_locations = face_recognition.face_locations(
                cv_image, 
                number_of_times_to_upsample=self.upsample_times, 
                model=self.model
            )
            end_time = time.time()
            self.get_logger().info(f'检测完成，耗时{end_time - start_time}')
            response.number = len(face_locations)
            response.use_time = end_time - start_time
            for top, right, bottom, left in face_locations:
                response.top.append(top)
                response.right.append(right)
                response.bottom.append(bottom)
                response.left.append(left)
        except Exception as e:
            self.get_logger().error(f"图像处理失败: {e}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = FaceDetectionNode()
    node.get_logger().info("节点已启动，等待服务调用...")
    rclpy.spin(node)
    rclpy.shutdown()