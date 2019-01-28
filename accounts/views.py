from music.models import Recommendation, UserSongs, Song
from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import UserProfileInfoForm, UserForm
from . models import UserProfileInfo
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic import UpdateView


class GeneralSettings(UpdateView):
    model = User
    template_name = 'accounts/general_settings.html'

    fields = ['username', 'first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('accounts:dashboard')


class ChangeSettings(UpdateView):
    model = UserProfileInfo
    template_name = 'accounts/profile_settings.html'

    fields = ['portfolio', 'profile_pic']

    def get_success_url(self):
        return reverse('accounts:dashboard')


@login_required(login_url='accounts:user_login')
def saved_songs(request):
    song_list = UserSongs.objects.filter(user=request.user.id)
    return render(request, 'accounts/favorite_songs.html', {
        'song_list': song_list,
    })


@login_required(login_url='accounts:user_login')
def index(request):
    current_user = UserProfileInfo.objects.get(user=request.user)
    friend_list = current_user.friends.all()
    recommended_songs = Recommendation.objects.filter(recommended_to_id=request.user.id)
    return render(request, 'accounts/home.html', {
        'current_user' : current_user,
        'friends' : friend_list,
        'recommended_songs' : recommended_songs
    })


def recommend_song(request, pk):
    to_user = User.objects.get(id=pk)
    song_list = UserSongs.objects.filter(user=request.user.id)
    return render(request, 'accounts/recommend_song.html',
                  {
                      'friend' : to_user,
                      'song_list' : song_list,
                  })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('music:album-list'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/registration.html',
                  {
                      'user_form' : user_form,
                      'profile_form' : profile_form,
                      'registered' : registered
                  })


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:dashboard'))

            else:
                return HttpResponse('<h2> Account Not Active </h2>')

        else:
            print('Someone tried to login failed on our site.')
            return HttpResponse('<h2>Invalid login credentials applied </h2>')

    else:
        return render(request, 'accounts/login.html', {})


def all_users(request):
    if request.user.is_anonymous:
        people = UserProfileInfo.objects.all()

    else:
        current_user = User.objects.get(username=request.user)
        print(current_user.id)
        current_instance = UserProfileInfo.objects.get(id=current_user.id)

        print(current_instance.friends.all())

        friend_list = [x.id for x in current_instance.friends.all()]

        people = UserProfileInfo.objects.exclude(user=request.user)

    return render(request, 'accounts/people.html',
                  {
                      'people' : people,
                      'friend_list' : friend_list
                  })


# Ajax based call to recommend a song to a friend.
def recommend_ajax(request):
    if request.method == 'POST':
        song_name = request.POST.get('song_name')
        user_to = request.POST.get('user_to')
        user_by = request.POST.get('user_by')

        # print(song_name)
        # print(user_to)
        # print(user_by)

        user_to_instance = User.objects.get(username=user_to)
        user_by_instance = User.objects.get(username=user_by)
        song_instance = Song.objects.get(song_name=song_name)

        recommended_song = Recommendation.objects.create(recommended_by=user_by_instance,
                                                         recommended_to=user_to_instance,
                                                         recommended_song=song_instance)
        recommended_song.save()

    return HttpResponse(status=204)


def add_friend(request):
    if request.method == 'POST':
        current_user = request.POST.get('current_user')
        follow_user = request.POST.get('follow_user')

        current_user = User.objects.get(username=current_user)
        follow_user = User.objects.get(username=follow_user)

        current_instance = UserProfileInfo.objects.get(user_id=current_user.id)
        follow_instance = UserProfileInfo.objects.get(user_id=follow_user.id)

        current_instance.friends.add(follow_instance)
        follow_instance.friends.add(current_instance)

        current_instance.save()
        follow_instance.save()

        print(current_instance.friends.all())
        print(follow_instance.friends.all())

    return HttpResponse(status=204)


def test(request):
    if request.method == 'POST':
        username = request.POST.get('somedata')
        password = request.POST.get('moredata')
        message = "This is an Ajax message" + username + password
    else:
        message = "Ajax error"
    return render(request, 'accounts/ajax.html', {'message': message})
