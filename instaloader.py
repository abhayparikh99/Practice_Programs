import instaloader
data = instaloader.Instaloader()
name = input("Enter insta profile : ")
data.download_profile(name,profile_pic_only = True)