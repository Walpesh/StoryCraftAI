from fastapi import Request, status
from fastapi.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import Response
from urllib.parse import quote

def register_error_handlers(app):

    @app.exception_handler(401)
    async def unauthorized_handler(request: Request, exc: StarletteHTTPException):
        return RedirectResponse(f"/error?message={quote('Ошибка: Неавторизован')}", status_code=303)

    @app.exception_handler(403)
    async def forbidden_handler(request: Request, exc: StarletteHTTPException):
        return RedirectResponse(f"/error?message={quote('Ошибка: Доступ запрещён')}", status_code=303)

    @app.exception_handler(404)
    async def not_found_handler(request: Request, exc: StarletteHTTPException):
        return RedirectResponse(f"/error?message={quote('Ошибка: Страница не найдена')}", status_code=303)

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(request: Request, exc: RequestValidationError):
        return RedirectResponse(f"/error?message={quote('Ошибка: Неверные данные формы')}", status_code=303)

    @app.exception_handler(500)
    async def internal_error_handler(request: Request, exc: Exception):
        return RedirectResponse(f"/error?message={quote('Ошибка: Внутренняя ошибка сервера')}", status_code=303)
