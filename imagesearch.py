from google_images_download import google_images_download  #used for searching and downloading images
response = google_images_download.googleimagesdownload()
search_queries=[]
keyw=int(input("Enter number of keywords : "))             #number of keywords that an user wants to search
for i in range(keyw):
    a=[]
    userinput=input("Enter keyword : ")
    a.append(userinput)
    n=int(input("Enter the required number of images : "))  #number of images of a particular keyword
    a.append(n)
    search_queries.append(a)
def downloadimages(search_queries):
    for query in search_queries:
        arguments = {"keywords": query[0],
                     "limit":query[1],
                     "print_urls":True,
                     "size": "medium",
                     "aspect_ratio": "panoramic"}
        try:
            response.download(arguments)
        except FileNotFoundError:                            #if the file is not found, aspect_ratio can be changed to check
            arguments = {"keywords": query[0],
                         "limit":query[1],
                         "print_urls":True,
                         "size": "medium"}
            try:
                response.download(arguments)
            except:                                          #if the image does not exist
                pass
downloadimages(search_queries)
print()
