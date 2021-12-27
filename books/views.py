from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Book
from unidecode import unidecode
from django.conf import settings


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        '''https://docs.djangoproject.com/en/3.1/ref/models/querysets/#queryset-api'''
        query = self.request.GET.get('q')
        if len(query) <= 2:
            return None
        object_list = Book.objects.filter(
            Q(title__icontains=str(query)) | Q(author__icontains=unidecode(query))
        )
        return object_list


class TransformerRecommendationResultsView(ListView):
    model = Book
    template_name = 'transformer_similar_books_results.html'
    # get loaded embedding weights end embedding indexes dict
    transformer_recommendations = getattr(settings, "TRANSFORMER_RECOMMENDATIONS", None)

    def get_queryset(self):
        query = self.request.GET.get('p')
        recommendations = self.find_recommendation(query)
        object_list = Book.objects.filter(Q(book_id__in=recommendations))
        return object_list

    def find_recommendation(self, book_id, n=4):
        recommendations = self.transformer_recommendations[int(book_id)][:n]
        # Get elements closest to sample
        return recommendations


class Word2VecRecommendationResultsView(ListView):
    model = Book
    template_name = 'word2vec_similar_books_results.html'
    # get loaded embedding weights end embedding indexes dict
    word2vec_recommendations = getattr(settings, "WORD2VEC_RECOMMENDATIONS", None)

    def get_queryset(self):
        query = self.request.GET.get('p')
        recommendations = self.find_recommendation(query)
        object_list = Book.objects.filter(Q(book_id__in=recommendations))
        return object_list

    def find_recommendation(self, book_id, n=4):
        recommendations = self.word2vec_recommendations[int(book_id)][:n]
        # Get elements closest to sample
        return recommendations


class CustomEmbeddingRecommendationResultsView(ListView):
    model = Book
    template_name = 'customemb_similar_books_results.html'
    # get loaded embedding weights end embedding indexes dict
    word2vec_recommendations = getattr(settings, "CUSTOM_EMBEDDING_RECOMMENDATIONS", None)

    def get_queryset(self):
        query = self.request.GET.get('p')
        recommendations = self.find_recommendation(query)
        object_list = Book.objects.filter(Q(book_id__in=recommendations))
        return object_list

    def find_recommendation(self, book_id, n=4):
        recommendations = self.word2vec_recommendations[int(book_id)][:n]
        # Get elements closest to sample
        return recommendations
