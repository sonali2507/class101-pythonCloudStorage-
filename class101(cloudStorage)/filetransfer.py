from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
           '''upload a file to Dropbox
           using API V2'''
           dbx = dropbox.Dropbox(self.access_token)

           with open(file_from,'rb') as f:
               dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BEbHRH65GoQyQPf2LJL06rq2VZV0NbmjWnxfqVqbG2AWfOzr33GdyJjtQ8YdlBhVnvwDhYnW3esSM8sxDJ7OfcxHboClnPS8E16AmeG99h3b7CuFvxYX67OnRjr0eTDM5izD8R6RtWov'
    transferData = TransferData(access_token)
    
    file_from = input("Enter the file path to transfer:= ")
    file_to = input("Enter the full path to upload to Dropbox:= ")

    #API V2
    transferData.upload_file(file_from,file_to)
    print("File has been moved!!!")
if __name__ == '__main__' :
    main()   

    # C:/Users/SONALI/Desktop/python/python_Notes/test1.txt
    # C:/Users/SONALI/Desktop/coding/certificate/class100.pdf