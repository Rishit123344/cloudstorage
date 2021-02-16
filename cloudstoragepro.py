import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Fi1w4B2KeSYAAAAAAAAAAXwbQETv2Mq8azn0n4IaHVsnO8c8Bm5xLar81STEv76B'
    transferData = TransferData(access_token)

    file_from = 'text.txt'
    file_to = '/newfolder/text.txt'

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()