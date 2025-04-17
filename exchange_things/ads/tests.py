from django.test import TestCase
from django.urls import reverse

from exchange_things.ads.models import Ads
from exchange_things.category.models import Category
from exchange_things.condition.models import Condition
from exchange_things.users.models import User


class TestAds(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="Name1",
            last_name="Family1",
            username="NameFamily1",
            email="NameFamily1@mail.tu",
        )
        self.user = User.objects.get(id=1)

        condition1 = Condition.objects.get(pk=1)
        condition2 = Condition.objects.get(pk=2)
        condition3 = Condition.objects.get(pk=3)
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category3 = Category.objects.get(pk=3)

        Ads.objects.create(
            title="title1",
            description="description1",
            image_url="image_url1",
            category=category1,
            condition=condition1,
        )
        Ads.objects.create(
            title="title2",
            description="description2",
            image_url="image_url2",
            category=category2,
            condition=condition2,
        )
        Ads.objects.create(
            title="title3",
            description="description3",
            image_url="image_url3",
            category=category3,
            condition=condition3,
        )

    def test_ads_list(self):
        response = self.client.get(reverse("ads"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ads.objects.count(), 3)

    def test_ads_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("ads_create"),
            {
                "title": "title4",
                "description": "description4",
                "image_url": "image_url4",
                "category": 3,
                "condition": 3,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("ads"))
        response = self.client.get(reverse("ads"))
        self.assertEqual(Ads.objects.count(), 4)

    def test_ads_update(self):
        self.client.force_login(self.user)
        ad = Ads.objects.get(id=3)
        response = self.client.post(
            reverse("ads_update", kwargs={"ads_id": ad.pk}),
            {
                "title": "title-new",
                "description": "description-new",
                "image_url": "image_url-new",
                "category": 2,
                "condition": 3,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("ads"))
        ad.refresh_from_db()
        self.assertEqual([ad.title, ad.description], ["title-new", "description-new"])

    def test_ad_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("ads_delete", kwargs={"ads_id": 1}))
        self.assertRedirects(response, reverse("ads"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ads.objects.count(), 2)
