# -*- coding: utf-8 -*-
"""Xsfer gd to tera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/118htDK6HaGQC6fMl3XR8JAP9CdtMPuM3

<h3>Execute every node in sequence</h3>
*recomended <br/>
or u will miss some important edits
"""

# required modules installation
!pip install internetarchive

# downloading anytype of file from server
import urllib.request
# following variable keep target file location with file extension
# It is google photos export download link
tar_loc="10.zip"
urllib.request.urlretrieve('https://00f74ba44b06ad2b25331f2222d0a6d55fd7beefcb-apidata.googleusercontent.com/download/storage/v1/b/dataliberation/o/20210531T101632Z%2F7404861098411033338%2F121bdc54-40a4-427c-b8ca-882a6e8b3d56%2F1%2F38af1e43-9dbf-42c4-9bf2-2f4f7e48e461?jk=AFshE3WvL6UYYr--0UO14GbtXUT2XMMJi0oQHYI7UPZ6JTrIjCpqaS6pG7cDfgB4gmIcIv0E4H70nveONj85dX-JAYVlOLvchlHjELfzrDfb6-ilfm3dt7v9QWJs0N0Wj32h7JFRGccO3ff1-F3OtB2UYk5TKG8DK5S3NEfTSShFa-cYdC8AhE7tn8M1w8nouvBh6-UtxFgSYV919G-23DxC9BheLWhxeg_xT6wkEWXqmZu7GWWr39kl5SCAqhz4ONhjEkhRISH7KlomtJhIF52Us3P8smV1SzlQLsap5BIcZftwvbV4Y3mW3MUSRZ_Nk39Y42iO2J3-3oxzwejCW6oop7LKjIKjg-5wuygPw6butE8uoMC09wntfGEtqh_4ZyVtqMN1bKQgvYv7e0b9GPP5ZowWY12V3jFyJ9Zit3ZWqcGQZS_e7b42vsCb62Le1MAYbTUFje45VenOOilw9IjE6gZWdOtK9RAQ9CNCZaMPDHpVK7C7M9RgxuOCNqoAbinTZ5g4XHU6mufLnwMKu092HrfhalrlQMEylRv99wV50J-6p6e_MgSWJ7S0TAL9miFw_sgymXmD9Ry84zPBixIjz3w3eN79NQtmzyJbsV6kR2HwgEYonQAoaUfaLGggKi3CehOCl5VaTFCdeXboXxTweKBzq1hwMUVz6Ss2UKSl42vItFSh15uWvZ5pEocXqRwIs-_f5o8lm_7n7uXlyRFdDY1gS6ISDkKWD2vsftdTM94cLL5MAhhdF68Mn6pQ_kDNYiBUF2hohqib1sFij_4ULikWngT6ctZzQ5SSY7EnZJiWlAzeYZeJa0mbyCa1gsbOUX60K8OjIxjJpJP8u1NLeX9ALYj84kiCQljxTBaPNhKt28_0oE-5PcfHEP5JJzizS1SE3Sjh8131Wm6gg2MJSsSwvNOZDQ0awJN9XmeFaD2Iz0xA5aMzNarrbFCT0UzagTIL6nDDBE9StDAuD1rXAgVhXt6IpbvktnIBzQfFCX5YPCWqd6x-JaXbWR4IVnn55z9O_WarZwavAeAgvMVznje98SeWIj4FkvUrrz3Z7yfZR_dLF-HCz2dz1ORoFTWa3TxDbEJXT48WkguvwqU&isca=1',tar_loc)

#making new directory for opr.
os.mkdir("/content/KOTL/")

#moving to work folder to execute unzip process
work_fol="/content/KOTL"
os.chdir(work_fol)
if os.getcwd() == work_fol:
  print(f'directory changed to {work_fol}')

# copying zip file to work folder

# file_path="/content/drive/MyDrive/gp_310521/10.zip"
# target_loc="/content/KOTL/"
# z="!cp "+file_path+" "+target_loc
# os.popen(z)

