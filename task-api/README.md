# Task API - Book Management

## 1. Giới thiệu

Bài tập xây dựng đặc tả API quản lý sách bằng **OpenAPI YAML**. Backend được triển khai bằng Flask ở giai đoạn tiếp theo.

## 2. Mục tiêu

- Thiết kế API theo các nguyên tắc REST.
- Mô tả endpoint, HTTP method, request và response.
- Tái sử dụng schema thông qua `$ref`.
- Kiểm tra tính hợp lệ của đặc tả OpenAPI.
- Triển khai và kiểm thử API sau khi hoàn thiện đặc tả.

## 3. Cấu trúc thư mục

| File/thư mục | Ý nghĩa |
|---|---|
| `openapi.yaml` | Đặc tả API: paths, parameters, request/response và reusable schemas. |
| `app/__init__.py` | Tạo Flask application và đăng ký routes. |
| `app/routes.py` | Khai báo endpoint và xử lý HTTP request/response. |
| `app/schemas.py` | Các hàm kiểm tra dữ liệu đầu vào ở phía Python; không tự sinh từ OpenAPI. |
| `app/services.py` | Xử lý nghiệp vụ quản lý sách, tách khỏi phần HTTP. |
| `tests/test_books.py` | Kiểm thử các endpoint bằng Flask test client. |
| `requirements.txt` | Danh sách thư viện Python cần cài. |

## 4. Các API

| Method | Endpoint | Chức năng |
|---|---|---|
| `GET` | `/books` | Lấy danh sách sách. |
| `GET` | `/books/{id}` | Lấy một cuốn sách theo ID. |
| `POST` | `/books` | Tạo sách mới. |
| `PUT` | `/books/{id}` | Thay thế thông tin sách. |
| `DELETE` | `/books/{id}` | Xóa sách. |

## 5. Schema dùng chung

Các schema được định nghĩa trong `components/schemas` của `openapi.yaml`:

- `Book`: sách đầy đủ, bao gồm `id`.
- `BookCreate`: dữ liệu tạo sách, không cần `id` do server cấp.
- `BookUpdate`: dữ liệu cập nhật; trong mẫu này yêu cầu đủ các trường có thể sửa theo ngữ nghĩa PUT.
- `Error`: cấu trúc phản hồi lỗi.

Trong `paths`, dùng `$ref: '#/components/schemas/Book'` hoặc các schema tương ứng để tránh lặp định nghĩa.

> `$ref` tái sử dụng định nghĩa trong tài liệu OpenAPI; nó không tự động sinh hay tái sử dụng mã Python. Nếu cần sinh code, phải dùng công cụ code generation riêng.

## 6. Công nghệ

- OpenAPI 3.0.3 / YAML: mô tả API.
- Flask: triển khai backend.
- pytest: kiểm thử tự động.
- Swagger UI hoặc trình soạn thảo OpenAPI tương thích: xem và thử đặc tả.

## 7. Chạy dự án

Từ thư mục `task-api/`:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Cài thư viện và chạy:

```bash
pip install -r requirements.txt
python -m flask --app app run --debug
```

Mặc định API chạy tại `http://127.0.0.1:5000`.

## 8. Kiểm thử

Khi môi trường ảo đã được kích hoạt:

```bash
pytest
```

Dữ liệu sách hiện được lưu trong bộ nhớ; khởi động lại server sẽ đặt dữ liệu về ban đầu. Đây là bản mẫu học tập, chưa dùng cơ sở dữ liệu.
