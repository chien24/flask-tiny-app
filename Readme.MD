# 1. Thông tin cá nhân
- **22689381 - Hoa Xuân Hoàn**
- **22685651 - Phan Công Chiến**


# 2. Mô tả Project
Viết một số website viết các blog đơn giản với Django, có các chức năng như xóa, sửa các bài viết do người dùng đăng và tạo các bài viết. Người dùng có thể nhìn thấy các bài viết của người khác. Chức năng chính của website là đăng nhập, đăng ký, quản lý các bài post. Đồng thời có các admin để quản lý người dùng trang web.

# 3. Hướng dẫn cài đặt
### 3.1 Cài đặt bằng code trên repository github
- Cài đặt một phiên bản ```python3``` ([Có thể download tại đây](https://www.python.org/downloads/))
- Mở Git Bash, tạo thư mục để lưu dự án: ```mkdir blogApp && cd blogApp/```
- Clone dự án ở repository github: ```git clone https://github.com/chien24/flask-tiny-app.git```
- Di chuyển vào thư mục chứa file **setup**: ```cd flask-tiny-app/blog_web```
- Kiểm tra các thư mục trong dự án và quyền: ```ls -la```
- Thêm quyền thực thi cho file **setup.sh**: ```chmod 755 setup.sh```
- Thực hiện chạy file **setup.sh** để khởi động chương trình: ```bash setup.sh```
- Truy cập ứng dụng tại: **[localhost:8000](http://localhost:8000/)**


### 3.1 Cài đặt bằng docker
- Cài đặt docker tại [đây](https://www.docker.com/products/docker-desktop/).
- Mở Git Bash, tạo thư mục để lưu dự án: ```mkdir blogApp && cd blogApp/```
- Clone dự án ở repository github: ```git clone https://github.com/chien24/flask-tiny-app.git```
- Di chuyển vào thư mục chứa file **Dockerfile**: ```cd flask-tiny-app/blog_web```
- Thực hiện build image từ Dockerfile:```Docker build -t blog_app .```
- Nếu không thể build thành công Image có thể download Image từ Docker Hub: ```docker pull hxhoan/blog_app:lattest```
- Khởi động Image nếu pull từ Docker Hub: ```docker run --name blog_app -p 8000:8000 hxhoan/blog_app:lattest```
- Khởi động Image nếu tự build image: ```docker run --name blog_app -p 8000:8000 blog_app```
- Truy cập ứng dụng tại: [localhost:8000](http://localhost:8000/)


# 4. Link Project
- Docker Hub: [https://hub.docker.com/repository/docker/hxhoan/blog_app/tags](https://hub.docker.com/repository/docker/hxhoan/blog_app/tags)
- Repository github: [https://github.com/chien24/flask-tiny-app.git](https://github.com/chien24/flask-tiny-app.git)
- Deployment site: [https://basicdjangoproject.onrender.com/](https://basicdjangoproject.onrender.com/)