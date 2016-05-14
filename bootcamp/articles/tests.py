from django.test import TestCase
from django.contrib.auth.models import User
from bootcamp.articles.models import Article
# Create your tests here.


class ArticleTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="user1", password="password")
        user = User.objects.get(username="user1")

        self.article = Article(title="test2", content="test content",
                               create_user=user)
        self.article.save();

    def tearDown(self):
        for article in Article.objects.all():
            article.delete()

        for user in User.objects.all():
            user.delete()

    def testSaveArticle(self):
        self.assertEqual(Article.objects.all()[0].title, "test2")

    def testGetPublishedArticles(self):
        # change status to Published
        self.article.status = 'P'
        self.article.save()
        self.assertEqual(Article.get_published()[0], self.article)

    def testGetSummary(self):
        self.assertEqual(Article.objects.all()[0].get_summary(),
                         self.article.content)

    def testCreateTags(self):
        self.article.create_tags("tag1 tag2")
        self.assertEqual(str(Article.objects.all()[0].get_tags()),
                         '[<Tag: tag1>, <Tag: tag2>]')

    def testGetComments_None(self):
        self.assertEqual(Article.objects.all()[0].get_comments(),
                         self.article.get_comments())
