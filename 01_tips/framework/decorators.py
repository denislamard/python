import logging
from .exceptions import IllegalArgumentError
from .models import UserRole
from django.core.exceptions import PermissionDenied


class ManageExcept(object):
    def __init__(self, exceptions):
        if type(exceptions).__name__ != 'list':
            raise IllegalArgumentError('parameter "Exceptions given" must be a list contains Exception classes')
        self.exceptions = exceptions        
    
    def __call__(self, func):
        def wrapped(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                if e not in self.exceptions:
                    raise e
            logger = logging.getLogger(__name__)
            logger.error(e)   
        return wrapped

class role_required(object):
    logger = logging.getLogger(__name__)
    
    def __init__(self, givenRoles):
        if type(givenRoles).__name__ != 'list':
            raise IllegalArgumentError('parameter "givenRoles" must be a list contains roles for user')
        self.givenRoles = givenRoles
        
    def __call__(self, func):
        def wrapped(view, *args, **kwargs):
            if view.request.user.is_authenticated():
                listUserRole = UserRole.objects.filter(user=view.request.user)
                for role in listUserRole:
                    if role.role.name in self.givenRoles:
                        return func(view, *args, **kwargs)
            self.logger.warning('the user "{} {}" has tried to access to a forbidden page'.format(view.request.user.first_name, view.request.user.last_name))        
            raise PermissionDenied        
        return wrapped
    
    
    
    
    
    
'''    
INSERT INTO public.eff_role(name) VALUES ('manager');
INSERT INTO public.eff_role(name) VALUES ('user');
INSERT INTO public.eff_role(name) VALUES ('R&D');
   
   
INSERT INTO public.eff_userrole(id_role, id_user) VALUES (1, 1);   
   
'''    