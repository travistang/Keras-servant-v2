import requests
import json
import urllib
class DatabaseBroker(object):
    def __init__(self,server_url,app_id,app_master_key):
        self.header = {
            'X-Parse-Application-Id': app_id,
            'X-Parse-Master-Key': app_master_key,
            'Content-Type': 'application/json',
        }
        self.server_url = server_url

    def _get(self,url):
        return requests.get(url,headers = self.header)
    def _post(self,url,payload):
        return requests.post(url,data = payload,headers = self.header)
    def _delete(self,url):
        return requests.delete(url,headers = self.header)
    def _put(self,url,payload):
        return requests.put(url,data = payload,headers = self.header)

class TaskBroker(DatabaseBroker):
    def __init__(self,server_url,app_id,app_master_key):
        super(TaskBroker,self).__init__(server_url,app_id,app_master_key)
        self.server_url = self.server_url + '/classes/Task'

    def get_tasks(self,**args):
        if len(args) == 0:
            return self._get(self.server_url).json()['results']
        else:
            data = urllib.parse.urlencode({'where':json.dumps(args)})
            return self._get(self.server_url + '?' + data).json()['results']

    def get_first_task(self,**args):
        tasks = self.get_tasks(**args)
        if len(tasks) == 0: return None
        return tasks[0]

    def create_task(self, **args):
        res = self._post(self.server_url,json.dumps(args)).json()
        res.update(args)
        return res
    def update_task(self, task):
        if 'objectId' not in task: raise ValueError("objectId must present in the task dict")
        id = task['objectId']
        url = self.server_url + '/' + id
        res = self._put(url,json.dumps(args)).json()
        res.update(task)
        return res
    def create_task_or_get_existing(self, name):
        task = self.get_first_task(name = name)
        if task: return task
        return self.create_task(name = name)
