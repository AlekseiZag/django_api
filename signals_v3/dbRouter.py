import signals_v3.models

allmodels = dict([(name.lower(), cls) for name, cls in signals_v3.models.__dict__.items() if isinstance(cls, type)])


class DBRouterV3(object):

    def db_for_read(self, model, **hints):
        """ reading model based on params """
        return getattr(model.params, 'db')

    def db_for_write(self, model, **hints):
        """ writing model based on params """
        return getattr(model.params, 'db')

