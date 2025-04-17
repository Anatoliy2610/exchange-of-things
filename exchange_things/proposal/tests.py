from django.test import TestCase
from django.urls import reverse

from exchange_things.ads.models import Ads
from exchange_things.category.models import Category
from exchange_things.condition.models import Condition
from exchange_things.proposal.models import ExchangeProposal
from exchange_things.status.models import Status
from exchange_things.users.models import User


class TestProposal(TestCase):
    def setUp(self):
        User.objects.create(
            first_name="Name",
            last_name="Family",
            username="NameFamily",
            email="NameFamily@mail.ru",
        )
        self.user = User.objects.get(id=1)
        author1 = User.objects.create(
            first_name="Name2",
            last_name="Family2",
            username="NameFamily2",
            email="NameFamily2@mail.ru",
        )
        author2 = User.objects.create(
            first_name="Name3",
            last_name="Family3",
            username="NameFamily3",
            email="NameFamily32@mail.ru",
        )
        status1 = Status.objects.get(pk=1)
        status2 = Status.objects.get(pk=2)
        status3 = Status.objects.get(pk=3)
        condition1 = Condition.objects.get(pk=1)
        condition2 = Condition.objects.get(pk=2)
        condition3 = Condition.objects.get(pk=3)
        category1 = Category.objects.get(pk=1)
        category2 = Category.objects.get(pk=2)
        category3 = Category.objects.get(pk=3)

        ad1 = Ads.objects.create(
            title="Объявление1",
            description="Описание1",
            category=category1,
            condition=condition1,
            author=self.user,
        )
        ad2 = Ads.objects.create(
            title="Объявление2",
            description="Описание2",
            category=category2,
            condition=condition2,
            author=author1,
        )
        ad3 = Ads.objects.create(
            title="Объявление3",
            description="Описание3",
            category=category3,
            condition=condition3,
            author=author2,
        )

        ExchangeProposal.objects.create(
            ad_sender=ad1,
            ad_receiver=ad2,
            comment="comment1",
            status=status1,
            author=self.user,
            recipient=author1,
        )
        ExchangeProposal.objects.create(
            ad_sender=ad2,
            ad_receiver=ad3,
            comment="comment2",
            status=status2,
            author=author1,
            recipient=author2,
        )
        ExchangeProposal.objects.create(
            ad_sender=ad3,
            ad_receiver=ad1,
            comment="comment3",
            status=status3,
            author=author2,
            recipient=self.user,
        )

    def test_proposal_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("proposal"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ExchangeProposal.objects.count(), 3)

    def test_proposal_create(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("proposal_create"),
            {
                "ad_sender": 1,
                "ad_receiver": 2,
                "comment": "comment4",
                "status": 3,
                "author": 1,
                "recipient": 2,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("proposal"))
        response = self.client.get(reverse("proposal"))
        self.assertEqual(ExchangeProposal.objects.count(), 4)

    def test_ads_update(self):
        self.client.force_login(self.user)
        proposal = ExchangeProposal.objects.get(id=3)
        response = self.client.post(
            reverse("proposal_update", kwargs={"proposal_id": proposal.pk}),
            {
                "status": 2,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("proposal"))
        proposal.refresh_from_db()
        self.assertEqual(
            [proposal.status, proposal.ad_sender],
            [Status.objects.get(pk=2), Ads.objects.get(pk=3)],
        )

    def test_ad_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("proposal_delete", kwargs={"proposal_id": 1})
        )
        self.assertRedirects(response, reverse("proposal"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ExchangeProposal.objects.count(), 2)
