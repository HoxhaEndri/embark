from django.contrib import admin

from users.models import User, Team, TeamMember

admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamMember)
