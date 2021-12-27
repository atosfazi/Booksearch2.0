from django.urls import path

from .views import HomePageView, SearchResultsView, TransformerRecommendationResultsView, Word2VecRecommendationResultsView, CustomEmbeddingRecommendationResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('similar_transformer_based/', TransformerRecommendationResultsView.as_view(), name='transformer_similar_books_results'),
    path('similar_word2vec_based/', Word2VecRecommendationResultsView.as_view(), name='word2vec_similar_books_results'),
    path('similar_custom_embedding_based/', CustomEmbeddingRecommendationResultsView.as_view(), name='customemb_similar_books_results'),
    path('', HomePageView.as_view(), name='home'),
]