import uvicorn
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from starlette.responses import JSONResponse


class Query(graphene.ObjectType):
    """
    graph query
    """

    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, _, name):
        """first resolver."""
        return f"Hello {name}"


app = FastAPI(
    title='ContactQL',
    description='GraphQL Contact APIs',
    version='0.1'
)


@app.get("/")
async def root():
    """root method"""
    return JSONResponse(
        content={"message": "Contact Applications!"},
        status_code=200
    )


app.add_route(
    "/graphql",
    GraphQLApp(schema=graphene.Schema(query=Query))
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True
    )
