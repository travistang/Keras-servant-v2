from keras.callbacks import Callback
from brokers import TaskBroker

class KerasServantCallback(Callback):
    def __init__(self,parse_server_url,parse_app_id,parse_master_key,object_id = None,**args):
        super(KerasServantCallback,self).__init__() # Python 3

        # setting up ParsePy
        self.broker = TaskBroker(parse_server_url,parse_app_id,parse_master_key)
        #os.environ["PYTHONHTTPSVERIFY"] = "0"
        self.task = None
        if object_id:
            self.task = self.broker.get_first_task(objectId=object_id)
        if self.task is None:
                # try to get the task in the database
                if 'name' not in args:
                    raise ValueError("either object_id or name of the task has to be given")
                task_name = args['name']
                self.task = self.broker.create_task_or_get_existing(task_name)

        print("Checking self.task:",self.task)
        # TODO: remove me
        self.task = self.broker.update_task(self.task,loss = 0.4)
        print("Updated self.task:", self.task)
    def on_train_begin(self,logs = {}):
        # TODO: interact with the database and create an entry
        pass
    def on_batch_end(self,batch,logs = {}):
        # TODO: submit the result to the database
        pass

if __name__ == '__main__':
    # Test here
    ksc = KerasServantCallback('http://localhost:1337/parse','KERAS_SERVANT','KERAS_SERVANT',name = 'test_task')
