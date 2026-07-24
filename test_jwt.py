from app.jwt_handler import create_access_token

token = create_access_token(
    {"sub": "saboor"}
)

print(token)