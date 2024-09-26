from fastapi import FastAPI, Request
from sentry_sdk import init, capture_exception
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://0e3bcb6cc88e5b7d2e76a8ed84197116@o4506443958976512.ingest.us.sentry.io/4507718967361536",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI()

app.add_middleware(SentryAsgiMiddleware)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/error")
async def cause_error():
    # Пример вызова ошибки для тестирования Sentry
    raise Exception("This is a test exception!")

# Обработчик ошибок
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    capture_exception(exc)  # Отправка исключения в Sentry
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred."},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    cause_error()
    exception_handler()
