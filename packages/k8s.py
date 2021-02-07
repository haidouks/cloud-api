from kubernetes import client, config
import json

class kubernetes:
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()


    def getNamespaces(self):
        namespaces = json.loads(self.v1.list_namespace(_preload_content=False).data)
        return namespaces