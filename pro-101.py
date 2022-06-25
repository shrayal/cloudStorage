import dropbox

class TransferData:
    def_init_(self,access_token):
        self.access_token = access_token

    def upload_file(self , file_from , file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from , 'rb')
        dbx.file_upload(f.read() , file_to)

    def main:
        access_token=