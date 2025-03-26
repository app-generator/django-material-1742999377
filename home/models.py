# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    coop_id = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Questionnaire(models.Model):

    #__Questionnaire_FIELDS__
    questionnaire_code = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Questionnaire_FIELDS__END

    class Meta:
        verbose_name        = _("Questionnaire")
        verbose_name_plural = _("Questionnaire")


class Question(models.Model):

    #__Question_FIELDS__
    question_id = models.CharField(max_length=255, null=True, blank=True)
    questionnaire = models.CharField(max_length=255, null=True, blank=True)
    question_texte = models.TextField(max_length=255, null=True, blank=True)
    type_question = models.CharField(max_length=255, null=True, blank=True)
    obligatoire = models.BooleanField()
    ordre_affichage = models.IntegerField(null=True, blank=True)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")


class Questionchoix(models.Model):

    #__Questionchoix_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ordre = models.IntegerField(null=True, blank=True)
    texte = models.CharField(max_length=255, null=True, blank=True)

    #__Questionchoix_FIELDS__END

    class Meta:
        verbose_name        = _("Questionchoix")
        verbose_name_plural = _("Questionchoix")


class Questionligne(models.Model):

    #__Questionligne_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte = models.CharField(max_length=255, null=True, blank=True)
    ordre = models.IntegerField(null=True, blank=True)

    #__Questionligne_FIELDS__END

    class Meta:
        verbose_name        = _("Questionligne")
        verbose_name_plural = _("Questionligne")


class Questionnairesession(models.Model):

    #__Questionnairesession_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    date_creation = models.DateTimeField(blank=True, null=True, default=timezone.now)
    note = models.TextField(max_length=255, null=True, blank=True)

    #__Questionnairesession_FIELDS__END

    class Meta:
        verbose_name        = _("Questionnairesession")
        verbose_name_plural = _("Questionnairesession")


class Reponse(models.Model):

    #__Reponse_FIELDS__
    session = models.ForeignKey(QuestionnaireSession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ligne = models.ForeignKey(QuestionLigne, on_delete=models.CASCADE)
    choix = models.ForeignKey(QuestionChoix, on_delete=models.CASCADE)
    valeur_texte = models.TextField(max_length=255, null=True, blank=True)
    date_reponse = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Reponse_FIELDS__END

    class Meta:
        verbose_name        = _("Reponse")
        verbose_name_plural = _("Reponse")



#__MODELS__END
