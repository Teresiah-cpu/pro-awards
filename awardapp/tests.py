from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review,Project,Profile

# Create your tests here.
class ReviewTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_review = Review.objects.create(user=self.robert,
                                                design_rating =4,
                                                design_avg=4,
                                                usability_rating =4,
                                                usability_avg=4,
                                                content_rating=4,
                                                content_avg=4,
                                                comment='Superb',
                                                score=4)
        self.test_review.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_review, Review))

    #Testing Save method
    def test_save_method(self):
        self.test_review.save()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    # Tear down
    def tearDown(self):
        Review.objects.all().delete()

    # delete methodTesting 
    def test_delete_review(self):
        self.test_review.delete()
        self.assertEqual(len(Review.objects.all()), 0)

class ProjectTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_profile= Project.objects.create(user=self.robert,
                                                name ='Obamana',
                                                project_image ='picture.jpg',
                                                about ='The greatest of all projects',
                                                project_link='https://obamana.com',)
        self.test_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Project))

    #Testing Save method
    def test_save_method(self):
        self.test_profile.save()
        profile = Project.objects.all()
        self.assertTrue(len(profile)>0)

    # Tear down
    def tearDown(self):
        Project.objects.all().delete()

    # delete methodTesting 
    def test_delete_project(self):
        self.test_profile.delete()
        self.assertEqual(len(Project.objects.all()), 0)


class ProfileTest(TestCase):
    def setUp(self):
        self.robert= User.objects.create(username="Robert")
        self.test_profile= Profile.objects.create(user=self.robert,
                                                bio ='No retreat no surrender',
                                                profile_pic ='picture.jpg',
                                                contact='0701316729' )
        self.test_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))

    #Testing Save method
    def test_save_method(self):
        self.test_profile.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    # Tear down
    def tearDown(self):
        Profile.objects.all().delete()

    # delete methodTesting 
    def test_delete_profile(self):
        self.test_profile.delete()
        self.assertEqual(len(Profile.objects.all()), 0)