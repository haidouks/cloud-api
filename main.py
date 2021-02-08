
from fastapi import FastAPI
from pprint import pprint
from routers import monitoring,k8s,ceph

try:
  tags_metadata = [
    {
        "name": "kubernetes",
        "description": "Operations related to kubernetes",
    },
    {
        "name": "monitoring",
        "description": "Monitoring endpoint",
    },
    {
        "name": "ceph",
        "description": "Operations related to ceph",
    },
  ]
  app = FastAPI(title="Cloud API", version="1.0.0", openapi_tags=tags_metadata)
  app.include_router(monitoring.router)
  app.include_router(k8s.router)
  app.include_router(ceph.router)

except Exception as e:
  pprint(e)

