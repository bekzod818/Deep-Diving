VIMEO_ACCESS_TOKEN = "5ffe30c125f4f53d20209d237b699fa7"
VIMEO_CLIENT_ID = "627758e72e6d99c372875bf2e76240dc8c3e7883"
VIMEO_CLIENT_SECRET = "/lhQdsO4nk+VqJJUIFtYLiVka0KhQQhYRNcveeK594rmhhI8BJtSCrXyJsF8Q50DqwIxrhrI2soPfUPQkTXlJWGCwULDMdtdKLkD5nynRvwEIVIC+/lFUtRipnDya83X"


import vimeo

client = vimeo.VimeoClient(
    token=VIMEO_ACCESS_TOKEN, key=VIMEO_CLIENT_ID, secret=VIMEO_CLIENT_SECRET
)
uri = "/tutorial"

response = client.upload("/Users/bekzod/Downloads/12345.MP4")
print(response)