# if os module don't work or coping undecided size file, then using unix command

# !cp "/content/drive/MyDrive/gp_310521/10.zip" "/content/KOTL/"

# or this for progress of copying file

!rsync -ah --progress "/content/drive/MyDrive/gp_310521/10.zip" "/content/KOTL/"
#1st parameter is source and 2nd is destination

# size suggestions in multiple of bytes / checking file size for confirmation.
# import os
file_loc="/content/KOTL/zipping/python.zip"
st=os.stat(file_loc).st_size
size="bytes"
gb=1
if st > gb*1024:
  size="kilobytes"
  gb=1024*gb
if st > gb*1024:
  size="megabytes"
  gb=1024*gb
if st > gb*1024:
  size="gigabytes"
  gb=1024*gb
if st > gb*1024:
  size="terabytes"
  gb=1024*gb
if str(st / gb).find('.') != 0:
  print(f'File Size in {size} is {str(st / gb)[0:(str(st / gb).find("."))+3]}')
else:
  print(f'File Size in {size} is {st / gb}')

#removing unwanted folder in google colab perticularly for tree structure deletion
import shutil
try:
  shutil.rmtree('/content/KOTL/Takeout')
except FileNotFoundError as er:
  print(er)

# unzipping with build-in module ZipFile
# directory or files names loop will truncate at 5000 lines [pre-decided]
import time
from zipfile import ZipFile
begin = time.time()
zip_loc="10.zip"
with ZipFile(zip_loc, 'r') as zip:
    print("available files in zip :\n")
    zip.printdir()
    print('\nExtracting all the files now...')
    zip.extractall()
    print('Unzipping Done!')
end = time.time()
print(f"\nTotal runtime of this code block is {end - begin}")

#making new directory for only .jpg type of files
#make sure KOTL folder already generated***
import os
try:
  os.mkdir("/content/KOTL/out")
except FileExistsError:
  print("folder already exists")
# now moving to that folder
work_fol="/content/KOTL/out"
os.chdir(work_fol)
if os.getcwd() == work_fol:
  print(f'directory changed to {work_fol}')

#taking out all .jpg .bmp .tif .tiff .jpeg .gif .png .eps images from this folder and all sub-folders
import glob
import os
i=0

#this function will remove <space>,),(,` from folder or file name
def changer(x):
  tmp=x
  if x.find(' ')>0:
    x=x.replace(' ','')
  if x.find('(')>0:
    x=x.replace('(','')
  if x.find('`')>0:
    x=x.replace('`','')
  if x.find(')')>0:
    x=x.replace(')','')
  print('changing name to ',x)
  os.rename(tmp,x)
  return x


def xsfer(cpf,cpt):
  types = ['*.bmp','*.tif','*.tiff','*.jpg', '*.jpeg','*.gif','*.png','*.eps']
  types1 = ['*.mp4']
  images = []
  for files in types1:
    images.extend(glob.glob(cpf + '/' +files))
  for x in images:
    if x.find(')') or x.find('(') or x.find(' ') or x.find('`'):
      x = changer(x)
    x='cp '+x+' '+ cpt
    os.popen(x)
    global i
    i=i+1
  pass
def caller(cpf,cpt):
  if cpf.find(')') or cpf.find('(') or cpf.find(' ') or cpf.find('`'):
    cpf = changer(cpf)
  print("changing to "+cpf+" .....")
  os.chdir(cpf)
  #these are the types of file we want to extract
  types = ['*.bmp','*.tif','*.tiff','*.jpg', '*.jpeg','*.gif','*.png','*.eps']
  types1 = ['*.mp4']
  files_grabbed = []
  for files in types1:
    files_grabbed.extend(glob.glob(cpf + '/' +files))
  if len(files_grabbed)>0:
    xsfer(cpf,cpt)
  dir=os.listdir('.')
  dir=list(filter(lambda x:x.find('.')<0,dir))
  print('available folders in ',dir)
  if len(dir)>0:
    for dir_loc in dir:
      caller(cpf+"/"+dir_loc,cpt)
  pass

