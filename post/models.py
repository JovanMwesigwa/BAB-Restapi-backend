from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from account.models import Profile

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    # products = models.ManyToManyField('Product', related_name='category_products', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    color = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, )
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='category', default=12, on_delete=models.CASCADE, null=True, blank=True)
    offer = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # likes = models.ManyToManyField('LikePost', related_name='likes', null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True )

    class Meta:
        ordering = ['-created']

    # index_together = ('id', 'slug')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    # 	return reverse('shop:product_detail', args=[self.id, self.slug])


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # active = models

    def __str__(self):
        return 'Comment by, {} on {}'.format(self.author.user, self.post.title)


class LikePost(models.Model):
    liker = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    liked_post = models.ManyToManyField(Post, related_name='likes',)
    date_liked = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return '{} liked some post'.format(self.liker)

