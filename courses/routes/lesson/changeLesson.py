from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from courses.models import Lesson, Course
from courses.serializers.lesson import LessonCreateSerializer
from accounts.permissions import IsTeacher


class ChangeLessonAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def put(self, request, course_id, lesson_id):
        course = get_object_or_404(Course, id=course_id)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
        serializer = LessonCreateSerializer(lesson, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
