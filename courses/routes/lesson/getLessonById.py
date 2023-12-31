from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Lesson
from courses.serializers.lesson import LessonDetailSerializer


class LessonDetailView(APIView):
    def get(self, request, course_id, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id, course_id=course_id)
        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)
