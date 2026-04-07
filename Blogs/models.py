from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
STATUS_CHOICES = ((0, 'Draft'), (1, 'Published'))   
)   
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d/', null=True, blank=True)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    blog_body = models.TextField(max_length=5000, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=draft)
    featured_post = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
