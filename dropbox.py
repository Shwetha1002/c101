import dropbox

def main():
    access_token = 'sl.BIZoyfdOHyUZFB2n2QP-8grbyQNex0ahjX44kVTlTaCcoKBukt8AXjGPKyRZOIf_fbgB7vcNKn2v9CHjlAbYN9YxOmALbCHIFzj6pC8LF9r4EpE3AZB95gZaqEUTd80xun3MGUQ'
    transfer_data = transferData(access_token)


    firstFile = input("Enter the file path that needs to be transfered")
    secondFile = input("enter the file path to which data has to be transfered, enter the full path")
    
    transfer_data.uploadFile(firstFile, secondFile)
    print("yayyy! your file has been moved!")

class transferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, firstFile, secondFile):
     dbx = dropbox.Dropbox(self.access_token)
     f = open(firstFile, 'rb')
     dbx.files_upload(f.read(), secondFile)


main()