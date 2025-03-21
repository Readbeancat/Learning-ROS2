import rclpy
from rclpy.node import Node
from chapt4_interfaces.srv import FaceDetector 
from ament_index_python.packages import get_package_share_directory
from cv_bridge import CvBridge  
import cv2
import os

class FaceDetectionClientNode(Node):
    def __init__(self):
        super().__init__('face_detection_client_node')
        self.bridge = CvBridge()
        self.client = self.create_client(FaceDetector, '/face_detect')
        self.get_logger().info("人脸检测服务启动")
        self.defaut_image_path = os.path.join(
            get_package_share_directory('demo_python_service'), 
            'resource', 
            'img2.png'
        )
        self.image = cv2.imread(self.defaut_image_path)
        if self.image is None:
            self.get_logger().error(f"无法加载默认图像: {self.defaut_image_path}")
        else:
            self.get_logger().info(f"加载默认图像: {self.defaut_image_path}")
        
        # 检查并转换图像格式为 BGR（如果需要）
        if len(self.image.shape) == 2:  # 如果是灰度图像
            self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        elif self.image.shape[2] == 4:  # 如果是带透明度的图像（如 RGBA）
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGBA2BGR)

    def send_request(self):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("服务未启动，等待中...")
        request = FaceDetector.Request()
        try:
            request.image = self.bridge.cv2_to_imgmsg(self.image, encoding='bgr8')
            future = self.client.call_async(request) 
            rclpy.spin_until_future_complete(self, future)  # 修正：添加 self 参数
            response = future.result()
            if response is not None:
                self.get_logger().info(f"检测到{response.number}个人脸，耗时{response.use_time}")
                self.show_response(response)
            else:
                self.get_logger().error("服务调用失败，未收到响应")
        except Exception as e:
            self.get_logger().error(f"服务调用失败: {e}")

    def show_response(self, response):
        for i, top in enumerate(response.top):
            cv2.rectangle(self.image, (response.left[i], top), (response.right[i], response.bottom[i]), (0, 0, 255), 4)
        cv2.imshow('Face Detection Result', self.image)
        cv2.waitKey(0)

def main(args=None):
    rclpy.init(args=args)
    node = FaceDetectionClientNode()
    node.get_logger().info("client节点已启动,等待服务调用...")
    node.send_request()
    rclpy.shutdown()