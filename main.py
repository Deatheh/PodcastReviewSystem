# Pr 1
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