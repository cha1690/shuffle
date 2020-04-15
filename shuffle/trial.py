# from apiclient.discovery import build
#
# DEVELOPER_KEY = "AIzaSyDEgXt5MtD9-J3B1B5x9KlxOnP1etevG6w"
# YOUTUBE_API_SERVICE_NAME = "youtube"
# YOUTUBE_API_VERSION = "v3"
#
# youtube_object = build(YOUTUBE_API_SERVICE_NAME,
#                        YOUTUBE_API_VERSION,
#                        developerKey=DEVELOPER_KEY)
#
#
# def get_videos():
#     categoryID= [2,17,22,]
#     choices = map(str, categoryID)
#     playlist=[]
#     for choice in choices:
#         video_category = youtube_object.videos().list(
#             part="snippet,contentDetails,statistics",
#             chart="mostPopular",
#             regionCode="IN",
#             videoCategoryId=choice
#         ).execute()
#         results = video_category.get("items", [])
#         for result in results:
#             playlist.append(result["id"])
#     print(playlist)
#
# if __name__ == "__main__":
#     get_videos()
