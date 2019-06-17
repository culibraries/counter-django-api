__author__ = 'mstacy'
class counterRouter(object):
    """
    A router to control all database operations on models in the
    counter application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read counter models go to counter db.
        """
        if model._meta.app_label == 'counter':
            return 'counter'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write counter models go to counter db.
        """
        if model._meta.app_label == 'counter':
            return 'counter'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the counter app is involved.
        """
        if obj1._meta.app_label == 'counter' or \
           obj2._meta.app_label == 'counter':
           return True
        return None

    #def allow_migrate(self, db, model):
    #    """
    #    Make sure the auth app only appears in the 'auth_db'
    #    database.
    #    """
    #    if db == 'counter':
    #        return model._meta.app_label == 'counter'
    #    elif model._meta.app_label == 'counter':
    #        return False
    #    return None
