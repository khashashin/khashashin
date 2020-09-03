from me.models import Me, SocialAccounts, Work, Education, Skills, Projects
from rest_framework import serializers


class SocialAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccounts
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class MeSerializer(serializers.ModelSerializer):
    social_accounts = SocialAccountsSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    skills = SkillsSerializer(many=True, read_only=True)
    projects = ProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = Me
        fields = [
            'first_name',
            'last_name',
            'img_width',
            'img_height',
            'tmb_width',
            'tmb_height',
            'image',
            'tmb_image',
            'slogan',
            'title',
            'about',
            'phone_number',
            'email',
            'website',
            'street',
            'street_number',
            'state',
            'land',
            'zip',
            'social_accounts',
            'work',
            'education',
            'skills',
            'projects'
        ]
