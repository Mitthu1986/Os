import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(fileFrom):
            for fileName in files :
                localPath =os.path.join(root,fileName)
                relative_path=os.path.relpath(localPath,fileFrom)
                dropbox_path=os.path.join(fileTo,relative_path)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
def main():
    access_token='sl.ApFHWTqgQINmRzN8g_BnPRKciKe4VUbx6RZX77mm6_kq9aOvfm95Fm6uthq505L4E-PG8vR82p6UpcCuzLi-kNaSDyAwPPNEjEn8m4EwddD2N1-K1jHz3M-bpTzGyzL4gZI04sw'
    dataTransfer=TransferData(access_token)
    fileFrom=str(input('Enter the folder path to transfer...'))
    fileTo=input('Enter the full path to upload to dropbox')
    dataTransfer.upload_files(fileFrom,fileTo)
    print('Come out of dreamland plz, the file has been moved...')

main()



