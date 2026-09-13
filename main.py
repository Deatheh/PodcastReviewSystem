# class Podcast():

#     def __init__(self, title, description):
#         self.__id = len(podcast)
#         self.__title = title
#         self.__description = description
#         self.__rate = None
#         self.__reviews = []

#     @property
#     def id(self):
#         return self.__id

#     @property
#     def title(self):
#         return self.__title

#     @title.setter
#     def title(self, title):
#         if len(title > 3 ):
#             self.__title = title
#         else:
#             print("Title len must be more then 3 chars!")

#     @property
#     def description(self):
#         return self.__description

#     @description.setter
#     def description(self, description):
#         if len(description > 3 ):
#             self.__description = description
#         else:
#             print("Description len must be more then 3 chars!")

#     @property
#     def rate(self):
#         return self.__rate
        

# class Review():

#     def __init__(self):
        

podcast = []
rewiews = []


def addPodcast(title):
    if title in podcast:
        print(f"Title {title} already exsist!")
        return
    if len(title) < 4:
        print(f"Title {title} is to short!")
        return
    podcast.append(title)



def addComment(podcastId, text):
    if (isExsistPodcatById(podcastId)):
        comment = [podcastId, text]
        rewiews.append(comment)
    else:
        print(f"Podcast with id {podcastId} is not exsist")


def isExsistPodcatById(id):
    try:
        podcast[id]
        return True
    except:
        return False

def isExsistCommentById(id):
    try:
        rewiews[id]
        return True
    except:
        return False


if __name__ == "__main__":
    print("Add posdcast 1")
    addPodcast("Podcast 1")
    print("Add podcast 2")
    addPodcast("Podcast 2")
    print("Add comment 1")
    addComment(0, "commnet 1 to 1 podcast")
    print("Add comment to not exsist podcast")
    addComment(3, "Comment to not exsist podcast")
    print(podcast)
    print(rewiews)
    print("Is exsist podcast:")
    print("1: " + str(isExsistPodcatById(0)))
    print("2: " + str(isExsistPodcatById(1)))
    print("3: " + str(isExsistPodcatById(2)))
    print("Is exsist commnet:")
    print("1: " + str(isExsistCommentById(0)))
    print("2: " + str(isExsistCommentById(1)))