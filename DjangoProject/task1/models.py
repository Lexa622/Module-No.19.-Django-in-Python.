from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=50)  # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)     # баланс(DecimalField)
    age = models.IntegerField()     # возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)    # название игры
    cost = models.DecimalField(max_digits=6, decimal_places=2)    # цена(DecimalField)
    size = models.DecimalField(max_digits=9, decimal_places=2)    # размер файлов игры(DecimalField)
    description = models.TextField()    # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)    # ограничение возраста 18+ (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='games')    # покупатель обладающий игрой (ManyToManyField).
    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.

    def __str__(self):
        return self.title


#   Модель для категории новостей
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


#   Модель новость
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']  # Сортировка по дате создания в обратном порядке
    # DecimalField - поле для дробных чисел.
    # BooleanField - поле для булевых значений.
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py startapp task1
# cd DjangoProject
