from django.db import migrations
from django.contrib.auth.models import Group, Permission

def create_groups(apps, schema_editor):


    # create "Creator" group with "add_task" permission
    creator_group = Group.objects.create(name='Creator')
    add_task_permission = Permission.objects.get(codename='add_task')
    creator_group.permissions.add(add_task_permission)


    # create "Editor" group with "change_task" permissioneditor_group = Group.objects.create(name='Editor')
    editor_group = Group.objects.create(name='Editor')
    change_task_permission = Permission.objects.get(codename='change_task')
    editor_group.permissions.add(change_task_permission)


    # create "Admin" group with all permissions
    admin_group = Group.objects.create(name='Admin')
    all_permissions = Permission.objects.filter(content_type__app_label='tasks')
    admin_group.permissions.set(all_permissions)


class Migration(migrations.Migration):
    dependencies = [
    ('tasks', '0001_initial'),
    ]
    operations = [
    migrations.RunPython(create_groups),
    ]

