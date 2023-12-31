from aas2openapi.middleware.middleware import Middleware
from models.quality import QualityDataAAS


middleware = Middleware()
middleware.load_pydantic_models([QualityDataAAS])
middleware.generate_rest_api()

app = middleware.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
# uvicorn.run(app)
