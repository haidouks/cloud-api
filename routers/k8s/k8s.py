from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from .base_models import *
from packages.k8s.k8s import kubernetes
from packages.auth.users import UserInventory
from packages.auth.roleChecker import RoleChecker

router = APIRouter()  
k8s = kubernetes()

k8sAdmin = RoleChecker(["k8s-admin"])

@router.get("/kubernetes/resources/namespace",response_model=NamespaceList, tags=["kubernetes"])
def get_kubernetes_namespaces():
  return k8s.getNamespaces()

@router.post("/kubernetes/resources/namespace", tags=["kubernetes"], dependencies=[Depends(k8sAdmin)])
def create_new_namespace(input: NamespaceInput, credentials: HTTPBasicCredentials = Depends(UserInventory.checkAuth)):
  return k8s.newNamespace(namespace=input.namespace)

@router.post("/kubernetes/tektoncd/pipelineRun", tags=["tektoncd"])
def trigger_tektoncd_pipeline(input: PipelineRunInput):
  return k8s.newPipelineRun(gitRepo=input.gitRepo, image=input.image, pipelineRef=input.pipelineRef, namespace=input.namespace)


@router.get("/kubernetes/tektoncd/pipelineRun/{pipelineRun}", tags=["tektoncd"])
def get_tektoncd_pipelineRun(pipelineRun: str, namespace: str = "default"):
  return k8s.getPipelineRun(pipelineRun=pipelineRun, namespace=namespace)