#this function will do this process of copying data to needed folder
caller('/content/KOTL/Takeout','/content/KOTL/out2')
print("total number of images transfered ",i)

#check size of folder using subprocess
import subprocess
path = '/content/KOTL/out1'
size = subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')
print("Directory size: " + size)

#numbers of files available in this perticular folder
print("number of files available :",len([name for name in os.listdir(path) if os.path.isfile(name)]))

#creating a new directory for zipp files
import os
try:
  os.mkdir("/content/KOTL/zipping")
except FileExistsError:
  print("folder already exists")
# now moving to that folder
work_fol="/content/KOTL/zipping"
os.chdir(work_fol)
if os.getcwd() == work_fol:
  print(f'directory changed to {work_fol}')

#now compressing files available in '/content/KOTL/out2' or sub-folders to into gpcontent.zip
import os
import zipfile
    
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))
      
zipf = zipfile.ZipFile('/content/KOTL/zipping/gpcontent.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/content/KOTL/out2', zipf)
zipf.close()

#uploadiong to internetarchive.org using ia module
#configuring user details for login into account

!ia configure

# or

# from internetarchive import configure
# configure('myemail!@example.com', 'password')

#checking secret content of created file
import os
fd = os.open('/root/.config/ia.ini',os.O_RDONLY)
os.lseek(fd, 0, 0)
str = os.read(fd, os.path.getsize(fd))
print(str.decode())

#creating session for upload
from internetarchive import get_session

#------ change these parameters as shown in above out field or got this url https://archive.org/account/s3.php after login
access = 'xxxxxxxxxxxxxxxx'
secret = 'xxxxxxxxxxxxxxxx'
#----------------------------

c = {'s3': {'access': access, 'secret': secret}}
session = get_session(config=c)
print(session)

# getting identifier for upload on ia
from internetarchive import get_item
cool_podcast = get_item('my_007') #this identifier is important, you need to init identifier before upload
print(cool_podcast.metadata)
upload_data = ['/content/KOTL/out'] # its an list of files or folders
# like the example given below, it will gonna upload every file available in that folder

# metadata of files we want to upload

md = {'title': 'Intellectual Property, and Other Legal Concerns" by Me (2016) - my_007',
      'mediatype': 'data',
      'collection': 'opensource_media',
      'date': '2021-06-01',
      'description': '<div><i>Pokémon GO</i> was an immediate sensation when Niantic released it in 2016, and it continues to be one of the highest-grossing apps on mobile devices. While the hype was still high, Tiffany C. Li wrote about potential legal rankles Niantic might face on the road to becoming a Poké Fan Master.<br /></div><div><br /></div><div><a href="https://osf.io/preprints/lawarxiv/gexpm/" rel="nofollow">The Paper.</a></div><div><br /></div><div>Mike Overby (<a href="https://twitter.com/lethargilistic" rel="nofollow">@lethargilistic</a>) reads <em>Amicus Lectio</em> (<a href="https://twitter.com/amicuslectio" rel="nofollow">@AmicusLectio</a></div>).',
      'subject': ['law', 'pokemon', 'pokemon go', 'amicus lectio',
                  'privacy', 'trespass', 'augmented reality', 'copyright',
                  'trademark', 'intellectual property'],
      'creator': 'HCS All Home',
      'language': 'English',
      'licenseurl': 'http://creativecommons.org/publicdomain/zero/1.0/'}

cool_podcast.upload(upload_data, metadata=md, verbose=True)
#this function return a status code like '200' which means everything is ok

#checking files uploaded on ia
from internetarchive import search_items
for item in search_items('identifier:hcs_007').iter_as_items():
  print(item.metadata['title'])

