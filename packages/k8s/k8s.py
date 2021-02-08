from kubernetes import client, config
import json
from pprint import pprint

class kubernetes:
    def __init__(self):
        config.load_kube_config()
        self.core = client.CoreV1Api()
        self.crd = client.CustomObjectsApi()

    def getNamespaces(self):
        namespaces = json.loads(self.core.list_namespace(_preload_content=False).data)
        return namespaces

    def newPipelineRun(self, pipelineRef: str, image: str, gitRepo: str, namespace: str= "default"):
        pipelineRun = {
            "apiVersion": "tekton.dev/v1beta1",
            "kind": "PipelineRun",
            "metadata": {"generateName": f"{pipelineRef}-"},
            "spec": {
                "params": [ {
                    "name": "image", 
                    "value": image
                    }],
                "pipelineRef": {
                    "name": pipelineRef
                },
                "resources": [
                    {
                        "name": "git-resource",
                        "resourceSpec": {
                            "params" : [{
                                "name": "url",
                                "value": gitRepo
                            }],
                            "type": "git"
                        }
                    }
                ]
            }
        }
        resource = self.crd.create_namespaced_custom_object(
            group = "tekton.dev",
            version = "v1beta1",
            namespace = namespace,
            plural = "pipelineruns",
            body = pipelineRun,
        )
        return resource
    
    def getPipelineRun(self, pipelineRun: str, namespace: str= "default"):
        resource = self.crd.get_namespaced_custom_object(
            group = "tekton.dev",
            version="v1beta1",
            name = pipelineRun,
            namespace = namespace,
            plural="pipelineruns",
        )
        return resource
