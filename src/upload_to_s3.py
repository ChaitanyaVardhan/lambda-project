def lambda_handler(event, context):
    # TODO implement
    print (event['key1'])
    print (event['key2'])
    print (event['key3'])
    return 'Hello from Lambda'

if __name__ == "__main__":
    class Event:
        def __init__(self):
            self.key1 = 'val1'
            self.key2 = 'val2'
            self.key3 = 'val3'
        
        def __getitem__(self, item):
            return getattr(self, item)

    event = Event()
    context = {'key': 'dummy context'}

    print(lambda_handler(event, context))
            
