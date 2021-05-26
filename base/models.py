from django.db import models

#richtext editor
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#slug
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=200)



	def __str__(self):
		return 	self.name

class Post (models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, blank=True, null=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to = "images", default="placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True) 
	slug = models.SlugField(blank=True, null=True)

	def __str__(self):
		return self.headline


	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count+=1
				slug = slugify(self.headline) + '-' + str(count)
				has_slug = Post.objects.filter(slug=slug).exists()
				

			self.slug = slug

		super().save(*args, **kwargs)


class Signup(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=32)

	def __str__(self):
		return 	self.username