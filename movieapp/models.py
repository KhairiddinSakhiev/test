from django.db import models

class ConstFields:
    languages = (
        (1, "English"),
        (2, "Russian"),
        (3, "Tajik"),
    )
    gender = (
        (1, "Male"),
        (2, "Female"),
    )
class Movie(models.Model):
    mov_title = models.CharField(max_length=50)
    mov_time = models.DateTimeField(auto_now_add=False)
    mov_year = models.IntegerField()
    mov_lang = models.IntegerField(max_length=3, choices=ConstFields.languages, default=3)
    move_rel_country = models.CharField(max_length=30)


class Actor(models.Model):
    act_id = models.IntegerField()
    act_fname=models.CharField(max_length=20)
    act_lname=models.CharField(max_length=20)
    act_gender=models.IntegerField(max_length=10, choices=ConstFields.gender, default=1)
    movie = models.ManyToManyField(Movie, related_name="movie_cast")
    


# class Director(models.Model):
#     dir_id = models.IntegerField()
#     dir_fname = models.CharField(max_length=20)
#     dir_lname = models.CharField(max_length=20)

# class Geners(models.Model):
#     gen_id = models.IntegerField()
#     gen_title = models.CharField(max_length=50)
