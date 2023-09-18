from strawberry.asgi import GraphQL
import strawberry
from typing import List
from fastapi import FastAPI

@strawberry.type
class Movie:
    title: str
    director: str

@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        # fetch movies from database
        movies_data = [
            Movie(title="Jurassic Park", director="Steven Spielberg"),
            Movie(title="Interstellar", director="Christopher Nolan"),
        ]
        return movies_data
    
schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to GraphQL API"}

app.add_route("/graphql", GraphQL(schema, debug=True))  


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)