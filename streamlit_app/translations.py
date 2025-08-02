#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 17:55:50 2025

@author: matheoeymar
"""
translations = {
    'English 🇺🇸': {
        'title': "Sentiment analysis on movie reviews",
        'explications': "Here is a list of explanations as to why {len} movie reviews were classified as they were : {explications}. Make a list of maximum 5 bullet points of the main reasons why some reviews were classified as positive, and do the same for the negative ones but do not provide an explanation, just a reason for each bullet point and do not provide any other answer than the bullet points",
        'evaluation':"Evaluate the sentiment of the following movie review: '{prompt}'.Respond with 0 if the review is negative, 1 if it is positive. Respond with the number on the first line only. Then, on the next line, provide a brief explanation summarizing the key sentiment cues that led to your decision. Focus only on the content of the review and avoid speculation.",
        'welcome':"Welcome to our graphical interface for sentiment analysis on movie reviews, powered by GeminiAI.\n\n",
        'positive': "This movie review is positive\u00A0\u00A0👍",
        'negative': "This movie review is negative\u00A0\u00A0👎",
        'key_provided': "API key provided",
        'key_not_provided': "API key not provided",
        'key_error':"This app is not going to work without an API key. You need to get one.",
        'reset':"Reset History",
        'history' : 'Review history:',
        'message': "Please enter a movie review to analyze.",
        'bar':"Enter a movie review",
        'explications_message':"Here are the key points why movie reviews were classified as such : ",
        'button': "See Reasoning",
        
    },
    'French 🇫🇷': {
        'title': 'Analyse de sentiments sur des critiques de films',
        'explications': 'Voici une liste d’explications indiquant pourquoi {len} critiques de films ont été classées ainsi : {explications}. Dressez une liste de 5 points maximum des principales raisons pour lesquelles certaines critiques ont été classées comme positives, et faites de même pour celles classées comme négatives. Ne donnez pas d’explication, uniquement une raison par point. N’ajoutez aucune autre réponse que les listes à puces.',
        'evaluation': 'Évaluez le sentiment de la critique de film suivante : « {prompt} ». Répondez par 0 si la critique est négative, 1 si elle est positive. Répondez uniquement par le chiffre sur la première ligne. Ensuite, sur la ligne suivante, fournissez une brève explication résumant les éléments clés du texte qui ont motivé votre décision. Concentrez-vous uniquement sur le contenu de la critique et évitez toute spéculation.',
        'welcome':"Bienvenue sur notre interface d'analyse de sentiments sur des critiques de films, propulsée par GeminiAI.",
        'positive': "Cette critique est positive\u00A0\u00A0👍",
        'negative': "Cette critique est négative\u00A0\u00A0👎",
        'key_provided': "Clé API fournie",
        'key_not_provided': "Clé API non fournie",
        'key_error':"Cette application ne fonctionnera pas sans clé d'API. Veuillez vous en procurer une.",
        'reset':"Réinitialiser l'historique",
        'history': "Historique des critiques :",
        'message': "Veuillez entrer une critique de film à analyser.",
        'bar': "Entrez une critique de film",
        'explications_message':"Voici les principales raisons pour lesquelles les critiques ont été classifiées comme telles : ",
        'button': "Voir le raisonnement",
    }
}