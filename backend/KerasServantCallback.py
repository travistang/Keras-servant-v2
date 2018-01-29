from keras.callbacks import Callback
from brokers import TaskBroker
from decimal import Decimal
class KerasServantCallback(Callback):
    def __init__(self,
            parse_server_url,
            parse_app_id,
            parse_master_key,
            object_id = None, # The id of the object in the database.
            report_gradients = False,
            report_activations = False,
            loss_func_builder = None,
            sample_data_generator = None,
            **args):
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
        self.report_activations = report_activations
        self.report_gradients = report_gradients
       
        if self.report_activations:
            if not sample_data_generator: raise ValueError("If report_activations is set to True, 'sample_data_generator' must be provided")
            self.sample_data_generator = sample_data_generator
        
        # create some placeholders and build the loss function for the gradient functions
        if self.report_gradients:
            if not loss_func_builder: raise ValueError("If report_gradients is set to True, 'loss_func_builder' must be provided")
            if not sample_data_generator: raise ValueError("If report_gradients is set to True, 'sample_data_generator' must be provided")
            self.loss_func_builder = loss_func
            self.sample_data_generator = sample_data_generator
            
    def set_model(self,model):
        self.model = model
        if self.report_activations:
            layer_outputs = [l.output for l in self.model.layers]
            self.activation_funcs = K.function(self.model.inputs,layer_outputs]
        if self.report_gradients:
            # create a list of placeholders
            self.target_phs = [K.placeholder(output.shape) for output in self.model.outputs]
            self.loss_func = self.loss_func_builder(self.model.outputs,self.target_phs)
            grad_ops = K.gradient(self.loss_func,self.model.trainable_weights)
            self.grad_log_function = K.function(self.model.inputs + self.target_phs,grad_ops)

    def on_train_begin(self,logs = {}):
        self.task['status'] = 'Started'
        self.task['total_epochs'] = self.params['epochs']
        self.task['epoch'] = 0
        self.update()

    def on_train_end(self,logs = {}):
        self.task['status'] = 'Ended'
        self.update()

    def on_batch_end(self,batch,logs = {}):
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
        self.update()
    def on_epoch_begin(self, epoch, logs=None):
        self.task['epoch'] = epoch
        self.update()

    def on_epoch_end(self, epoch, logs=None):
        if hasattr(self,'sample_data_generator'):
            data = sel.sample_data_generator.__next__()
            if len(data) == 2:
                X,y = data
            elif len(data) == 3:
                X,y,mask = data
            else:
                raise ValueError("The given data sample generator must have either 2 or 3 inputs")
        # then prepare the X,y for feeding into the functions
        X = [X]

        else:
            return # or do you need to log something at the end of the epoch?
        if self.report_activations:
            # gather activation information
            layer_outputs = self.activation_funcs(X) 
        if self.report_gradients:
            pass

    def update(self):
        self.broker.update_task(self.task)
if __name__ == '__main__':
    # Test here
    ksc = KerasServantCallback('http://localhost:1337/parse','KERAS_SERVANT','KERAS_SERVANT',name = 'test_task')
