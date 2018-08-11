import pandas as pd

def lambda_handler(event, context):
    # print values to see if lambda_handler triggered
    print (event['key1'])
    print (event['key2'])
    print (event['key3'])

    print("reading excel")
    data_frame = pd.read_excel('C:\steel-eye\ISO10383_MIC.xls', sheetname='MICs Modifications')

    row_list = data_frame.to_dict(orient='row')

    print('num of rows: %d ' % len(row_list))

    with open('C:\steel-eye\data.json', 'wb') as outfile:
        json.dump(row_list, outfile)

    return 'Returning from Lambda'

if __name__ == "__main__":

    # simulate the event and context object for testing locally out of Lambda
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
            
