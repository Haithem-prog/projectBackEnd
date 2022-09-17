from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Book(models.Model):
    name = models.CharField('name', max_length=255)
    bookImageUrl = models.URLField(null= True, blank= True, default= 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png') # add this instead of book_image
    published = models.DateField(editable=True, verbose_name='Published Data')
    description = models.TextField('description', null=True, blank=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    rate = models.DecimalField('rate', blank=True, null=True, max_digits=2, decimal_places=1)
    pages = models.IntegerField('pages')
    total_sales = models.IntegerField()
    genre = models.ForeignKey('Genre', verbose_name='genre', related_name='books', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('Author', verbose_name='author', related_name='books', null=True, blank=True, on_delete=models.SET_NULL)
    language = models.CharField('Language',max_length=10,choices=[
        ('Arabic','Arabic'),
        ('English','English'),
    ])
    def __str__(self):
        return self.name


class Saved_Books(models.Model):
    user = models.ForeignKey(User, verbose_name=("user_saved_Books"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=("saved_Books"), on_delete=models.CASCADE, related_name='here')
    saved = models.BooleanField('isSaved')
    def __str__(self):
        return self.book.name
    

class Items(models.Model):
    user = models.ForeignKey(User, verbose_name='user', related_name='DesiredBooks', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='book', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    inCart = models.BooleanField(default=False)
    isBought = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.book.name}'


class Genre(models.Model):
    name = models.CharField('name', max_length=255)
    genresImageUrl = models.URLField(null= True, blank= True, default= 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png') # add this instead of book_image
    is_active = models.BooleanField('is active')
    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField('name', max_length=255)
    authorImageUrl = models.URLField(null= True, blank= True, default= 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png') # add this instead of book_image
    is_active = models.BooleanField('is active')
    def __str__(self):
        return f'{self.name}'
