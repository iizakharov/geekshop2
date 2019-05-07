import requests
from io import BytesIO

from social_core.exceptions import AuthForbidden
from django.core import files

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        # print(response.keys())
        # print(response.items())
        if 'gender' in response.keys():
            if response['gender'] == 'male':
                user.shopuserprofile.gender = ShopUserProfile.MALE
            else:
                user.shopuserprofile.gender = ShopUserProfile.FEMALE

        if 'tagline' in response.keys():
            user.shopuserprofile.tagline = response['tagline']

        if 'aboutMe' in response.keys():
            user.shopuserprofile.aboutMe = response['aboutMe']

        if 'picture' in response.keys():
            url = response['picture']
            resp = requests.get(url)
            if resp.status_code != requests.codes.ok:
                print('error')

            fp = BytesIO()
            fp.write(resp.content)
            file_name = url.split("/")[-1]
            user.avatar.save(file_name, files.File(fp))

        if 'ageRange' in response.keys():
            minAge = response['ageRange']['min']
            if int(minAge) < 18:
                user.delete()
                raise AuthForbidden('social_core.backends.google.GoogleOAuth2')
        user.save()
    elif backend.name == "vk-oauth2":
        # print(response.keys())
        # print(response.items())
        if 'photo' in response.keys():
            url = response['photo']
            resp = requests.get(url)
            print(f'{resp} | {resp.content}')
            if resp.status_code != requests.codes.ok:
                print('error')

            fp = BytesIO()
            fp.write(resp.content)
            file_name = url.split("/")[-1]
            user.avatar.save(file_name, files.File(fp))
