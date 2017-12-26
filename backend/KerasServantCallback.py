from keras.callbacks import Callback
from brokers import TaskBroker
from decimal import Decimal
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

        self.ignore_attrs = []
        if 'ignore_attrs' in args:
            self.ignore_attrs = args['ignore_attrs']

    def on_train_begin(self,logs = {}):
        # TODO: interact with the database and create an entry
        pass
    def on_batch_end(self,batch,logs = {}):
        # TODO: submit the result to the database
        # loss = logs.get('loss')
        # if 'loss' not in self.task:
        #     self.task['loss'] = []
        for attr_name in logs:
            # skipping those attributes
            if attr_name in self.ignore_attrs: continue
            
            if attr_name not in self.task:
                self.task[attr_name] = []
            val = logs.get(attr_name)
            # TODO: what about non-scaler logs?
            if type(val) == int:
                self.task[attr_name].append(val)
            elif type(val) == float:
                self.task[attr_name].append(Decimal(val))
            #elif type(val) in [np.float32,np.float64]:
            else:
                self.task[attr_name].append(Decimal(val.item()))
        self.broker.update_task(self.task)

if __name__ == '__main__':
    # Test here
    ksc = KerasServantCallback('http://localhost:1337/parse','KERAS_SERVANT','KERAS_SERVANT',name = 'test_task')
