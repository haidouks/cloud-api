from fastapi import APIRouter
from .base_models import *
from packages.k8s.k8s import kubernetes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pprint import pprint
import json

router = APIRouter()  
k8s = kubernetes()

@router.get("/kubernetes/resources/namespace",response_model=NamespaceList, tags=["kubernetes"])
def get_kubernetes_namespaces():
  return k8s.getNamespaces()

@router.post("/kubernetes/resources/namespace", tags=["kubernetes"])
def create_new_namespace(input: NamespaceInput):
  return k8s.newNamespace(namespace=input.namespace)

@router.post("/kubernetes/tektoncd/pipelineRun", tags=["tektoncd"])
def trigger_tektoncd_pipeline(input: PipelineRunInput):
  return k8s.newPipelineRun(gitRepo=input.gitRepo, image=input.image, pipelineRef=input.pipelineRef, namespace=input.namespace)


@router.get("/kubernetes/tektoncd/pipelineRun/{pipelineRun}", tags=["tektoncd"])
def get_tektoncd_pipelineRun(pipelineRun: str, namespace: str = "default"):
  return k8s.getPipelineRun(pipelineRun=pipelineRun, namespace=namespace)
