from fastapi import FastAPI

books = [
    {"id": 1, "title": "Python Basic", "quantity": 12},
    {"id": 2, "title": "FastAPI Beginner", "quantity": 3},
    {"id": 3, "title": "Clean Code", "quantity": 5},
    {"id": 4, "title": "Database Design", "quantity": 0},
    {"id": 5, "title": "Web API Design", "quantity": 20},
]


app = FastAPI(
    title=" Quản lý thư viện",
    description="API lấy danh sách những quyển sách sắp hết hàng",
    version="1.0.0",
)


app.get(path="/books/low-stock", tags=[" books"])


def get_book_low_stock():
    book_low_stock = []
    for book in books:
        if "quantity" not in book:
            continue

        if book["quantity"] < 0:
            continue
        if book["quantity"] < 5:
            book_low_stock.append(book)

    if not book_low_stock:
        return {"message": "Không có sách nào sắp hết hàng", "data": []}

    return {"message": "Danh sách những quyển sách sắp hết hàng", "data": []}


# Input của bài toán là danh sách books gồm id, title và quantity.
# Output là trả về danh sách các sách sắp hết hàng dưới dạng JSON.
# Nếu không có sách nào sắp hết hàng thì trả về:
# {"message": "Không có sách nào sắp hết hàng", "data": []}
# Điều kiện xác định sách sắp hết hàng là:
# quantity <= 5.
