from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Project, Review
from .forms import EditProfileForm, AddProjectForm, AddReviewForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProfileSerializer, ProjectSerializer
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    projects=Project.objects.all()
    title='welcome to awards app where you can vote for any project.'
    return render(request, 'index.html', {'title':title, 'projects':projects})
    
@login_required(login_url='login')
def profile(request):
    title='Build your profile'
    current_user = request.user
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user =current_user
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm()

    project=Project.get_project_by_user(Project,current_user)
    user=current_user
    profile=Profile.get_profile(Profile, user)
    return render(request, 'profile.html', {'title':title, 'profile':profile, 'projects':project,'form':form})

@login_required(login_url='login')
def new_project(request):
    title='Add a project of your own'
    current_user = request.user
    project=Project.objects.all()
    if request.method == 'POST':
        form =AddProjectForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            project = form.save(commit=False)
            project.user =current_user
            
            project.save()
        return redirect('home')

    else:
        form = AddProjectForm()
    
    return render(request, 'new_project.html', {'title':title,'form':form})


@login_required(login_url='login')
def review(request, project):
    projects=Project.objects.get(id=project)
    rankings=Review.objects.filter(project=projects).all()
    # status=None
    if request.method=='POST':
        form=AddReviewForm(request.POST)
        if form.is_valid():
            rating=form.save(commit=False)
            rating.user=request.user
            rating.project=projects
            rating.save()

            project_ratings=Review.objects.filter(project=project)

            design=[r.design_rating for r in project_ratings]
            design_average=sum(design) /len(design)

            content=[c.content_rating for c in project_ratings]
            content_average=sum(content) /len(content)

            usability=[u.usability_rating for u in project_ratings]
            usability_average=sum(usability) /len(usability)
            score=(design_average + content_average + usability_average)/3
            rating.design_avg=round(design_average, 2)
            rating.usability_avg=round(usability_average, 2)
            rating.content_avg=round(content_average, 2)
            rating.score=round(score, 2)
            rating.save()
            print(rating)

            return HttpResponseRedirect(request.path_info)
    else:
        form=AddReviewForm()

    parameters={
        'project':project,
        'rank_form':form,
        'id':project,
        'ranks':rankings
        # 'rating_status':status
    }
    return render(request, 'review.html', parameters )


def search_project(request):
    title="Find"
    projects=Project.objects.all()
    
    if 'project_name' in request.GET and request.GET['project_name']:
        search_term = request.GET.get('project_name')
        found_results = Project.objects.filter(name__icontains=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{'title':title,'results': found_results, 'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


    #    API
class profileList(APIView):
    def get(self, request, format=None):
        all_profiles= Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)

class projectList(APIView):
    def get(self, request, format=None):
        all_profiles= Project.objects.all()
        serializers = ProjectSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_profile(pk)
        serializers = ProfileSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProfileSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        merch = self.get_profile(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_project(pk)
        serializers = ProjectSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = ProjectSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        merch = self.get_project(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)