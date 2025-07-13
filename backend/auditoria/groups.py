from django.contrib.auth.models import Group, Permission

def create_default_groups():
    groups = ['admin', 'ale']
    for name in groups:
        Group.objects.get_or_create(name=name)

def assign_user_to_group(user, role_name):
    """Assigns a user to a group."""
    group = Group.objects.get(name=role_name)
    user.groups.add(group)

def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()