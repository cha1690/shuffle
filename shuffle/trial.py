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
#     video_category = youtube_object.videos().list(
#         part="snippet,contentDetails,statistics",
#         chart="mostPopular",
#         regionCode="IN",
#         videoCategoryId="1"
#     ).execute()
#
#     results = video_category.get("items", [])
#     videos_categories = []
#     for result in results:
#         videos_categories.append((result["id"], result["snippet"]["title"]))
#
#     # return videos_categories
#     print(videos_categories)
#
# if __name__ == "__main__":
#     youtube_video_categories()
