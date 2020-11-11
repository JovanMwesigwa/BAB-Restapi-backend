from django.urls import path

from .views import (
			CategoryListView,
			CategoryDetailView,
			PostListView,
			PostCreateView,
			PostUpdateView,
			PostDeleteView,
			PostDetailView,
			CommentCreateView,
			CommentListView,
			CommentUpdateView,
			CommentDestroyView,
			CommentDetailView,
			CurrentUserPostListView,
			UserOnlyPostList,
			LikePostListView,
			LikePostDetailView,
			LikePostCreateView,
			LikePostDeleteView,
			)

urlpatterns = [
	path('categories/', CategoryListView.as_view(), name='category_list'),
	path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
	path('posts/', PostListView.as_view(), name='posts'),
	path('usersposts/', CurrentUserPostListView.as_view(), name='users_posts'),
	path('profileposts/<username>/', UserOnlyPostList.as_view(), name='profile_posts'),
	path('post/create/', PostCreateView.as_view(), name='post-create'),
	path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<pk>/detail/', PostDetailView.as_view(), name='post-detail'),
	path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('comments/', CommentListView.as_view(), name='comments'),
	path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
	path('comment/<pk>/detail/', CommentDetailView.as_view(), name='comment-detail'),
	path('comment/<pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
	path('comment/<pk>/delete/', CommentDestroyView.as_view(), name='comment-delete'),
	path('likes/', LikePostListView.as_view(), name="post-likes"),
	path('like_post/', LikePostCreateView.as_view(), name="like_post"),
	path('like_post/<pk>/detail/', LikePostDetailView.as_view(), name="like_post_detail"),
	path('unlike_post/<pk>/delete/', LikePostDeleteView.as_view(), name="delete_like_post"),

]
