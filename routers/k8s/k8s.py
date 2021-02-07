from fastapi import APIRouter
from .base_models import *
from packages.k8s import kubernetes

router = APIRouter()  
k8s = kubernetes()

@router.get("/kubernetes/namespaces",response_model=NamespaceList, tags=["kubernetes"])
def get_kubernetes_namespaces():
  return k8s.getNamespaces()
