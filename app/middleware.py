from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from jose import JWTError, jwt
from app.config import settings

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token:
            token = token.split(" ")[1]  # Extract the token part
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
                request.state.user = payload  # Attach the user info to the request
            except JWTError:
                raise HTTPException(status_code=401, detail="Invalid token")
        response = await call_next(request)
        return response
