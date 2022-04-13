from django.db import models

class QuizzModel(models.Model):
    titre = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    niveau = models.IntegerField(max_length=200)
    photo = models.ImageField(upload_to='images/resolution-definition.jpg')

class QuesModel(models.Model):
    quizz = models.ForeignKey(QuizzModel,on_delete=models.CASCADE,null=True)
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def str(self):
        return self.question