
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                   
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                #dropbox_path = os.path.join(file_to, file_from)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BEYtFvBUchX9CUMsH0lPzQspJnE_X0yJvE6QLi-adb8WqWU6ySs1lXcu0AyMs4-BRvCK5ifcM2-ErsaOwknh5zUVvl0TMMYeiv0ZfHY4SbCzAn8iuFtMNuW6cQwLNhj9FTy5ECo'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer:"))
    file_to = input("enter the full path to upload to dropbox:")  
    
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()