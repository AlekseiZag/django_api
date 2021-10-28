import signals_v2.models as md

allmodels = dict([(name.lower(), cls) for name, cls in md.__dict__.items() if isinstance(cls, type)])


class DBRouterV2(object):

    def db_for_read(self, model, **hints):
        """ reading model based on params """
        return getattr(model.params, 'db')

    def db_for_write(self, model, **hints):
        """ writing model based on params """
        return getattr(model.params, 'db')


