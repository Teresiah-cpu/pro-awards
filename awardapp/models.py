from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.TextField(max_length=200, null=True, blank=True, default="name")
    project_image = models.ImageField(upload_to='Project_images/', null=True, blank=True)
    about = models.TextField()
    project_link=models.URLField(max_length=250)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    

    def save_project(self):
        self.save()

    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    def get_project_by_user(cls, user):
        projects = cls.objects.filter(user=user)
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def update_project(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    @classmethod
    def update_description(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    def __str__(self):
        return self.name

# class Review(models.Model):
    Rank_Index= ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),)

    design_rating = models.IntegerField(choices=Rank_Index, default=0)
    design_avg=models.FloatField(default=0, blank=True)
    usability_rating = models.IntegerField(choices=Rank_Index, default=0)
    usability_avg=models.FloatField(default=0, blank=True)
    content_rating = models.IntegerField(choices=Rank_Index, default=0)
    content_avg=models.FloatField(default=0, blank=True)
    comment = models.TextField()
    score=models.FloatField(default=0, blank=True)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def save_review(self):
        self.save()

    def get_review(self, id):
        reviews = Review.objects.filter(project=id)
        return reviews

    def average(self,design_rating, usability_rating, content_rating):
        avg=(design_rating+ usability_rating+content_rating)/2
        return avg

    def __str__(self):
        return self.comment


class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="Joy, peace...")
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default= 0)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    contact=models.IntegerField(default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def get_profile(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username